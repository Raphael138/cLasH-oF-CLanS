from ultralytics import YOLO

# Load a pretrained model 
model = YOLO('yolov8n.pt')

# Train and test model 
results = model.train(data='coc.yaml', epochs=10)