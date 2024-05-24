import os
import time
from dotenv import load_dotenv
load_dotenv()

from bucketFile import downloadBucketFile, uploadBucketFile

def createFile(filePath):
  if not os.path.exists(filePath): 
    with open(filePath, 'w') as file: 
      file.write('')

def fileBaseName(filePath):
  fileName = os.path.basename(filePath)
  return os.path.splitext(fileName)[0]

class TimeStamp:
  def __init__(self) -> None:
    self.startTime = time.time()
    
  def stamp(self):
    timeGap = time.time() - self.startTime
    self.startTime = time.time()
    return timeGap
  
  def stampPrint(self, log):
    timeGap = self.stamp()
    print(f'\n\n\n{log}:', timeGap, '\n\n\n')
    return timeGap

def tuneModel(modelKey):
  modelPath = 'test.onnx'
  enginePath = f'{modelPath}.trt'
  timeStamp = TimeStamp()
  
  downloadBucketFile(modelPath, os.environ['ONNX_BUCKET'], modelKey)
  timeStamp.stampPrint(f'DOWNLOAD ONNX MODEL:')

  conversionResult = os.system(f'trtexec --onnx={modelPath} --fp16 --saveEngine={enginePath}')
  if conversionResult != 0:
    print('CONVERSION FAILED')
  timeStamp.stampPrint(f'CREATE TENSORRT ENGINE:')
  
  validateResult = os.system(f'trtexec --loadEngine={enginePath}')
  if validateResult != 0:
    print('VALIDATION FAILED')
  timeStamp.stampPrint(f'VALIDATE ENGINE:')
  
  engineKey = f'{modelKey}.trt'
  uploadBucketFile(enginePath, os.environ['TRT_BUCKET'], engineKey)
  timeStamp.stampPrint(f'UPLOAD TRT ENGINE:')
