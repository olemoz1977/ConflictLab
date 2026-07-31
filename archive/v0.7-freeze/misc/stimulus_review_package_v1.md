# ConflictLab — Stimulus Review Package v1.0

**Data:** 2026-07-30
**Paskirtis:** Nepriklausomas metodologinis auditas
**Versija:** v0.6.0 stimulų biblioteka
**Stimulų skaičius:** 12
**Ašys:** approach_withdrawal (aw) · certainty_seeking (cs) · control_release (cr)
**Skalė:** -1.0 → +1.0 (neigiamas = atsitraukimas/neapibrėžtumas/paleidimas)

---

## SVARBI PASTABA AUDITORIUI

Šis dokumentas pateikia VISĄ vidinę sistemos logiką, įskaitant:
- Vartotojui nematomas aw/cs/cr reikšmes
- Metodologines rizikas
- Claude savikritines pastabas

Stimulai rodomi be situacijos konteksto — tai sąmoningas sprendimas (v0.6).

---

---

# ST-001

**Nuotrauka:** `p2_window_silhouette.png`
*(Žmogus stovi prie lango nugara į žiūrovą, lietus už lango)*

**Ašis:** approach_withdrawal (aw)
**Polius:** neigiamas (-1 / atsitraukimas)

---

### Situacijos tikslas

Siekia išprovokuoti **pirmąją reakciją į distancijos ir izoliuotumo vaizdą**.
Neapibrėžtumas: ar žmogus prie lango laukia, atsitraukia, ar tiesiog stovi?
Pasirinkta, nes figūros nugara pašalina veidą ir emociją — interpretacija priklauso nuo žiūrovo projekcijos.

---

### Vartotojui rodomi variantai

- A: *"Norėjosi pabūti vienam"*
- B: *"Galvojau kas vyksta lauke"*
- C: *"Laukimas — normalu"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Norėjosi pabūti vienam | -0.55 | -0.20 | -0.30 |
| B — Galvojau kas vyksta lauke | +0.25 | +0.15 | +0.10 |
| C — Laukimas — normalu | -0.10 | -0.30 | -0.15 |

**A:** Stiprus atsitraukimo signalas. Žmogus identifikuojasi su izoliacija.
**B:** Silpnas artėjimo signalas — domisi kas už lango (išorinis dėmesys).
**C:** Neutralus — pasyvus laukimas, nė viena kryptis.

---

### Kodėl šie variantai?

Matuoja ar žmogus į distanciją reaguoja: (A) traukdamasis, (B) žvelgdamas pro ją, (C) neutraliai priims.
Hipotezė: kuo stipresnis A pasirinkimas, tuo stipresnis aw neigiamas signalas.

---

### Metodologinės rizikos

⚠️ **Socialiai pageidaujamas pasirinkimas:** B gali atrodyti "pozityvesnis" — smalsumas vs. izoliacija.
⚠️ **Nuotrauka primeta nuotaiką:** Lietus + nugara = liūdesys daugeliui kultūrų. Gali matuoti kultūrinę asociaciją, ne reakciją.
⚠️ **C per neutralus:** "Laukimas — normalu" yra racionalizacija, ne reakcija.
⚠️ **Kelios interpretacijos:** Žmogus gali žiūrėti pro langą iš įpročio, ne iš norų pabūti vienam.

---

### Claude savikritika

**Silpniausia:** Nuotrauka per daug "kino" — sukuria melancholijos lūkestį. Tai gali manipuliuoti pasirinkimu.
**Keisčiau:** Variantą C pakeisčiau į ką nors konkretesnio: *"Pastebėjau, kad stoviu prie lango ir neveikiu"* — mažiau racionalizacija.

---

---

# ST-002

**Nuotrauka:** `ax_approach.png`
*(Du žmonės koridoriuje veidu vienas į kitą, tamsus biuro koridorius)*

**Ašis:** approach_withdrawal (aw)
**Polius:** teigiamas (+1 / artėjimas)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į tiesioginį tarpasmeninį kontaktą**.
Neapibrėžtumas: ar tai konfliktas, pokalbis, ar susitikimas?
Pasirinkta, nes du žmonės veidu į veidą be konteksto sukuria maksimalų interpretacijos laisvę.

