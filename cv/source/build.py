import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, Flowable, CondPageBreak, KeepTogether)
import content as C

PHOTO, OUT = sys.argv[1], sys.argv[2]


def font(*paths):
    """First existing file: Linux (Liberation Sans, DejaVu Sans) or Windows (Arial has the same metrics)."""
    for p in paths:
        if os.path.exists(p):
            return p
    raise SystemExit('Font not found: ' + ', '.join(paths))


F = '/usr/share/fonts/truetype/'
WF = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', '')
pdfmetrics.registerFont(TTFont('L', font(F + 'liberation/LiberationSans-Regular.ttf', WF + 'arial.ttf')))
pdfmetrics.registerFont(TTFont('LB', font(F + 'liberation/LiberationSans-Bold.ttf', WF + 'arialbd.ttf')))
pdfmetrics.registerFont(TTFont('DV', font(F + 'dejavu/DejaVuSans.ttf', WF + 'seguisym.ttf', WF + 'arial.ttf')))
pdfmetrics.registerFontFamily('L', normal='L', bold='LB', italic='L', boldItalic='LB')

W, H = letter
RED = colors.HexColor('#2DD4BF')
GREY = colors.HexColor('#ededed')
MUTED = colors.HexColor('#9a9a9a')
LM = 30            # content left margin
LABEL_W = 150
CW = W - 2 * LM    # content width

body = ParagraphStyle('body', fontName='L', fontSize=9.5, leading=12.2, textColor=colors.black)
label = ParagraphStyle('label', parent=body, fontName='LB', alignment=TA_RIGHT)
bullet = ParagraphStyle('bullet', parent=body, leftIndent=14, firstLineIndent=-14)
h_sec = ParagraphStyle('hsec', fontName='L', fontSize=19, leading=23)
h_sub = ParagraphStyle('hsub', fontName='L', fontSize=14.5, leading=18)
h_item = ParagraphStyle('hitem', fontName='LB', fontSize=11.5, leading=14)
meta = ParagraphStyle('meta', parent=body, textColor=colors.HexColor('#555555'))

BUL = '<font name="DV" size="6.5">○</font>&nbsp;&nbsp;&nbsp;'
def B(t): return Paragraph(BUL + t, bullet)


class Band(Flowable):
    """Full-bleed grey band wrapping inner flowables."""
    def __init__(self, inner, pad=9):
        super().__init__(); self.inner, self.pad = inner, pad
    def wrap(self, aw, ah):
        self.aw = aw
        self.hs = [f.wrap(aw, ah)[1] for f in self.inner]
        self.height = sum(self.hs) + 2 * self.pad
        return aw, self.height
    def draw(self):
        c = self.canv
        c.setFillColor(GREY); c.rect(-LM, 0, W, self.height, stroke=0, fill=1)
        y = self.height - self.pad
        for f, h in zip(self.inner, self.hs):
            y -= h; f.drawOn(c, 0, y)


class SectionTitle(Flowable):
    def __init__(self, text, style=h_sec):
        super().__init__(); self.p = Paragraph(text, style)
    def wrap(self, aw, ah):
        self.ph = self.p.wrap(aw, ah)[1]; self.height = self.ph + 7; return aw, self.height
    def draw(self):
        self.p.drawOn(self.canv, 0, 7)
        self.canv.setFillColor(RED); self.canv.rect(0, 0, 46, 3.2, stroke=0, fill=1)


def rows_table(rows, extra_style=()):
    """rows: list of (label_html or '', flowable)."""
    data = [[Paragraph(l, label) if l else '', v] for l, v in rows]
    t = Table(data, colWidths=[LABEL_W, CW - LABEL_W])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (0, -1), 10),
        ('RIGHTPADDING', (1, 0), (1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1.6), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.6),
        ('NOSPLIT', (0, 0), (-1, min(3, len(rows) - 1))), ('NOSPLIT', (0, max(0, len(rows) - 3)), (-1, -1)),
        *extra_style]))
    return t


def item_header(title, sub):
    return Band([Paragraph(title, h_item), Spacer(1, 2), Paragraph(sub, meta)], pad=7)


def labelled(lbl, bullets):
    return [(lbl if i == 0 else '', B(b)) for i, b in enumerate(bullets)]


def first_page(c, doc):
    # header: name, red bar, title, years, round photo
    c.saveState()
    c.setFont('LB', 30); c.drawString(LM, H - 62, 'Siarhei Vei')
    c.setFillColor(RED); c.rect(LM, H - 76, 54, 4, stroke=0, fill=1)
    c.setFillColor(colors.black); c.setFont('L', 15.5); c.drawString(LM, H - 104, 'Senior fullstack engineer')
    c.setFillColor(MUTED); c.setFont('L', 13.5); c.drawString(LM, H - 123, f'{C.YEARS} years of experience')
    r, cx, cy = 44, W - LM - 60, H - 84
    p = c.beginPath(); p.circle(cx, cy, r); c.clipPath(p, stroke=0, fill=0)
    c.drawImage(PHOTO, cx - r, cy - r, 2 * r, 2 * r)
    c.restoreState()
    footer(c, doc)


