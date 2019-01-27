# Importando as libraries

import numpy as np
import pandas as pd
from requests import get, exceptions
import tweepy
import settings
from tweet_frases import tweet_arroba, tweet_orgao

# Fingindo ser um humano

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Autenticando o Twitter

consumer_key = settings.consumer_key
consumer_secret = settings.consumer_secret
access_token = settings.access_token
access_token_secret = settings.access_token_secret

# App no Twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
bot = tweepy.API(auth)

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
            status_code = get(row['url'], timeout=10).status_code
            print(f'{url} : {status_code}\n{orgao}\n{arroba}\n')
            if status_code != 200:
                if arroba == "":
                    print(tweet_orgao(url=url, orgao=orgao))
                else:
                    print(tweet_arroba(url=url, arroba=arroba))
        except exceptions.ConnectionError:
            continue
        else:
            break
    else:  # Caso exceda 10 tentativas de acessar o site.
        if arroba == "":
            print(tweet_orgao(url=url, orgao=orgao))
        else:
            print(tweet_arroba(url=url, arroba=arroba))
        continue
