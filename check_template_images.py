import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

images = []
for rel in doc.part.rels.values():
    if "image" in rel.target_ref:
        images.append((rel.target_ref, len(rel.target_part.blob)))

print("Images found in template:", len(images))
for img in images:
    print(img)
