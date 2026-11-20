from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.platypus import Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

OUTPUT = "/mnt/user-data/outputs/BFC Polished Concrete Customer Acknowledgement.pdf"

DARK_BLUE   = colors.HexColor("#1A3A5C")
MID_BLUE    = colors.HexColor("#2E6DA4")
LIGHT_BLUE  = colors.HexColor("#EAF2FB")
ACCENT_GOLD = colors.HexColor("#C8922A")
LIGHT_GRAY  = colors.HexColor("#F5F5F5")
MID_GRAY    = colors.HexColor("#CCCCCC")
TEXT_DARK   = colors.HexColor("#1C1C1C")

doc = SimpleDocTemplate(
    OUTPUT, pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.5*inch, bottomMargin=0.5*inch,
)

styles = getSampleStyleSheet()
story = []
W = 7.0*inch

# ── LOGO HEADER ───────────────────────────────────────────────
logo = RLImage("/home/claude/bfc_logo_final.jpg", width=2.5*inch, height=0.55*inch)
contact_style = ParagraphStyle("CS", parent=styles["Normal"],
    fontSize=8, fontName="Helvetica", textColor=colors.HexColor("#444444"),
    alignment=TA_RIGHT, leading=12)
contact_info = (
    "4410 W. Union Hills Dr. Ste 7-125, Glendale AZ 85308<br/>"
    "P: 623-688-8422  |  Services@BrooksFloorCovering.com  |  ROC #226840"
)
header_table = Table([[logo, Paragraph(contact_info, contact_style)]],
                     colWidths=[2.8*inch, 4.2*inch])
header_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), colors.white),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0),(-1,-1), 6),
    ("BOTTOMPADDING", (0,0),(-1,-1), 6),
    ("LEFTPADDING",   (0,0),(0,-1),  0),
    ("RIGHTPADDING",  (1,0),(1,-1),  0),
    ("LINEBELOW",     (0,0),(-1,-1), 2, DARK_BLUE),
]))
story.append(header_table)
story.append(Spacer(1, 10))

# ── TITLE BANNER ──────────────────────────────────────────────
title_table = Table([[Paragraph(
    "Polished Concrete  Customer Acknowledgement",
    ParagraphStyle("TT", parent=styles["Normal"], fontSize=13,
        fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_CENTER))
]], colWidths=[W])
title_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), ACCENT_GOLD),
    ("TOPPADDING",    (0,0),(-1,-1), 10),
    ("BOTTOMPADDING", (0,0),(-1,-1), 10),
]))
story.append(title_table)
story.append(Spacer(1, 10))

# ── INTRO ─────────────────────────────────────────────────────
intro_style = ParagraphStyle("IS", parent=styles["Normal"], fontSize=9.5,
    fontName="Helvetica", textColor=TEXT_DARK, leading=15, alignment=TA_JUSTIFY)

story.append(Paragraph(
    "Polished concrete is a beautiful and durable flooring option, but it is also a process that requires a thorough "
    "understanding of its nature before proceeding. Every concrete slab is unique, and the final appearance of a "
    "polished concrete floor is influenced by many factors beyond our control. Please read the following carefully "
    "and ask any questions before work begins. Your signature below confirms that you have read, understood, and "
    "accepted the characteristics and limitations of polished concrete.",
    intro_style))
story.append(Spacer(1, 12))

# ── SECTION HEADER HELPER ─────────────────────────────────────
def section_header(text):
    t = Table([[Paragraph(text, ParagraphStyle("SH", parent=styles["Normal"],
        fontSize=10, fontName="Helvetica-Bold", textColor=colors.white))]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), MID_BLUE),
        ("TOPPADDING",    (0,0),(-1,-1), 6),
        ("BOTTOMPADDING", (0,0),(-1,-1), 6),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
    ]))
    return t

bullet_style = ParagraphStyle("BS", parent=styles["Normal"], fontSize=9,
    fontName="Helvetica", textColor=TEXT_DARK, leading=14,
    leftIndent=14, firstLineIndent=-10, spaceAfter=3)