---

### Vartotojui rodomi variantai

- A: *"Artumas — kažkas sprendžiasi"*
- B: *"Įtampa — per arti"*
- C: *"Neutralu — tiesiog du žmonės"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Artumas — kažkas sprendžiasi | +0.50 | +0.20 | +0.15 |
| B — Įtampa — per arti | -0.25 | +0.35 | +0.25 |
| C — Neutralu — tiesiog du žmonės | +0.05 | -0.10 | -0.05 |

**A:** Stiprus artėjimo + aiškumo siekimo signalas.
**B:** Atsitraukimas nuo artumo + nerimastingas aiškumo siekimas.
**C:** Beveik nulis — žmogus nemato įtampos.

---

### Metodologinės rizikos

⚠️ **Lyties signalas:** Nuotraukoje matomas vyras ir moteris. Tai gali aktyvuoti lyčių dinamikos schemas.
⚠️ **"Įtampa" negatyvus žodis:** B variantas turi negatyvią konotaciją — gali būti vengiamas dėl socialinio pageidaujamumo.
⚠️ **Koridoriaus kontekstas:** Biuro aplinka kuria hierarchijos lūkestį.
⚠️ **Per daug akivaizdu:** Du žmonės veidu į veidą = "susitikimas ar konfliktas" — per siaurą interpretacijos erdvė.

---

### Claude savikritika

**Silpniausia:** Lyties dinamika. Turėtų būti du identiški siluetai be lytinių požymių.
**Keisčiau:** Naudočiau abstrakčesnes figūras (ST-001 stiliaus siluetus) — ne realistines.

---

---

# ST-003

**Nuotrauka:** `v2_p2_corridor.png`
*(Žmogus eina tolstančiu koridoriumi, fluorescencinės šviesos)*

**Ašis:** approach_withdrawal (aw)
**Polius:** neigiamas (-1 / atsitraukimas)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į judančią figūrą kuri tolsta**.
Neapibrėžtumas: žmogus išeina po darbo, po susitikimo, ar pabėga?
Pasirinkta kaip dinaminis atsitraukimo vaizdas — veiksmas, ne statinė poza.

---

### Vartotojui rodomi variantai

- A: *"Išeiti greičiau"*
- B: *"Palaukti ir pasikalbėti"*
- C: *"Tiesiog eiti savo keliu"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Išeiti greičiau | -0.50 | -0.10 | -0.30 |
| B — Palaukti ir pasikalbėti | +0.40 | +0.10 | +0.15 |
| C — Tiesiog eiti savo keliu | -0.10 | -0.20 | +0.20 |

---

### Metodologinės rizikos

⚠️ **Klausimas "ką norėjosi daryti"** — tai jau interpretacinis klausimas, ne reakcija į vaizdą.
⚠️ **Institucinis kontekstas:** Fluorescencinės šviesos + koridorius = biuras/ligoninė. Kontekstas veikia.
⚠️ **C formuluotė:** "Tiesiog eiti savo keliu" yra pozityvi racionalizacija — gali maskuoti atsitraukimą.

---

### Claude savikritika

**Silpniausia:** Klausiamas elgesys ("ką norėjosi daryti"), o ne reakcija ("kas šovė į galvą"). Tai matuoja ketinimus, ne signalą.
**Keisčiau:** Klausimą į: *"Kas pirmiausia šovė į galvą žiūrint į šį vaizdą?"*

---

---

# ST-004

**Nuotrauka:** `v2_p4_person_alone.png`
*(Žmogus vienas sėdi didelėje konferencijų salėje)*

**Ašis:** approach_withdrawal (aw)
**Polius:** neigiamas (-1 / izoliacija)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į socialinę izoliaciją erdviame kontekste**.
Neapibrėžtumas: žmogus liko po susirinkimo, atvyko anksti, ar sąmoningai sėdi vienas?
Pasirinkta, nes erdvė + vienas žmogus sukuria stiprų kontrastą.

---

### Vartotojui rodomi variantai

