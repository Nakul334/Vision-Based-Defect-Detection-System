import os
import sys
import glob
from ultralytics import YOLO

def run_predictions():
    best_model_path = os.path.join("runs", "obb", "runs", "obb", "defect_detection", "weights", "best.pt")
    
    if not os.path.exists(best_model_path):
        print(f"Error: Trained model not found at {best_model_path}")
        print("Please run train.py to train the model first.")
        sys.exit(1)

    print(f"Loading trained model: {best_model_path}")
    try:
        best_model = YOLO(best_model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

    # Use the validation set images as the source for batch prediction
    # Or you can change this to a directory of new images
    source_dir = os.path.join("dataset", "valid", "images")
    if not os.path.exists(source_dir):
        print(f"Error: Source directory {source_dir} not found.")
        sys.exit(1)

    print(f"\nRunning prediction on images in: {source_dir}")
    print("This will output images with rotated bounding boxes, defect names, and confidence percentage.")
    
    try:
        # Run prediction
        # Results are automatically saved to runs/obb/predict
        results = best_model.predict(
            source=source_dir,
            save=True,
            conf=0.25, # Confidence threshold
            project=os.path.join("runs", "obb"),
            name="predict"
        )
        
        print("\nPrediction complete!")
        print("Output images have been saved to the latest runs/obb/predict directory.")
        
    except Exception as e:
        print(f"Error during prediction: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_predictions()
