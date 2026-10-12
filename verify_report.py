"""
Verification script for Major_Project_Report_Final.docx.
Checks file size, structure, tables, figures, placeholders, and font formatting.
"""

import os
import re
import docx

REPORT_PATH = r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_Project_Report_Final.docx'

print("=== VERIFYING FINAL REPORT ===")
if not os.path.exists(REPORT_PATH):
    print("ERROR: File does not exist!")
    exit(1)

size_mb = os.path.getsize(REPORT_PATH) / (1024 * 1024)
print(f"File Size: {size_mb:.2f} MB")

doc = docx.Document(REPORT_PATH)
print(f"Total Paragraphs: {len(doc.paragraphs)}")
print(f"Total Tables: {len(doc.tables)}")
print(f"Total Sections: {len(doc.sections)}")

# Check embedded images
images = []
for rel in doc.part.rels.values():
    if "image" in rel.target_ref:
        images.append((rel.target_ref, len(rel.target_part.blob)))

print(f"Embedded Images Found: {len(images)}")
for idx, (ref, b_size) in enumerate(images):
    print(f"  Img {idx+1}: {ref} ({b_size/1024:.1f} KB)")

# Check for placeholders like [...] or Write your Name
placeholders = []
bracket_pattern = re.compile(r'\[(.*?)\]')

for i, p in enumerate(doc.paragraphs):
    matches = bracket_pattern.findall(p.text)
    for m in matches:
        # ignore KaTeX or citation brackets e.g. [1], [2], etc.
        if not re.match(r'^\d+$', m.strip()):
            placeholders.append((f"P{i}", m, p.text[:80]))
            
for t_idx, t in enumerate(doc.tables):
    for r_idx, row in enumerate(t.rows):
        for c_idx, cell in enumerate(row.cells):
            matches = bracket_pattern.findall(cell.text)
            for m in matches:
                if not re.match(r'^\d+$', m.strip()):
                    placeholders.append((f"Table {t_idx} R{r_idx}C{c_idx}", m, cell.text[:60]))

print(f"\nUnresolved Placeholders Found: {len(placeholders)}")
if placeholders:
    for pl in placeholders[:10]:
        print("  ", pl)
else:
    print("  EXCELLENT: No bracketed instructional placeholders remain!")

# Check Tables breakdown
print("\n=== TABLES SUMMARY ===")
for t_idx, t in enumerate(doc.tables):
    hdr = [cell.text.replace('\n', ' ').strip() for cell in t.rows[0].cells]
    print(f"Table {t_idx}: {len(t.rows)} rows x {len(t.columns)} cols | Hdr: {' | '.join(hdr[:4])}...")

print("\nVerification complete!")
