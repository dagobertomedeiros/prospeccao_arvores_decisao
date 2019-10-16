import requests
import json
import time
import pandas as pd
import re

url = 'https://www.receitaws.com.br/v1/cnpj/'

#Carregando CNPJ das empresas em dataframe
arq = pd.read_excel('EMP_CNPJS.xlsx', 'Planilha1')
dt = pd.DataFrame(arq)

#Consultando através do CNPJ a atividade principal da empresa
#utilizando api do receitaws, como a versão pública e gratuita desta api permite no máximo 3 
#consultas por minuto foi introduzido no código um delay de 22s por consulta assim retornando 
#todos os valores sem erros
i = 0
ativPrincipal = []
while(i < dt.size/3):
    cnpj = str(dt['CNPJ'][i])
    if(len(cnpj) < 14):
        while(len(cnpj) < 14):
            cnpj = '0' + cnpj
    page = requests.get(url + cnpj)
    if(page):
        jsonAll = json.loads(page.text)
        jsonAtiv = jsonAll['atividade_principal']
        codAtiv = str(jsonAtiv[0].get('code'))
        codAtiv = codAtiv.replace('.', '')
        codAtiv = codAtiv.replace('-', '')
        ativPrincipal.append(codAtiv)
        time.sleep(22)
    i+=1

#adicionando os novos dados conseguidos ao dt
dt['cod_atividade'] = ativPrincipal

#salvando tudo em um novo arquivo
dt.to_excel('EMP_CNPJS_ATIVIDADES.xlsx')