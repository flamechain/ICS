from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    DEBUG = bool(os.getenv('DEBUG'))
    KEY = str(os.getenv('KEY'))
    SERVER = os.getenv('SERVER')
    PORT = int(os.getenv('PORT'))
