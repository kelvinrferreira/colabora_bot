import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('./conf_files') / '.env'
load_dotenv(dotenv_path=env_path,override=True)

# [Twitter API Keys]
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