- A: *"Vienišumas — sunkiai jaučiasi"*
- B: *"Ramybė — laikas sau"*
- C: *"Ar reikia pagalbos?"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Vienišumas | -0.40 | +0.20 | -0.20 |
| B — Ramybė | -0.15 | -0.35 | -0.35 |
| C — Ar reikia pagalbos? | +0.35 | +0.30 | +0.20 |

---

### Metodologinės rizikos

⚠️ **A variantas interpretavimas, ne reakcija:** "Sunkiai jaučiasi" — projektuojame emociją į figūrą, ne reaguojame į vaizdą.
⚠️ **B gali būti socialiai pageidaujamas:** "Ramybė" skamba pozityviai — gali būti renkamas norint "atrodyti gerai".
⚠️ **C keistas:** Klausimas apie pagalbą yra socialinio altruizmo matas, ne reakcijos į vaizdą matas.

---

### Claude savikritika

**Silpniausia:** Visi trys variantai matuoja **projekciją į figūrą**, o ne žiūrovo **paties reakciją**. Tai metodologinis defektas.
**Keisčiau:** Variantus į pirmą asmenį: *"Norėjosi priartėti"* / *"Norėjosi palikti ramybėje"* / *"Pajutau nerimą dėl jo"*

---

---

# ST-005

**Nuotrauka:** `p1_phone_table.png`
*(Telefonas ant tamsaus medinio stalo, ekranas išjungtas)*

**Ašis:** certainty_seeking (cs)
**Polius:** teigiamas (+1 / aiškumo siekimas)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į laukimą ir neapibrėžtumą komunikacijoje**.
Neapibrėžtumas: ar žinutė atsakyta? Ar laukiama? Ar telefonas tiesiog guli?
Pasirinkta kaip šiuolaikinis laukimo simbolis.

---

### Vartotojui rodomi variantai

- A: *"Ar atsakė?"*
- B: *"Nutylęs — normalu"*
- C: *"Pradėjau galvoti ką daryti"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Ar atsakė? | +0.10 | +0.65 | +0.30 |
| B — Nutylęs — normalu | -0.10 | -0.35 | -0.20 |
| C — Pradėjau galvoti ką daryti | +0.20 | +0.45 | +0.55 |

---

### Metodologinės rizikos

⚠️ **A variantas per siauras:** "Ar atsakė?" — reiškia kad žmogus ŽINO jog laukia žinutės. Bet gal ne.
⚠️ **Telefonas be konteksto:** Ekranas išjungtas — nėra jokio signalo kad laukiama. Žiūrovas pats kuria kontekstą.
⚠️ **C dubliuojasi su A:** Abu matuoja aktyvų atsakymo siekimą, skiriasi tik intensyvumu.

---

### Claude savikritika

**Silpniausia:** A ir C per panašūs — abu yra cs+ signalas, tik skirtingo stiprumo. Trūksta tikro cs- varianto (tolerancija neapibrėžtumui).
**Keisčiau:** B variantą į *"Telefonas nėra svarbus šiuo metu"* — tikresnis cs- signalas.

---

---

# ST-006

**Nuotrauka:** `p3_chat_screen.png`
*(Telefono ekranas su viena išsiųsta žinute ir "skaitytas" statusu, tušia erdve po)*

**Ašis:** certainty_seeking (cs)
**Polius:** teigiamas (+1 / aiškumo siekimas)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į matytą bet neatsakytą žinutę**.
Neapibrėžtumas: ar žmogus nedraugiškas, užsiėmęs, ar ignoruoja?
Pasirinkta kaip labiausiai šiuolaikiškai atpažįstama socialinė įtampa.

---

### Vartotojui rodomi variantai

- A: *"Tuščia vieta po žinute — neramina"*
- B: *"Faktas, palaukiu"*
- C: *"Rašyti dar kartą"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Neramina | +0.10 | +0.65 | +0.30 |
| B — Faktas, palaukiu | -0.15 | -0.40 | -0.25 |
| C — Rašyti dar kartą | +0.20 | +0.50 | +0.60 |

---

### Metodologinės rizikos

