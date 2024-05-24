import os
import time
import onnx

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
  
  trtLogger = trt.Logger(trt.Logger.INFO)
  trtBuilder = trt.Builder(trtLogger)
  trtNetwork = trtBuilder.create_network(0)
  onnxParser = trt.OnnxParser(trtNetwork, trtLogger)
  timeStamp.stampPrint(f'SETUP:')
  
  parsedSuccess = onnxParser.parse_from_file(modelPath)
  for idx in range(onnxParser.num_errors):
    print(onnxParser.get_error(idx))
  timeStamp.stampPrint(f'PARSED: {parsedSuccess}')
  
  if parsedSuccess:
    trtConfig = trtBuilder.create_builder_config()
    serializedEngine = trtBuilder.build_serialized_network(trtNetwork, trtConfig)
    timeStamp.stampPrint(f'CREATE SERIALIZE ENGINE:')

    enginePath = 'sample.engine'
    with open(enginePath, 'wb') as f:
      f.write(serializedEngine)
      timeStamp.stampPrint(f'SAVE SERIALIZE ENGINE:')
      
    model = onnx.load("path/to/model.onnx")
    inputShapes = [[d.dim_value for d in _input.type.tensor_type.shape.dim] for _input in model.graph.input]
    stringShape = 'x'.join(inputShapes[0])
    validateResult = os.system(f'trtexec --shapes=input:{stringShape} --loadEngine={enginePath}')
    if validateResult != 0:
      print('VALIDATION FAILED')
    timeStamp.stampPrint(f'VALIDATE ENGINE:')

    with open(enginePath, 'rb') as f:
      serializedEngine = f.read()
      timeStamp.stampPrint(f'LOAD SERIALIZE ENGINE:')
    
    runtime = trt.Runtime(trtLogger)
    engine = runtime.deserialize_cuda_engine(serializedEngine)
    context = engine.create_execution_context()
    # context.set_tensor_address(name, ptr)
