"""
Chapter 1: Introduction Module for Major Project Report.
Project: Vision-Based Defect Detection System for Industrial Quality Inspection
Author: Nakul S. Dube
Guide: Dr. Swapnil Gundewar | Coordinator: Dr. Subodh Daronde
"""

from common_styles import add_p, add_h1, add_h2, add_h3, add_bullet

def add_chapter_1(doc):
    add_h1(doc, "Chapter 1", is_chapter=True)
    add_h1(doc, "Introduction", is_chapter=True)
    
    add_p(doc, 
        "Automated surface quality assurance in high-throughput food container and packaging manufacturing "
        "represents a critical engineering imperative to guarantee structural hermeticity, preserve shelf-life integrity, "
        "and safeguard consumer health. In modern food manufacturing facilities, packaging containers—specifically "
        "thermoformed and injection-molded polymer casings utilized for ready-to-eat rice meals—are manufactured "
        "at rates exceeding several thousands of units per hour. During these high-speed cyclic thermal and mechanical "
        "forming operations, polymeric casings are susceptible to severe morphological, physical, and particulate anomalies. "
        "These flaws encompass polymer carbonization black dots, guillotine edge-trimming tears, micro-abrasion scratches, "
        "sub-millimeter thermoforming pinholes, structural shrivel wrinkles, and biological contaminants such as insects. "
        "Among these, micro-perforations spanning less than 0.2 mm in diameter and elongated diagonal scratches compromise "
        "the protective atmospheric barrier of the packaging. Such breaches allow oxygen ingress, microbial infiltration, "
        "and moisture migration, precipitating rapid food spoilage, commercial product recalls, and severe brand liability."
    )
    
    add_p(doc,
        "Ensuring complete zero-defect escape in high-speed packaging requires an inspection mechanism capable of detecting, "
        "classifying, and precisely localizing multi-scale anomalies at line speeds exceeding 1.2 m/s. However, the industrial "
        "environment introduces harsh constraints: variable ambient illumination, non-uniform specular reflections across "
        "curved polymeric surfaces, high optical conveyance jitter, and strict edge computational latency budgets. This project "
        "formulates, develops, and experimentally validates a vision-based defect detection system for industrial quality inspection "
        "driven by an optimized YOLOv8 Oriented Bounding Box (YOLOv8-OBB) architecture to overcome these industrial inspection bottlenecks."
    )
    
    # 1.1 Background / Domain Context
    add_h2(doc, "1.1 Background / Domain Context")
    add_p(doc,
        "The food packaging sector constitutes a multi-billion-dollar global enterprise operating under stringent international "
        "sanitary and quality standards (e.g., ISO 22000, HACCP, FDA Title 21). Packaging casings constructed from multi-layer "
        "polypropylene (PP), polyethylene terephthalate (PET), and high-barrier ethylene vinyl alcohol (EVOH) copolymers serve as "
        "the primary line of defense against biological decomposition. As high-speed automated packaging machinery scales production "
        "velocities to meet global consumer demand, the temporal window available for visual inspection shrinks to tens of milliseconds "
        "per unit. Consequently, manual visual inspection and legacy rule-based optical inspection systems have become major operational "
        "bottlenecks in modern packaging facilities."
    )
    
    # 1.1.1 Existing Methods / Technologies
    add_h3(doc, "1.1.1 Existing Methods / Technologies")
    add_p(doc,
        "Industrial quality control on packaging conveyance lines has traditionally relied upon two foundational inspection paradigms:"
    )
    add_bullet(doc,
        "Human visual inspection remains widely deployed across many packaging plants. Human inspectors observe moving conveyor lines "
        "to manually detect and segregate anomalous containers.",
        bold_prefix="Manual Human Visual Inspection:"
    )
    add_bullet(doc,
        "First-generation automated optical inspection systems employ handcrafted image processing operators, including Sobel and "
        "Canny edge detectors, Otsu dynamic thresholding, morphological opening/closing filters, and template matching algorithms. "
        "These algorithms rely on rigid photometric and spatial assumptions to identify contrast variations on container rims and surfaces.",
        bold_prefix="Traditional Rule-Based Automated Optical Inspection (AOI):"
    )
    add_bullet(doc,
        "In recent years, standard deep learning object detectors such as Faster R-CNN, SSD, YOLOv5, and default YOLOv8 have been "
        "introduced to industrial inspection. These detectors employ standard horizontal axis-aligned bounding boxes (HBB) defined by "
        "coordinates [x_min, y_min, x_max, y_max] to delineate defective regions.",
        bold_prefix="Standard Deep Learning Horizontal Detectors (HBB):"
    )
    
    # 1.1.2 Limitations of Existing Methods
    add_h3(doc, "1.1.2 Limitations of Existing Methods")
    add_p(doc,
        "Despite their widespread historical adoption, existing inspection methodologies suffer from severe operational limitations:"
    )
    add_bullet(doc,
        "Human inspection suffers from rapid physiological eye fatigue, cognitive lapses, subjectivity in defect grading, and an inability "
        "to sustain inspection accuracy on conveyor lines moving faster than 0.5 m/s. Empirical studies reveal defect escape rates of 12% to 18% "
        "during sustained human shifts.",
        bold_prefix="Physiological Fatigue and Throughput Ceilings:"
    )
    add_bullet(doc,
        "Classical rule-based algorithms are notoriously brittle when deployed in dynamic factory environments. Curved thermoformed casings "
        "exhibit non-uniform specular reflections, subtle color variations across different polymer batches, and ambient factory lighting "
        "fluctuations. Rule-based edge filters frequently trigger false-positive alarms on harmless surface reflections while missing low-contrast "
        "scratches and pinholes.",
        bold_prefix="Environmental Sensitivity and False Alarm Spikes:"
    )
    add_bullet(doc,
        "Standard horizontal bounding boxes (HBB) present a fundamental geometric mismatch when applied to slender, arbitrarily oriented industrial "
        "flaws such as diagonal scratches, curving flange tears, and oblique shrivel wrinkles. An axis-aligned rectangle enclosing a 45-degree scratch "
        "inevitably encloses up to 85% extraneous non-defective background pixels. This causes severe feature dilution, where the neural network's "
        "convolutional layers average defect gradients with background noise, leading to catastrophic miss rates (empirically exceeding 87% for fine scratches).",
        bold_prefix="Severe Feature Dilution in Axis-Aligned Bounding Boxes:"
    )
    add_bullet(doc,
        "When multiple defects occur in close spatial proximity along container edges, horizontal bounding boxes overlap excessively. During "
        "standard Non-Maximum Suppression (NMS), overlapping boxes suppress valid adjacent defect detections, generating false-negative escapes.",
        bold_prefix="NMS Suppression of Clustered Flaws:"
    )
    
    # 1.2 Aim and Motivation
    add_h2(doc, "1.2 Aim and Motivation")
    
    # 1.2.1 Aim
    add_h3(doc, "1.2.1 Aim")
    add_p(doc,
        "To develop, optimize, and deploy a vision-based defect detection system for industrial quality inspection using an oriented bounding box "
        "deep learning model (YOLOv8-OBB) for high-speed, sub-millimeter surface defect detection on thermoformed industrial packaging casings."
    )
    
    # 1.2.2 Background
    add_h3(doc, "1.2.2 Background")
    add_p(doc,
        "Oriented Bounding Box (OBB) representation extends conventional object detection by predicting an orientation angle parameter "
        "theta in addition to centroid coordinates and dimensions [x, y, w, h, theta]. While widely explored in aerial satellite imagery, "
        "OBB architectures have rarely been adapted for high-speed, resource-constrained industrial manufacturing cells where inference latency "
        "must remain strictly below 25 ms. By tightly enclosing flaws along their principal axes of inertia, OBB eliminates extraneous background "
        "pixels, preserves high-frequency edge gradients, and provides exact geometric coordinates for downstream robotic pick-and-place actuators."
    )
    
    # 1.2.3 Motivation for the Project
    add_h3(doc, "1.2.3 Motivation for the Project")
    add_p(doc,
        "The motivation for this project stems from urgent industrial and economic demands. Contaminated or compromised food packaging triggers "
        "catastrophic commercial repercussions: nationwide product recalls costing millions of dollars, severe regulatory penalties, and reputational "
        "damage. A single undetected 0.2 mm pinhole can spoil an entire production batch within 48 hours of hermetic sealing. By deploying an "
        "intelligent, deterministic edge vision inspection cell operating at over 40 frames per second with near-zero defect escape (less than 0.3%), "
        "manufacturing enterprises can eliminate human inspection labor overheads, reduce scrap rates, and ensure complete packaging integrity."
    )
    
    # 1.2.4 Expected Contributions of the Project
    add_h3(doc, "1.2.4 Expected Contributions of the Project")
    add_p(doc,
        "This project delivers four key technical and architectural contributions to the field of automated optical quality engineering:"
    )
    add_bullet(doc,
        "Formulation and implementation of an optimized YOLOv8-OBB deep neural network incorporating decoupled oriented bounding box heads, "
        "Gaussian Wasserstein Distance (GWD) regression loss, and Varifocal classification loss tailored for high-aspect-ratio packaging defects.",
        bold_prefix="1. Orientation-Aware Deep Architecture:"
    )
    add_bullet(doc,
        "Discovery and rigorous empirical validation of micro-defect augmentation suppression: demonstrating that eliminating spatial mosaic "
        "transformations and restricting geometric translation/scaling prevents the destruction of slender sub-pixel flaw features, elevating "
        "micro-scratch detection mAP50 by an astonishing 83.24 percentage points (from 12.61% to 95.85%).",
        bold_prefix="2. Micro-Defect Augmentation Theory:"
    )
    add_bullet(doc,
        "Compilation of an industrial packaging benchmark dataset comprising 5,065 high-resolution images annotated across nine defect categories "
        "with ground-truth rotated bounding polygons, establishing an open benchmark for packaging quality inspection.",
        bold_prefix="3. Comprehensive Industrial Flaw Benchmark:"
    )
    add_bullet(doc,
        "Development of an integrated edge deployment pipeline utilizing ONNX-Slim optimization, TensorRT acceleration, and a ROS2-PLC real-time "
        "middleware synchronization architecture that achieves an end-to-end cycle latency of 24.0 ms (41.6 FPS) on edge industrial hardware.",
        bold_prefix="4. Real-Time Robotic Edge Integration:"
    )
    
    # 1.3 General Problem Statement
    add_h2(doc, "1.3 General Problem Statement")
    add_p(doc,
        "In high-speed industrial packaging manufacturing lines operating at conveyance velocities of 0.8 to 1.2 m/s, conventional human inspection "
        "and horizontal automated optical inspection (AOI) frameworks fail to reliably detect, classify, and localize slender, diagonally oriented, "
        "and sub-millimeter surface flaws (such as micro-scratches, pinholes, and shrivel wrinkles) due to extreme background feature dilution, "
        "illumination sensitivity, and severe execution latency bottlenecks. This leads to prohibitive defect escape rates exceeding 14%, frequent "
        "food packaging barrier failure, and massive commercial recall risks. There is an urgent engineering need for a deterministic, real-time, "
        "vision-based defect detection system for industrial quality inspection that achieves greater than 95% mAP50 across all defect classes within a strict 25 ms cycle time."
    )
    
    # 1.4 Research Question
    add_h2(doc, "1.4 Research Question")
    add_p(doc,
        "How can deep oriented bounding box regression architectures and hyperparameter augmentation strategies be optimized and integrated "
        "with embedded edge accelerators to achieve real-time, sub-millimeter surface flaw localization on high-speed industrial packaging conveyors "
        "without suffering from small-object feature dilution or exceeding factory latency budgets?"
    )
    
    # 1.4.1 Research Objectives
    add_h3(doc, "1.4.1 Research Objectives")
    add_p(doc,
        "To systematically address the research question, five measurable engineering and scientific objectives were defined and executed:"
    )
    add_bullet(doc,
        "Curate, clean, and annotate an exhaustive industrial dataset of 5,065 high-resolution packaging casing images across nine flaw classes "
        "using rotated bounding boxes [x, y, w, h, theta] to establish ground-truth orientation baselines.",
        bold_prefix="Objective 1 (Dataset Engineering):"
    )
    add_bullet(doc,
        "Design and construct an industrial optomechanical vision enclosure featuring coaxial diffuse ring illumination, high-speed optical "
        "triggering, and telecentric optics to eliminate specular reflections and optical distortion on curved polymer casings.",
        bold_prefix="Objective 2 (Optomechanical Design):"
    )
    add_bullet(doc,
        "Formulate, adapt, and train an optimized YOLOv8-OBB model incorporating decoupled orientation heads, Gaussian Wasserstein Distance loss, "
        "and Varifocal classification loss to resolve boundary discontinuity and feature dilution.",
        bold_prefix="Objective 3 (Model Formulation & Training):"
    )
    add_bullet(doc,
        "Conduct systematic ablation studies to investigate the impact of spatial mosaic augmentation, scale transformations, and adaptive "
        "optimizers (AdamW vs. SGD-M) on micro-defect detection fidelity.",
        bold_prefix="Objective 4 (Algorithmic Ablation & Optimization):"
    )
    add_bullet(doc,
        "Serialize, optimize, and deploy the neural network on an edge computing node via ONNX/TensorRT, establishing real-time ROS2 middleware "
        "synchronization with downstream pneumatic ejection actuators to achieve continuous sorting under 25 ms latency.",
        bold_prefix="Objective 5 (Edge Deployment & Actuation Validation):"
    )
    
    # 1.5 Project Report Organization
    add_h2(doc, "1.5 Project Report Organization")
    add_p(doc,
        "The remainder of this Major Project Report is structured into four cohesive chapters:"
    )
    add_bullet(doc,
        "Presents a comprehensive systematic literature survey conducted in accordance with PRISMA guidelines. Evaluates 30 landmark peer-reviewed "
        "studies across deep learning AOI, oriented bounding box models, small object detection, and edge robotics, culminating in a detailed "
        "literature review matrix and explicit research gap analysis.",
        bold_prefix="Chapter 2 (Literature Survey):"
    )
    add_bullet(doc,
        "Details the end-to-end system methodology, optomechanical enclosure design, 5,065-image dataset taxonomy, YOLOv8-OBB network architecture, "
        "mathematical loss derivations (GWD, VFL, DFL), rotated polygon NMS clipping, micro-defect augmentation suppression theory, and ROS2/PLC edge integration.",
        bold_prefix="Chapter 3 (Methodology):"
    )
    add_bullet(doc,
        "Provides extensive empirical findings, quantitative per-class performance comparisons, stepwise ablation analysis (M1–M5), training convergence "
        "curves, normalized confusion matrix, visual qualitative detections, edge latency profiling across hardware targets, cross-architecture benchmarks, "
        "economic ROI analysis, and failure mode mitigation protocols.",
        bold_prefix="Chapter 4 (Results and Discussion):"
    )
    add_bullet(doc,
        "Synthesizes the overall research achievements against each stated objective, lists the key quantitative project outcomes, outlines future "
        "directions for short-wave infrared (SWIR) imaging and INT8 edge quantization, and documents research publications.",
        bold_prefix="Chapter 5 (Conclusion & Future Direction):"
    )

print("Chapter 1 updated with exact project title!")
