# preprocessing.py
from libraries import *

def load_data(file_path):
    # Carregar dados
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Realizar pré-processamento
    # Exemplo: df = df.dropna()
    return df

# Código para testar as funções, se necessário
if __name__ == "__main__":
    df = load_data('seu_dataset.csv')
    df_preprocessed = preprocess_data(df)
