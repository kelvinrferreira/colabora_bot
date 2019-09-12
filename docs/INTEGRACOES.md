## Integrações do bot
Aqui estão descritas as integrações do bot. 
> Aviso: Essas configurações são opicionais para o funcionamento do bot em modo DEBUG.

### No Twitter

Você deverá obter suas tokens para usar a API do Twitter: 

1. Crie sua conta normalmente, caso não a tenha. 
2. Em seguida solicite uma developer account [aqui](https://developer.twitter.com/en/apply/user). 

Hoje a requisição pode demorar dias (e há relatos de pessoas que nunca receberam). Seja o mais descritivo possível com relação ao seu projeto e fique atento aos e-mails, pois o Twitter poderá pedir informações adicionais. Também é por email que o Twitter avisará que sua requisição foi aceita. Caso isso aconteça: comemore (uhull!) e crie um app clicando [aqui](https://developer.twitter.com/en/apps). Desta forma você terá acesso as suas tokens que são: consumer_key, consumer_secret, access_token e access_token_secret.

Coloque suas tokens no arquivo `.env` conforme o exemplo.

### No Mastodon

1. Crie uma conta na instância de sua preferência. Nós escolhemos a [Bots in Space](https://botsin.space/about/more), mas o procedimento deve ser semelhante para qualquer outra. Certifique-se que o bot que você está configurando não irá infringir os termos de conduta da instância de sua escolha, já que as regras podem ser diferentes!

2. Registre o seu bot na instância rodando o código abaixo:

```python
from mastodon import Mastodon

Mastodon.create_app(
     'colaborabot',
     api_base_url = 'https://botsin.space',
     to_file = 'colaboradonte_clientcred.secret'
)
```

Em seguida, rode o código a seguir:

```python
from mastodon import Mastodon

mastodon = Mastodon(
    client_id = 'colaboradonte_clientcred.secret',
    api_base_url = 'https://botsin.space'
)
mastodon.log_in(
    'seu_login@servidor.com',
    'senhamuitoboaesupersegura',
    to_file = 'colaboradonte_usercred.secret'
)
```

Certifique-se de modificar os parâmetros conforme necessário.

3. Recupere as chaves criadas `pytooter_clientcred.secret` e `pytooter_usercred.secret` as insira no arquivo `.env`

* [Documentação original](https://mastodonpy.readthedocs.io/en/stable/#) da biblioca usada para autenticação.

### Google Sheets

Para utilizar o Google Sheets, utilizamos a biblioteca [gspread](https://gspread.readthedocs.io/en/latest/) juntamente com a [Authlib](https://blog.authlib.org/2018/authlib-for-gspread) para autenticação.

1. O primeiro passo é conseguir um token de acesso de aplicação do Google Sheets. Acesse o [Google API Console](https://console.developers.google.com/project) e crie um projeto (ou selecione um que você já tenha criado).

2. No menu do lado esquerdo, selecione "Credenciais" e clique no botão "Criar credenciais", escolhendo a opção de "Chave de conta de serviço". Escolha o formato json e salve o arquivo em seu computador.

3. Este arquivo deverá ser inserido na pasta `credenciais\colaborabot-gAPI.json`, assim como está descrito no programa `autenticadores.py`.