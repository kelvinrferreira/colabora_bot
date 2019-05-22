from authlib.client import AssertionSession
from mastodon import Mastodon
import settings
import tweepy
import json


def masto_auth():
    mastodon = Mastodon(
        access_token=settings.mastodon_key,
        api_base_url='https://botsin.space'
    )
    return mastodon


def twitter_auth():
    consumer_key = settings.consumer_key
    consumer_secret = settings.consumer_secret
    access_token = settings.access_token
    access_token_secret = settings.access_token_secret

    # App no Twitter

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    bot = tweepy.API(auth)
    return bot


def google_api_auth(arqv_json='credenciais/colaborabot-gAPI.json', subject=None):
    with open(arqv_json, 'r') as f:
        conf = json.load(f)

    token_url = conf['token_uri']
    issuer = conf['client_email']
    key = conf['private_key']
    key_id = conf.get('private_key_id')

    header = {'alg': 'RS256'}
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    if key_id:
        header['kid'] = key_id

    # Google puts scope in payload
    claims = {'scope': ' '.join(scopes)}
    return AssertionSession(
        grant_type=AssertionSession.JWT_BEARER_GRANT_TYPE,
        token_url=token_url,
        issuer=issuer,
        audience=token_url,
        claims=claims,
        subject=subject,
        key=key,
        header=header,
    )


def id_mastodon():
    id_perfil = settings.mastodon_profile_id
    return id_perfil
