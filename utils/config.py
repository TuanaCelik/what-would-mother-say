import os
from dotenv import load_dotenv

load_dotenv()
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
SERPER_KEY = os.getenv('SERPER_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')