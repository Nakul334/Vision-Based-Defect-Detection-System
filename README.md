# Vision-Based Defect Detection System for Industrial Quality Inspection

[![Architecture](https://img.shields.io/badge/Architecture-YOLOv8--OBB-blue.svg)](https://github.com/ultralytics/ultralytics)
[![Accuracy](https://img.shields.io/badge/mAP50-97.55%25-brightgreen.svg)]()
[![Inference Speed](https://img.shields.io/badge/Inference-41.6%20FPS-orange.svg)]()
[![Dataset](https://img.shields.io/badge/Dataset-5%2C065%20Images-purple.svg)]()

> **Major Project-I**  
> **Student:** Nakul S. Dube (Enrollment No.: DMET1323009 / C2023FE00055)  
> **Supervisor / H.O.D / Dean Academics:** Dr. Utkarsha Pacharaney  
> **Coordinators:** Dr. Swapnil Gundewar, Dr. Subodh Daronde  
> **Department:** Department of Artificial Intelligence and Machine Learning  
> **Institution:** Faculty of Engineering and Technology, Adani Institute of Higher Education and Research (DU), Sawangi (Meghe), Wardha, Maharashtra – 442107  
> **Session:** October 2026  

---

## 📌 Project Overview

Automated surface quality assurance in high-throughput food container and packaging manufacturing requires robust, sub-millimeter flaw localization capable of handling arbitrary spatial orientations. Conventional machine vision frameworks predominantly rely on horizontal axis-aligned bounding boxes (HBB), which encompass substantial extraneous background noise when encapsulating slender, diagonally oriented flaws (such as scratches, edge fissures, and material wrinkles). This background noise causes severe feature dilution, resulting in prohibitive miss rates for micro-defects.

This repository implements an end-to-end industrial robotic vision inspection pipeline driven by an optimized **YOLOv8 Oriented Bounding Box (YOLOv8-OBB)** deep neural network developed specifically for thermoformed and injection-molded rice packaging casings.

---

## 🚀 Key Experimental Findings & Quantitative Metrics

* **Detection Accuracy:** Boosted overall mean Average Precision (**mAP50**) from baseline **49.02% to 97.55%**.
* **Micro-Defect Sensitivity:** Skyrocketed critical micro-scratch recall and precision from **12.61% to 95.85%**.
* **High-Throughput Edge Latency:** Achieved **24.0 ms** total pipeline cycle latency (**41.6 FPS**) on embedded industrial nodes via ONNX Runtime & TensorRT engine compilation.
* **Deterministic Synchronization:** Real-time ROS2 / PLC middleware communication trigger for downstream pneumatic ejection actuators (< 25 ms cycle time, supporting line speeds > 120 units/minute).
* **Industrial Flaw Taxonomy:** Evaluated across nine annotated industrial flaw categories:
  * Black dots, defective foreign bodies, flange bad cutting, insects, intense scratches, pinholes, scratches, shrivel wrinkles, and yellow points.

---

## 📊 Output Visualizations & Defect Inspections

| Evaluation Metric | Visual Result |
| :--- | :--- |
| **Training & Loss Convergence** | ![Training Convergence](output_images/training_curves.png) |
| **Normalized Confusion Matrix** | ![Confusion Matrix](output_images/confusion_matrix.png) |
| **Precision-Recall Curve (OBB)** | ![PR Curve](output_images/BoxPR_curve.png) |
| **Validation Predictions Batch** | ![Validation Predictions](output_images/val_batch0_pred.jpg) |
| **Representative Flaw Samples** | ![Defect Samples](output_images/composite_defect_samples.jpg) |

---

## 📂 Repository Structure

```text
├── Rice_Defect_Detection_OBB/          # YOLOv8-OBB model pipeline & execution scripts
│   ├── train.py                        # Model training routine
│   ├── validate.py                     # Metric validation script
│   ├── predict.py                      # Defect inference script
│   ├── export_model.py                 # ONNX / TensorRT export
│   └── requirements.txt                # Python dependencies
├── output_images/                      # Output figures, curves & defect inspection samples
│   ├── training_curves.png             # Loss and mAP convergence graphs
│   ├── confusion_matrix.png            # Multi-class confusion matrix
│   ├── BoxPR_curve.png                 # Precision-recall curves
│   ├── val_batch0_pred.jpg             # Model validation detection samples
│   └── composite_defect_samples.jpg    # Sample container surface defects
├── data.yaml                           # YOLOv8 dataset configuration
├── README.roboflow.txt                 # Dataset export metadata
└── README.md                           # Project documentation
```

---

## ⚙️ Model Pipeline & Setup

```bash
# Clone the repository
git clone https://github.com/Nakul334/Vision-Based-Defect-Detection-System.git
cd Vision-Based-Defect-Detection-System

# Install Ultralytics YOLOv8
pip install ultralytics

# Run OBB validation
yolo obb val model=yolov8m-obb.pt data=data.yaml
```
