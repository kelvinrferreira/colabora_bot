import datetime
import gspread
from time import sleep
from autenticadores import google_api_auth


def auth_google():
    session = google_api_auth()
    ggle_cred = gspread.Client(None, session)
    return ggle_cred


def cria_planilha(ggle_cred):
    data = datetime.datetime.now()
    dia, mes, ano = data.day, data.month, data.year
    planilha = ggle_cred.create('Colaborabot - Sites Offline {:02d}/{:02d}/{:04d}'.format(dia, mes, ano))
    sleep(5)
    planilha.share('joaoernanepaula@gmail.com', perm_type='user', role='writer')
    return planilha


def preenche_tabela(ggle_cred, planilha, dados):
    tabela = ggle_cred.open(planilha.title)
    planilha = tabela.get_worksheet(index=0)
    planilha.append_row(values=dados)
