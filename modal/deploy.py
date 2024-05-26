from modal import Image, App, web_endpoint, Secret
from dotenv import load_dotenv
load_dotenv()
import os

from util import tuneModel

app = App(name=os.environ.get('APP_NAME'))
image = Image.from_registry(
  'nvcr.io/nvidia/tensorrt:24.04-py3',
  add_python="3.11"
).pip_install(
  'python-dotenv==1.0.1', 'boto3==1.34.112'
)

timeout = 60 * 60 * 3

@app.function(
  image=image,
  secrets=[Secret.from_name("onnx2tensorrt")],
  container_idle_timeout=2,
  timeout=timeout,
  cpu=0.25,
  gpu='t4'
)
@web_endpoint()
def t4_build(key: str = 'test.onnx'):
  tuneModel(key)
