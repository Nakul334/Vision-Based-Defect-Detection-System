import os
import sys
import torch
from ultralytics import YOLO

def train_model():
    try:
        # Check GPU Availability
        print("Checking GPU Availability...")
        is_gpu_available = torch.cuda.is_available()
        print(f"GPU Available: {is_gpu_available}")
        
        if is_gpu_available:
            print(f"GPU Name: {torch.cuda.get_device_name(0)}")
            device = 0
        else:
            print("WARNING: No GPU detected! Training on CPU will be very slow.")
            device = 'cpu'

        # Load YOLOv8-OBB model
        # Using yolov8s-obb.pt as requested, not yolov8n.pt
        model_name = "yolov8s-obb.pt"
        print(f"\nLoading model: {model_name}")
        model = YOLO(model_name)

        # Verify model task is OBB
        if model.task != "obb":
            print(f"Error: Model task is '{model.task}', expected 'obb'. Please use a YOLOv8-OBB model.")
            sys.exit(1)
        
        print(f"Model Task: {model.task}")

        # Check dataset path
        # Assume download_dataset.py downloaded it to dataset/
        data_yaml = "dataset/data.yaml"
        if not os.path.exists(data_yaml):
            print(f"Error: Dataset configuration file not found at {data_yaml}")
            print("Please run download_dataset.py first.")
            sys.exit(1)

        print("\nStarting Training for Defect Detection (OBB)...")
        print("Optimizing for small object detection with imgsz=640")

        # Train model
        results = model.train(
            data=data_yaml,
            epochs=100,
            imgsz=640,
            batch=16,
            device=device,
            project="runs/obb",
            name="defect_detection"
        )

        print("\nTraining completed successfully!")
        best_model_path = os.path.join("runs", "obb", "defect_detection", "weights", "best.pt")
        print(f"Best model saved to: {best_model_path}")
        
    except Exception as e:
        print(f"Error during training: {e}")
        sys.exit(1)

if __name__ == "__main__":
    train_model()
