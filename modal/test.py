import requests
from dotenv import load_dotenv
load_dotenv()
import os

containerType = 't4-build'
appName = os.environ['APP_NAME']
modalWorkspace = os.environ['MODAL_WORKSPACE']
res = requests.get(f'https://{modalWorkspace}--{appName}-{containerType}.modal.run')
