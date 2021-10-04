import Conexao_BD as cBD
import APP_Previsao_Tempo as AppPT

# ********************************
def Gera_Index():

    pagina=open("templates/index.html", "w", encoding="UTF-8")
    pagina.write(f"""<!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Previsão do Tempo</title>

        <link rel="stylesheet" href="../static/css/style.css">
        
    </head>
    <body>
        <header class="container" >
            <h1><a href="/"> Projeto página Previsão do Tempo</a></h1>
            <div><h1><a href="graficos" >Acessar Gráficos</a></h1></div>
        </header>
        
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

        sql_v = f"SELECT capitais.capital, valores.codigo, valores.atualizacao, valores.pressao, valores.temperatura, valores.tempo, valores.tempo_desc, valores.umidade, valores.vento_dir, valores.vento_int, valores.intensidade FROM valores, capitais WHERE capitais.codigo = valores.codigo and capitais.regiao = '{cod_selec}'" 
        ret = AppPT.consultar(cBD.vcon,sql_v)

        for num,i in enumerate(ret):
            pagina.write(f"""
                <div class="posicao_div">
                    <h2>Capital: {ret[num][0]}</h2>
                    <h3>Código: {ret[num][1]}</h3>
                    <p>Atualização: {ret[num][2]}</p>
                    <p>Pressão: {ret[num][3]}</p>
                    <p>Temperatura: {ret[num][4]}</p>
                    <p>Tempo: {ret[num][5]}</p>
                    <p>Descrição do Tempo: {ret[num][6]}</p>
                    <p>umidade: {ret[num][7]}</p>
                    <p>vento_dir: {ret[num][8]}</p>
                    <p>vento_int: {ret[num][9]}</p>
                    <p class="last_p">Intensidade: {ret[num][10]}</p>
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

        <script type="text/javascript" src="../static/javascript.js">
        </script>
        
    </body>
    </html>
        """)

    pagina.close()
    
Gera_Index()