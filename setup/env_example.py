# RENAME THIS FILE TO env.py
import os

os.environ['SECRET_KEY'] = 'your-key'
os.environ['DEBUG'] = '1' # '' is false
os.environ['ALLOWED_HOSTS'] = f'["127.0.0.1", "localhost"]'
os.environ['LANGUAGE_CODE'] = 'pt-br'
os.environ['TIME_ZONE'] = 'America/Sao_Paulo'