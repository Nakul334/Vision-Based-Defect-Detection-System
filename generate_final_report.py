"""
Full Major Project-I Report Generation Script for DMIHER FEAT
Project: An Automated Robotic Vision System for Precision Surface Defect Inspection in Industrial Packaging Using YOLOv8-OBB
Authors: Nakul Dube, Sahil Dhurve, Mukul Argade
Guide: Dr. Subodh Daronde
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8'
TEMPLATE_PATH = os.path.join(BASE_DIR, 'Major_project Report_Templet.docx')
OUTPUT_PATH = os.path.join(BASE_DIR, 'Major_Project_Report_Final.docx')
FIGURES_DIR = os.path.join(BASE_DIR, r'Rice_Defect_Detection_OBB\paper\figures')
VAL_DIR = os.path.join(BASE_DIR, r'Rice_Defect_Detection_OBB\runs\obb\val')

print("Starting generation script setup...")
