import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

for i, sec in enumerate(doc.sections):
    xml = sec._sectPr.xml
    # check page numbering type
    pgNum = sec._sectPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pgNumType')
    pgNum_str = pgNum.attrib if pgNum is not None else "None"
    print(f"Section {i}: pgNumType={pgNum_str}")
