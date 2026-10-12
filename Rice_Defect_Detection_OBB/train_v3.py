import os
import sys
import torch
from ultralytics import YOLO

def train_model_v3():
    try:
        print("Checking GPU Availability...")
        is_gpu_available = torch.cuda.is_available()
        print(f"GPU Available: {is_gpu_available}")
        
        if is_gpu_available:
            print(f"GPU Name: {torch.cuda.get_device_name(0)}")
            device = 0
        else:
            print("WARNING: No GPU detected! Training on CPU will be very slow.")
            device = 'cpu'

        model_name = "yolov8s-obb.pt"
        print(f"\nLoading model: {model_name}")
        model = YOLO(model_name)

        if model.task != "obb":
            print(f"Error: Model task is '{model.task}', expected 'obb'. Please use a YOLOv8-OBB model.")
            sys.exit(1)
        
        print(f"Model Task: {model.task}")

        data_yaml = "dataset/data.yaml"
        if not os.path.exists(data_yaml):
            print(f"Error: Dataset configuration file not found at {data_yaml}")
            sys.exit(1)

        print("\nStarting Training for Defect Detection V3 (OBB)...")
        print("Applying industrial hyperparameter tuning for small objects...")

        # Train model with advanced hyperparams
        results = model.train(
            data=data_yaml,
            epochs=100,
            imgsz=640,
            batch=8,  # Safe batch size for 4GB VRAM at 640x640
            device=device,
            optimizer="AdamW",
            lr0=0.001,
            cos_lr=True,
            patience=50,
            mosaic=0.0,
            close_mosaic=0,
            degrees=5.0,
            translate=0.05,
            scale=0.2,
            fliplr=0.5,
            project="runs/obb",
            name="defect_v4"
        )

        print("\nTraining completed successfully!")
        best_model_path = os.path.join("runs", "obb", "defect_v4", "weights", "best.pt")
        print(f"Best model saved to: {best_model_path}")
        
    except Exception as e:
        print(f"Error during training: {e}")
        sys.exit(1)

if __name__ == "__main__":
    train_model_v3()
