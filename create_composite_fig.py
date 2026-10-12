from PIL import Image, ImageDraw, ImageFont
import os

fig_dir = r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Rice_Defect_Detection_OBB\paper\figures'
img_scratch = Image.open(os.path.join(fig_dir, 'defect_sample_scratch.jpg'))
img_wrinkle = Image.open(os.path.join(fig_dir, 'defect_sample_wrinkle.jpg'))
img_foreign = Image.open(os.path.join(fig_dir, 'defect_sample_foreign.jpg'))
img_pinhole = Image.open(os.path.join(fig_dir, 'defect_sample_pinhole.jpg'))

# Let's inspect sizes
print("Scratch:", img_scratch.size)
print("Wrinkle:", img_wrinkle.size)
print("Foreign:", img_foreign.size)
print("Pinhole:", img_pinhole.size)

# Create a composite 2x2 image with target size 600x600 each
target_w, target_h = 600, 450
img_scratch_r = img_scratch.resize((target_w, target_h), Image.Resampling.LANCZOS)
img_wrinkle_r = img_wrinkle.resize((target_w, target_h), Image.Resampling.LANCZOS)
img_foreign_r = img_foreign.resize((target_w, target_h), Image.Resampling.LANCZOS)
img_pinhole_r = img_pinhole.resize((target_w, target_h), Image.Resampling.LANCZOS)

padding = 20
label_bar = 40
grid_w = target_w * 2 + padding * 3
grid_h = (target_h + label_bar) * 2 + padding * 3

composite = Image.new('RGB', (grid_w, grid_h), color=(255, 255, 255))
draw = ImageDraw.Draw(composite)

try:
    font = ImageFont.truetype("arial.ttf", 22)
except:
    font = ImageFont.load_default()

items = [
    (img_scratch_r, "(a) Micro-Scratch Defect (Tight OBB Localization)", padding, padding),
    (img_wrinkle_r, "(b) Shrivel Wrinkle Flaw (Oriented Bounding Box)", target_w + padding * 2, padding),
    (img_foreign_r, "(c) Defective Foreign Body Inclusion", padding, target_h + label_bar + padding * 2),
    (img_pinhole_r, "(d) Thermoforming Pinhole Perforation", target_w + padding * 2, target_h + label_bar + padding * 2)
]

for img, label, x, y in items:
    composite.paste(img, (x, y))
    # Draw border around image
    draw.rectangle([x, y, x + target_w, y + target_h], outline=(180, 180, 180), width=2)
    # Draw label text below
    draw.text((x + 10, y + target_h + 8), label, fill=(20, 20, 20), font=font)

out_path = os.path.join(fig_dir, 'composite_defect_samples.jpg')
composite.save(out_path, quality=95)
print(f"Saved composite image to {out_path} with size {composite.size}")
