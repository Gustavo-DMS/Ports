from turtle import left, right
import numpy as np
import pandas as pd

colunas = ['S1','S2','S3','S4','S5','S6','S7','S8']
def abrirArquivo(path):
    df = pd.read_excel(path)
    df = df.fillna(0)
    return df

def somarColunas(df):
    sf = df[colunas].sum()
    soma = pd.DataFrame({'Semana':sf.index, 'Horas':sf.values},index=None, columns=None)
    soma = soma.transpose()
    return soma


def horasFuncionario(df,funcionario):
    return f'O funcionario {funcionario} trabalhou durante ' + f'''{df.query(f'Responsável == "{funcionario}"')[colunas].values.sum():.0f}''' + ' horas'

def horasTotais(df):
    return 'Um total de ' + f'{df[colunas].values.sum():.0f}' + ' horas foram alocadas'

def custoTotal(cronograma,custo):
    horas = cronograma.set_index("Responsável")[colunas].sum(axis=1).groupby("Responsável").sum().reset_index()
    join = horas.merge(custo,left_on='Responsável',right_on='Profissional')
    join = join[0]*join['Custo']
    return 'O custo do projeto foi de R$ ' + f'{join.sum():,.2f}'


def main():
    custoHora = abrirArquivo(r'C:\Users\ra00297155\Desktop\Port 2 m9\Port2m9\custohora.xlsx')
    cronograma = abrirArquivo(r'C:\Users\ra00297155\Desktop\Port 2 m9\Port2m9\cronograma.xlsx')
    print(somarColunas(cronograma))
    print(horasFuncionario(cronograma,'C'))
    print(horasTotais(cronograma))
    print(custoTotal(cronograma,custoHora))

main()