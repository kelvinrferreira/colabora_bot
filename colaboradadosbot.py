#Importando as libraries

import os
import numpy as np
import pandas as pd
import requests
import tweepy
import configparser
import settings
import random

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

#Acessando urls

for index, row in df.iterrows():

    try:
        url = row['url']
        arroba = row['arroba']
        orgao = row['orgao']
        status_code = requests.get(row['url'], headers=headers).status_code
        
#Lista de frases que o bot vai twittar

        #Frases com nome do órgão

        com_orgao = [f"O portal com dados públicos [ {url} ] do órgão {orgao} parece não estar funcionando. Poderia me ajudar a checar?",
                     f"Hum, parece que o site [ {url} ], mantido pelo órgão {orgao}, está apresentando erro. Poderia dar uma olhadinha?",
                     f"Poxa, tentei acessar [ {url} ] e não consegui. Este site é mantido pelo órgão {orgao}. Você pode confirmar isso?",
                     f"Não consigo acessar [ {url} ], e eu sei que ele é mantido pelo órgão {orgao}. Você pode me ajudar a verificar?",
                     f"Sabe o portal [ {url} ], mantido pelo orgão {orgao}? Ele parece estar fora do ar. Você pode confirmar?"]                    
        msg_orgao = random.choice(com_orgao)
        tweet_orgao = f'{msg_orgao}'

        #Frases com arroba

        com_arroba = [f"Parece que [ {url} ] está apresentando probleminhas para ser acessado. O que está acontecendo {arroba}?",
                     f"Oi {arroba}, tudo bem? Pois com esse site [ {url} ] parece não estar, já que ele possui problemas de acesso.",
                     f"Portais da transparência são um direito ao acesso à informação {arroba}, mas parece que [ {url} ] está fora do ar.",
                     f"Opa {arroba}, parece que o site [ {url} ] não está acessível como deveria. O que está acontecendo?",
                     f"Tentei acessar o site [ {url} ] e não consegui. {arroba} está acontecendo algum problema com essa portal de transparência?"]
        msg_arroba = random.choice(com_arroba)
        tweet_arroba = f'{msg_arroba}'

#Dando diagnóstico e twittando

    except (requests.HTTPError, requests.ConnectionError) as erro:
        if arroba == "":
            bot.update_status(tweet_orgao)
        else:
            bot.update_status(tweet_arroba)