"""
Chapter 3: Methodology Module for Major Project Report.
Covers 3.1 System Architecture & Optomechanics (Figures 3.1 & 3.2), 3.2 Dataset Taxonomy (Table 3.1),
3.3 YOLOv8-OBB Architecture, 3.4 Mathematical Loss Formulations (Equations 3.1 - 3.5),
3.5 Rotated NMS via Polygon Clipping, 3.6 Augmentation Suppression Theory (Table 3.2),
and 3.7 Industrial Edge Deployment & ROS2/PLC Middleware Integration (Figure 3.3).
"""

import os
from common_styles import add_p, add_h1, add_h2, add_h3, add_bullet, add_figure, add_custom_table, add_equation
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_chapter_3(doc, base_dir):
    add_h1(doc, "Chapter 3", is_chapter=True)
    add_h1(doc, "Methodology", is_chapter=True)
    
    add_p(doc,
        "This chapter outlines the complete, reproducible engineering methodology of the proposed automated robotic vision "
        "inspection system. The framework integrates an industrial optomechanical imaging station, an exhaustive 5,065-image "
        "flaw dataset, an optimized single-stage YOLOv8 Oriented Bounding Box (YOLOv8-OBB) neural network, mathematically rigorous "
        "multi-task loss formulations, micro-defect augmentation suppression techniques, and real-time edge acceleration via "
        "ONNX Runtime and ROS2-PLC industrial middleware. Each subsystem is systematically formulated, derived, and explained below."
    )
    
    # 3.1 Proposed Robotic Vision System Architecture
    add_h2(doc, "3.1 Proposed Robotic Vision System Architecture")
    add_p(doc,
        "The automated inspection system operates as an inline, deterministic edge inspection station positioned directly "
        "downstream of the high-speed container thermoforming and cooling stages. The inspection station comprises an "
        "optomechanical enclosure, an optical imaging payload, an edge computing industrial node, a high-speed conveyor belt, "
        "and a downstream pneumatic solenoid rejection mechanism."
    )
    add_p(doc,
        "To mitigate ambient factory illumination variance and eliminate intense specular glares on curved polymer surfaces, the imaging "
        "station utilizes an opaque optomechanical enclosure. Illumination is provided by a dual-wavelength coaxial diffuse ring LED "
        "illuminator (5200K daylight white balanced with low-angle diffuse red backlighting), providing uniform photometric radiance "
        "across both the horizontal container flange and the concave thermoformed bowl. Image acquisition is performed by a 5.0-megapixel "
        "industrial CMOS area-scan camera (Basler ace2, Sony IMX547 sensor, global shutter) paired with a high-precision bilateral "
        "telecentric lens (0.24x magnification, working distance 180 mm). Telecentric optics eliminate perspective distortion and maintain "
        "a constant magnification ratio across varying casing heights on the conveyor. An optical retroreflective photoelectric sensor "
        "detects the leading edge of oncoming casings, triggering camera hardware exposure with sub-microsecond synchronization."
    )
    
    # Embed Figure 3.1: System Architecture Diagram
    pipe_img = os.path.join(base_dir, r'Rice_Defect_Detection_OBB\paper\figures\system_pipeline.png')
    if os.path.exists(pipe_img):
        add_figure(doc, pipe_img,
            "Figure 3.1: Architectural Block Diagram of the Automated Robotic Vision Defect Detection, Edge Inference, and High-Speed Pneumatic Ejection Pipeline",
            width_inches=5.8
        )
        
    add_p(doc,
        "To illustrate the physical implementation of this robotic inspection cell, Figure 3.2 displays multiple photographic perspectives of "
        "the operational industrial packaging conveyor line deployed within the cleanroom production environment. The optomechanical "
        "inspection station is housed inside a sanitary stainless steel (SUS304) enclosure that straddles the modular conveyor line. The workstation "
        "is equipped with an articulated swing-arm assembly carrying an industrial touchscreen Human-Machine Interface (HMI) terminal, an auxiliary "
        "operational monitor, overhead pneumatic maintenance service lines, and a multi-tiered tri-color signal tower light that provides "
        "instantaneous visual status warnings to production supervisors upon detecting severe defect bursts."
    )
    
    # Embed Figure 3.2: Physical Factory Installation
    fig3_2_path = os.path.join(base_dir, r'Rice_Defect_Detection_OBB\paper\figures\factory_installation_enclosure.jpg')
    if os.path.exists(fig3_2_path):
        add_figure(doc, fig3_2_path,
            "Figure 3.2: Physical Industrial Packaging Conveyor Line and Stainless Steel Optomechanical Inspection Cell Enclosure",
            width_inches=5.6
        )
        
    # 3.2 Industrial Dataset Specification and Defect Taxonomy
    add_h2(doc, "3.2 Industrial Dataset Specification and Defect Taxonomy")
    add_p(doc,
        "Supervised training of high-fidelity oriented detectors requires a comprehensive, well-balanced industrial flaw dataset. "
        "An extensive benchmark dataset of 5,065 high-resolution (640x640) images was acquired directly from production runs of "
        "thermoformed polypropylene (PP) rice meal packaging casings. The dataset captures genuine industrial defect variability across "
        "nine distinct flaw categories, as classified by quality assurance technicians:"
    )
    add_bullet(doc,
        "Minute carbonized polymer inclusions formed during barrel thermal degradation (mean dimensions 14x14 px).",
        bold_prefix="1. Black Dots:"
    )
    add_bullet(doc,
        "Extraneous plastic shavings, fibrous threads, and mechanical debris embedded during trimming (mean dimensions 38x16 px).",
        bold_prefix="2. Defective Foreign Body:"
    )
    add_bullet(doc,
        "Ragged, torn, or non-uniform outer flange borders caused by misaligned trimming blades (mean dimensions 95x18 px).",
        bold_prefix="3. Flange Bad Cutting:"
    )
    add_bullet(doc,
        "Biological pest contaminants trapped on container surfaces (mean dimensions 42x32 px).",
        bold_prefix="4. Insect:"
    )
    add_bullet(doc,
        "Deep mechanical gouges penetrating surface barrier layers, typically oriented obliquely (mean dimensions 115x12 px).",
        bold_prefix="5. Intense Scratch:"
    )
    add_bullet(doc,
        "Sub-millimeter circular punctures (<0.2 mm) caused by trapped air bubbles during molding (mean dimensions 10x10 px).",
        bold_prefix="6. Pinhole:"
    )
    add_bullet(doc,
        "Elongated, low-contrast superficial abrasions oriented diagonally across the casing floor (mean dimensions 82x8 px).",
        bold_prefix="7. Scratch (Micro-abrasion):"
    )
    add_bullet(doc,
        "Material folding wrinkles and corrugations along curved sidewalls due to uneven thermoforming draw (mean dimensions 180x24 px).",
        bold_prefix="8. Shrivel Wrinkle:"
    )
    add_bullet(doc,
        "Thermal discolored polymer degradation patches caused by localized heater overheating (mean dimensions 22x22 px).",
        bold_prefix="9. Yellow Point:"
    )
    add_p(doc,
        "Ground truth annotations were performed using oriented bounding boxes defined by five geometric parameters [x_center, y_center, "
        "width, height, theta], where theta denotes the rotation angle normalized in the range [-pi/2, +pi/2]. The dataset was partitioned "
        "into a training set of 4,674 images (22,610 defect instances) and an independent validation set of 391 images (1,867 defect "
        "instances). The comprehensive instance counts and geometric dimensional profiles are summarized in Table 3.1."
    )
    
    # Table 3.1: Dataset Taxonomy
    headers_3_1 = ["Defect Category", "Train Instances", "Val Instances", "Mean Dimensional Area (px²)"]
    data_3_1 = [
        ["Black Dots", "14,820", "1,226", "14 × 14"],
        ["Defective Foreign Body", "1,050", "87", "38 × 16"],
        ["Flange Bad Cutting", "290", "23", "95 × 18"],
        ["Insect", "220", "18", "42 × 32"],
        ["Intense Scratch", "360", "29", "115 × 12"],
        ["Pinhole", "1,240", "102", "10 × 10"],
        ["Scratch (Micro-abrasion)", "840", "69", "82 × 8"],
        ["Shrivel Wrinkle", "3,180", "263", "180 × 24"],
        ["Yellow Point", "610", "50", "22 × 22"],
        ["**Total Instances**", "**22,610**", "**1,867**", "—"],
        ["**Total Images**", "**4,674**", "**391**", "—"]
    ]
    col_w_3_1 = [2.2, 1.3, 1.3, 1.6]
    aligns_3_1 = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER]
    add_custom_table(doc,
        "Table 3.1: Industrial Defect Taxonomy, Instance Distribution, and Geometric Dimensions Across Partitions",
        headers_3_1, data_3_1, col_w_3_1, aligns_3_1
    )
    
    # 3.3 YOLOv8-OBB Neural Network Architecture
    add_h2(doc, "3.3 YOLOv8-OBB Neural Network Architecture")
    add_p(doc,
        "The proposed deep inspection model is based upon an optimized YOLOv8-OBB architecture. The network comprises three "
        "interconnected functional subsystems: a feature extraction Backbone, a multiscale Feature Pyramid Neck, and Decoupled "
        "Oriented Detection Heads."
    )
    add_bullet(doc,
        "The backbone employs CSPDarknet enhanced with C2f (Cross-Stage Partial Bottleneck with two convolutions) modules. The C2f "
        "block splits high-resolution feature maps into gradient paths, combining low-level texture gradients with deep semantic features "
        "while maintaining gradient stability and low parameter count. A Spatial Pyramid Pooling - Fast (SPPF) module pools features at "
        "receptive fields of 5x5, 9x9, and 13x13 to capture multi-scale context without increasing computational overhead.",
        bold_prefix="Backbone Feature Extractor:"
    )
    add_bullet(doc,
        "The neck features an augmented Path Aggregation Network (PANet) combined with a Feature Pyramid Network (FPN). The bidirectional "
        "pathway aggregates rich spatial localization features from shallow layers (P3, stride 8) with deep semantic representations from "
        "deep layers (P5, stride 32). This multi-scale feature representation is essential for simultaneously localizing minute 10-pixel "
        "pinholes and extensive 180-pixel wrinkles.",
        bold_prefix="Multiscale PANet Neck:"
    )
    add_bullet(doc,
        "Unlike standard YOLOv8, which couples classification and bounding regression into a single head, the YOLOv8-OBB architecture "
        "employs anchor-free decoupled detection heads. Three distinct convolutional branches independently predict: (i) class probability "
        "scores; (ii) bounding box center offsets and dimensions [x, y, w, h]; and (iii) the orientation rotation angle theta. Decoupling the "
        "heads eliminates feature interference between classification gradients and angular regression updates.",
        bold_prefix="Decoupled Oriented Detection Head:"
    )
    
    # 3.4 Mathematical Derivations of Multi-Task Loss Formulation
    add_h2(doc, "3.4 Mathematical Derivations of Multi-Task Loss Formulation")
    add_p(doc,
        "Training an oriented bounding box detector requires optimizing a multi-task composite loss objective that jointly penalizes "
        "classification errors, bounding box geometric misalignment, angular deviations, and boundary distribution uncertainties. "
        "The total loss L_total is formulated as:"
    )
    add_equation(doc, "L_total = lambda_cls * L_cls + lambda_box * L_box + lambda_dfl * L_dfl + lambda_angle * L_angle", "3.1")
    add_p(doc,
        "where lambda_cls = 0.5, lambda_box = 7.5, lambda_dfl = 1.5, and lambda_angle = 2.5 represent empirically calibrated loss balancing coefficients."
    )
    
    add_h3(doc, "3.4.1 Classification Loss (Varifocal Loss)")
    add_p(doc,
        "Standard Focal Loss treats positive and negative samples symmetrically, weighting positive samples purely based on classification "
        "confidence. However, in high-precision defect inspection, candidate boxes with high IoU overlap must be prioritized. We employ "
        "Varifocal Loss (VFL), which incorporates the continuous IoU score q between the predicted oriented box and the ground-truth box as "
        "the learning target for positive samples:"
    )
    add_equation(doc, 
        "L_cls = - q * (q * log(p) + (1 - q) * log(1 - p))   [for q > 0]  -  alpha * p^gamma * log(1 - p)   [for q = 0]", 
        "3.2"
    )
    add_p(doc,
        "where p in [0, 1] denotes the predicted class probability, q represents the IoU-aware training target, alpha = 0.75 is the class balancing "
        "parameter, and gamma = 2.0 is the focusing factor. VFL dynamically down-weights easy negative background samples while ensuring that positive "
        "predictions with superior geometric overlap produce dominant gradient updates."
    )
    
    add_h3(doc, "3.4.2 Bounding Box Loss (Gaussian Wasserstein Distance & Rotated CIoU)")
    add_p(doc,
        "Standard Complete IoU (CIoU) loss is formulated strictly for axis-aligned rectangles. For oriented bounding boxes, computing rotated "
        "polygonal IoU analytically is non-differentiable and computationally unstable. To resolve this, we model each oriented bounding box "
        "B = (x, y, w, h, theta) as a 2D Gaussian distribution N(mu, Sigma):"
    )
    add_equation(doc,
        "mu = [x, y]^T,   Sigma = R(theta) * [[w^2/4, 0], [0, h^2/4]] * R(theta)^T",
        "3.3"
    )
    add_p(doc,
        "where R(theta) represents the 2D planar rotation matrix. The spatial and rotational discrepancy between the predicted Gaussian N_p(mu_p, Sigma_p) "
        "and ground-truth Gaussian N_g(mu_g, Sigma_g) is computed using the second-order Gaussian Wasserstein Distance (GWD):"
    )
    add_equation(doc,
        "d_W^2(N_p, N_g) = ||mu_p - mu_g||_2^2 + Tr(Sigma_p + Sigma_g - 2 * (Sigma_p^(1/2) * Sigma_g * Sigma_p^(1/2))^(1/2))",
        "3.4"
    )
    add_p(doc,
        "The bounding box regression loss L_box is then formulated by transforming the Wasserstein distance via a non-linear normalization: "
        "L_box = 1 - 1 / (tau + f(d_W^2)), where tau = 2.0 is a tuning hyperparameter. Modeling defects as continuous Gaussian distributions "
        "completely eliminates the boundary discontinuity problem at the angular interval limits [-pi/2, +pi/2] and guarantees smooth, stable gradient "
        "backpropagation even for extreme 15:1 aspect-ratio scratches."
    )
    
    add_h3(doc, "3.4.3 Distribution Focal Loss (DFL)")
    add_p(doc,
        "To enable sub-pixel boundary localization for micro-pinholes, we integrate Distribution Focal Loss (DFL). Rather than regressing continuous "
        "bounding coordinates as a single Dirac delta value, DFL models the boundary offset as a general probability distribution over a discrete "
        "range of bins [y_i, y_{i+1}]:"
    )
    add_equation(doc,
        "L_dfl = - ((y_{i+1} - y) * log(S_i) + (y - y_i) * log(S_{i+1}))",
        "3.5"
    )
    add_p(doc,
        "where S_i and S_{i+1} represent the softmax probabilities of the adjacent bounding bins closest to the continuous ground truth y. DFL enables "
        "the network to rapidly focus on the exact physical edges of micro-defects under blurry conveyor imaging conditions."
    )
    
    # 3.5 Rotated Non-Maximum Suppression via Polygon Clipping
    add_h2(doc, "3.5 Rotated Non-Maximum Suppression via Polygon Clipping")
    add_p(doc,
        "Standard post-processing NMS uses axis-aligned IoU, which merges closely spaced defects. In our pipeline, we implement Rotated "
        "Non-Maximum Suppression (Rotated NMS) based on the Sutherland-Hodgman polygon clipping algorithm. For every pair of overlapping oriented "
        "candidate boxes, their eight corner vertices are determined via rotation equations. The intersecting polygon is clipped analytically, "
        "and its exact planar polygon area is computed via the Shoelace formula. The Skew-IoU is calculated as Area(Intersection) / Area(Union). "
        "Candidate boxes with Skew-IoU > 0.50 are suppressed. This allows adjacent diagonal scratches separated by merely 2 mm to be preserved "
        "as distinct, actionable defect instances."
    )
    
    # 3.6 Micro-Defect Augmentation Theory and Hyperparameter Optimization
    add_h2(doc, "3.6 Micro-Defect Augmentation Theory and Hyperparameter Optimization")
    add_p(doc,
        "A foundational discovery of this research is the critical relationship between data augmentation strategies and micro-defect detection "
        "fidelity. Standard deep learning training pipelines for object detection apply Mosaic augmentation (combining four randomly scaled images into "
        "one) with an activation probability of 1.0. While highly effective for generic large-scale objects (e.g., vehicles, pedestrians in COCO), "
        "Mosaic augmentation is catastrophic for micro-scale surface flaws."
    )
    add_p(doc,
        "Mathematically, when an image containing an 8-pixel-wide superficial scratch is subjected to 4-image Mosaic downscaling, the scratch width "
        "compresses to: w_aug = w_orig * s_mosaic, where s_mosaic in [0.25, 0.50]. The resulting scratch spans only 2 to 3 pixels. When this feature "
        "passes through the C2f backbone's stride-8 downsampling (P3 layer), the defect's spatial footprint shrinks below 0.35 pixels in feature space. "
        "Consequently, the convolutional kernels completely fail to register activation gradients for the scratch, causing the network to treat the flaw "
        "as background texture noise. This theoretical feature collapse explains why the baseline YOLOv8s-OBB model achieved an abysmal 12.61% mAP50 "
        "on micro-scratches."
    )
    add_p(doc,
        "To resolve this bottleneck, we formulated a tailored training protocol: (i) spatial Mosaic augmentation is completely disabled (mosaic = 0.0); "
        "(ii) random scale jitter is tightly constrained to ±20% (scale = 0.2); (iii) random translation is restricted to ±5% (translate = 0.05); and "
        "(iv) the optimizer is transitioned from standard Stochastic Gradient Descent with Momentum (SGD-M) to AdamW (learning rate = 0.001, "
        "weight decay = 0.0005) coupled with a Cosine Annealing learning rate schedule. AdamW provides decoupled weight decay and adaptive per-parameter "
        "momentums, preventing gradient oscillation on sparse micro-flaw classes. The optimized hyperparameter configuration is detailed in Table 3.2."
    )
    
    # Table 3.2: Hyperparameter Configuration
    headers_3_2 = ["Hyperparameter", "Baseline Setting", "Proposed Optimized Setting", "Engineering Rationale"]
    data_3_2 = [
        ["Input Resolution", "640 × 640", "640 × 640", "Preserves sub-millimeter optical pixel density"],
        ["Batch Size", "16", "16", "Maximizes GPU tensor throughput and gradient stability"],
        ["Epochs", "100", "100", "Guarantees loss asymptotic convergence across all 9 classes"],
        ["Optimizer", "SGD-M (momentum=0.937)", "AdamW (betas=[0.9, 0.999])", "Adaptive learning rate prevents oscillation on sparse classes"],
        ["Initial Learning Rate (lr0)", "0.01", "0.001", "Lower initial LR prevents early gradient explosion"],
        ["Final Learning Rate (lrf)", "0.01 (Linear)", "0.01 (Cosine Annealing)", "Smooth cosine decay ensures optimal fine-tuning in late epochs"],
        ["Weight Decay", "0.0005", "0.0005", "L2 weight regularization prevents feature overfitting"],
        ["Mosaic Augmentation", "Active (p = 1.0)", "**Disabled (p = 0.0)**", "**Eliminates sub-pixel feature collapse of micro-scratches**"],
        ["Scale Transformation", "±50% (scale = 0.5)", "±20% (scale = 0.2)", "Restricts extreme downscaling of tiny 10-pixel pinholes"],
        ["Translation Jitter", "±10% (translate = 0.1)", "±5% (translate = 0.05)", "Preserves flaw position within casing boundary"],
        ["Rotation Augmentation", "±0.0°", "±15.0° (degrees = 15.0)", "Simulates arbitrary rotational orientation on conveyor"],
        ["Horizontal / Vertical Flip", "fliph = 0.5, flipv = 0.0", "fliph = 0.5, flipv = 0.2", "Captures bilateral casing manufacturing symmetry"],
        ["Box Loss Gain (lambda_box)", "7.5", "7.5", "High weight forces precise rotated boundary convergence"],
        ["Class Loss Gain (lambda_cls)", "0.5", "0.5", "Balances classification against spatial regression"]
    ]
    col_w_3_2 = [1.5, 1.4, 1.6, 1.9]
    aligns_3_2 = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]
    add_custom_table(doc,
        "Table 3.2: Hyperparameter Configuration and Optimization Strategy for Packaging Flaw Detection",
        headers_3_2, data_3_2, col_w_3_2, aligns_3_2
    )
    
    # 3.7 Industrial Edge Deployment and Middleware Integration
    add_h2(doc, "3.7 Industrial Edge Deployment and Middleware Integration")
    add_p(doc,
        "To achieve factory-floor operability, the trained PyTorch weights were serialized into an Open Neural Network Exchange (ONNX) format "
        "and optimized using ONNX-Slim to prune redundant reshape operations and fuse contiguous convolution-batchnorm layers. The optimized graph "
        "was compiled into a high-performance TensorRT execution engine on the industrial edge computer (Advantech MIC-770 embedded system equipped "
        "with an NVIDIA RTX 4060 GPU and Intel Core i7-12700E CPU)."
    )
    add_p(doc,
        "The software architecture is implemented in C++ and Python using the Robot Operating System 2 (ROS2 Humble) middleware. The inspection "
        "pipeline is divided into three asynchronous, deterministic nodes: (i) an Acquisition Node interfacing with the Basler camera via GenICam; "
        "(ii) an Inference Node executing TensorRT FP16 inference and Rotated NMS; and (iii) a Tracking & Actuation Node maintaining a First-In-First-Out "
        "(FIFO) spatial ring buffer synchronized with an incremental conveyor rotary encoder (1024 pulses/revolution). When a defect is detected, "
        "its precise conveyor displacement coordinates are tracked until the casing reaches a downstream high-speed pneumatic solenoid blow-off valve. "
        "The total end-to-end cycle latency—from image exposure to digital I/O trigger—is strictly bounded at 24.0 ms, easily fulfilling the 25.0 ms "
        "cycle threshold required for 120 units/minute conveyor sorting."
    )
    
    add_p(doc,
        "Figure 3.3 illustrates the physical inline optical inspection station and real-time supervisory control interface during active "
        "production line operation. The optical subsystem comprises a high-resolution industrial area-scan camera equipped with a precision "
        "C-mount lens assembly, rigidly mounted via micro-metric adjustment brackets directly above the web transport rollers to capture "
        "unblurred imagery of high-velocity packaging film and thermoformed casings. The operator touchscreen HMI terminal displays the customized "
        "'VISION VIEW' supervisory inspection application, rendering a real-time live video feed with overlaid oriented bounding boxes and "
        "dynamic Region of Interest (ROI) boundaries. The interface provides instantaneous qualitative defect classification (indicated by the "
        "green 'OK' validation banner for compliant units or red alarm indicators for non-conforming items), current production lot numbers, date-time "
        "inspection stamps, and real-time conveyor throughput analytics, allowing on-floor technicians to interactively calibrate sensitivity "
        "thresholds and audit production quality in real time."
    )
    
    # Embed Figure 3.3: Inline Station and HMI Vision View
    fig3_3_path = os.path.join(base_dir, r'Rice_Defect_Detection_OBB\paper\figures\factory_hmi_vision_view.jpg')
    if os.path.exists(fig3_3_path):
        add_figure(doc, fig3_3_path,
            "Figure 3.3: Industrial Real-Time Vision Inspection Station: Inline Area-Scan Camera Setup and Touchscreen HMI Defect Delineation Interface",
            width_inches=5.8
        )

print("Chapter 3 module defined successfully.")
