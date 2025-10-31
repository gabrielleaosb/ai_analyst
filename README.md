# AI Analyst

AI Analyst é uma aplicação web em Django que permite enviar arquivos CSV para análise automatizada utilizando a inteligência artificial do modelo Ollama.

O foco do projeto é análise de dados de forma prática e rápida, com suporte a arquivos pequenos, médios e grandes (processamento em background).

## Funcionalidades

- Upload de arquivos CSV diretamente pela interface web  
- Detecção automática do tamanho do arquivo (pequeno, médio, grande)  
- Geração de análises inteligentes com o modelo **Llama 3 (Ollama)**  
- Interface simples e moderna em Django  
- Processamento local — seus dados não saem da sua máquina  

## 🧩 Tecnologias principais

- **Python 3.12+**
- **Django 5**
- **LangChain + Ollama**
- **Pandas / NumPy**
- **Tailwind (frontend minimalista)**

---

## ⚙️ Instalação local

1. Clone o repositório:

```bash
git clone https://github.com/gabrielleaosb/ai_analyst.git
cd ai_analyst
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate       # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados e crie as tabelas:

```bash
python manage.py migrate
```

5. Inicie o Ollama (certifique-se que está instalado):

```bash
ollama serve
```

6. Rode o servidor Django:

```bash
python manage.py runserver
```

8. Acesse a aplicação no navegador:

```
http://127.0.0.1:8000/
```

## Observações

- Para arquivos grandes, o processamento pode levar alguns minutos.
- O modelo Ollama deve estar rodando na porta `11434`.

---

Projeto pronto para estudo, contribuições e uso pessoal. Open Source.