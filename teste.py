# pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import Conexao_BD as cBD
import APP_Previsao_Tempo as AppPT


qtd_sql = "SELECT COUNT(valores.codigo) FROM valores"
res_qtd = AppPT.consultar(cBD.vcon, qtd_sql)
res_qtd2 = res_qtd[0]

sql = f"SELECT  capitais.capital, valores.temperatura, valores.umidade FROM valores, capitais WHERE valores.id_values <= '{res_qtd2}'"
res = AppPT.consultar(cBD.vcon, sql)
print(res)
# tabela = pd.DataFrame(res)
# tabela.head()
# print(tabela)


# x1 = np.arange(0, 1000,1) # MÉTODO PARA CRIAR ARRAY
# lista = [0]*1000
# plt.plot(res)
# plt.show()
# # ############################
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [9.5,10.5,8.8,7,6,5,4,3,2,1]
# plt.scatter(x,y) # CRIA A COMPARAÇÃO ENTRE AS ARRAYS x E y
# # plt.show() # VAI MOSTRAR NA O GRÁFICO 
