# Importando as libraries

import numpy as np
import pandas as pd
import tweepy
import settings

from requests import get, exceptions
from tweet_frases import tweet_arroba, tweet_orgao

TOTAL_RETRY = 10
STATUS_SUCCESS = 200

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


def tweet_status_site(arroba, orgao, url):
    """Criando o tweet com o status do site recém acessado"""
    if arroba == "":
        bot.update_status(tweet_orgao(url=url, orgao=orgao))
    else:
        bot.update_status(tweet_arroba(url=url, arroba=arroba))


def load_site_data():
    """
    Abrindo a lista de portais da transparência e tratando
    informações que serão tratados como NaN para o pandas.
    """
    df = pd.read_csv(
        'lista_portais.csv',
        header=None,
        names=['url', 'arroba', 'orgao'],
        sep=';'
    )
    df = df.replace(np.nan, '', regex=True)

    return df


def fetch_and_access_sites(sites):
    """
    Percorrendo a lista de sites para verificar
    a sua disponibilidade. Caso o código de status
    seja 200 (OK), então ela está disponível para acesso.

    Caso contrário, envie um novo tweet avisando da indisponibilidade
    citando o perfil do órgão no Twitter caso tenha.
    """
    for index, row in sites.iterrows():
        url, arroba, orgao = row['url'], row['arroba'], row['orgao']

        for tentativa in range(TOTAL_RETRY):
            try:
                response = get(row['url'], timeout=30, headers=headers)
                if response.status_code == STATUS_SUCCESS:
                    continue

                tweet_status_site(arroba, orgao, url)
            except exceptions.ConnectionError:
                print(f"Problemas na conexão ao acessar o órgão {orgao}")
            except exceptions.ReadTimeout:
                tweet_status_site(arroba, orgao, url)


if __name__ == '__main__':
    sites = load_site_data()
    fetch_and_access_sites(sites)
