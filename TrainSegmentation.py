from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

results = model.train(
    data='../datasets/Apples-dataset/apple_v8.yaml',
    epochs=200,
    patience=30,
    name='apple_yolov8'
  )

print('done')