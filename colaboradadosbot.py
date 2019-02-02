# Importando as libraries

import numpy as np
import pandas as pd
import google_sheets
from requests import get, exceptions
from autenticadores import twitter_auth
from tweet_frases import tweet_arroba, tweet_orgao
from time import sleep


creds = google_sheets.auth_google()
planilha = google_sheets.cria_planilha(ggle_cred=creds)
print(planilha.id)


bot = twitter_auth()

# Fingindo ser um humano

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Abrindo a lista de portais da transparência

df = pd.read_csv('lista_portais.csv', header=None, names=['url', 'arroba', 'orgao'], sep=';')

# Mudando o NaN padrão do Pandas para ""

df = df.replace(np.nan, '', regex=True)

# Acessando urls

for index, row in df.iterrows():
    url = row['url']
    arroba = row['arroba']
    orgao = row['orgao']
    for tentativas in range(10):
        try:
            status_code = get(row['url'], timeout=10, headers=headers).status_code
            dados = [url, arroba, orgao, status_code]
            if status_code != 200:
                if arroba == "":
                    google_sheets.preenche_tabela(ggle_cred=creds, planilha=planilha, dados=dados)
                else:
                    google_sheets.preenche_tabela(ggle_cred=creds, planilha=planilha, dados=dados)
        except exceptions.ConnectionError:
            continue
        except exceptions.ReadTimeout:
            continue
        else:
            break
    else:  # Caso exceda 10 tentativas de acessar o site.
        if arroba == "":
            google_sheets.preenche_tabela(ggle_cred=creds, planilha=planilha, dados=dados)
        else:
            google_sheets.preenche_tabela(ggle_cred=creds, planilha=planilha, dados=dados)
        continue
    sleep(120)
