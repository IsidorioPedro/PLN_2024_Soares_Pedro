import pandas as pd

def load_and_prepare_data(file_path):
    # Carregar dados de um arquivo JSON
    df = pd.read_json(file_path, orient='records', lines=True)

    # Concatenar as colunas relevantes em uma única string
    df['combined_text'] = (
        df['NomePessoaNacional'].fillna('') + ' | ' +
        df['NomePessoaEstrangeira'].fillna('') + ' | ' +
        df['PaisPessoaEstrangeira'].fillna('') + ' | ' +
        df['MoedaOperacao'].fillna('')
    )

    return df
