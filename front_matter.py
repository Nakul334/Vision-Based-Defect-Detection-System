"""
Front matter handler: Updates Section 0 and Section 1 of the template docx.
Preserves all original drawing lines (signature lines in Approval and Declaration),
exact paragraph alignments (Right alignment for student signature blocks),
and exact user text for Title, Author, Approval, Declaration, and Acknowledgment.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def update_front_matter(doc):
    paragraphs = doc.paragraphs
    
    # -------------------------------------------------------------
    # 1. OUTER TITLE PAGE (P0 - P8)
    # -------------------------------------------------------------
    paragraphs[0].text = "Vision-Based Defect Detection System for Industrial Quality Inspection"
    paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[0].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = RGBColor(31, 78, 120)
        
    paragraphs[1].text = "Nakul S. Dube"
    paragraphs[1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[1].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(13)
        r.font.bold = True
        
    # P2 contains the University Logo - leave untouched!
    
    paragraphs[3].text = "DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING"
    paragraphs[3].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[3].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        
    paragraphs[4].text = "FACULTY OF ENGINEERING AND TECHNOLOGY,"
    paragraphs[4].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[4].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        
    paragraphs[5].text = "DATTA MEGHE INSTITUTE OF HIGHER EDUCATION AND"
    paragraphs[5].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[5].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        
    paragraphs[6].text = "RESEARCH (DU)"
    paragraphs[6].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[6].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        
    paragraphs[7].text = "SAWANGI (MEGHE), WARDHA, MAHARASHTRA-442107"
    paragraphs[7].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[7].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        
    paragraphs[8].text = "OCTOBER, 2026"
    paragraphs[8].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[8].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True

    # -------------------------------------------------------------
    # 2. INNER TITLE PAGE (P11 - P27)
    # -------------------------------------------------------------
    paragraphs[11].text = "Vision-Based Defect Detection System for Industrial Quality Inspection"
    paragraphs[11].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[11].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(15)
        r.font.bold = True
        r.font.color.rgb = RGBColor(31, 78, 120)
        
    paragraphs[12].text = "The Major Project-I report submitted in partial fulfilment of the requirement"
    paragraphs[13].text = "For the Award of the Degree of"
    paragraphs[14].text = "Bachelor of Technology"
    paragraphs[15].text = "(Semester VII)"
    for idx in [12, 13, 14, 15]:
        paragraphs[idx].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in paragraphs[idx].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.font.bold = (idx in [14, 15])
            
    paragraphs[17].text = "By"
    paragraphs[18].text = "Nakul S. Dube"
    paragraphs[19].text = "(Enrollment No.: DMET1323009)"
    for idx in [17, 18, 19]:
        paragraphs[idx].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in paragraphs[idx].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11.5)
            r.font.bold = (idx == 18)
            
    paragraphs[20].text = "Under the Guidance of"
    paragraphs[21].text = "Dr. Swapnil Gundewar"
    for idx in [20, 21]:
        paragraphs[idx].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in paragraphs[idx].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.font.bold = (idx == 21)
            
    # P22 contains the University Logo - leave untouched!
    
    paragraphs[23].text = "Department of Artificial Intelligence and Machine Learning"
    paragraphs[24].text = "Faculty of Engineering and Technology,"
    paragraphs[25].text = "Datta Meghe Institute of Higher Education and Research (DU)"
    paragraphs[26].text = "Sawangi (Meghe), Wardha, Maharashtra-442107"
    paragraphs[27].text = "October 2026"
    for idx in [23, 24, 25, 26, 27]:
        paragraphs[idx].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in paragraphs[idx].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11.5)
            r.font.bold = True

    # -------------------------------------------------------------
    # 3. MAJOR PROJECT-I APPROVAL (P28 - P41)
    # Preserves drawing lines and exact run layout from template!
    # -------------------------------------------------------------
    # P28: Title
    p28 = paragraphs[28]
    p28.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if len(p28.runs) >= 2:
        p28.runs[0].text = "Major Project-I "
        p28.runs[0].font.name = 'Times New Roman'
        p28.runs[0].font.size = Pt(16)
        p28.runs[0].font.bold = True
        p28.runs[0].font.color.rgb = RGBColor(255, 0, 0) # Red as in template
        
        p28.runs[1].text = "Approval"
        p28.runs[1].font.name = 'Times New Roman'
        p28.runs[1].font.size = Pt(16)
        p28.runs[1].font.bold = True
        p28.runs[1].font.color.rgb = RGBColor(0, 0, 0)

    # P29: Title & Author text
    p29 = paragraphs[29]
    p29.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    # Update runs cleanly
    if len(p29.runs) >= 8:
        p29.runs[0].text = "Major Project-I entitled: "
        p29.runs[1].text = ""
        p29.runs[2].text = "Vision-Based Defect Detection System for Industrial Quality Inspection"
        p29.runs[3].text = " "
        p29.runs[4].text = "by "
        p29.runs[5].text = "Nakul S. Dube"
        p29.runs[6].text = " "
        p29.runs[7].text = "is approved for the degree of"
        for r in p29.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.font.color.rgb = RGBColor(0, 0, 0)
    else:
        p29.text = "Major Project-I entitled: Vision-Based Defect Detection System for Industrial Quality Inspection by Nakul S. Dube is approved for the degree of"
        for r in p29.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)

    # P30: Degree & Department text
    p30 = paragraphs[30]
    p30.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if len(p30.runs) >= 7:
        p30.runs[0].text = "B.Tech Semester "
        p30.runs[1].text = ""
        p30.runs[2].text = "VII in "
        p30.runs[3].text = ""
        p30.runs[4].text = "Artificial Intelligence and Machine Learning"
        p30.runs[5].text = " "
        p30.runs[6].text = "of Faculty of Engineering And Technology, Wardha."
        for r in p30.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.font.color.rgb = RGBColor(0, 0, 0)
    else:
        p30.text = "B.Tech Semester VII in Artificial Intelligence and Machine Learning of Faculty of Engineering And Technology, Wardha."
        for r in p30.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)

    # P31: Examiners
    p31 = paragraphs[31]
    p31.runs[0].text = "Examiners"
    p31.runs[0].font.name = 'Times New Roman'
    p31.runs[0].font.size = Pt(12)
    p31.runs[0].font.bold = True

    # P32: (i) [preserve drawing line in runs[1]]
    p32 = paragraphs[32]
    p32.runs[0].text = "(i) "
    p32.runs[0].font.name = 'Times New Roman'
    p32.runs[0].font.size = Pt(11)

    # P33: (ii) [preserve drawing line in runs[1]]
    p33 = paragraphs[33]
    p33.runs[0].text = "(ii) "
    p33.runs[0].font.name = 'Times New Roman'
    p33.runs[0].font.size = Pt(11)

    # P34: drawing line for Supervisor/H.O.D (untouched!)
    # P35: Supervisor/H.O.D text
    p35 = paragraphs[35]
    p35.runs[0].text = "Supervisor/H.O.D"
    p35.runs[0].font.name = 'Times New Roman'
    p35.runs[0].font.size = Pt(11)

    # P36: drawing line for Dean Academics (untouched!)
    # P37: Dean Academics text
    p37 = paragraphs[37]
    p37.runs[0].text = "Dean Academics"
    p37.runs[0].font.name = 'Times New Roman'
    p37.runs[0].font.size = Pt(11)

    # P38: drawing line for Dean, FEAT (untouched!)
    # P39: Dean, FEAT text
    p39 = paragraphs[39]
    p39.runs[0].text = "Dean, FEAT"
    p39.runs[0].font.name = 'Times New Roman'
    p39.runs[0].font.size = Pt(11)

    # P40: Date: [preserve drawing line in runs[1]]
    p40 = paragraphs[40]
    p40.runs[0].text = "Date: "
    p40.runs[0].font.name = 'Times New Roman'
    p40.runs[0].font.size = Pt(11)

    # P41: Place: Wardha
    p41 = paragraphs[41]
    if len(p41.runs) >= 2:
        p41.runs[0].text = "Place: "
        p41.runs[1].text = "Wardha"
    else:
        p41.text = "Place: Wardha"
    for r in p41.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    # -------------------------------------------------------------
    # 4. DECLARATION (P42 - P49)
    # -------------------------------------------------------------
    p42 = paragraphs[42]
    p42.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p42.runs[0].text = "Declaration"
    p42.runs[0].font.name = 'Times New Roman'
    p42.runs[0].font.size = Pt(16)
    p42.runs[0].font.bold = True

    p43 = paragraphs[43]
    p43.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p43.runs[0].text = "I declare that this submission is my own work and ideas. If I have used someone else’s words or ideas, I have properly cited and referenced them."
    p43.runs[0].font.name = 'Times New Roman'
    p43.runs[0].font.size = Pt(12)

    p44 = paragraphs[44]
    p44.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p44.runs[0].text = "I confirm that I have followed all rules of academic honesty and integrity. I have not misrepresented, fabricated, or falsified any information, data, or sources in this submission."
    p44.runs[0].font.name = 'Times New Roman'
    p44.runs[0].font.size = Pt(12)

    p45 = paragraphs[45]
    p45.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p45.runs[0].text = "I understand that breaking these rules can lead to disciplinary action by the institute and possible legal consequences from the original sources if proper credit or permission has not been given."
    p45.runs[0].font.name = 'Times New Roman'
    p45.runs[0].font.size = Pt(12)

    # P46: Student Name (RIGHT ALIGNED)
    p46 = paragraphs[46]
    p46.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p46.runs[0].text = "Nakul S. Dube"
    p46.runs[0].font.name = 'Times New Roman'
    p46.runs[0].font.size = Pt(11.5)
    p46.runs[0].font.bold = True
    p46.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    # P47: Enrollment No (RIGHT ALIGNED)
    p47 = paragraphs[47]
    p47.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if len(p47.runs) >= 2:
        p47.runs[0].text = "Enrollment No.: "
        p47.runs[1].text = "C2023FE00055"
    else:
        p47.text = "Enrollment No.: C2023FE00055"
    for r in p47.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # P48: Date: [preserve drawing line in runs[1]]
    p48 = paragraphs[48]
    p48.runs[0].text = "Date: "
    p48.runs[0].font.name = 'Times New Roman'
    p48.runs[0].font.size = Pt(11)

    # P49: Place: Wardha
    p49 = paragraphs[49]
    p49.text = "Place: Wardha"
    for r in p49.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    # -------------------------------------------------------------
    # 5. ACKNOWLEDGMENT (P51 - P59)
    # -------------------------------------------------------------
    p51 = paragraphs[51]
    p51.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p51.runs[0].text = "Acknowledgment"
    p51.runs[0].font.name = 'Times New Roman'
    p51.runs[0].font.size = Pt(16)
    p51.runs[0].font.bold = True

    # P52: First paragraph with Guide and HOD
    p52 = paragraphs[52]
    p52.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if len(p52.runs) >= 15:
        p52.runs[0].text = "The making of the project needed the cooperation and guidance of a number of people. I therefore consider it my prime duty to thank all those who helped me through this venture. It is my immense pleasure to express my gratitude to "
        p52.runs[1].text = ""
        p52.runs[2].text = "Dr. Swapnil Gundewar"
        p52.runs[3].text = ""
        p52.runs[4].text = ""
        p52.runs[5].text = " as a guide and "
        p52.runs[6].text = "Dr. Utkarsha Pacharaney"
        p52.runs[7].text = ", "
        p52.runs[8].text = "HOD"
        p52.runs[9].text = " of "
        p52.runs[10].text = "Artificial Intelligence and Machine Learning"
        p52.runs[11].text = " who"
        p52.runs[12].text = " had provided me with constructive"
        p52.runs[13].text = " "
        p52.runs[14].text = "and positive feedback during this major project-I."
        for r in p52.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.font.color.rgb = RGBColor(0, 0, 0)
    else:
        p52.text = "The making of the project needed the cooperation and guidance of a number of people. I therefore consider it my prime duty to thank all those who helped me through this venture. It is my immense pleasure to express my gratitude to Dr. Swapnil Gundewar as a guide and Dr. Utkarsha Pacharaney, HOD of Artificial Intelligence and Machine Learning who had provided me with constructive and positive feedback during this major project-I."
        for r in p52.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)

    # P53: Coordinator Dr. Subodh Daronde
    p53 = paragraphs[53]
    p53.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if len(p53.runs) >= 3:
        p53.runs[0].text = "I would also like to thank my coordinator "
        p53.runs[1].text = "Dr. Subodh Daronde "
        p53.runs[2].text = "for his guidance and support throughout the development of this project. His valuable suggestions greatly contributed to the successful completion of this work."
    else:
        p53.text = "I would also like to thank my coordinator Dr. Subodh Daronde for his guidance and support throughout the development of this project. His valuable suggestions greatly contributed to the successful completion of this work."
    for r in p53.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

    # P54: CSE department staff
    p54 = paragraphs[54]
    p54.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p54.text = "I sincerely thank all other staff members of the Computer Science and Engineering department for their kind co-operation."
    for r in p54.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

    # P55: Dean Academics & Dean FEAT
    p55 = paragraphs[55]
    p55.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if len(p55.runs) >= 5:
        p55.runs[0].text = "I would like to thank "
        p55.runs[1].text = "Dr. Utkarsha Pacharaney"
        p55.runs[2].text = ", dean academics of our institution, and also "
        p55.runs[3].text = "Prof. (Dr.) K.T.V. Reddy"
        p55.runs[4].text = ", dean of our institution, for providing the necessary facilities during the period of working on this report."
    else:
        p55.text = "I would like to thank Dr. Utkarsha Pacharaney, dean academics of our institution, and also Prof. (Dr.) K.T.V. Reddy, dean of our institution, for providing the necessary facilities during the period of working on this report."
    for r in p55.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

    # P56: Friends and library
    p56 = paragraphs[56]
    p56.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p56.text = "I am thankful to my friends and library staff members whose encouragement and suggestions helped me to complete my minor project."
    for r in p56.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

    # P57: Parents
    p57 = paragraphs[57]
    p57.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p57.text = "I am also thankful to my parents whose best wishes are always with me."
    for r in p57.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

    # P58: Student Name (RIGHT ALIGNED)
    p58 = paragraphs[58]
    p58.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p58.runs[0].text = "Nakul S. Dube"
    p58.runs[0].font.name = 'Times New Roman'
    p58.runs[0].font.size = Pt(11.5)
    p58.runs[0].font.bold = True
    p58.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    # P59: Enrollment No (RIGHT ALIGNED)
    p59 = paragraphs[59]
    p59.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if len(p59.runs) >= 2:
        p59.runs[0].text = "Enrollment No.:  "
        p59.runs[1].text = "C2023FE00055"
    else:
        p59.text = "Enrollment No.:  C2023FE00055"
    for r in p59.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0, 0, 0)

    # -------------------------------------------------------------
    # 6. ABSTRACT & KEYWORDS (P61 - P64)
    # -------------------------------------------------------------
    paragraphs[61].text = "Abstract"
    paragraphs[61].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[61].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = RGBColor(31, 78, 120)
        
    paragraphs[62].text = "Automated surface quality assurance in high-throughput food container and packaging manufacturing requires robust, sub-millimeter flaw localization capable of handling arbitrary spatial orientations. Conventional machine vision frameworks predominantly rely on horizontal axis-aligned bounding boxes (HBB), which encompass substantial extraneous background pixels when encapsulating slender, diagonally oriented flaws such as scratches, edge fissures, and material wrinkles. This background noise causes severe feature dilution, resulting in prohibitive miss rates for micro-defects. In this project, an end-to-end industrial robotic inspection pipeline driven by an optimized YOLOv8 Oriented Bounding Box (YOLOv8-OBB) deep neural architecture is developed specifically for thermoformed and injection-molded rice packaging casings. To resolve critical detection bottlenecks on small-scale anomalies, spatial mosaic augmentation is eliminated, excessive geometric translation and scaling are suppressed, and an AdamW optimizer coupled with cosine learning rate scheduling is employed. The proposed framework is evaluated on a benchmark dataset comprising 5,065 annotated industrial images across nine defect categories: black dots, defective foreign bodies, flange bad cutting, insects, intense scratches, pinholes, scratches, shrivel wrinkles, and yellow points. Experimental evaluations demonstrate that the optimized YOLOv8-OBB model improves the mean Average Precision at IoU 0.50 (mAP50) from an initial baseline of 49.02% to 97.55%, while elevating the detection rate of critical micro-scratches from 12.61% to 95.85%. Integrated with an Open Neural Network Exchange (ONNX) deployment runtime, the vision system achieves an inference latency of 24.0 ms per casing (41.6 FPS), enabling continuous, real-time rejection on conveyor lines operating at over 120 units per minute."
    paragraphs[62].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for r in paragraphs[62].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        
    paragraphs[63].text = "" # blank
    paragraphs[64].text = "Keywords: Vision-Based Defect Detection; Oriented Bounding Box (OBB); YOLOv8-OBB; Automated Optical Inspection (AOI); Industrial Surface Quality Assurance."
    paragraphs[64].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for r in paragraphs[64].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.bold = True

    # -------------------------------------------------------------
    # 7. CONTENTS (TABLE OF CONTENTS - TABLE 0)
    # -------------------------------------------------------------
    toc_table = doc.tables[0]
    toc_data = [
        ("Abstract", "i"),
        ("List of Figures", "iv"),
        ("List of Tables", "v"),
        ("Abbreviations", "vi"),
        ("Chapter 1: Introduction", "1"),
        ("    1.1 Background / Domain Context", "1"),
        ("        1.1.1 Existing Methods / Technologies", "2"),
        ("        1.1.2 Limitations of Existing Methods", "3"),
        ("    1.2 Aim and Motivation", "4"),
        ("        1.2.1 Aim", "4"),
        ("        1.2.2 Background", "4"),
        ("        1.2.3 Motivation for the Project", "5"),
        ("        1.2.4 Expected Contributions of the Project", "5"),
        ("    1.3 General Problem Statement", "6"),
        ("    1.4 Research Question", "6"),
        ("        1.4.1 Research Objectives", "6"),
        ("    1.5 Project Report Organization", "7"),
        ("Chapter 2: Literature Survey", "8"),
        ("    2.1 Identification Phase", "8"),
        ("    2.2 Screening Phase", "9"),
        ("    2.3 Eligibility Phase", "10"),
        ("    2.4 Inclusion Phase", "11"),
        ("    2.5 Summary of Literature Survey", "11"),
        ("    2.6 Summary Gap Analysis", "13"),
        ("        2.6.1 Observations from the Literature", "13"),
        ("        2.6.2 Research Gaps", "14"),
        ("    Table 2.1: Literature Review Table", "15"),
        ("Chapter 3: Methodology", "17"),
        ("    3.1 Proposed Robotic Vision System Architecture", "17"),
        ("    3.2 Industrial Dataset Specification and Defect Taxonomy", "20"),
        ("    3.3 YOLOv8-OBB Neural Network Architecture", "22"),
        ("    3.4 Mathematical Derivations of Multi-Task Loss Formulation", "24"),
        ("    3.5 Rotated Non-Maximum Suppression via Polygon Clipping", "26"),
        ("    3.6 Micro-Defect Augmentation Theory and Hyperparameter Optimization", "27"),
        ("    3.7 Industrial Edge Deployment and Middleware Integration", "29"),
        ("Chapter 4: Results and Discussion", "32"),
        ("    4.1 Quantitative Performance Analysis and Class Breakdown", "32"),
        ("    4.2 Systematic Ablation Study", "34"),
        ("    4.3 Training Convergence Dynamics", "35"),
        ("    4.4 Confusion Matrix and Error Analysis", "36"),
        ("    4.5 Qualitative Visual Inspection and Tight-Fitting Evaluation", "37"),
        ("    4.6 Edge Inference Latency and Hardware Profiling", "40"),
        ("    4.7 Cross-Architecture Comparative Evaluation", "41"),
        ("    4.8 Economic Feasibility and Return on Investment (ROI) Analysis", "43"),
        ("    4.9 Challenges, Limitations, and Failure Mode Analysis", "44"),
        ("Chapter 5: Conclusion and Future Direction", "46"),
        ("    5.1 Achievement of Research Objectives", "46"),
        ("    5.2 Key Project Outcomes", "47"),
        ("    5.3 Future Direction", "48"),
        ("References", "49"),
        ("Publications", "53"),
        ("Student Formatting & Submission Checklist", "54")
    ]
    
    while len(toc_table.rows) < len(toc_data) + 1:
        toc_table.add_row()
    while len(toc_table.rows) > len(toc_data) + 1:
        toc_table._tbl.remove(toc_table.rows[-1]._tr)
        
    hdr_cells = toc_table.rows[0].cells
    hdr_cells[0].text = "Contents / Chapter Title"
    hdr_cells[1].text = "Page No."
    for c in hdr_cells:
        for r in c.paragraphs[0].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            r.font.bold = True
            
    for idx, (title, pg) in enumerate(toc_data):
        row_cells = toc_table.rows[idx + 1].cells
        row_cells[0].text = title
        row_cells[1].text = pg
        row_cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        for c in row_cells:
            for r in c.paragraphs[0].runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
                if not title.startswith("    "):
                    r.font.bold = True

    # -------------------------------------------------------------
    # 8. LIST OF FIGURES & LIST OF TABLES (P70 - P77)
    # -------------------------------------------------------------
    paragraphs[70].text = "List of Figures"
    paragraphs[70].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[70].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = RGBColor(31, 78, 120)
        
    figures_list_text = (
        "Figure 2.1: PRISMA Flow Diagram for Systematic Literature Search and Selection Methodology ......... 10\n"
        "Figure 3.1: Architectural Block Diagram of Proposed Automated Robotic Vision Inspection Pipeline ...... 18\n"
        "Figure 3.2: Physical Industrial Packaging Conveyor Line and Optomechanical Inspection Cell Enclosure ... 19\n"
        "Figure 3.3: Industrial Real-Time Vision Inspection Station: Camera Setup and Touchscreen HMI Interface . 31\n"
        "Figure 4.1: Training Loss Convergence and Metric Trajectory Curves Across 100 Epochs .................... 35\n"
        "Figure 4.2: Normalized Confusion Matrix Across Nine Packaging Defect Categories ............................ 36\n"
        "Figure 4.3: Qualitative Inference Outputs with Oriented Bounding Box Tight-Fitting Delineation .......... 38\n"
        "Figure 4.4: Validation Precision-Recall (P-R) and F1-Confidence Curves on Validation Partition ........... 39\n"
        "Figure 4.5: Representative Validation Batch Inference Predictions with Sub-Millimeter Localizations ...... 40"
    )
    paragraphs[72].text = figures_list_text
    paragraphs[72].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for r in paragraphs[72].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        
    paragraphs[74].text = "List of Tables"
    paragraphs[74].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[74].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = RGBColor(31, 78, 120)
        
    tables_list_text = (
        "Table 2.1: Systematic Literature Review Matrix on Industrial Packaging Flaw Detection ................... 15\n"
        "Table 3.1: Defect Taxonomy, Instance Count, and Geometric Dimensional Profile Across Partitions ........ 21\n"
        "Table 3.2: Hyperparameter Configuration and Training Optimization Settings ................................... 28\n"
        "Table 4.1: Quantitative Performance Comparison Between Baseline and Proposed YOLOv8-OBB ........... 33\n"
        "Table 4.2: Systematic Ablation Study Evaluating Stepwise Algorithmic and Augmentation Contributions ... 34\n"
        "Table 4.3: Inference Latency and Computational Throughput Profile on Edge Industrial Hardware .......... 41\n"
        "Table 4.4: Cross-Architecture Performance Benchmark Across Deep Single-Stage and Two-Stage Detectors .. 42\n"
        "Table 4.5: Economic Feasibility and Return on Investment (ROI) Analysis for High-Volume Packaging ..... 44\n"
        "Table 5.1: Research Publication and Intellectual Property Details .................................................... 53"
    )
    paragraphs[76].text = tables_list_text
    paragraphs[76].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for r in paragraphs[76].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    # -------------------------------------------------------------
    # 9. ABBREVIATIONS (P78 & TABLE 1)
    # -------------------------------------------------------------
    paragraphs[78].text = "Abbreviations"
    paragraphs[78].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in paragraphs[78].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = RGBColor(31, 78, 120)
        
    abbrev_table = doc.tables[1]
    abbrev_data = [
        ("OBB", "Oriented Bounding Box"),
        ("HBB", "Horizontal Bounding Box"),
        ("AOI", "Automated Optical Inspection"),
        ("YOLO", "You Only Look Once"),
        ("mAP", "Mean Average Precision"),
        ("IoU", "Intersection over Union"),
        ("GWD", "Gaussian Wasserstein Distance"),
        ("VFL", "Varifocal Loss"),
        ("DFL", "Distribution Focal Loss"),
        ("CIoU", "Complete Intersection over Union"),
        ("NMS", "Non-Maximum Suppression"),
        ("ONNX", "Open Neural Network Exchange"),
        ("TensorRT", "High-Performance Deep Learning Inference Optimizer & Runtime"),
        ("ROS2", "Robot Operating System 2"),
        ("PLC", "Programmable Logic Controller"),
        ("FPS", "Frames Per Second"),
        ("CNN", "Convolutional Neural Network"),
        ("FPN", "Feature Pyramid Network"),
        ("PANet", "Path Aggregation Network"),
        ("C2f", "CSP Bottleneck with 2 Convolutions"),
        ("FTE", "Full-Time Equivalent (Labor Unit)"),
        ("ROI", "Return on Investment")
    ]
    
    while len(abbrev_table.rows) < len(abbrev_data) + 1:
        abbrev_table.add_row()
    while len(abbrev_table.rows) > len(abbrev_data) + 1:
        abbrev_table._tbl.remove(abbrev_table.rows[-1]._tr)
        
    hdr_abbrev = abbrev_table.rows[0].cells
    hdr_abbrev[0].text = "Abbreviation"
    hdr_abbrev[1].text = "Full Form / Technical Definition"
    for c in hdr_abbrev:
        for r in c.paragraphs[0].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            r.font.bold = True
            
    for idx, (abbr, full) in enumerate(abbrev_data):
        row_cells = abbrev_table.rows[idx + 1].cells
        row_cells[0].text = abbr
        row_cells[1].text = full
        for c in row_cells:
            for r in c.paragraphs[0].runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10.5)
        row_cells[0].paragraphs[0].runs[0].font.bold = True

    print("Front matter updated with exact layout and preserved drawing lines!")
