# RGB-staken

3D-printad adventsljusstake med 7 ljus och RGB-belysning (WS2812B/SK6812 + XIAO ESP32C3, WLED).

![Basen framifrån](solidcraft/bas_bage_fram.png)

## Status (2026-11-08)

Basen är ombyggd efter uppmätta mått (v2). **Arbetet pågår:**

- `solidcraft/bas.sc` (v2): klar utom gängorna. 3 av 7 M16-gängor är skurna (mitten, vänster 1 och 2).
- `solidcraft/pelare.sc` och `solidcraft/lagan.sc`: ännu inte uppdaterade till Ø16-rör och M16.
- `stl/`: innehåller fortfarande **v1** (uppskattade mått, M20, skruvad skarv). Skriv inte ut dem.

## Mått (v2)

| | |
|---|---|
| c/c mellan ljusen | 50 mm |
| Steghöjd | 40 mm (plattor 180 / 140 / 100 / 60 mm) |
| Bågens öppning / topp | 300 mm vid fotens ovansida / 130 mm över golvet |
| Fötter | 70 × 75 × 20 mm, total bredd 420 mm |
| Djup | 34 mm |
| Ljusrör | Ø16 mm, M16-gänga ner i basen |
| Ljusets topp | platta + 100 mm, alltså mitten 280 och ytterst 160 mm |

## Delar

| Del | Antal | Kommentar |
|---|---|---|
| Vänster bashalva | 1 | Med mittblocket (ovanför z 160) och limtungan, 240,5 mm. Skrivs ut stående. |
| Höger bashalva | 1 | XIAO-fack + USB-C i foten, 209,5 mm. Skrivs ut stående. |
| Pelare (ljus) | 7 | Ø16, M16-gänga 16 mm, kabelhål Ø7, LED-urtag Ø12 × 9. |
| Låga | 7 | Räfflad kupa, transparent/natural PETG. |

CAD-filer (SolidCraft) finns i `solidcraft/`: `bas.sc`, `pelare.sc`, `lagan.sc`.

## Montering

- Bashalvorna trycks ihop i mitten och limmas. En dold tunga (20 mm bred, 0,15 mm limspel)
  från vänster halva går in i ett spår i höger.
- Pelarna skruvas ner i basens M16-hylsor tills de bottnar.
- Kablarna går i en invändig kanal längs bågen och ner till XIAO-facket i högra foten.

## Elektronik

- 7 × WS2812B eller SK6812 RGBW på rund PCB (≤ Ø11,5 mm), en i toppen av varje pelare.
- XIAO ESP32C3 matas via USB-C, LED:erna från 5V-pinnen (≈ 0,4 A max).
- ~330 Ω på data, ~470 µF över 5V/GND. Mjukvara: WLED.