⚠️ **Stipriausias cs stimulas bibliotekoje** — gali dominuoti rezultatus.
⚠️ **Generacinė problema:** Šis stimulas labiausiai rezonuoja su 20-35 m. — vyresni žmonės gali neturėti šios patirties.
⚠️ **AI generuotas tekstas ekrane:** Matosi nesuprantami žodžiai (AI artefaktai) — tai gali blaškydyti.
⚠️ **A = socialiai "jautrus"** — gali būti vengiamas norint neatrodyti nerūpestingam.

---

### Claude savikritika

**Silpniausia:** AI artefaktai ekrane (nesuprantamas tekstas). Tai vizualinis triukšmas.
**Keisčiau:** Naudočiau tikrą ekrano mockup su aiškiai matomu "Skaitytas" ir tuščia erdve — be AI sugeneruotų žodžių.

---

---

# ST-007

**Nuotrauka:** `ax_uncertainty.png`
*(Tuščias baltas lapas ant tamsaus paviršiaus, šviesa iš šono)*

**Ašis:** certainty_seeking (cs)
**Polius:** neigiamas (-1 / neapibrėžtumo tolerancija)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į grynąjį neapibrėžtumą — tuščią erdvę**.
Neapibrėžtumas: ar tai galimybė, ar spaudimas? Ar lapas laukia užpildymo, ar yra tuščias?
Pasirinkta kaip universaliausias neapibrėžtumo simbolis.

---

### Vartotojui rodomi variantai

- A: *"Galimybė — rašyti bet ką"*
- B: *"Nerimas — nežinau nuo ko pradėti"*
- C: *"Tyla — nieko nereikia"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Galimybė | +0.10 | -0.45 | -0.20 |
| B — Nerimas | -0.10 | +0.55 | +0.30 |
| C — Tyla | -0.20 | -0.50 | -0.45 |

---

### Metodologinės rizikos

⚠️ **A ir C abi cs-** — du "tolerancijos" variantai prieš vieną "nerimo". Asimetrija.
⚠️ **B "nerimas" per diagnostinis:** Žodis "nerimas" yra psichologinis terminas — gali aktyvuoti saviidentifikaciją, ne reakciją.
⚠️ **Kontekstas neaiškus:** Ar lapas ant darbo stalo? Namuose? Mokykloje? Reikšmė kinta.

---

### Claude savikritika

**Silpniausia:** Asimetrija — du cs- variantai prieš vieną cs+. Turėtų būti: vienas cs-, vienas cs+, vienas neutralus.
**Keisčiau:** B į *"Pirmiausia pagalvojau kas reikia parašyti"* — aktyvus aiškumo siekimas be "nerimo" etiketo.

---

---

# ST-008

**Nuotrauka:** `v2_p3_notebook.png`
*(Užrašų knygelė su išbrauktais žodžiais, tamsus fonas)*

**Ašis:** certainty_seeking (cs)
**Polius:** teigiamas (+1 / aiškumo siekimas per korekciją)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į mąstymo proceso vizualizaciją — ieškojimą teisingo atsakymo**.
Neapibrėžtumas: ar braukimas yra procesas, ar klaida, ar nepasitenkinimas?
Pasirinkta nes išbraukti žodžiai yra fizinis aiškumo siekimo ženklas.

---

### Vartotojui rodomi variantai

- A: *"Noras surasti teisingą"*
- B: *"Normalus mąstymo procesas"*
- C: *"Kažkas neišspręsta"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Noras surasti teisingą | +0.10 | +0.60 | +0.50 |
| B — Normalus procesas | +0.05 | -0.20 | -0.10 |
| C — Kažkas neišspręsta | -0.10 | +0.40 | +0.20 |

---

### Metodologinės rizikos

⚠️ **AI tekstas neįskaitomas:** Knygelėje matosi pseudotekstas — vizualinis triukšmas mažina autentiškumą.
⚠️ **A ir C labai panašūs:** Abu cs+ — skiriasi tik intensyvumu. Nėra tikro cs- varianto.
⚠️ **B "normalus" — racionalizacija:** Žodis "normalus" yra neutralizuojantis — gali būti renkamas vengiant "pripažinti" nerimą.

---

### Claude savikritika

**Silpniausia:** AI pseudotekstas knygelėje. Tai metodologiškai problemiška — žiūrovas reaguoja į vizualinį triukšmą.
**Keisčiau:** Realistiška knygelė su tikrais (bet neįskaitomais) rankraščiais.

