import pandas as pd
import numpy as np
import xmltodict
from sqlite3 import Error
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen

import Conexao_BD


# data['capitais']['metar'][0].keys()
# tabela = pd.DataFrame(data['capitais']['metar'])
# A propriedade loc seleciona apenas a linha, dentro desse
# m = tabela.loc[tabela['vento_int']=='11']

def ChamaXML():
    # VAI PEGAR TODAS AS INFORMAÇÕES DA XML
    file = urlopen('http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    return data 


# comandos de delete, update e insert 
def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Ação realizada com sucesso !")
    except Error as ex:
        print(ex)
    # finally:
    #     print("Operação Realizada com sucesso")


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
    sql = "CREATE TABLE IF NOT EXISTS capitais(codigo text primary key, capital text, uf text, regiao text)"
    query(Conexao_BD.vcon, sql)
    
    # CRIANDO TABELAS COM OS VALORES DE CADA CAPITAL
    sql = "CREATE TABLE IF NOT EXISTS valores(id_values integer primary key AUTOINCREMENT , codigo text UNIQUE, atualizacao text, pressao text, temperatura text, tempo text, tempo_desc text, umidade text, vento_dir text, vento_int text, intensidade text, FOREIGN KEY(codigo) REFERENCES capitais(codigo))"
    query(Conexao_BD.vcon, sql)

def InsertCapitais():
    sql = """INSERT INTO capitais(codigo, capital, uf, regiao) VALUES 
    ('SBAR',	'Aracaju'		,'SE','Nordeste'),
    ('SBBE',	'Belém'			,'PA','Norte'),
    ('SBCF',	'Belo Horizonte','MG','Sudeste'),
    ('SBBV',	'Boa Vista'		,'RR','Norte'),
    ('SBBR',	'Brasília'		,'DF','Centro-Oeste'),
    ('SBCG',	'Campo Grande'	,'MS','Centro-Oeste'),
    ('SBCY',	'Cuiabá'		,'MT','Centro-Oeste'),
    ('SBCT',	'Curitiba'		,'PR','Sul'),
    ('SBFL',	'Teresina'		,'SC','Sul'),
    ('SBFZ',	'Fortaleza'		,'CE','Nordeste'),
    ('SBGO',	'Goiânia'		,'GO','Centro-Oeste'),
    ('SBJP',	'João Pessoa'	,'PB','Nordeste'),
    ('SBMQ',	'Macapá'		,'AP','Norte'),
    ('SBMO',	'Maceió'		,'AL','Nordeste'),
    ('SBMN',	'Manaus'		,'AM','Norte'),
    ('SBNT',	'Natal'			,'RN','Nordeste'),
    ('SBPA',	'Porto Alegre'	,'RS','Sul'),
    ('SBPV',	'Porto Velho'  	,'RO','Norte'),
    ('SBRF',	'Recife'  		,'PE','Nordeste'),
    ('SBRB',	'Rio Branco'	,'AC','Norte'),
    ('SBRJ',	'Rio de Janeiro','RJ','Sudeste'),
    ('SBSV',	'Salvador'		,'BA','Nordeste'),
    ('SBSL',	'São Luís'		,'MA','Nordeste'),
    ('SBSP',	'São Paulo'		,'SP','Sudeste'),
    ('SBTE',	'Teresina'    	,'PI','Nordeste'),
    ('SBVT',	'Vitória'		,'ES','Sudeste')"""
    
    query(Conexao_BD.vcon, sql)

def InsertValores(allcod):

    sql = "INSERT or REPLACE INTO valores (codigo, atualizacao, pressao, temperatura, tempo, tempo_desc, umidade, vento_dir, vento_int, intensidade) VALUES ('"+allcod['codigo']+"','"+allcod['atualizacao']+"','"+allcod['pressao']+"','"+allcod['temperatura']+"','"+allcod['tempo']+"','"+allcod['tempo_desc']+"', '"+allcod['umidade']+"','"+allcod['vento_dir']+"','"+allcod['vento_int']+"','"+allcod['intensidade']+"')"
    query(Conexao_BD.vcon, sql)
    return True

def cod_atuali(res):
    sql_valores = f"SELECT atualizacao FROM valores WHERE codigo = '{res[0][0]}'"
    res_valores = consultar(Conexao_BD.vcon,sql_valores)  
    return res_valores

def Regioes():
    retorno = query_cria_grafico('Nordeste')
    retorno = query_cria_grafico('Norte')
    retorno = query_cria_grafico('Centro-Oeste')
    retorno = query_cria_grafico('Sul')
    retorno = query_cria_grafico('Sudeste')
    return True


# ESSA FUNÇÃO VAI CRIAR TODOS OS GRAFICOS
def query_cria_grafico(regiao):

    sql = f"SELECT  capitais.capital, valores.temperatura FROM valores, capitais WHERE valores.codigo = capitais.codigo  and capitais.regiao = '{regiao}'"
    res = consultar(Conexao_BD.vcon, sql)

    lista = []

    for num, i in enumerate(res):
        # print(f"{num}   {i}")
        ii = list(i)
        ii[1] = int(ii[1])
        lista.append(ii)

    # print(lista)
    colunas = pd.DataFrame(lista, columns=['capital', 'temperatura']) # ESSE METODO COLOCA NOMES NAS COLUNAS
    plot = sns.barplot(data=colunas, x='capital', y='temperatura')
    plot.get_figure().savefig(f"static/graficos/temperatura_{regiao}.png")
    plt.close()
    return True


def Dados_Capitais():
    # VAI PEGAR TODAS AS INFORMAÇÕES DA XML
    data = ChamaXML()
    allcod = data['capitais']['metar']


    sql_s = "SELECT codigo FROM capitais"
    res = consultar(Conexao_BD.vcon,sql_s)

    sql_valores = f"SELECT atualizacao FROM valores WHERE codigo = '{res[0][0]}'"
    res_valores = consultar(Conexao_BD.vcon,sql_valores)  

    print(f"{res_valores[0][0]}  :  {allcod[0]['atualizacao']}")
    
    # ESSE IF  VAI IMPEDIR DO CODIGO ATUALIZAR
    if allcod[0]['atualizacao'] != res_valores[0][0]:
        
        retorno_reg = Regioes() # VAI GERAR OS GRÁFICOS

        # FAZ A CONTAGEM DE METAS PARA CRIAR O LOOP DE REPETICAO
        for i in range(0,len(data['capitais']['metar'])):
            
            # PEGANDO OS VALORES DA XML E COMPARANDO SE EXISTE A SUA CAPITAL REGISTRADA NO BD
            # CONVERTENDO O VALOR DA TAG XML E PASSANDO PARA TUPLE PARA COMPRAR COM O VALOR NO BANCO DE DADOS
            tupla_de_comparacao = [0]
            tupla_de_comparacao[0] = allcod[i]['codigo']
            tupla_de_comparacao = tuple(tupla_de_comparacao)
            
            # CASO TENHA O CODIGO DAS CAPITAIS VAI SALVAR A INFORMACAO NO BANCO
            if tupla_de_comparacao in res:
                # TRATAMENTO DOS CARACTERES ESPECIAIS
                if allcod[i]['tempo_desc'] == 'PredomÃ\xadnio de Sol':
                    allcod[i]['tempo_desc'] = 'Predomínio de Sol'

                elif allcod[i]['tempo_desc'] == 'Chuvas periÃ³dicas':
                    allcod[i]['tempo_desc'] = 'Chuvas Periódicas'
                
                # FUNCAO COM RETORNO QUE SALVA OS DADOS NO BANCO DE DADOS
                insirirBD = InsertValores(allcod[i])

def SelectBD():

    sql = "select * from capitais"
    res = consultar(Conexao_BD.vcon,sql)
    print(res)
    sql = "select * from valores"
    res = consultar(Conexao_BD.vcon,sql)
    print(res)

# ESSA FUNÇÃO VAI ENVIAR O PARAMETRO DA REGIAO DO SQL


# FUNÇÕES START
# Criartabela()
# InsertCapitais()
Dados_Capitais()
# SelectBD()
# Regioes()
# Conexao_BD.vcon.close()

