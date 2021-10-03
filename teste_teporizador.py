import chamandopaghtml as run_pag
import APP_Previsao_Tempo as AppPT


import sched, time
s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
    print("Doing stuff...")
    AppPT.Dados_Capitais()
    AppPT.Regioes()
    run_pag.Gera_Index()
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()