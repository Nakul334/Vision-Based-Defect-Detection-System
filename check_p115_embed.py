import docx
import re

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

xml = doc.paragraphs[115]._p.xml
embeds = re.findall(r'r:embed="([^"]+)"', xml)
print("P115 embeds:", embeds)
for e in embeds:
    print(f"  {e} -> {doc.part.rels[e].target_ref}")
