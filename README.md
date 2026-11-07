# RGB-staken

3D-printad adventsljusstake med 7 ljus och RGB-belysning (WS2812B/SK6812 + XIAO ESP32C3, WLED).
Utkast – måtten är uppskattade från foton av en befintlig trästake och ska bytas mot uppmätta.

![Basen framifrån](solidcraft/bas_bage_fram.png)

## Delar

| Fil | Del | Antal | Kommentar |
|---|---|---|---|
| `stl/base_left.stl` | Vänster bashalva | 1 | Med mittblocket och tungan, 231 mm. Skrivs ut stående. |
| `stl/base_right.stl` | Höger bashalva | 1 | XIAO-fack + USB-C i foten, 197 mm. Skrivs ut stående. |
| `stl/pillar.stl` | Pelare (ljus) | 7 | M20-gänga, kabelhål Ø9, LED-urtag Ø14 × 9. |
| `stl/flame.stl` | Låga | 7 | Räfflad kupa Ø17 × 44 mm, transparent/natural PETG. |

CAD-filer (SolidCraft) finns i `solidcraft/`: `bas.sc`, `pelare.sc`, `lagan.sc`.

## Montering

- Bashalvorna skruvas ihop i mitten med 2 × M4 + muttrar genom den dolda tungan.
- Pelarna skruvas ner i basens gängade hylsor (M20).
- Kablarna går i en invändig kanal längs bågen till XIAO-facket i högra foten.

## Elektronik

- 7 × WS2812B eller SK6812 RGBW på rund PCB (≤ Ø14 mm), en i toppen av varje pelare.
- XIAO ESP32C3 matas via USB-C, LED:erna från 5V-pinnen (≈ 0,4 A max).
- ~330 Ω på data, ~470 µF över 5V/GND. Mjukvara: WLED.
