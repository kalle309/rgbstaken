# RGB-staken

3D-printad adventsljusstake med 7 ljus och RGB-belysning (WS2812B/SK6812 + XIAO ESP32C3, WLED).

![RGB-staken i fönstret en decemberkväll](bilder/fonster_december.png)

*Rendering (inte foto) i Blender Cycles. Staken är byggd av de riktiga STL-filerna i `stl/`, allt runt omkring är scenografi.
Rendera om med `blender -b -P bilder/render_scen.py -- <projektmapp> bilder/fonster_december.png 512`.*

![Basen framifrån](solidcraft/bas_bage_fram.png)

## Status (2026-11-11)

STL-filer i `stl/`: `base_left.stl`, `base_right.stl`, `pillar.stl` (skriv ut 7), `flame.stl` (skriv ut 7)
och `channel_lid.stl` (skriv ut 2).

Efter första provutskriften (v2.1):
- Pelarens gänga är kortad till 13 mm (hylsan är 16) så att röret själv tar stopp mot hylsans kant – ingen gänga syns.
- Gängan har en konisk inledning (~3,5 mm) och lite mer spel (0,97 i XY ≈ 0,24 mm radiellt) – lättare att skruva i.
- Kabelkanalen är öppen nedåt: ett spår i bågens undersida som täcks av en locklist, och en öppen ränna under
  högra foten in till XIAO-facket. Kablarna läggs i i stället för att dras igenom.

## Mått (v2)

| | |
|---|---|
| c/c mellan ljusen | 50 mm |
| Steghöjd | 40 mm (plattor 180 / 140 / 100 / 60 mm) |
| Bågens öppning / topp | 300 mm vid fotens ovansida / 130 mm över golvet |
| Fötter | kloss 70 × 75 × 20 mm med avsats, total bredd 420 mm |
| Armänden | konkav utsvängning (R 28) ner mot foten, som på förlagan |
| Djup | 34 mm |
| Ljusrör | Ø16 mm, M16-gänga ner i basen |
| Ljusets topp | platta + 100 mm, alltså mitten 280 och ytterst 160 mm |

## Delar

| Del | Antal | Kommentar |
|---|---|---|
| Vänster bashalva | 1 | Med mittblocket (ovanför z 160) och limtungan, 240,5 mm. Skrivs ut stående. |
| Höger bashalva | 1 | XIAO-fack + USB-C i foten, 209,5 mm. Skrivs ut stående. |
| Pelare (ljus) | 7 | Ø16 × 61 mm synligt, M16-gänga 13 mm med konisk inledning, kabelhål Ø7 (Ø6 i gängan), LED-urtag Ø12,4 × 9. |
| Locklist | 2 | 185 × 15,7 × 2,3 mm, täcker kabelspåret i bågens undersida. Skrivs ut liggande. |
| Låga | 7 | Räfflad kupa Ø15 × 39 mm + tapp Ø12, transparent/natural PETG, 0 % fyllning. |

CAD-filer (SolidCraft) finns i `solidcraft/`: `bas.sc`, `pelare.sc`, `lagan.sc`, `lock.sc`.

## Montering

- Bashalvorna trycks ihop i mitten och limmas. En dold tunga (20 mm bred, 0,15 mm limspel)
  från vänster halva går in i ett spår i höger.
- Pelarna skruvas ner i basens M16-hylsor tills rörets kant tar stopp i hylsans försänkning.
- Kablarna läggs i det öppna spåret i bågens undersida (10 mm brett, ≈ 20 mm djupt) och ner genom rännan under
  högra foten till XIAO-facket. Sedan trycks locklisterna in i falsen (16 × 3 mm) och fästs med några droppar
  lim eller smältlim (går att öppna igen).

## Elektronik

- 7 × WS2812B eller SK6812 RGBW på rund PCB (≤ Ø12 mm), en i toppen av varje pelare.
- XIAO ESP32C3 matas via USB-C, LED:erna från 5V-pinnen (≈ 0,4 A max).
- ~330 Ω på data, ~470 µF över 5V/GND. Mjukvara: WLED eller ESPHome.

Kopplingsschema, dragning i basen och färdig konfiguration för WLED och ESPHome finns i
[`elektronik/`](elektronik/README.md).

![Kopplingsschema](elektronik/kopplingsschema.svg)

## Licens

Allt i repot (CAD-filer, STL, kod, konfiguration och bilder) är släppt som
[CC0 1.0 Universal](LICENSE), alltså fri allmän egendom. Du får ladda ner, ändra, sprida och använda
materialet precis som du vill, även kommersiellt, utan att fråga och utan att ange källa.
