"""
Master Builder Script for Major Project Report Generation.
Assembles Front Matter, Chapters 1-5, References, Publications, and Checklist.
Integrates user PRISMA chart and technical metrics.
"""

import os
import sys
import docx
from common_styles import configure_document_styles, set_page_number_footer
from front_matter import update_front_matter
from build_chapter1 import add_chapter_1
from build_chapter2 import add_chapter_2
from build_chapter3 import add_chapter_3
from build_chapter4 import add_chapter_4
from build_chapter5 import add_chapter_5
from build_back_matter import add_back_matter

BASE_DIR = r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8'
TEMPLATE_PATH = os.path.join(BASE_DIR, 'Major_project Report_Templet.docx')
OUTPUT_PATH = os.path.join(BASE_DIR, 'Major_Project_Report_Final.docx')
OUTPUT_PATH_V2 = os.path.join(BASE_DIR, 'Major_Project_Report_Final_v2.docx')

def build_report():
    print(f"Loading template from: {TEMPLATE_PATH}")
    doc = docx.Document(TEMPLATE_PATH)
    
    print("Configuring document styles...")
    configure_document_styles(doc)
    
    print("Updating Front Matter (Sections 0 & 1)...")
    update_front_matter(doc)
    
    print("Pruning template placeholder elements from Section 2...")
    children = list(doc._body._element)
    print(f"  Initial body children: {len(children)}")
    
    for c in children[82:-1]:
        doc._body._element.remove(c)
        
    print(f"  Body children after pruning: {len(list(doc._body._element))}")
    
    print("Configuring Section 2 footer page numbering (decimal, start=1)...")
    set_page_number_footer(doc.sections[2], fmt="decimal", start=1)
    
    print("Building Chapter 1: Introduction...")
    add_chapter_1(doc)
    
    print("Building Chapter 2: Literature Survey...")
    add_chapter_2(doc, BASE_DIR)
    
    print("Building Chapter 3: Methodology...")
    add_chapter_3(doc, BASE_DIR)
    
    print("Building Chapter 4: Results and Discussion...")
    add_chapter_4(doc, BASE_DIR)
    
    print("Building Chapter 5: Conclusion and Future Direction...")
    add_chapter_5(doc)
    
    print("Building Back Matter (References, Publications, Checklist)...")
    add_back_matter(doc)
    
    target_saved = None
    try:
        print(f"Attempting to save to: {OUTPUT_PATH}")
        doc.save(OUTPUT_PATH)
        target_saved = OUTPUT_PATH
        print("Document saved successfully to primary path!")
    except PermissionError:
        print(f"Notice: {OUTPUT_PATH} is currently open in Microsoft Word.")
        print(f"Saving to fallback path: {OUTPUT_PATH_V2}")
        doc.save(OUTPUT_PATH_V2)
        target_saved = OUTPUT_PATH_V2
        print(f"Document saved successfully to: {OUTPUT_PATH_V2}")

    return target_saved

if __name__ == '__main__':
    saved_file = build_report()
    print("Build complete. Output:", saved_file)