def footer(c, doc):
    c.saveState(); c.setFont('L', 8); c.setFillColor(MUTED)
    c.drawRightString(W - LM, 20, f'Siarhei Vei · {doc.page}'); c.restoreState()


doc = BaseDocTemplate(OUT, pagesize=letter, title='Siarhei Vei - Senior fullstack engineer', author='Siarhei Vei')
fr = dict(leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([
    PageTemplate('first', [Frame(LM, 36, CW, H - 36 - 140, **fr)], onPage=first_page, autoNextPageTemplate='rest'),
    PageTemplate('rest', [Frame(LM, 36, CW, H - 36 - 34, **fr)], onPage=footer),
])

S = []
S.append(Band([B(t) for t in C.SUMMARY]))
S.append(Spacer(1, 14))

core = Table([[SectionTitle('Core competencies'), Paragraph(C.CORE, body)]], colWidths=[LABEL_W + 22, CW - LABEL_W - 22])
core.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                          ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
                          ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
S += [core, Spacer(1, 14)]

S += [Paragraph('Technical skills', h_sub), Spacer(1, 6)]
S.append(rows_table([(l, Paragraph(v, body)) for l, v in C.SKILLS]))
S += [Spacer(1, 10), Paragraph('Soft skills', h_sub), Spacer(1, 5)]
S += [B(t) for t in C.SOFT]
S.append(Spacer(1, 12))

edu = rows_table([
    ('Education:', Paragraph('<b>Brest State Technical University (BSTU)</b><br/>Bachelor of Applied Science in Applied Information Technology Software', body)),
    ('Languages:', Paragraph('English - Upper-Intermediate', body)),
])
S += [Band([edu]), Spacer(1, 14)]

# certificates
cert_rows = []
for name, sub, url in C.CERTS:
    link = f' · <a href="{url}" color="#0F766E">{"verify" if "skilljar" in url else "view certificate"}</a>' if url else ''
    cert_rows.append(('', Paragraph(f'<b>{name}</b><br/><font color="#555555">{sub}{link}</font>', body)))
ct = Table([[r[1]] for r in cert_rows], colWidths=[CW])
ct.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 3),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
S.append(KeepTogether([SectionTitle('Certificates'), Spacer(1, 6), ct]))
S.append(Spacer(1, 14))

# experience
S += [CondPageBreak(200), SectionTitle('Work experience'), Spacer(1, 10)]
for e in C.EXPERIENCE:
    rows = [('Stack:', Paragraph(e['stack'], body)),
            ('Role:', Paragraph(e['role'], body)),
            ('Project description:', Paragraph(e['desc'], body))]
    rows += labelled('Responsibilities:', e['bullets'])
    if e.get('extra'):
        x = e['extra']
        rows.append((x['label'], Paragraph(x['desc'], body)))
        rows += labelled('', x['bullets'])
    S += [CondPageBreak(150), item_header(e['name'], f"{e['period']} · {e['role']} · {e['team']}"),
          Spacer(1, 6), rows_table(rows), Spacer(1, 12)]

# personal projects
S += [CondPageBreak(220), SectionTitle('Personal projects'), Spacer(1, 8),
      Paragraph(C.OBYN_INTRO, body), Spacer(1, 4),
      Paragraph('<b>Backend:</b> ' + C.OBYN_BACKEND, body), Spacer(1, 10)]
for p in C.PROJECTS:
    host = p['url'].replace('https://', '').rstrip('/')
    rows = [('Description:', Paragraph(p['desc'], body))]
    rows += labelled('Key features:', p['bullets'])
    for lbl, bl in p.get('sections', []):
        rows += labelled(lbl, bl)
    rows.append(('Stack:', Paragraph(p['stack'], body)))
    S += [CondPageBreak(140),
          item_header(p['name'], f"{p['tag']} · Personal project · <a href=\"{p['url']}\" color=\"#0F766E\">{host}</a>"),
          Spacer(1, 6), rows_table(rows), Spacer(1, 12)]

contacts = rows_table([(l, Paragraph(f'<a href="{u}" color="#0F766E">{t}</a>', body)) for l, t, u in C.CONTACTS]
                      + [('Hobbies:', Paragraph(C.HOBBIES, body))])
S.append(KeepTogether([Band([contacts])]))

doc.build(S)
