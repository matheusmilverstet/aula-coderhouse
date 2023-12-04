from plyer import notification
from datetime import datetime
def alerta(nivel, base, etapa):
    '''
        Alerta de falha de carregamento de base de dados
    '''
    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")

    msg = f"Falha no carregamento da base {base} na etapa {etapa}.\n{formatted_now}"


    if nivel == 1:
        title = 'ATENÇÃO: Alerta Baixo'
    elif nivel == 2:
        title = 'ATENÇÃO: Alerta Médio'
    elif nivel  == 3:
        title = 'ATENÇÃO: Alerta Alto'
    else:
        print("Nivel",nivel,"não disponível!")

    notification.notify(
            title=title,
            message=msg,
            app_name='alerta',
            timeout=10
        )

alerta(nivel = 1,
        base = "TESTE",
        etapa = "IMPORTAÇÃO")