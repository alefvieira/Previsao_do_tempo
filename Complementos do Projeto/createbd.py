# IMPORTANDO A BIBLIOTECA SQL
# ABRINDO A CONEXÃO
import _sqlite3

conexao = _sqlite3.connect("previ_temp.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS capitais(codigo text unique, nome text )")
# inserindo valor
cursor.execute("INSERT INTO capitais(codigo, nome) VALUES ('SBRJ', 'Rio de Janeiro'), ('SBSP', 'São Paulo'),('SBVT', 'Vitória'), ('SBCF', 'Belo Horizonte')")
# CRIANDO A TABELA QUE REFERENCIA TODAS AS TAGS DENTRO DO <metar>
cursor.execute("CREATE TABLE IF NOT EXISTS valores(codigo text unique, atualizacao text, pressao text, temperatura text, tempo text, tempo_desc text, umidade text, vento_dir text, vento_int text, intensidade text)" )
# ENCERRANDO CONEXÃO COM O BANCO DE DADOS
conexao.commit()
cursor.close()
conexao.close()