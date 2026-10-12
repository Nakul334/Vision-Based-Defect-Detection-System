import docx

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

children = list(doc._body._element)
print(f"Total children: {len(children)}")
for idx, child in enumerate(children):
    tag = child.tag.split('}')[-1]
    text = ""
    if tag == 'p':
        text = "".join(child.itertext())
    elif tag == 'tbl':
        text = f"TABLE with {len(child.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'))} rows"
    elif tag == 'sectPr':
        text = "SECTPR (Section Break)"
    
    clean_text = text[:60].encode('ascii', 'replace').decode('ascii')
    if idx < 15 or (70 <= idx <= 95) or idx >= 180:
        print(f"Child {idx:03d} [{tag}]: {clean_text}")
