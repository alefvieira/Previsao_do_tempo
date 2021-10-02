import Conexao_BD as cBD
import APP_Previsao_Tempo as AppPT
# ********************************

pagina=open("index.html","w", encoding="UTF-8")
pagina.write(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Previsão do Tempo</title>

    <link rel="stylesheet" href="style.css">
    
</head>
<body>
    <header class="container" ><h1>Projeto página Previsão do Tempo</h1></header>
    
    <main class="container">""")


pagina.write(f"""
        <form class="regiao_Pesq">
            <div >
                <input type="radio" name="regiao" onclick="Select_Page()" id="norte" value="Norte"> <label class="anima" for="norte">Norte</label> 
            </div><div>
                <input type="radio" name="regiao" id="nordeste" value="Nordeste"  onclick="Select_Page()"> <label class="anima" for="nordeste">Nordeste </label> 
            </div><div>
                <input type="radio" name="regiao" id="centroeste" value="Centro-Oeste"  onclick="Select_Page()"><label class="anima" for="centroeste">Centro-Oeste</label> 
            </div><div>
                <input type="radio" name="regiao" id="sudeste" value="Sudeste"  checked  onclick="Select_Page()"><label class="anima" for="sudeste">Sudeste</label> 
            </div><div>
                <input type="radio" name="regiao" id="sul" value="Sul"  onclick="Select_Page()"><label class="anima" for="sul">Sul</label> 
            </div>
        </form>""")

pagina.write("""<div class="container"><h2 class="regiao_capitais"></h2></div>""")

def gera_section(cod_selec):
    sql = f"SELECT codigo from capitais where regiao ='{cod_selec}'"
    res = AppPT.consultar(cBD.vcon, sql)

    pagina.write(f"""<section class="{cod_selec}">""")

    for i in res:
        ii = i[0]
        sql_v = f"SELECT capitais.capital, valores.codigo, valores.atualizacao, valores.pressao, valores.temperatura, valores.tempo, valores.tempo_desc, valores.umidade, valores.vento_dir, valores.vento_int, valores.intensidade FROM valores, capitais WHERE capitais.codigo = '{ii}' and capitais.regiao = '{cod_selec}'" 
        ret = AppPT.consultar(cBD.vcon,sql_v)
        print(ret)
        pagina.write(f"""
            <div class="posicao_div">
                <h2>Capital: {ret[0][0]}</h2>
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
    # FORA DO FOR
    pagina.write("""
    </section>""")

# CHAMADA DAS FUNÇÕES PARA CRIAR AS SEÇÕES COM AS INFORMAÇÕES DAS CAPITAIS
gera_section("Sudeste")
gera_section("Sul")
gera_section("Centro-Oeste")
gera_section("Norte")
gera_section("Nordeste")


pagina.write("""</main>
    <p></p>
    <footer class="container">
        <p>Desenvolvido por Álef Vieira Coutinho e Kennedy Oliveira</p>
    </footer>

    <script type="text/javascript" src="javascript.js">
    </script>
    


</body>
</html>
    """)

# Select_Page()

pagina.close()