def bullet(text):
    return Paragraph(f"•  {text}", bullet_style)

body_style = ParagraphStyle("BDY", parent=styles["Normal"], fontSize=9,
    fontName="Helvetica", textColor=TEXT_DARK, leading=14, alignment=TA_JUSTIFY, spaceAfter=4)

warning_style = ParagraphStyle("WS", parent=styles["Normal"], fontSize=9,
    fontName="Helvetica-Bold", textColor=colors.HexColor("#8B0000"), leading=14,
    leftIndent=14, firstLineIndent=-10, spaceAfter=3)

def warning_bullet(text):
    return Paragraph(f"•  {text}", warning_style)

# ── SECTION 1: SLAB CHARACTERISTICS ──────────────────────────
items_1 = [
    "Every concrete slab is unique. Concrete porosity, hardness, flatness, and the method used by the original concrete finisher all directly affect the final appearance. The same process performed on different slabs can produce entirely different results.",
    "Wavy or uneven floors may cause machines to tilt at odd angles, potentially leaving irregular lines or scratches that require additional labor to address.",
    "Inconsistent aggregate exposure will occur unless the slab was specifically designed, poured, and finished with the intent of polishing.",
]
story.append(KeepTogether([
    section_header("1.  Slab Characteristics and Natural Variation"),
    Spacer(1, 4),
    Table([[b] for b in [bullet(i) for i in items_1]], colWidths=[W],
        style=TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT_GRAY),
                          ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
                          ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                          ("LINEBELOW",(0,-1),(-1,-1),0.5,MID_GRAY)])),
]))
story.append(Spacer(1, 10))

# ── SECTION 2: PRE-EXISTING CONDITIONS ───────────────────────
items_2 = [
    "Previous floor coverings, adhesive residue, tile grid lines, and patterns that were not visible prior to grinding may become apparent once the surface is exposed.",
    "Concrete finisher footprints, tooling marks, screed marks, trowel patterns, and swirl marks left at the time the slab was originally finished may become visible during the polishing process. These patterns are embedded in the slab and cannot be fully removed.",
    "Any prior application or spill involving chemicals, oils, solvents, adhesives, thinset, paint, coatings, or similar substances may show through in some form.",
    "Upon grinding, small hairline cracks may become more visible throughout the slab. This is known as crazing, a common occurrence caused by rapid moisture loss during the original curing process.",
    "Efflorescence (white mineral deposits) may surface as the slab is opened up during grinding.",
    "When dye is applied, absorption will vary across the slab due to differences in porosity, hardness, and surface density. Color variation from one area to another is a natural characteristic of dyeing concrete and is not a defect in workmanship.",
    "Extremely wavy or uneven slabs (low floor flatness numbers) may limit how evenly tooling can contact the surface, affecting consistency of the finished appearance.",
    "Areas where the slab was cut and re-poured, including utility trenches, patches, and saw-cut repairs, will almost always look different than the surrounding concrete. These areas cannot be made to match.",
    "Holes, voids, and spalls in the slab will require repair. All repaired areas will be visible in the finished floor.",
]
story.append(KeepTogether([
    section_header("2.  Pre-Existing Conditions"),
    Spacer(1, 4),
    Table([[b] for b in [bullet(i) for i in items_2]], colWidths=[W],
        style=TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT_GRAY),
                          ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
                          ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                          ("LINEBELOW",(0,-1),(-1,-1),0.5,MID_GRAY)])),
]))
story.append(Spacer(1, 10))

