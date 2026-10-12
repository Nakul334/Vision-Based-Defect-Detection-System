import docx
from PIL import Image
import io

doc = docx.Document(r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Major_project Report_Templet.docx')

im1_blob = doc.part.rels['rId7'].target_part.blob
im1 = Image.open(io.BytesIO(im1_blob))
print(f"Image1: format={im1.format}, size={im1.size}")

im2_blob = doc.part.rels['rId20'].target_part.blob
im2 = Image.open(io.BytesIO(im2_blob))
print(f"Image2: format={im2.format}, size={im2.size}")
