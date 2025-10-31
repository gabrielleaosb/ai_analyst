import pandas as pd

def classify_file_size(file):
    """Classifica o arquivo como pequeno, médio ou grande."""
    size_mb = file.size / (1024 * 1024)
    if size_mb < 10:
        return "small"
    elif size_mb < 100:
        return "medium"
    else:
        return "large"

def read_file(file, nrows=None):
    """Lê CSV ou Excel, opcionalmente limitando linhas."""
    if file.name.endswith(".csv"):
        return pd.read_csv(file, nrows=nrows)
    elif file.name.endswith((".xls", ".xlsx")):
        return pd.read_excel(file, nrows=nrows)
    else:
        raise ValueError("Formato de arquivo não suportado.")