# ── SECTION 3: REPAIRS AND CRACK FILL ────────────────────────
items_3 = [
    "All repairs (cracks, divots, control joints, filled areas) will be visible in the finished floor. This is inherent to the nature of polished concrete.",
    "Grout coat and crack repair materials will not match the surrounding concrete. Color variation between repair areas and the base slab is to be expected. Repair material is functional, not aesthetic.",
    "Repair materials may look different from one area of the floor to another, even when the same product is used.",
    "Filled areas may remain slightly lower than the surrounding surface, or repair material may be pulled out during the polishing process. Both outcomes are typical.",
    "Repairs are performed during the polishing process and are subsequently run over with transitioning tooling on heavy equipment. Some repairs may require re-application.",
    "Joint filler is functional, not cosmetic. Color and texture will not match the concrete.",
    "Two-part urethane repair materials such as TX3 are designed as concrete repair products, not aesthetic match products. Their final appearance is a single solid color that may complement but will not match the surrounding concrete.",
    "The color of two-part repair materials can change when ground or cut into during the polishing process, as this exposes different portions of the cured material. When Part A and Part B mix and cure, a chemical reaction occurs that can cause the color to flash or vary. This is a known characteristic of the product and not a workmanship defect.",
]
story.append(KeepTogether([
    section_header("3.  Repairs, Crack Fill, and Joint Filler"),
    Spacer(1, 4),
    Table([[b] for b in [bullet(i) for i in items_3]], colWidths=[W],
        style=TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT_GRAY),
                          ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
                          ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                          ("LINEBELOW",(0,-1),(-1,-1),0.5,MID_GRAY)])),
]))
story.append(Spacer(1, 10))

# ── SECTION 4: SCOPE AND PROCESS ─────────────────────────────
items_4 = [
    "The polishing process is specific to the grit steps outlined in the estimate. It does not include cutting deeper into the slab or polishing to a higher sheen than quoted unless separately agreed upon in writing.",
    "The price includes normal prep work. Any additional prep identified at time of installation, including extra chemicals, grout coat, joint work, or crack repair, will be assessed on-site and billed accordingly.",
    "Brooks Floor Covering is not responsible for inconsistent aggregate exposure. Aggregate consistency is determined by the original pour and finishing of the slab.",
    "Densifier is applied to harden and dust-proof the slab. Results vary based on the porosity and hardness of the concrete.",
    "Sealer is applied to protect the surface. Sealer sheen and longevity will vary based on traffic, cleaning methods, and ongoing maintenance.",
    "Polished concrete is not recommended for areas subject to prolonged chemical exposure, harsh solvents, or standing water. Such conditions can deteriorate the sealer and affect the surface over time.",
    "The finished sheen level is determined by the grit sequence outlined in the estimate and the characteristics of the slab. Results will vary when comparing different slabs or projects, as each slab polishes differently based on its own conditions.",
]
story.append(KeepTogether([
    section_header("4.  Scope of Work and Process Limitations"),
    Spacer(1, 4),
    Table([[b] for b in [bullet(i) for i in items_4]], colWidths=[W],
        style=TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT_GRAY),
                          ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
                          ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                          ("LINEBELOW",(0,-1),(-1,-1),0.5,MID_GRAY)])),
]))
story.append(Spacer(1, 10))

# ── SECTION 5: CARE AND MAINTENANCE ──────────────────────────
items_5_bullets = [
    "Polished concrete should be cleaned with a neutral pH cleaner only. Acidic or alkaline cleaners will etch and damage the surface.",
    "Do not use oil-based soaps, wax, or any topical coating on polished concrete. These products cause buildup and will alter the appearance of the finish.",
    "Rubber-backed mats may discolor or stain polished concrete over time. Use only breathable mats designed for use on polished floors.",
    "Standing water and spills should be cleaned up promptly. While polished concrete is durable, prolonged moisture exposure can affect the sealer and surface.",
    "Heavy scratching from abrasive materials (sand, grit tracked in from outside) will dull the finish over time. Entry mats are recommended at all exterior doors.",

]

items_5_warnings = [
    "NEVER use tape of any kind on polished concrete. Tape — including painter's tape, masking tape, duct tape, and all adhesive products — will bond to the sealer and damage or permanently dull the surface when removed.",
    "NEVER drag heavy objects or furniture directly across polished concrete. Always use felt pads or lift and carry.",
    "NEVER use abrasive scrubbing pads, steel wool, or scouring agents on the surface.",
]

