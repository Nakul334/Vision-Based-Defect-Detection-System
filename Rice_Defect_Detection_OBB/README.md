# YOLOv8-OBB Defect Detection System

This project implements an industrial quality inspection and robotic vision system to detect small surface defects (e.g., wrinkle, scratch, hole, dot) on rice cases using Oriented Bounding Boxes (OBB).

## Project Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Download Dataset:**
   The dataset is hosted on Roboflow. Run the download script to fetch the YOLOv8-OBB formatted dataset.
   ```bash
   python download_dataset.py
   ```
   *Note: This requires the Roboflow API key which is hardcoded in the script.*

## Workflow

### 1. Training the Model
Train the `yolov8s-obb.pt` model on the downloaded dataset. The script will automatically check for GPU availability and optimize for small object detection.
```bash
python train.py
```
*The best model will be saved at: `runs/obb/defect_detection/weights/best.pt`*

### 2. Validation
Evaluate the trained model's performance (Precision, Recall, mAP) on the validation set, including class-wise accuracies.
```bash
python validate.py
```

### 3. Batch Prediction
Run predictions on a folder of validation images and save the outputs with drawn rotated bounding boxes and confidence scores.
```bash
python predict.py
```

### 4. Single Image Testing
Test the model on a specific image and print out the detected defect locations (OBB coordinates) and confidence scores.
```bash
python test_image.py path/to/your/image.jpg
```
*The annotated image will be saved to the `outputs/` directory.*

### 5. Export for Deployment
Export the trained `.pt` model to ONNX format for deployment with OpenCV, ROS2, or robotic vision pipelines.
```bash
python export_model.py
```

## Error Handling
The scripts include robust error handling to notify you if:
- The dataset is missing (run `download_dataset.py` first)
- No GPU is available (warns about slow training)
- The YOLO model task is incorrect
- The trained `best.pt` weights are missing
