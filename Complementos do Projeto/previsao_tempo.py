import pandas as pd 
import numpy as np
import xmltodict
from urllib.request import urlopen

import _sqlite3

file = urlopen('http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml')
data = file.read()
file.close()

data = xmltodict.parse(data)
# data['capitais']['metar'][0].keys()
tabela = pd.DataFrame(data['capitais']['metar'])
cidades = {
    'SBRJ':'Rio de Janeiro',
    'SBSP':'São Paulo',
    'SBVT':'Vitória',
    'SBCF':'Belo Horizonte'}


def functINSERT():
  conexao = _sqlite3.connect("previ_temp.db")
  cursor = conexao.cursor()
  cursor.execute("INSERT OR REPLACE INTO valores VALUES (?,?,?,?,?,?,?,?,?,?)", (allcod['codigo'],allcod['atualizacao'], 
                                                                      allcod['tempo'],allcod['pressao'], allcod['temperatura'], 
                                                                      allcod['tempo_desc'], allcod['umidade'],allcod['vento_dir'], 
                                                                      allcod['vento_int'],allcod['intensidade']))
  conexao.commit()
  cursor.close()
  conexao.close()
  return True

for i in range(0,26):
  allcod = data['capitais']['metar'][i]
  if allcod['codigo'] in cidades:
    print(cidades[allcod['codigo']])
    if allcod['tempo_desc'] == 'PredomÃ\xadnio de Sol':
      allcod['tempo_desc'] = 'Predominio de Sol'
    elif allcod['tempo_desc'] == 'Chuvas periÃ³dicas':
      allcod['tempo_desc'] = 'Chuvas periodicas'
    print(allcod)
    retorna = functINSERT()