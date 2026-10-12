import os
import sys
from ultralytics import YOLO

def validate_model():
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

    data_yaml = "dataset/data.yaml"
    if not os.path.exists(data_yaml):
        print(f"Error: Dataset configuration file not found at {data_yaml}")
        sys.exit(1)

    print("\nStarting Validation...")
    try:
        # Validate model
        metrics = best_model.val(data=data_yaml)

        # Print overall metrics
        print("\n--- Validation Results ---")
        print(f"mAP50:     {metrics.box.map50:.4f}")
        print(f"mAP50-95:  {metrics.box.map:.4f}")
        
        # Calculate precision and recall across all classes
        # Note: metrics.box.p and metrics.box.r return arrays per class, mean() gives overall
        p = metrics.box.p.mean() if len(metrics.box.p) > 0 else 0
        r = metrics.box.r.mean() if len(metrics.box.r) > 0 else 0
        print(f"Precision: {p:.4f}")
        print(f"Recall:    {r:.4f}")

        # Class-wise performance
        print("\n--- Class-wise Performance ---")
        class_names = best_model.names
        
        # Depending on ultralytics version, metrics.box.maps might contain AP50-95 per class
        # We can extract precision, recall, mAP50, and mAP50-95 per class
        for i, class_idx in enumerate(metrics.box.ap_class_index):
            name = class_names[class_idx]
            cls_p = metrics.box.class_result(i)[0]
            cls_r = metrics.box.class_result(i)[1]
            cls_ap50 = metrics.box.class_result(i)[2]
            cls_ap = metrics.box.class_result(i)[3]
            
            print(f"{name.capitalize()} Accuracy:")
            print(f"  Precision: {cls_p:.4f}")
            print(f"  Recall:    {cls_r:.4f}")
            print(f"  mAP50:     {cls_ap50:.4f}")
            print(f"  mAP50-95:  {cls_ap:.4f}")
            print()

    except Exception as e:
        print(f"Error during validation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate_model()
