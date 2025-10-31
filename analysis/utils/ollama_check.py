import socket
from analysis.utils.logger import logger

OLLAMA_HOST = "127.0.0.1"
OLLAMA_PORT = 11434

def check_ollama_server_socket(timeout=3):
    """Verifica se a porta do Ollama está aberta (Ollama rodando)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((OLLAMA_HOST, OLLAMA_PORT))
        s.close()
        logger.info("Ollama server está disponível.")
        return True
    except (socket.timeout, ConnectionRefusedError) as e:
        logger.warning(f"Ollama server não disponível: {e}")
        return False
