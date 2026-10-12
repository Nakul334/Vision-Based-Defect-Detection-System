import os
import sys
import argparse
from ultralytics import YOLO

def test_single_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        sys.exit(1)

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

    print(f"\nProcessing image: {image_path}")
    try:
        # Run inference
        results = model(image_path)
        
        # Process results
        for result in results:
            print("\nDetected defects:")
            print("-----------------")
            
            # Extract OBB predictions
            # result.obb contains xywhr or xyxyxyxy coordinates, confidences, and classes
            if result.obb is not None and len(result.obb) > 0:
                # Iterate through each detection
                for i in range(len(result.obb)):
                    # Get class index, confidence, and OBB coordinates
                    cls_id = int(result.obb.cls[i].item())
                    cls_name = model.names[cls_id]
                    conf = result.obb.conf[i].item()
                    
                    # Coordinates in xywhr format (center x, center y, width, height, rotation)
                    coords = result.obb.xywhr[i].tolist()
                    
                    print(f"{cls_name.capitalize()} detected")
                    print(f"confidence: {conf:.2f}")
                    print("Location:")
                    print(f"OBB coordinates (x_c, y_c, w, h, r): {coords}")
                    print("-" * 20)
                
                # Save the image with boxes
                output_dir = "outputs"
                os.makedirs(output_dir, exist_ok=True)
                save_path = os.path.join(output_dir, f"tested_{os.path.basename(image_path)}")
                result.save(filename=save_path)
                print(f"\nOutput image saved to: {save_path}")
            else:
                print("No defects detected.")
                
    except Exception as e:
        print(f"Error during inference: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test YOLOv8-OBB model on a single image.")
    parser.add_argument("image_path", type=str, help="Path to the input image")
    args = parser.parse_args()
    
    test_single_image(args.image_path)
