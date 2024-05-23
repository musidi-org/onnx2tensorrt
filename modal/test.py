import requests
from dotenv import load_dotenv
load_dotenv()
import os

containerType = 't4-1'
appName = os.environ.get('APP_NAME')
modalWorkspace = os.environ.get('MODAL_WORKSPACE')
res = requests.get(f'https://{modalWorkspace}--{appName}-{containerType}.modal.run')
