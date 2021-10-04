from flask import Flask, render_template
import chamandopaghtml as run_pag
import APP_Previsao_Tempo as AppPT

app = Flask(__name__)



@app.route("/")

def index():
    AppPT.Dados_Capitais()
    run_pag.Gera_Index()
    return render_template('index.html')

@app.route('/graficos')
def graficos():
    AppPT.Regioes()
    return render_template('secao_graficos.html')

app.run(host='0.0.0.0', port=5000)



# import sched, time
# s = sched.scheduler(time.time, time.sleep)

# def do_something(sc): 
#     print("Dados Atualizados")
#     AppPT.Dados_Capitais()
#     AppPT.Regioes()
#     run_pag.Gera_Index()
#     s.enter(300, 1, do_something, (sc,))

# s.enter(300, 1, do_something, (s,))
# s.run()

# def app():
#     AppPT.Dados_Capitais()
#     AppPT.Regioes()
#     run_pag.Gera_Index()

