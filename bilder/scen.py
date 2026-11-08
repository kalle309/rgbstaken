"""Ritar RGB-staken (mått från bas.sc v2) i ett svenskt fönster en decemberkväll -> SVG."""
import random, sys

W, Hh = 1200, 820
CX, Y0, S = 600, 676, 1.45          # mittlinje, golvlinje (z=0) i bilden, px per mm
random.seed(7)

def P(x, z):
    return f"{CX + x*S:.1f},{Y0 - z*S:.1f}"

# ---- basens profil (samma som ProfileSketch) ----
sp, bw, st, H0, r = 50, 34, 40, 180, 16
H = [H0 - i*st for i in range(4)]
R = r * S
prof = [f"M{P(-167,10)}", f"L{P(-163.64,10)}", f"L{P(0,130)}", f"L{P(163.64,10)}",
        f"L{P(167,10)}", f"L{P(167,60)}", f"L{P(133,60)}", f"A{R:.1f},{R:.1f} 0 0 1 {P(117,76)}",
        f"L{P(117,100)}", f"L{P(83,100)}", f"A{R:.1f},{R:.1f} 0 0 1 {P(67,116)}",
        f"L{P(67,140)}", f"L{P(33,140)}", f"A{R:.1f},{R:.1f} 0 0 1 {P(17,156)}",
        f"L{P(17,180)}", f"L{P(-17,180)}", f"L{P(-17,156)}", f"A{R:.1f},{R:.1f} 0 0 1 {P(-33,140)}",
        f"L{P(-67,140)}", f"L{P(-67,116)}", f"A{R:.1f},{R:.1f} 0 0 1 {P(-83,100)}",
        f"L{P(-117,100)}", f"L{P(-117,76)}", f"A{R:.1f},{R:.1f} 0 0 1 {P(-133,60)}",
        f"L{P(-167,60)}", "Z"]
profile = " ".join(prof)

def foot(xc):
    c = 3
    pts = [(xc-35,0),(xc+35,0),(xc+35,20-c),(xc+35-c,20),(xc-35+c,20),(xc-35,20-c)]
    return "M" + " L".join(P(*p) for p in pts) + " Z"

out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}">')
a('''<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#050b1c"/><stop offset="0.6" stop-color="#13254a"/><stop offset="1" stop-color="#2a3f6b"/></linearGradient>
 <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2a1f1a"/><stop offset="0.75" stop-color="#4a362a"/><stop offset="1" stop-color="#3a2a21"/></linearGradient>
 <radialGradient id="room" cx="0.5" cy="0.62" r="0.55">
  <stop offset="0" stop-color="#ffb35c" stop-opacity="0.35"/><stop offset="1" stop-color="#ffb35c" stop-opacity="0"/></radialGradient>
 <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#fff6e6"/><stop offset="1" stop-color="#d9cdb8"/></linearGradient>
 <linearGradient id="stake" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#e6dccb"/></linearGradient>
 <linearGradient id="tube" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#e3d8c6"/><stop offset="0.35" stop-color="#fffdf7"/><stop offset="1" stop-color="#d6c9b4"/></linearGradient>
 <radialGradient id="flame" cx="0.5" cy="0.6" r="0.6">
  <stop offset="0" stop-color="#fffef5"/><stop offset="0.55" stop-color="#ffe9b0"/><stop offset="1" stop-color="#ffc66b"/></radialGradient>
 <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0" stop-color="#ffd9a0" stop-opacity="0.75"/><stop offset="0.35" stop-color="#ffb860" stop-opacity="0.28"/>
  <stop offset="1" stop-color="#ff9a40" stop-opacity="0"/></radialGradient>
 <linearGradient id="snowground" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#c9d6ee"/><stop offset="1" stop-color="#8ea3c8"/></linearGradient>
 <filter id="blur2"><feGaussianBlur stdDeviation="2"/></filter>
 <filter id="blur6"><feGaussianBlur stdDeviation="6"/></filter>
 <clipPath id="glass"><rect x="170" y="70" width="860" height="560"/></clipPath>
</defs>''')

