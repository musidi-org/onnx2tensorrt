# Onnx2tensorrt
Self hostable service to convert an ONNX model to TensorRT engine.

## Deployment
Server deployment is mandatory for running this app. The fullstack app does not need to be deployed.

### Server deployment
1. Create a [Modal](https://modal.com/) account.
Low usage should fit within the $30 monthly free tier.

2. Create `.env` file in project root for Modal backend deployment:
```
APP_NAME=
MODAL_WORKSPACE=
```

3. Install python package and deploy:
```
poetry install
pnpm run deploy:modal
```

4. Create 2 [Cloudflare](https://www.cloudflare.com/) R2 buckets with access key

5. Create a Modal secret:
```
ONNX_BUCKET=
TRT_BUCKET=
S3_ENDPOINT=
S3_KEY_ID=
S3_KEY=
REGION_NAME=auto
```

## Attribution
- [Modal](https://modal.com/) - Serverless GPU FAAS platform.
- [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/quick-start-guide/index.html#convert-onnx-engine) - Build fast ML models for Nvidia GPU