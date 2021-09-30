import Conexao_BD as cBD
import APP_Previsao_Tempo as AppPT


pagina=open("index.html","w", encoding="UTF-8")
pagina.write("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <!--<meta charset="UTF-8">-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Previsão do Tempo</title>

    <link rel="stylesheet" href="style.css">
    
</head>
<body>
    <header class="container" ><h1>Projeto página Previsão do Tempo</h1></header>
    
    <main class="container">""")

sql = "SELECT COUNT(codigo) from valores"
res = AppPT.consultar(cBD.vcon,sql)
res2 = int(res[0][0])
for i in range(1,res2+1):

    sql_valores = "SELECT * FROM valores WHERE "
    sql_v = "SELECT * FROM valores, capitais WHERE capitais.codigo = valores.codigo and valores.id_values = "+ str(i)
    ret = AppPT.consultar(cBD.vcon,sql_v)
    print(ret)
    pagina.write(f"""
    <div class="posicao_div">
        <h2>Capital: {ret[0][12]}</h2>
        <h3>Código: {ret[0][1]}</h3>
        <p>Atualização: {ret[0][2]}</p>
        <p>Pressão: {ret[0][3]}</p>
        <p>Temperatura: {ret[0][4]}</p>
        <p>Tempo: {ret[0][5]}</p>
        <p>Descrição do Tempo: {ret[0][6]}</p>
        <p>umidade: {ret[0][7]}</p>
        <p>vento_dir: {ret[0][8]}</p>
        <p>vento_int: {ret[0][9]}</p>
        <p class="last_p">Intensidade: {ret[0][10]}</p>
    </div>
    """)

pagina.write("""</main>

    <footer class="container">
        <p>Desenvolvido por Álef Vieira Coutinho e Kennedy Oliveira</p>
    </footer>

    <script src="javascript.js"></script>

</body>
</html>
    """)
pagina.close()

