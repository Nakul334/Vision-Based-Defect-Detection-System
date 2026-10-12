import os
import shutil
import sys
from roboflow import Roboflow

def download_data():
    try:
        # Define dataset directory
        dataset_dir = "dataset"
        
        # Remove old dataset if it exists to avoid conflicts
        if os.path.exists(dataset_dir):
            print(f"Removing old dataset directory: {dataset_dir}...")
            shutil.rmtree(dataset_dir)
            
        print("Initializing Roboflow...")
        rf = Roboflow(api_key="g0NC8mdsIMUgtzz9fkHX")
        
        print("Connecting to workspace 'juggank2' and project 'rice_case_01'...")
        project = rf.workspace("juggank2").project("rice_case_01")
        
        print("Fetching version 4...")
        version = project.version(4)
        
        print("Downloading dataset in yolov8-obb format...")
        # Note: Roboflow download might extract directly into the current directory
        # depending on the setup. We will define the location if possible.
        dataset = version.download("yolov8-obb", location=dataset_dir)
        
        print(f"Dataset downloaded successfully to {dataset_dir}.")
        
        # Check dataset structure
        if not os.path.exists(dataset_dir):
            print(f"Error: Dataset directory {dataset_dir} not found after download.")
            sys.exit(1)
            
        print("Dataset structure:")
        for root, dirs, files in os.walk(dataset_dir):
            level = root.replace(dataset_dir, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files[:3]:
                print(f"{subindent}{f}")
            if len(files) > 3:
                print(f"{subindent}...")
                
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_data()
