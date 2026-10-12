import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

with open(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\template_logo.jpg', 'wb') as f:
    f.write(doc.part.rels['rId7'].target_part.blob)

with open(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\template_prisma.jpg', 'wb') as f:
    f.write(doc.part.rels['rId20'].target_part.blob)

print("Saved template_logo.jpg and template_prisma.jpg")
