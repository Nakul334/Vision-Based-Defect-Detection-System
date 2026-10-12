import os
import sys
from ultralytics import YOLO

def export_model():
    best_model_path = os.path.join("runs", "obb", "runs", "obb", "defect_detection", "weights", "best.pt")
    
    if not os.path.exists(best_model_path):
        print(f"Error: Trained model not found at {best_model_path}")
        print("Please run train.py to train the model first.")
        sys.exit(1)

    print(f"Loading trained model: {best_model_path}")
    try:
        model = YOLO(best_model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

    print("\nExporting model to ONNX format...")
    print("This format is suitable for deployment with OpenCV, ROS2, industrial cameras, and robot vision pipelines.")
    
    try:
        # Export the model
        # Using export parameters suitable for production
        export_path = model.export(
            format="onnx",
            imgsz=640,          # Ensure input size matches training
            half=False,         # Use FP32. Set to True for FP16 optimization if target device supports it
            dynamic=False,      # Fixed input size is generally faster
            simplify=True       # Simplify the ONNX model for better compatibility
        )
        
        print(f"\nModel successfully exported to: {export_path}")
        print("You can now use this ONNX model for deployment.")
        
    except Exception as e:
        print(f"Error exporting model: {e}")
        sys.exit(1)

if __name__ == "__main__":
    export_model()
