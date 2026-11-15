# Changelog

Alla iterationer av RGB-staken, nyast först. Datum är när ändringen gjordes och pushades.

## 2026-11-15 – Minibas med 5 ljus (ny del)
- Ny bas `minibas.sc` / `mini_base.stl` som skrivs ut i ett stycke på P2S: 250 × 60 × 140 mm, 5 ljus med c/c 44,
  plattor på 140 / 100 / 60 mm. Samma M16-hylsor som den stora basen, så alla pelare, lågor, manschetter och
  pärlor passar.
- Samma elektronik som den stora: XIAO-fack, USB-C, kondensatorfack, öppen kabelkanal med locklist
  (`lock_mini.sc` / `mini_channel_lid.stl`, 2 st). Antennslitsen är lodrät längs armens yttersida.

## 2026-11-15 – Bas v2.6: mer höjdspel i skarven
- Provutskrift av båda halvorna: höger halvas topp sprack (lagren släppte) när halvorna trycktes ihop. Troligen
  satt delar av supporten kvar, och undersidorna på tungan och mittklossen blir ojämna eftersom de skrivs ut som
  överhäng. Spelet i bredd var bra.
- Bara höger halva är ändrad och bara i höjdled:
  - Tungans spår är 0,5 mm högre än tungan både över och under (tidigare 0,15).
  - Bommen mellan tungan och mittklossen är sänkt 0,5 mm, så att den har spel mot klossens undersida (tidigare 0).
  - Lockets tak har 0,4 mm spel mot klossens topp (tidigare 0,15). Locket är då 2,25 mm tjockt.
- Vänster halva är oförändrad, så en redan utskriven vänster halva passar.

## 2026-11-15 – Manschett v1.1: stift för pärlorna
- **Manschett:** ett stift Ø2 × 2 mm mitt i varje kopps botten (z 2–4).
- **Pärla:** hål Ø2,4 × 2,5 mm i den platta botten (0,2 mm spel för lim), så att pärlan hamnar mitt i koppen.

## 2026-11-15 – Bas v2.5: vågrät tunga
- Provutskriften visade att halvorna inte gick ihop. Den sneda tungan (parallell med undersidan) måste skjutas in
  längs bågens lutning, men lockets tak över mittklossen kräver att höger halva kommer rakt från sidan.
- Tungan är nu **vågrät**: 20 × 18 mm (z 136–154), sticker 13,5 mm in i höger halva (x 0,5–14), med 0,15 mm limspel.
  Höger halva skjuts rakt in från höger. Det gamla spåret är igenfyllt. Kabelkanalen och mittljusets Ø8-kabelhål
  är uppskurna genom tungan igen. Inga gängor behövde räknas om.
- Pelare med gängad låga passade perfekt i samma provutskrift.

## 2026-11-14 – Högergängad låga
- Lågans och pelarens M12×1-gänga är nu **högergängad** igen (vanlig medurs iskruvning). Vänstergängan från
  tidigare samma dag är borttagen.

## 2026-11-14 – Inledning på lågans gänga
- **Låga:** 0,8 mm fas på den gängade tappens underkant, så att den får en slät, konisk nos som styr in innan
  första gängvarvet tar.
- **Pelare:** 45°-försänkning vid M12-hylsans öppning (Ø ≈ 11,8 → 14,2).

## 2026-11-14 – Bas v2.4, pelare v2.2, låga v3
- **Bas v2.4 – centrerad skarv:** höger halva har ett lock (2,5 mm gods, 0,15 mm limspel) över vänster halvas
  mittkloss på framsidan, baksidan, toppen och högersidan. Skarven syns därför bara som en rak linje mitt på staken.
  På toppen rundar den mittljuset i en halvcirkel (r 9) så att mittljusets gänga inte behövde röras.
  Tidigare låg skarven 17 mm åt höger ovanför z 160.
- **Pelare v2.2:** gängad M12×1-hylsa i toppen (6 mm) för lågan. LED-urtaget Ø12,4 ligger kvar under gängan.
- **Låga v3:** den släta tappen Ø12 är ersatt av en gängad ring M12×1 (5,6 mm) med Ø8 ljushål.
  Gängan gjordes först vänstergängad men ändrades senare samma dag (se ovan).
- **LED-kortet måste nu vara ≤ Ø10 mm** för att gå genom gängan (tidigare ≤ Ø12).

## 2026-11-14 – Tillval: manschett med pärlor
- Ny del `manschett.sc` / `cuff.stl`: svart ring (Ø16,6 inuti) som träs över pelaren och vilar på plattan, med fyra
  koppar à 10 spetsiga taggar. Ringen går att trä på även när lågan sitter i.
- Ny del `parla.sc` / `bead.stl`: äggformad pärla 9 × 11 mm med platt botten som limmas i kopparna (4 per ljus).
- Inspirerad av en ljusstake i en butik (foton `PXL_20261114_*`).

## 2026-11-13 – Bas v2.3: kondensatorfack
- Fack 10 × 15 × 10 mm rakt ut från XIAO-fackets sida vid USB-änden för en 470 µF/16 V elektrolyt (Ø8 × 11,5)
  liggande, med benen raka in mot stiften. Öppet underifrån, fästs med smältlim.

## 2026-11-13 – Bas v2.2: antennslits
- Snett slits (2,2 × 22 mm, 45°, parallell med armens utsvängning) i högra armen för XIAO:ns FPC-antenn
  (40 × 20 mm). Går från fotens undersida genom XIAO-facket och ≈41 mm upp i armen.
- Ny provutskrift av pelare v2.1 och hylsa: gängorna fungerar mycket bättre.

## 2026-11-11 – v2.1 efter första provutskriften
- **Pelare:** gängan kortad till 13 mm (hylsan är 16) så att röret tar stopp mot hylsans kant och ingen gänga syns.
  Konisk inledning (~3,5 mm) och mer spel (skalad 0,97 i XY ≈ 0,24 mm radiellt). Gängan var trög och syntes förut.
- **Bas:** kabelkanalen är öppen nedåt – ett spår i bågens undersida med fals för en locklist, och en öppen ränna
  under högra foten in till XIAO-facket. Kablarna läggs i i stället för att dras igenom.
- **Ny del:** locklist `lock.sc` / `channel_lid.stl` (skriv ut 2).
- Gamla `flame_v1.stl` borttagen.

## 2026-11-09 – Licens
- Allt släppt som CC0 1.0 Universal.

## 2026-11-08 – Elektronik
- Kopplingsschema, WLED-presets och ESPHome-konfiguration i `elektronik/`. Data på D10/GPIO10, ljus 1 = höger ytter.

## 2026-11-08 – Bas v2 och rendering
- **Bas v2** med uppmätta mått från förlagan: c/c 50, steghöjd 40, mittplatta 180 mm, bågens öppning 300 mm,
  total bredd 420 mm. Konkav utsvängning ner mot fötterna och profilerade fötter (70 × 75 × 20 mm med avsats).
- Skarv i mitten utan skruvar: trycks ihop och limmas, med en dold tunga från vänster halva. Mittljusets hylsa
  i vänster halva.
- Alla sju hylsor med M16-gänga (tidigare M20). Pelare Ø16 som förlagans ljusrör, ny räfflad låga
  Ø15 × 39 mm med tapp Ø12 (låga v2).
- Fotorealistisk rendering `bilder/fonster_december.png` (Blender Cycles).

## 2026-11-07 – Första utkastet (v1)
- Bas, pelare och låga modellerade i SolidCraft med mått uppskattade från foton på förlagan (en trästake).
- Basen i två halvor hopskruvade med M4-skruvar, M20-gängade pelare.