# vägg
a(f'<rect width="{W}" height="{Hh}" fill="url(#wall)"/>')

# ---- utsikten ----
a('<g clip-path="url(#glass)">')
a('<rect x="170" y="70" width="860" height="560" fill="url(#sky)"/>')
for _ in range(90):  # stjärnor
    x, y = random.uniform(170, 1030), random.uniform(70, 330)
    a(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(0.4,1.2):.1f}" fill="#dfe8ff" opacity="{random.uniform(.3,.9):.2f}"/>')
a('<circle cx="880" cy="150" r="26" fill="#f4f1de" opacity="0.9"/><circle cx="880" cy="150" r="60" fill="#f4f1de" opacity="0.08"/>')
# granskog i fjärran
for i in range(40):
    x = 170 + i*23 + random.uniform(-6, 6); h = random.uniform(40, 85); b = 470
    a(f'<path d="M{x:.0f},{b-h:.0f} L{x-h*0.28:.0f},{b} L{x+h*0.28:.0f},{b} Z" fill="#0b1830"/>')
# hus på andra sidan gatan
houses = [(190, 120, 95, "#7a2a22"), (330, 150, 115, "#8a3328"), (520, 110, 90, "#c7b48a"),
          (660, 160, 120, "#7a2a22"), (850, 130, 100, "#3d4f66")]
for hx, hw, hh, col in houses:
    base = 520
    a(f'<rect x="{hx}" y="{base-hh}" width="{hw}" height="{hh}" fill="{col}" opacity="0.55"/>')
    a(f'<path d="M{hx-8},{base-hh} L{hx+hw/2},{base-hh-45} L{hx+hw+8},{base-hh} Z" fill="#e8eefb" opacity="0.85"/>')
    for k in range(2):
        wx = hx + 18 + k*(hw-50); wy = base - hh + 28
        a(f'<rect x="{wx}" y="{wy}" width="28" height="34" fill="#ffcf7a" opacity="0.9"/>')
        a(f'<rect x="{wx-10}" y="{wy-10}" width="48" height="54" fill="#ffcf7a" opacity="0.15" filter="url(#blur6)"/>')
        # små adventsljusstakar i grannarnas fönster
        for j in range(5):
            dx = wx + 4 + j*5; hgt = 6 + (2 - abs(j-2))*3
            a(f'<rect x="{dx}" y="{wy+30-hgt}" width="1.6" height="{hgt}" fill="#fff4d6"/>')
            a(f'<circle cx="{dx+0.8}" cy="{wy+28-hgt}" r="1.4" fill="#fff8e0"/>')
# snötäckt mark
a('<path d="M170,520 Q400,500 600,515 T1030,508 L1030,630 L170,630 Z" fill="url(#snowground)"/>')
a('<path d="M170,560 Q350,545 520,565 T1030,555 L1030,630 L170,630 Z" fill="#b4c4e2" opacity="0.6"/>')
# gatlykta
a('<rect x="985" y="330" width="4" height="200" fill="#0a1122"/><circle cx="987" cy="328" r="7" fill="#ffe2a8"/>')
a('<circle cx="987" cy="328" r="40" fill="#ffe2a8" opacity="0.12" filter="url(#blur6)"/>')
# snöflingor
for _ in range(260):
    x, y = random.uniform(170, 1030), random.uniform(70, 630)
    a(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(0.8,2.6):.1f}" fill="#ffffff" opacity="{random.uniform(.35,.95):.2f}"/>')
a('</g>')

# ---- fönsterbåge (spröjsat, två bågar) ----
a('<g fill="url(#wood)">')
a('<rect x="150" y="50" width="900" height="20"/><rect x="150" y="50" width="20" height="600"/>'
  '<rect x="1030" y="50" width="20" height="600"/>')
a('<rect x="588" y="50" width="24" height="600"/>')                       # mittpost
a('<rect x="170" y="290" width="418" height="12"/><rect x="612" y="290" width="418" height="12"/>')  # spröjs
a('<rect x="373" y="70" width="10" height="560"/><rect x="817" y="70" width="10" height="560"/>')
a('</g>')
# frost i hörnen
for (fx, fy) in []:
    a(f'<ellipse cx="{fx}" cy="{fy}" rx="70" ry="22" fill="#ffffff" opacity="0.18" filter="url(#blur6)"/>')

