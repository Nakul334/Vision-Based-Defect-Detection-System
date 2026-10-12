import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8.5, 9.5), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Colors
header_color = '#1f4e78'
box_color = '#f2f4f8'
border_color = '#2f5597'
text_color = '#1a1a1a'

# Title
ax.text(50, 97, 'PRISMA 2020 Flow Diagram for Literature Search & Selection', 
        ha='center', va='center', fontsize=13, fontweight='bold', color=header_color)

def draw_box(x, y, w, h, title, text_lines, is_side=False):
    fill = '#fff2cc' if is_side else box_color
    stroke = '#d6b656' if is_side else border_color
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", 
                                  facecolor=fill, edgecolor=stroke, linewidth=1.5)
    ax.add_patch(rect)
    
    # Title
    ax.text(x + w/2, y + h - 2.2, title, ha='center', va='center', 
            fontsize=10, fontweight='bold', color='#1f4e78' if not is_side else '#b45f06')
    
    # Content
    y_cursor = y + h - 5.5
    for line in text_lines:
        ax.text(x + 1.5, y_cursor, line, ha='left', va='center', fontsize=8.5, color=text_color)
        y_cursor -= 2.8

def draw_phase_banner(y, h, text):
    banner = patches.Rectangle((2, y), 6, h, facecolor=header_color, edgecolor=header_color)
    ax.add_patch(banner)
    ax.text(5, y + h/2, text, ha='center', va='center', rotation=90, 
            fontsize=9.5, fontweight='bold', color='white')

# 1. Identification
draw_phase_banner(76, 17, 'IDENTIFICATION')
draw_box(12, 76, 52, 17, 'Records Identified from Databases', [
    'Databases searched: IEEE Xplore, ScienceDirect,',
    'SpringerLink, ACM Digital Library (2018–2026)',
    '• IEEE Xplore: n = 184',
    '• ScienceDirect (Elsevier): n = 212',
    '• SpringerLink: n = 145',
    '• ACM Digital Library: n = 78   [Total: n = 619]'
])

draw_box(68, 79, 28, 12, 'Duplicate Removal', [
    'Duplicate records removed',
    'prior to screening',
    '(n = 142)'
], is_side=True)

# Arrow from DB to duplicates
ax.annotate('', xy=(68, 85), xytext=(64, 85),
            arrowprops=dict(arrowstyle="->", color='#333333', lw=1.5))

# 2. Screening
draw_phase_banner(51, 20, 'SCREENING')
draw_box(12, 53, 52, 16, 'Records Screened', [
    'Records screened based on Title & Abstract',
    '(n = 477 records)',
    'Inclusion criteria: Deep learning, surface flaw,',
    'automated inspection, packaging or manufacturing.'
])

draw_box(68, 54, 28, 14, 'Records Excluded', [
    'Records excluded by',
    'title/abstract screening',
    '(n = 385)',
    'Reasons: Non-optical/medical,',
    'irrelevant flaw geometry.'
], is_side=True)

# Arrow down from ID to Screening
ax.annotate('', xy=(38, 69), xytext=(38, 76),
            arrowprops=dict(arrowstyle="->", color='#333333', lw=1.5))
# Arrow across to Excluded
ax.annotate('', xy=(68, 61), xytext=(64, 61),
            arrowprops=dict(arrowstyle="->", color='#333333', lw=1.5))

# 3. Eligibility
draw_phase_banner(26, 21, 'ELIGIBILITY')
draw_box(12, 28, 52, 17, 'Reports Assessed for Eligibility', [
    'Full-text articles retrieved and evaluated',
    'for detailed methodological eligibility (n = 92)',
    'Criteria: Quantitative metrics (mAP, FPS),',
    'bounding representations (HBB/OBB),',
    'industrial high-speed packaging relevance.'
])

draw_box(68, 28, 28, 17, 'Full-Text Excluded', [
    'Full-text articles excluded',
    'with specific reasons (n = 62):',
    '• Acoustic/ultrasound (n = 18)',
    '• Lacking mAP/latency data (n = 24)',
    '• Theoretical/no edge impl. (n = 20)'
], is_side=True)

# Arrow down from Screening to Eligibility
ax.annotate('', xy=(38, 45), xytext=(38, 53),
            arrowprops=dict(arrowstyle="->", color='#333333', lw=1.5))
# Arrow across to Full-Text Excluded
ax.annotate('', xy=(68, 36.5), xytext=(64, 36.5),
            arrowprops=dict(arrowstyle="->", color='#333333', lw=1.5))

# 4. Inclusion
draw_phase_banner(4, 18, 'INCLUDED')
draw_box(12, 5, 52, 16, 'Studies Included in Synthesis', [
    'Final benchmark corpus of included studies:',
    '(n = 30 seminal articles)',
    '• Deep learning surface AOI: 12 studies',
    '• Oriented bounding box architectures: 10 studies',
    '• Micro-defect / edge deployment: 8 studies'
])

# Arrow down from Eligibility to Included
ax.annotate('', xy=(38, 21), xytext=(38, 28),
            arrowprops=dict(arrowstyle="->", color='#333333', lw=1.5))

plt.tight_layout()
out_fig = r'C:\Users\nakul\Downloads\Major_P_CJ_Rice\Rice_Case_01.yolov8\Rice_Defect_Detection_OBB\paper\figures\prisma_flowchart.png'
plt.savefig(out_fig, bbox_inches='tight', dpi=300)
plt.close()
print("Saved PRISMA flowchart to:", out_fig)
