from random import choice

#Lista de frases que o robô vai twittar

def tweet_orgao(url, orgao):
    com_orgao = [
        f"🤖 O portal com dados públicos [ {url} ] do órgão {orgao} parece não estar funcionando. Poderia me ajudar a checar?",
        f"🤖 Hum, parece que o site [ {url} ], mantido pelo órgão {orgao}, está apresentando erro. Poderia dar uma olhadinha?",
        f"🤖 Poxa, tentei acessar [ {url} ] e não consegui. Este site é mantido pelo órgão {orgao}. Você pode confirmar isso?",
        f"🤖 Não consigo acessar [ {url} ], e eu sei que ele é mantido pelo órgão {orgao}. Você pode me ajudar a verificar?",
        f"🤖 Sabe o portal [ {url} ], mantido pelo orgão {orgao}? Ele parece estar fora do ar. Você pode confirmar?"]
    msg_orgao = choice(com_orgao)
    return msg_orgao


def tweet_arroba(url, arroba):
    com_arroba = [
        f"🤖 Parece que [ {url} ] está apresentando probleminhas para ser acessado. O que está acontecendo {arroba}?",
        f"🤖 Oi {arroba}, tudo bem? Pois com esse site [ {url} ] parece não estar, já que ele possui problemas de acesso.",
        f"🤖 Portais da transparência são um direito ao acesso à informação {arroba}, mas parece que [ {url} ] está fora do ar.",
        f"🤖 Opa {arroba}, parece que o site [ {url} ] não está acessível como deveria. O que está acontecendo?",
        f"🤖 Tentei acessar o site [ {url} ] e não consegui. {arroba} está acontecendo algum problema com essa portal de transparência?"]
    msg_arroba = choice(com_arroba)
    return msg_arroba