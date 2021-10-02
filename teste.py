# pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns
import Conexao_BD as cBD
import APP_Previsao_Tempo as AppPT


reg = "Nordeste"
sql = f"SELECT  capitais.capital, valores.temperatura, valores.umidade FROM valores, capitais WHERE valores.codigo = capitais.codigo  and capitais.regiao = '{reg}'"
res = AppPT.consultar(cBD.vcon, sql)
print(res)
# aaa = [['A', 1, 15], ['B', 2, 20], ['C', 3, 8], ['D', 4, 10]]
# df = pd.DataFrame(aaa,columns=)
# tabela = pd.DataFrame(res)
# ESSE METODO PERMITE COLOCAR O NOME NAS COLUNAS
# colunas = pd.DataFrame(res, columns=['capital', 'temperatura', 'umidade'])
# testee = sns.barplot(res=colunas, x='capital', y='temperatura')
# testee.get_figure().savefig('teste.png')



# sql_create = "CREATE TABLE IF NOT EXISTS grafics (cont BLOB)"
# res100 = AppPT.consultar(cBD.vcon, sql_create)

lista = []

for num, i in enumerate(res):
    print(f"{num}   {i}")
    ii = list(i)
    ii[1] = int(ii[1])
    ii[2] = int(ii[2])
    lista.append(ii)

print(lista)

colunas = pd.DataFrame(lista, columns=['capital', 'temperatura', 'umidade']) # ESSE METODO COLOCA NOMES NAS COLUNAS
plot = sns.barplot(data=colunas, x='capital', y='temperatura')
# plt.bar(data=plot, x='capital', height='temperatura')
plot.get_figure().savefig('graficos/teste.png')
# plt.bar(colunas['capital'], colunas['temperatura'], color = "#4CAF50")
plt.show()

# sql_insert = f"INSERT OR REPLACE INTO grafics VALUES ('')"
# res1000 = AppPT.consultar(cBD.vcon, sql_insert)

# sql_select = "SELECT * FROM grafics"
# res10000 = AppPT.consultar(cBD.vcon, sql_select)

# plt.bar(c_cap, c_temp, color = "#4CAF50")
# plt.show()

# plt.scatter(c_cap, c_temp)
# plt.show()

# x1 = np.arange(0, 1000,1) # MÉTODO PARA CRIAR ARRAY
# plt.plot(res)
# plt.show()
# # ############################
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [9.5,10.5,8.8,7,6,5,4,3,2,1]
# plt.scatter(x,y) # CRIA A COMPARAÇÃO ENTRE AS ARRAYS x E y
# # plt.show() # VAI MOSTRAR NA O GRÁFICO 
