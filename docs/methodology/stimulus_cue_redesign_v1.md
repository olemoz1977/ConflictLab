# Stimulus Redesign — 5 palyginimų demonstracija
**Principas:** UI rodo attention cue → sistema mato choice_id su svoriais (nekeičiami)
**Klausimas:** neutralus, ne emocinis. **Cues:** 1-3 žodžiai, nekyla iš teorijos

---

## L05 — Telefonas ant stalo (waiting / cs+)

**Vaizdas:** Telefonas ant tamsaus stalo. Ekranas juodas.

**ESAMA:**
```
Q: "Kas pirmiausia šovė į galvą?"
A: "Ar atsakė?"                      → aw:+.10 cs:+.65 cr:+.30
B: "Telefonas nutylęs — nieko"       → aw:-.10 cs:-.40 cr:-.20
C: "Pradėjau galvoti ką daryti"      → aw:+.20 cs:+.45 cr:+.55
```
⚠️ A ir C abu cs+ ir interpretuoja situaciją

**NAUJA:**
```
Q: "Kas pirmiausia patraukė dėmesį?"
A: "žinutė"                          → aw:+.10 cs:+.65 cr:+.30
B: "tyla"                            → aw:-.10 cs:-.40 cr:-.20
C: "ką daryti toliau"                → aw:+.20 cs:+.45 cr:+.55
```
✓ Trys skirtingi dėmesio objektai: objektas / būsena / veiksmas
✓ Nė vienas nėra "geresnis" socialiai
✓ Svoriai identiški

---

## L10 — Tuščia konferencijų salė (waiting / cr)

**Vaizdas:** Ilgas stalas, tuščios kėdės, miestas pro langą.

**ESAMA:**
```
Q: "Ką jaučiau žiūrėdamas?"
A: "Palengvėjimas — čia tuščia"      → aw:-.15 cs:-.30 cr:-.60
B: "Tuoj prasidės kažkas"            → aw:+.15 cs:+.45 cr:+.50
C: "Pagalvojau kas čia buvo"         → aw:+.20 cs:+.25 cr:-.10
```
⚠️ Klausia emocijų tiesiogiai. A — pilnas sakinys su interpretacija.

**NAUJA:**
```
Q: "Kas pirmiausia patraukė dėmesį?"
A: "tuštuma"                         → aw:-.15 cs:-.30 cr:-.60
B: "laukimas"                        → aw:+.15 cs:+.45 cr:+.50
C: "kas čia buvo"                    → aw:+.20 cs:+.25 cr:-.10
```
✓ Trys skirtingi dėmesio kryptys: būsena / procesas / praeitinė situacija
✓ Klausimas neutralus — apie dėmesį, ne emociją

---

## L12 — Tuščias stalas dviem (waiting / cr-)

**Vaizdas:** Mažas apvalus stalas, dvi tuščios kėdės, restoranas.

**ESAMA:**
```
Q: "Kas pirmiausia šovė į galvą?"
A: "Tuštuma — nieko nevyksta"        → aw:-.25 cs:-.30 cr:-.55
B: "Tvarka — viskas gerai"           → aw:+.10 cs:+.20 cr:+.60
C: "Pagalvojau kas čia sėdės"        → aw:+.30 cs:+.20 cr:+.15
```
⚠️ A ir B — pilni sakiniai su vertinimu ("nieko nevyksta", "gerai")

**NAUJA:**
```
Q: "Kas pirmiausia patraukė dėmesį?"
A: "tuščios kėdės"                   → aw:-.25 cs:-.30 cr:-.55
B: "tvarka"                          → aw:+.10 cs:+.20 cr:+.60
C: "kas čia sėdės"                   → aw:+.30 cs:+.20 cr:+.15
```
✓ Objektas / savybė / anticipacija — trys skirtingi lygiai
✓ Pašalintas vertinimas

---

## L01 — Žmogus prie lango (withdrawal / aw-)

**Vaizdas:** Siluetas prie lango, tamsi erdvė, šviesa iš lauko.

**ESAMA:**
```
Q: "Kas pirmiausia šovė į galvą?"
A: "Norėjosi pabūti vienam"          → aw:-.55 cs:-.20 cr:-.30
B: "Pagalvojau kas vyksta lauke"     → aw:+.25 cs:+.15 cr:+.10
C: "Laukimas — nieko ypatingo"       → aw:-.10 cs:-.30 cr:-.15
```
⚠️ A — gryna interpretacija ("norėjosi"). C — mišrus sakinys.

**NAUJA:**
```
Q: "Kas pirmiausia patraukė dėmesį?"
A: "vienatvė"                        → aw:-.55 cs:-.20 cr:-.30
B: "kas lauke"                       → aw:+.25 cs:+.15 cr:+.10
C: "laukimas"                        → aw:-.10 cs:-.30 cr:-.15
```
✓ Trys kryptys: vidus / išorė / procesas
✓ Nė vienas neatspindi "teisingos" reakcijos

---

## L02 — Dvi abstrakčios figūros (encounter / aw+)

**Vaizdas:** Dvi figūros artėja viena kitos link.

**ESAMA:**
```
Q: "Ką jaučiau žiūrėdamas?"
A: "Kažkas čia vyksta"               → aw:+.50 cs:+.20 cr:+.15
B: "Per arti — nesmagu"              → aw:-.25 cs:+.35 cr:+.25
C: "Tiesiog du žmonės"               → aw:+.05 cs:-.10 cr:-.05
```
⚠️ Klausia emocijų. B — vertinimas ("nesmagu").

**NAUJA:**
```
Q: "Kas pirmiausia patraukė dėmesį?"
A: "susitikimas"                     → aw:+.50 cs:+.20 cr:+.15
B: "atstumas"                        → aw:-.25 cs:+.35 cr:+.25
C: "du žmonės"                       → aw:+.05 cs:-.10 cr:-.05
```
✓ Santykis / erdvė / objektas
✓ Pašalintas emocinis vertinimas
✓ Svoriai identiški

---

## Palyginimas: vienas klausimas visiems 5

**ESAMA:** Skirtingi klausimai
- "Ką jaučiau žiūrėdamas?"
- "Ką norėjosi daryti?"
- "Kas pirmiausia šovė į galvą?"

**NAUJA:** Vienas klausimas visiems
- "Kas pirmiausia patraukė dėmesį?"

**Kodėl vienas klausimas?**
Vienodas klausimas pašalina klausimo efektą — žmogus orientuojasi į vaizdą, o ne į klausimo formuluotę.

---

## Signalų integracija (A variantas patvirtintas)

```
Vartotojas mato:    Sistema mato:
─────────────────   ──────────────────────────
"žinutė"         →  choice_id: L05_A
                    aw: +0.10, cs: +0.65, cr: +0.30

"tyla"           →  choice_id: L05_B
                    aw: -0.10, cs: -0.40, cr: -0.20
```

Raktažodis nėra signalo pavadinimas.
Jis yra UI reprezentacija `choice_id`.
Tas pats žodis kitame stimule = visiškai kiti svoriai.

---

## Sprendimas prieš taikant visai bibliotekai

Rekomenduojama: įdiegti šiuos 5 stimulus kaip A/B testą.
Stebėti per beta: ar cues sukelia natūralesnes reakcijas?
Metrika: Q2 atsakymų kokybė ("to nebuvau pastebėjęs" vs. "žinojau")