---

---

# ST-009

**Nuotrauka:** `p5_person_laptop.png`
*(Žmogus prie kompiuterio nugara, mėlynas ekranas, telefonas šalia)*

**Ašis:** control_release (cr)
**Polius:** teigiamas (+1 / kontrolė)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į darbinę kontrolę ir prioritetų valdymą**.
Neapibrėžtumas: ar žmogus susikoncentravęs, ar vengia telefono, ar tiesiog dirba?
Pasirinkta nes du įrenginiai (kompiuteris + telefonas) kuria prioritetų pasirinkimo situaciją.

---

### Vartotojui rodomi variantai

- A: *"Darbas — viskas kontroliuojama"*
- B: *"Norėjosi dirbti ir nekreipti dėmesio"*
- C: *"Telefonas šalia — stebimas"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Darbas — kontroliuojama | +0.10 | +0.30 | +0.65 |
| B — Nekreipti dėmesio | -0.20 | -0.15 | -0.30 |
| C — Telefonas stebimas | +0.15 | +0.40 | +0.45 |

---

### Metodologinės rizikos

⚠️ **A ir C abi cr+** — du kontrolės variantai. B yra vienintelis cr-.
⚠️ **"Kontroliuojama" — pozityvus žodis:** A gali būti renkamas dėl socialinio pageidaujamumo.
⚠️ **B formuluotė:** "Norėjosi dirbti ir nekreipti dėmesio" — tai vengimas, ne paleidimas. Skirtingi konstruktai.

---

### Claude savikritika

**Silpniausia:** B matuoja vengimą (aw-), o ne paleidimą (cr-). Tai konstrukto validumo problema.
**Keisčiau:** B į *"Telefonas nėra svarbus — darbas svarbiau"* — tikresnis cr+ be vengimo konotacijos.

---

---

# ST-010

**Nuotrauka:** `v2_p1_empty_room.png`
*(Tuščia konferencijų salė vakaro metu, miestas fone pro langus)*

**Ašis:** control_release (cr)
**Polius:** neigiamas (-1 / paleidimas)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į tuščią erdvę po veiklos — paleidimą**.
Neapibrėžtumas: ar salė tuščia nes susirinkimas baigėsi, ar nes niekas neatėjo?
Pasirinkta kaip "po" momento vizualizacija.

---

### Vartotojui rodomi variantai

- A: *"Palengvėjimas — nieko nevyksta"*
- B: *"Laukimas — tuoj pradės"*
- C: *"Galimybė kontroliuoti"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Palengvėjimas | -0.20 | -0.40 | -0.60 |
| B — Laukimas | +0.10 | +0.45 | +0.30 |
| C — Galimybė kontroliuoti | +0.20 | +0.35 | +0.65 |

---

### Metodologinės rizikos

⚠️ **C variantas abstraktus:** "Galimybė kontroliuoti" — ką? Salę? Susirinkimą? Per abstraktu.
⚠️ **Vizualiai gražiausias stimulas:** Miestas fone + vakaro šviesa gali sukelti estetinę reakciją, ne reakciją į situaciją.
⚠️ **A "palengvėjimas" — diagnostinis:** Žodis nurodo emociją, ne reakciją.

---

### Claude savikritika

**Silpniausia:** C variantas nesuprantamas be konteksto. Kas kontroliuojama?
**Keisčiau:** C į *"Norėjosi sutvarkyti erdvę prieš kitus ateinant"* — konkretus kontrolės gestas.

---

---

# ST-011

**Nuotrauka:** `ax_release.png`
*(Tamsus koridorius su atviromis durimis — šviesa iš lauko)*

**Ašis:** control_release (cr)
**Polius:** neigiamas (-1 / paleidimas/laisvė)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į galimybę išeiti — laisvę ar sprendimą**.
Neapibrėžtumas: ar durys kviečia, ar rodo išėjimą?
Pasirinkta kaip universaliausias "paleidimo" simbolis.

---

### Vartotojui rodomi variantai

