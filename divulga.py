from autenticadores import google_api_auth
from random import choice
import gspread


def google_sshet():
    """
    Função simples para retornar um objeto capaz de manipular as planilhas do Google Sheets.
    """
    session = google_api_auth()
    ggle_cred = gspread.Client(None, session)
    return ggle_cred


def lista_frases(url, orgao):
    com_orgao = [
        f"🤖 O portal com dados públicos {url} do órgão {orgao} parece não estar funcionando. Poderia me ajudar a checar?",
        f"🤖 Hum, parece que o site {url}, mantido pelo órgão {orgao}, está apresentando erro. Poderia dar uma olhadinha?",
        f"🤖 Poxa, tentei acessar {url} e não consegui. Este site é mantido pelo órgão {orgao}. Você pode confirmar isso?",
        f"🤖 Não consigo acessar {url}, e eu sei que ele é mantido pelo órgão {orgao}. Você pode me ajudar a verificar?",
        f"🤖 Sabe o portal {url}, mantido pelo orgão {orgao}? Ele parece estar fora do ar. Você pode confirmar?",
        f"🤖 Parece que {url} está apresentando probleminhas para ser acessado. Alguém pode avisar a(o) {orgao}?",
        f"🤖 Oi, parece que esse site {url} possui problemas de acesso. {orgao} está sabendo disso?",
        f"🤖 Portais da transparência são um direito ao acesso à informação {orgao}, mas parece que {url} está fora do ar.",
        f"🤖 Opa {orgao}, parece que o site {url} não está acessível como deveria. O que está acontecendo?",
        f"🤖 Tentei acessar o site {url} e não consegui. {orgao} está acontecendo algum problema com essa portal de transparência?"
]
    msg_orgao = choice(com_orgao)
    return msg_orgao


def checar_timelines(mastodon_handler, url, orgao):
    """
    Recupera os 10 últimos toots da conta do Mastodon.
    Caso a URL não esteja entre as últimas notificadas, é feita a postagem.
    Feature necessária para não floodar a timeline alheia caso um site fique offline por longos períodos de tempo.
    """
    mastodon_bot = mastodon_handler
    urls_postadas = []
    timeline = mastodon_bot.timeline_home(limit=10)
    for toot in timeline:
        urls_postadas.append(toot["content"])
    contem = any(url in toot
                 for toot in urls_postadas)
    if not contem:
        mastodon_bot.toot(lista_frases(url=url, orgao=orgao))
        # Lugar reservado para tweetar, caso queiram.
