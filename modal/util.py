import os
import time

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



def tuneModel(modelPath):
  import tensorrt as trt
  timeStamp = TimeStamp()
  
  trtLogger = trt.Logger(trt.Logger.WARNING)
  trtBuilder = trt.Builder(trtLogger)
  trtNetwork = trtBuilder.create_network(0)

  onnxParser = trt.OnnxParser(trtNetwork, trtLogger)
  parsedSuccess = onnxParser.parse_from_file(modelPath)
  timeStamp.stampPrint(f'PARSED: {parsedSuccess}')
  
  return