- A: *"Laisvė — galima išeiti"*
- B: *"Galimybė — kažkas naujo laukia"*
- C: *"Sprendimas — reikia pasirinkti"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Laisvė | -0.10 | -0.30 | -0.65 |
| B — Galimybė | +0.30 | -0.15 | -0.20 |
| C — Sprendimas | +0.10 | +0.50 | +0.40 |

---

### Metodologinės rizikos

⚠️ **Visi trys variantai interpretuoja tą pačią situaciją skirtingai** — tai gera metodologiškai.
⚠️ **"Laisvė" ir "Galimybė" labai panašios:** Abu teigiami, abu cr-. Skirtumas subtilus.
⚠️ **Stipriausias vizualinis stimulas:** Šviesa iš tamsos — archetipinis vaizdas. Gali sukelti per stiprų estetinį atsaką.

---

### Claude savikritika

**Stipriausias stimulas vizualiai.** Metodologiškai — A ir B per panašūs.
**Keisčiau:** B į *"Pagalvojau ar reikia eiti ar likti"* — labiau abejojimo, mažiau entuziazmo.

---

---

# ST-012

**Nuotrauka:** `p4_empty_table.png`
*(Tuščias stalas su keturiomis kėdėmis, lietus pro langą, vienišas žibintas)*

**Ašis:** control_release (cr)
**Polius:** neigiamas (-1 / neutrali tuštuma)

---

### Situacijos tikslas

Siekia išprovokuoti **reakciją į socialinę tuštumą — buvusią bet nebeesamą veiklą**.
Neapibrėžtumas: ar žmonės išėjo, ar dar neatėjo?
Pasirinkta kaip laukimo ir praradimo vizualinis simbolis.

---

### Vartotojui rodomi variantai

- A: *"Tuštuma — nieko nevyksta"*
- B: *"Tvarka — viskas savo vietoje"*
- C: *"Laukimas — kažkas ateis"*

---

### Vidinė sistemos logika

| Variantas | aw | cs | cr |
|---|---|---|---|
| A — Tuštuma | -0.25 | -0.30 | -0.55 |
| B — Tvarka | +0.10 | +0.20 | +0.60 |
| C — Laukimas | -0.15 | +0.30 | -0.10 |

---

### Metodologinės rizikos

⚠️ **A ir B yra semantiškai priešingi, bet abu galimi:** "Tuštuma" = kažko trūksta; "Tvarka" = viskas gerai. Tas pats vaizdas.
⚠️ **"Tvarka" — pozityvus terminas:** Gali būti renkamas socialinio pageidaujamumo.
⚠️ **Dubliuojasi su ST-010:** Abi nuotraukos rodo tuščias sales. Bibliotekoje du labai panašūs stimulai.

---

### Claude savikritika

**Silpniausia:** Dubliuojasi su ST-010 (tuščia sala). Metodologiškai nereikalingas dublikatas.
**Keisčiau:** Pakeisčiau šią nuotrauką į visiškai kitokį cr ašies stimulą — pvz. ranka leidžia plazdantį popieriaus lapą.

---

---

# BENDRA ANALIZĖ

## 1. Penki stipriausi stimulai

| Reitingas | Stimulas | Kodėl stiprus |
|---|---|---|
| 1 | **ST-011** (Atviros durys) | Aiškus cr- signalas, variantai metodologiškai skirtingi, minimalistiškas |
| 2 | **ST-007** (Tuščias lapas) | Universalus cs simbolis, gera A/C diferenciacija |
| 3 | **ST-005** (Telefonas ant stalo) | Šiuolaikiškas, atpažįstamas, geras cs+ signalas |
| 4 | **ST-009** (Žmogus prie kompiuterio) | Konkretus situacinis kontekstas |
| 5 | **ST-001** (Žmogus prie lango) | Stipriausia vizualinė metafora aw ašiai |

## 2. Penki silpniausi stimulai

| Reitingas | Stimulas | Kodėl silpnas |
|---|---|---|
| 1 | **ST-002** (Du žmonės koridoriuje) | Lyties signalas, realistiniai veidai |
| 2 | **ST-012** (Tuščias stalas) | Dubliuojasi su ST-010 |
| 3 | **ST-008** (Knygelė) | AI pseudotekstas, variantai per panašūs |
| 4 | **ST-004** (Žmogus salėje) | Variantai matuoja projekciją, ne reakciją |
| 5 | **ST-006** (Pokalbio ekranas) | AI artefaktai ekrane, per siaura demografija |