story.append(KeepTogether([
    section_header("5.  Care, Maintenance, and Important Warnings"),
    Spacer(1, 4),
    Table([[b] for b in [bullet(i) for i in items_5_bullets]], colWidths=[W],
        style=TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT_GRAY),
                          ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
                          ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10)])),
]))
story.append(Table([[b] for b in [warning_bullet(i) for i in items_5_warnings]], colWidths=[W],
    style=TableStyle([("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#FFF5F5")),
                      ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                      ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
                      ("LINEBELOW",(0,-1),(-1,-1),0.5,MID_GRAY),
                      ("LINEABOVE",(0,0),(-1,0),0.5,colors.HexColor("#8B0000"))])))
story.append(Spacer(1, 12))

# ── ACKNOWLEDGEMENT STATEMENT ─────────────────────────────────
ack_table = Table([[Paragraph(
    "By signing below, I acknowledge that I have read and fully understand the characteristics, limitations, "
    "and care requirements of polished concrete as outlined in this document. I accept these conditions and "
    "authorize Brooks Floor Covering to proceed with the work as described in the accompanying estimate.",
    ParagraphStyle("ACK", parent=styles["Normal"], fontSize=9, fontName="Helvetica",
        textColor=DARK_BLUE, leading=14, alignment=TA_JUSTIFY))
]], colWidths=[W])
ack_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), LIGHT_BLUE),
    ("TOPPADDING",    (0,0),(-1,-1), 10),
    ("BOTTOMPADDING", (0,0),(-1,-1), 10),
    ("LEFTPADDING",   (0,0),(-1,-1), 12),
    ("RIGHTPADDING",  (0,0),(-1,-1), 12),
    ("BOX",           (0,0),(-1,-1), 1, MID_BLUE),
]))
story.append(ack_table)
story.append(Spacer(1, 14))

# ── SIGNATURE BLOCK ───────────────────────────────────────────
sig_lbl = ParagraphStyle("SL", parent=styles["Normal"], fontSize=9,
    fontName="Helvetica-Bold", textColor=DARK_BLUE)
sig_line = ParagraphStyle("SLN", parent=styles["Normal"], fontSize=9,
    fontName="Helvetica", textColor=TEXT_DARK)

sig_data = [
    [Paragraph("Print Name:", sig_lbl), Paragraph("", sig_line),
     Paragraph("Date:", sig_lbl), Paragraph("", sig_line)],
    [Paragraph("Signature:", sig_lbl), Paragraph("", sig_line), "", ""],
]
sig_table = Table(sig_data, colWidths=[1.1*inch, 2.9*inch, 0.6*inch, 2.4*inch])
sig_table.setStyle(TableStyle([
    ("BOX",           (0,0),(-1,-1), 0.75, DARK_BLUE),
    ("BACKGROUND",    (0,0),(-1,-1), colors.white),
    ("TOPPADDING",    (0,0),(-1,-1), 12),
    ("BOTTOMPADDING", (0,0),(-1,-1), 12),
    ("LEFTPADDING",   (0,0),(-1,-1), 10),
    ("RIGHTPADDING",  (0,0),(-1,-1), 10),
    ("LINEBELOW",     (0,0),(1,0),   0.5, MID_GRAY),   # Print name line
    ("LINEBELOW",     (2,0),(3,0),   0.5, MID_GRAY),   # Date line
    ("LINEBELOW",     (0,1),(1,1),   0.5, MID_GRAY),   # Signature line
    ("SPAN",          (2,1),(3,1)),
    ("LINEBELOW",     (0,0),(-1,0),  0.5, MID_GRAY),
    ("VALIGN",        (0,0),(-1,-1), "BOTTOM"),
]))
story.append(sig_table)
story.append(Spacer(1, 14))

# ── FOOTER ────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=1, color=MID_GRAY))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Brooks Floor Covering  |  brooksfloorcovering.com  |  ROC #226840  |  Services@BrooksFloorCovering.com",
    ParagraphStyle("Ft", parent=styles["Normal"], fontSize=8,
        fontName="Helvetica", textColor=colors.HexColor("#999999"), alignment=TA_CENTER)))

doc.build(story)
print(f"Done → {OUTPUT}")
