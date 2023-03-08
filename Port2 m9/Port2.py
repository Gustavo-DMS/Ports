import numpy as np
import pandas as pd


def abrirArquivo(path):
    df = pd.read_excel(path)
    df = df.fillna(0)
    return df
custoHora = abrirArquivo('custohora.xlsx')
cronograma = abrirArquivo('cronograma.xlsx')



print(cronograma)