## 3. Pasikartojančios klaidos

**K1 — Projekcija į figūrą, ne žiūrovo reakcija:**
ST-001, ST-004 variantai kalba apie figūroje esantį žmogų ("sunkiai jaučiasi"), o ne apie žiūrovo reakciją. Turėtų būti pirmas asmuo.

**K2 — Variantų asimetrija:**
Keliais stimulais du variantai matuoja tą pačią kryptį, vienas — priešingą (ST-007, ST-009, ST-005). Turėtų būti 1 teigiamas / 1 neigiamas / 1 neutralus.

**K3 — Socialiai pageidaujami žodžiai:**
"Ramybė", "Tvarka", "Normalus", "Kontroliuojama" — visi turi pozityvią konotaciją ir gali būti renkami ne dėl reakcijos, o dėl norimo savęs vaizdavimo.

**K4 — AI vizualiniai artefaktai:**
ST-006 ir ST-008 turi neperskaitomą AI tekstą. Tai vizualinis triukšmas kuris gali veikti pasirinkimą.

**K5 — Semantinis skirtumas tarp vengimo ir paleidimo:**
ST-009 B variantas ("nekreipti dėmesio") matuoja vengimą (aw-), ne paleidimą (cr-). Konstrukto supainiojimas.

## 4. Ar aw/cs/cr logika nuosekli?

**Iš dalies.** Pagrindinė logika tinkama, bet:
- aw ir cr ašys kartais susipynusios (vengimas vs. paleidimas)
- cs ašis stipriausiai reprezentuota (ST-005, ST-006, ST-007, ST-008) — keturi cs stimulai, iš kurių trys cs+
- cr ašis silpniau diferencijuota

## 5. Ar kuri nors ašis dominuoja?

**Taip — cs (certainty_seeking) dominuoja.**
4 iš 12 stimulų yra cs ašies, ir 3 iš 4 yra cs+ poliaus.
Rezultate vartotojas greičiausiai gaus cs+ signalą — ne dėl savo tikros reakcijos, o dėl stimulų paskirstymo.

## 6. Kurie stimulai turėtų būti kuriami iš naujo?

| Stimulas | Rekomendacija |
|---|---|
| ST-002 | Pakeisti abstrakčiais siluetais be lyties požymių |
| ST-004 | Pakeisti variantus į pirmą asmenį |
| ST-006 | Pakeisti nuotrauką — realistinis ekranas be AI artefaktų |
| ST-008 | Pakeisti nuotrauką — realistinė knygelė |
| ST-012 | Pakeisti visiškai — dubliuojasi su ST-010 |

## 7. Didžiausios metodologinės rizikos

**R1 — Socialiai pageidaujamas pasirinkimas:**
Žmonės renkasi "gerai atrodančius" atsakymus, ne tikrąją reakciją. Ypač pavojinga kai variantuose yra žodžiai "ramybė", "normalus", "kontroliuojama".

**R2 — Projekcija vs. reakcija:**
Sistema nori matuoti žiūrovo reakciją, bet keli variantai klausia apie figūros emociją. Tai matuoja empatiją, ne signalą.

**R3 — cs ašies dominavimas:**
4 cs stimulai reiškia, kad cs bus stipriausiai matuojama ašis. Kiti vartotojai gali gauti cs dėsningumą ne dėl savo reakcijų, o dėl stimulų paskirstymo.

**R4 — Vizualiniai AI artefaktai:**
Du stimulai turi AI sugeneruotą nesuprantamą tekstą. Tai gali blaškydyti ir mažinti stimulo autentiškumą.

**R5 — Konstrukto supainiojimas (vengimas vs. paleidimas):**
Atsitraukimas (aw-) ir paleidimas (cr-) yra skirtingi konstruktai, bet kai kurių variantų formuluotės juos supainioja.

---

*ConflictLab Stimulus Review Package v1.0*
*Paruošta metodologiniam auditui: 2026-07-30*
*Claude savikritikos lygis: maksimalus*
