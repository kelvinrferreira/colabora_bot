#Importando as libraries

import os
import numpy as np
import pandas as pd
import requests
import tweepy
import configparser
import settings

#Fingindo ser um humano

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Importando tokens

config = configparser.ConfigParser()
config.sections()
config.read('colaboradados.conf')

# Autenticando o Twitter

consumer_key = settings.consumer_key
consumer_secret = settings.consumer_secret
access_token = settings.access_token
access_token_secret = settings.access_token_secret

# App no Twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
bot = tweepy.API(auth)

#Abrindo a lista de portais da transparência

df = pd.read_csv('lista_portais.csv', header=None, names=['url', 'arroba', 'orgao'], sep=';')

#Mudando o NaN padrão do Pandas para ""

df = df.replace(np.nan, '', regex=True) 

#Acessando urls e dando diagnóstico

for index, row in df.iterrows():

    try:
        url = row['url']
        arroba = row['arroba']
        orgao = row['orgao']
        status_code = requests.get(row['url'], headers=headers).status_code

    except requests.HTTPError as erro:
        if arroba == "":
            bot.update_status(f"O portal com dados públicos [ {url} ] do órgão {orgao} parece não estar funcionando. Poderia me ajudar a checar?")
        else:
            bot.update_status(f"Parece que [ {url} ] está apresentando está com probleminhas para ser acessado. O que está acontecendo {arroba}?")

    except requests.ConnectionError as erro1:
        if arroba == "":
            bot.update_status(f"Hum, parece que o site [ {url} ], mantido pelo órgão {orgao}, está apresentando erro. Poderia dar uma olhadinha?")
        else:
            bot.update_status(f"Tentei acessar [ {url} ], mas não consegui. {arroba} o que houve com os dados públicos?")