# fönsterbräda
a('<rect x="110" y="640" width="980" height="44" fill="url(#wood)"/>')
a('<rect x="110" y="684" width="980" height="16" fill="#bfb19a"/>')
a(f'<rect x="0" y="700" width="{W}" height="{Hh-700}" fill="#2b201a"/>')

# rumsljus från staken
a(f'<rect width="{W}" height="{Hh}" fill="url(#room)"/>')

# skugga under staken
a(f'<ellipse cx="{CX}" cy="{Y0+2}" rx="330" ry="9" fill="#5a4630" opacity="0.45" filter="url(#blur6)"/>')

# ---- staken ----
a(f'<path d="{profile}" fill="url(#stake)" stroke="#cbbfa9" stroke-width="1"/>')
for xc in (-175, 175):
    a(f'<path d="{foot(xc)}" fill="url(#stake)" stroke="#cbbfa9" stroke-width="1"/>')
xs = [0, 50, -50, 100, -100, 150, -150]
hs = [H[0], H[1], H[1], H[2], H[2], H[3], H[3]]
glows, flames = [], []
for x, h in zip(xs, hs):
    tube_top = h + 61
    tl = CX + (x-8)*S; tw = 16*S
    a(f'<rect x="{tl:.1f}" y="{Y0-tube_top*S:.1f}" width="{tw:.1f}" height="{61*S:.1f}" fill="url(#tube)" rx="1.5"/>')
    # låga: kulform med spetsig topp, synlig höjd 39 mm, Ø15
    bx, by = CX + x*S, Y0 - tube_top*S
    hgt, w = 39*S, 7.5*S
    d = (f"M{bx-w*0.62:.1f},{by:.1f} C{bx-w*1.05:.1f},{by-hgt*0.22:.1f} {bx-w*1.05:.1f},{by-hgt*0.55:.1f} "
         f"{bx-w*0.45:.1f},{by-hgt*0.82:.1f} Q{bx:.1f},{by-hgt*1.02:.1f} {bx:.1f},{by-hgt:.1f} "
         f"Q{bx:.1f},{by-hgt*1.02:.1f} {bx+w*0.45:.1f},{by-hgt*0.82:.1f} "
         f"C{bx+w*1.05:.1f},{by-hgt*0.55:.1f} {bx+w*1.05:.1f},{by-hgt*0.22:.1f} {bx+w*0.62:.1f},{by:.1f} Z")
    glows.append(f'<circle cx="{bx:.1f}" cy="{by-hgt*0.45:.1f}" r="{95:.0f}" fill="url(#glow)"/>')
    flames.append(f'<path d="{d}" fill="url(#flame)"/>')
    for k in (-0.5, -0.17, 0.17, 0.5):    # räfflor
        flames.append(f'<path d="M{bx+k*w*1.3:.1f},{by-1:.1f} Q{bx+k*w*1.9:.1f},{by-hgt*0.45:.1f} {bx+k*w*0.6:.1f},{by-hgt*0.86:.1f}" '
                      f'stroke="#f0c070" stroke-width="0.8" fill="none" opacity="0.55"/>')
    flames.append(f'<ellipse cx="{bx:.1f}" cy="{by-hgt*0.42:.1f}" rx="{w*0.35:.1f}" ry="{hgt*0.2:.1f}" fill="#ffffff" opacity="0.8" filter="url(#blur2)"/>')
a('<g style="mix-blend-mode:screen">' + "".join(glows) + '</g>')
a("".join(flames))
# ljusreflex i glaset bakom
for x, h in zip(xs, hs):
    a(f'<circle cx="{CX + x*S + 6:.1f}" cy="{Y0 - (h+80)*S - 4:.1f}" r="5" fill="#ffe6b8" opacity="0.18" filter="url(#blur2)"/>')

a('</svg>')
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out))
print("ok")
