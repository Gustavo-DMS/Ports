import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

faixas = [0,18,23, 28, 33,38,43,48,53,58,200]
def abrirArquivo(path,faixa):
    df = pd.read_excel(path)
    df = df.fillna(0)
    df['idade'] = df['idade'].apply(np.floor)
    cut = pd.cut(df['idade'],faixas,include_lowest=True)
    df['faixas'] = cut
    cut = cut.cat.rename_categories(['Faixa 1','Faixa 2','Faixa 3','Faixa 4','Faixa 5','Faixa 6','Faixa 7','Faixa 8','Faixa 9','Faixa 10'])
    df['faixas_num'] = cut
    df['total_unit'] = df['vl_unit']*df['qtde']
    return df




def groupbySum(df,groupby:list,sum):
    df = df.groupby(groupby)[sum].sum(sum).reset_index()
    return(df)

def groupbyCount(df,groupby:list,count):
    df = df.groupby(groupby)[count].count().reset_index()
    return(df)

def sortHead(df,sort,ascending:bool,head):
    df = df.sort_values(sort,ascending=ascending).head(head)
    return df

def doppler(df,string):
    df['Ano'] = df['atend'].dt.year
    query = df.query(f'servico.str.contains("{string}")')
    query = query.groupby(['Ano']).sum('total_unit')
    return(query[['qtde','total_unit']])

def diferenca(df,max,min):
    df['max'] = df['vl_ref']*max
    df['min'] = df['vl_ref']*min
    query = df.query(f'vl_unit > max or vl_unit < min')['qtde'].count()
    return(query)

def grafico(df,groupby:list,sum):
    fds = groupbySum(df,groupby,sum)
    fig, ax = plt.subplots()
    ax.pie(fds[sum],labels=fds[groupby],autopct='%1.1f%%', pctdistance=0.75, textprops={'size': 'smaller'},radius=1.35)
    plt.show()


def main():
    contas = abrirArquivo('Port3M9\Contas.xlsx',faixas)
    print('-----------------------------------------------------')
    print(groupbySum(contas.copy(),['sexo','faixas'],'qtde'))
    print('-----------------------------------------------------')
    print(groupbyCount(contas.copy(),['sexo','faixas'],'qtde'))
    print('-----------------------------------------------------')
    print(groupbySum(contas.copy(),['plano','sexo','faixas'],'total_unit'))
    print('-----------------------------------------------------')
    print(sortHead(contas.copy(),'total_unit',False,10))
    print('-----------------------------------------------------')
    print(doppler(contas.copy(),"ECODOPPLERCARDIOGRAMA"))
    print('-----------------------------------------------------')
    print(diferenca(contas.copy(),1.3,0.7))
    print('-----------------------------------------------------')
    print(grafico(contas.copy(),'faixas_num','total_unit'))

main()