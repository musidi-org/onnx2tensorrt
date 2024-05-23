from modal import Image, App, web_endpoint
from dotenv import load_dotenv
load_dotenv()
import os

from util import tuneModel
import package

app = App(name=os.environ.get('APP_NAME'))
image = Image.from_registry(
  'nvcr.io/nvidia/tensorrt:24.02-py3',
  add_python="3.11"
).pip_install(
  'python-dotenv==1.0.1', 'tensorrt==10.0.1'
)

timeout = 60 * 60 * 12

@app.function(image=image, container_idle_timeout=2, timeout=timeout, cpu=1, gpu='t4')
@web_endpoint()
def t4_1():
  return tuneModel('package/test.onnx')
