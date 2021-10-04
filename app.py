from flask import Flask, render_template
import chamandopaghtml as run_pag
import APP_Previsao_Tempo as AppPT

app = Flask(__name__)

@app.route("/")

def index():
    AppPT.Dados_Capitais()
    Gera_Index() # VAI GERAR A PÁGINA HTML
    return render_template('index.html')

@app.route('/graficos')
def graficos():
    
    return render_template('secao_graficos.html')


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

# app.run()

