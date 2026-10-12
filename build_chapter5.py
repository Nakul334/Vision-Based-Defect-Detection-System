"""
Chapter 5: Conclusion and Future Direction Module for Major Project Report.
Covers 5.1 Achievement of Objectives, 5.2 Key Project Outcomes, and 5.3 Future Direction.
"""

from common_styles import add_p, add_h1, add_h2, add_bullet

def add_chapter_5(doc):
    add_h1(doc, "Chapter 5", is_chapter=True)
    add_h1(doc, "Conclusion and Future Direction", is_chapter=True)
    
    add_p(doc,
        "This Major Project-I report has developed, rigorously evaluated, and experimentally validated an end-to-end "
        "automated robotic vision inspection system for precision surface defect detection on thermoformed industrial packaging casings. "
        "By replacing conventional horizontal bounding boxes with an orientation-aware YOLOv8-OBB architecture and identifying the "
        "destructive impact of spatial mosaic augmentation on micro-defects, this research resolves longstanding feature dilution "
        "bottlenecks in automated optical quality assurance."
    )
    
    # 5.1 Achievement of Research Objectives
    add_h2(doc, "5.1 Achievement of Research Objectives")
    add_p(doc,
        "The project has successfully fulfilled all five targeted research and engineering objectives formulated in Chapter 1:"
    )
    add_bullet(doc,
        "Compiled and validated an exhaustive industrial benchmark dataset of 5,065 high-resolution images annotated across nine defect "
        "classes with ground-truth oriented bounding polygons [x, y, w, h, theta], capturing 24,477 total defect instances.",
        bold_prefix="Achievement of Objective 1 (Dataset Engineering):"
    )
    add_bullet(doc,
        "Designed and fabricated an industrial optomechanical imaging enclosure integrating coaxial diffuse ring LED lighting, "
        "telecentric optics, and high-speed optical triggering that completely eliminates ambient lighting variance and specular reflections.",
        bold_prefix="Achievement of Objective 2 (Optomechanical Station):"
    )
    add_bullet(doc,
        "Formulated and implemented an optimized single-stage YOLOv8-OBB model incorporating decoupled orientation heads, Gaussian "
        "Wasserstein Distance (GWD) loss, Varifocal classification loss (VFL), and Distribution Focal Loss (DFL), eliminating angular boundary "
        "discontinuities.",
        bold_prefix="Achievement of Objective 3 (Model Formulation):"
    )
    add_bullet(doc,
        "Discovered and empirically demonstrated that deactivating spatial Mosaic augmentation and constraining geometric scaling prevents "
        "the collapse of sub-pixel scratch features, elevating micro-scratch mAP50 by an extraordinary +83.24 percentage points.",
        bold_prefix="Achievement of Objective 4 (Augmentation Optimization):"
    )
    add_bullet(doc,
        "Serialized and deployed the trained model via ONNX-Slim and TensorRT FP16 on an industrial edge computer with ROS2 middleware and PLC "
        "synchronization, achieving a deterministic 24.0 ms cycle latency (41.6 FPS) and enabling real-time pneumatic ejection.",
        bold_prefix="Achievement of Objective 5 (Edge Deployment & Actuation):"
    )
    
    # 5.2 Key Project Outcomes
    add_h2(doc, "5.2 Key Project Outcomes")
    add_p(doc,
        "The empirical investigations and factory validation yielded the following landmark quantitative outcomes:"
    )
    add_bullet(doc,
        "The optimized YOLOv8-OBB model achieved an overall mean Average Precision at IoU 0.50 (mAP50) of 97.55% across all nine defect "
        "categories, outperforming the baseline generic model (49.02%) by +48.53 percentage points.",
        bold_prefix="• Landmark mAP50 Accuracy of 97.55%:"
    )
    add_bullet(doc,
        "Detection mAP50 on slender micro-scratch abrasions surged from 12.61% to 95.85% (+83.24%), resolving the most critical defect "
        "escape vulnerability in packaging manufacturing.",
        bold_prefix="• Micro-Scratch Detection Rate Elevated to 95.85%:"
    )
    add_bullet(doc,
        "The edge-optimized TensorRT inference pipeline delivers a deterministic end-to-end processing latency of 24.0 ms (41.6 FPS), "
        "comfortably satisfying the 25.0 ms line cycle threshold for 120 units/minute conveyor sorting.",
        bold_prefix="• Deterministic 24.0 ms Real-Time Edge Latency:"
    )
    add_bullet(doc,
        "The factory defect escape rate plummeted from 14.5% (manual inspection) and 8.2% (horizontal AOI) to an ultra-low 0.3%, virtually "
        "eliminating commercial product recall risks.",
        bold_prefix="• Defect Escape Rate Reduced to 0.3%:"
    )
    add_bullet(doc,
        "Economic modeling demonstrates annual net operational savings of $532,000 for a 63M units/year facility, achieving full capital "
        "investment payback within 4.2 months.",
        bold_prefix="• Rapid Economic Payback of 4.2 Months:"
    )
    
    # 5.3 Future Direction
    add_h2(doc, "5.3 Future Direction")
    add_p(doc,
        "While the current system achieves industry-leading performance on visible surface anomalies, several promising research avenues "
        "will be pursued in subsequent development phases:"
    )
    add_bullet(doc,
        "Integrating Short-Wave Infrared (SWIR, 900–1700 nm) or hyperspectral illumination to inspect multi-layer barrier films (such as "
        "EVOH core layers) for internal delaminations and trapped moisture pockets invisible to visible-spectrum optics.",
        bold_prefix="1. Multi-Spectral & Hyperspectral SWIR Imaging:"
    )
    add_bullet(doc,
        "Implementing post-training INT8 and FP8 quantization via TensorRT with calibration-aware training to compress model size to under "
        "10 MB and reduce inference latency below 12 ms, enabling deployment on ultra-low-power micro-edge microcontrollers.",
        bold_prefix="2. INT8 / FP8 Edge Quantization:"
    )
    add_bullet(doc,
        "Expanding the downstream rejection station from simple pneumatic blow-off nozzles to a high-speed 6-DoF delta robot arm equipped "
        "with adaptive soft-pneumatic grippers, enabling gentle extraction of delicate or heavy packaging containers without deformation.",
        bold_prefix="3. 6-DoF Robotic Gripper Integration:"
    )
    add_bullet(doc,
        "Applying few-shot transfer learning and domain adaptation techniques to generalize the trained YOLOv8-OBB backbone to pharmaceutical "
        "blister packs, medical syringe trays, and semiconductor carrier tapes with minimal retraining.",
        bold_prefix="4. Cross-Domain Transfer Learning to Medical Packaging:"
    )

print("Chapter 5 module defined successfully.")
