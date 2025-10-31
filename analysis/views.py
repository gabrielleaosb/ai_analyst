from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from analysis.utils.logger import logger
from analysis.utils.file_utils import classify_file_size, read_file
from analysis.utils.ollama_check import check_ollama_server_socket
from langchain_ollama import OllamaLLM
import pandas as pd
import os


def dashboard_view(request):
    return render(request, "dashboard.html")


class AnalyzeFileView(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        user_instructions = request.POST.get("instructions", "")

        if not file:
            logger.warning("Nenhum arquivo enviado.")
            return Response({"error": "Nenhum arquivo enviado."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Checa o Ollama
            if not check_ollama_server_socket():
                return Response({"error": "Ollama server não está disponível."}, status=503)

            # Classifica o tamanho do arquivo
            file_category = classify_file_size(file)
            logger.info(f"Arquivo recebido: {file.name}, categoria: {file_category}")

            # Salva temporariamente o arquivo
            temp_dir = "temp_uploads"
            os.makedirs(temp_dir, exist_ok=True)
            temp_path = os.path.join(temp_dir, file.name)

            with open(temp_path, "wb+") as f:
                for chunk in file.chunks():
                    f.write(chunk)

            # Lê e resume o dataset localmente
            df = pd.read_csv(temp_path)
            numeric_summary = df.describe(include="all").to_string()
            sample = df.sample(min(50, len(df))).to_string(index=False)
            cat_cols = df.select_dtypes(include=['object']).columns.tolist()
            value_counts_summary = {col: df[col].value_counts().head(10).to_dict() for col in cat_cols}
            columns = ", ".join(df.columns)

            # Monta o prompt resumido
            prompt_text = f"""
            Você é um analista de dados experiente.

            Detalhes do dataset:
            - Nome das colunas: {columns}
            - Total de registros: {len(df)}

            Estatísticas numéricas resumidas:
            {numeric_summary}

            Contagem top 10 valores das colunas categóricas:
            {value_counts_summary}

            Amostra aleatória do dataset:
            {sample}

            Instruções adicionais do usuário:
            {user_instructions}

            Gere uma análise detalhada, incluindo insights e tendências.
            """

            # Envia o prompt ao Ollama
            llm = OllamaLLM(model="llama3", host="127.0.0.1", port=11434)
            result = llm.invoke(prompt_text)

            # Remove o arquivo temporário
            os.remove(temp_path)

            return Response({"analysis": result})

        except Exception as e:
            logger.error(f"Erro na análise: {str(e)}", exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
