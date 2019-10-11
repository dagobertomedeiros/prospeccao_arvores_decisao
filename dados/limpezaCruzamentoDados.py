import pandas as pd
#import re
from fuzzywuzzy import fuzz
#from fuzzywuzzy import process

dadosLinhasSite = pd.ExcelFile('linhasSite.xls')
dfLinhasSite = pd.read_excel(dadosLinhasSite, 'Sheet1')

dadosRegioes = pd.ExcelFile('regioes.xlsx')
dfRegioes = pd.read_excel(dadosRegioes, 'Plan1')

qtdLinhas = []
i = 0

while(i < (dfRegioes.size/2)):
    j=0
    valor=0
    while(j < (dfLinhasSite.size/2)):
        reg = dfRegioes.loc[i, 'Bairro']
        lin = dfLinhasSite.loc[j, 'LINHAS']
        scoreFuzz = fuzz.ratio(reg,lin)
        if(scoreFuzz > 85):
            #print(reg, '--->> ', lin)
            valor+=1
        if(j == (dfLinhasSite.size/2)-1):
            qtdLinhas.append(valor)
        j += 1
    i += 1
bairro = dfRegioes['Bairro']
dfBairroQtdLinhas = pd.DataFrame(bairro)
dfBairroQtdLinhas['qtdLinhas'] = qtdLinhas
#dfBairroQtdLinhas.to_excel("bairros_qtd_linhas.xlsx")
dfBairroQtdLinhas.to_csv('/home/dagoberto/Documentos/TRABALHO/treedecision_prospect/dados/bairros_qtd_linhas.csv')
#print(dfBairroQtdLinhas)
