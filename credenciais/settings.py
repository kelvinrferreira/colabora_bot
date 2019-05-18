import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('./credenciais') / '.env'
load_dotenv(dotenv_path=env_path, override=True)

debug = os.getenv("DEBUG", False)
# [Twitter API Keys]
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# [Mastodon API Key]
mastodon_key = os.environ.get('DONTE_USERCRED')

# [Plataforms IDs]
mastodon_profile_id = os.environ.get('ID_CONTA_MASTODON')
