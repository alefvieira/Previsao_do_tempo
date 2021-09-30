import pandas as pd
import numpy as np
import xmltodict
from urllib.request import urlopen
import Conexao_BD
from sqlite3 import Error


file = urlopen('http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml')
data = file.read()
file.close()
data = xmltodict.parse(data)
# data['capitais']['metar'][0].keys()
# tabela = pd.DataFrame(data['capitais']['metar'])

# comandos de delete, update e insert 
def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    # finally:
    #     print("Operação Realizada com sucesso")

cidades = {
    'SBRJ':'Rio de Janeiro',
    'SBSP':'São Paulo',
    'SBVT':'Vitória',
    'SBCF':'Belo Horizonte'}

# função de consulta(select)
def consultar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        conexao.commit()
        return resultado
    except Error as ex:
        print(ex)

def Criartabela():
    # CRIANDO A TABELA DAS CAPITAIS
    sql = "CREATE TABLE IF NOT EXISTS capitais(codigo text primary key, nome text )"
    query(Conexao_BD.vcon, sql)
    
    # CRIANDO TABELAS COM OS VALORES DE CADA CAPITAL
    sql = "CREATE TABLE IF NOT EXISTS valores(id_values integer primary key AUTOINCREMENT , codigo text UNIQUE, atualizacao text, pressao text, temperatura text, tempo text, tempo_desc text, umidade text, vento_dir text, vento_int text, intensidade text, FOREIGN KEY(codigo) REFERENCES capitais(codigo))"
    query(Conexao_BD.vcon, sql)

def InsertCapitais():
    sql = "INSERT INTO capitais(codigo, nome) VALUES ('SBRJ', 'Rio de Janeiro'), ('SBSP', 'São Paulo'),('SBVT', 'Vitória'), ('SBCF', 'Belo Horizonte')"
    query(Conexao_BD.vcon, sql)

def InsertValores(allcod):

    sql = "INSERT INTO valores (codigo, atualizacao, tempo, pressao, temperatura, tempo_desc, umidade, vento_dir, vento_int, intensidade) VALUES ('"+allcod['codigo']+"','"+allcod['atualizacao']+"','"+allcod['tempo']+"','"+allcod['pressao']+"', '"+allcod['temperatura']+"','"+allcod['tempo_desc']+"', '"+allcod['umidade']+"','"+allcod['vento_dir']+"','"+allcod['vento_int']+"','"+allcod['intensidade']+"')"
    query(Conexao_BD.vcon, sql)
    return True

def valoresSuldeste():
    for i in range(0,26):
        allcod = data['capitais']['metar'][i]
        if allcod['codigo'] in cidades:
            # print(cidades[allcod['codigo']])
            if allcod['tempo_desc'] == 'PredomÃ\xadnio de Sol':
                allcod['tempo_desc'] = 'Predominio de Sol'
            elif allcod['tempo_desc'] == 'Chuvas periÃ³dicas':
                allcod['tempo_desc'] = 'Chuvas periodicas'
            # print(allcod)
            insirirBD = InsertValores(allcod)


def SelectBD():

    sql = "select * from capitais"
    res = consultar(Conexao_BD.vcon,sql)
    print(res)
    sql = "select * from valores"
    res = consultar(Conexao_BD.vcon,sql)
    print(res)

# FUNÇÕES START
# Criartabela()
# InsertCapitais()
# valoresSuldeste()
# SelectBD()

# Conexao_BD.vcon.close()

