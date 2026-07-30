# ConflictLab — Stimulus Validation Protocol
**Versija:** v1.0
**Statusas:** Aktyvus standartas
**Data:** 2026-07-30
**Peržiūros ciklas:** Kas 12 mėnesių arba po didelio bibliotekos atnaujinimo

---

## Architektūrinis principas

> Stimulas nematuoja žmogaus. Stimulas sukuria sąlygas stebėti reakciją.

Šis dokumentas apibrėžia kriterijus, kuriuos turi atitikti kiekvienas stimulas prieš patenkant į ConflictLab biblioteką. Jis taikomas nepriklausomai nuo bibliotekos dydžio ar laikotarpio.

**Validation Protocol yra aukštesnio prioriteto dokumentas negu bet kuris Stimulus Review.**
Jei Review prieštarauja Protocol — taisomas Review, o ne Protocol.

---

## Validacijos proceso apžvalga

Kiekvienas naujas stimulas privalo praeiti šešis validacijos etapus **eilės tvarka**.

| Etapas | Pavadinimas | Privalomas |
|---|---|---|
| V1 | Vizualinė validacija | Taip |
| V2 | Psichologinė validacija | Taip |
| V3 | Konstrukto validacija | Taip |
| V4 | Daugiateorinė validacija | Taip |
| V5 | Bibliotekos validacija | Taip |
| V6 | Empirinė validacija | Prieš pilną naudojimą |

V1–V5 atliekami prieš stimulą įtraukiant į beta biblioteką.
V6 atliekamas per pirmuosius 30 dienų nuo naudojimo.

---

## V1. Vizualinė validacija

### V1.1 Neutralumas

**Taisyklė:** Vaizdas turi leisti bent dvi skirtingas, lygiavertes interpretacijas.

- ✓ Priimti: Koridorius gali reikšti išėjimą po darbo, pabėgimą, judėjimą link tikslo.
- ⛔ Atmesti: Verkiantis žmogus — tik viena interpretacija.
- ◆ Ribinis atvejis: Jei vaizdas turi 2+ interpretacijas, bet viena dominuoja >80% — peržiūrėti variantus.

### V1.2 AI artefaktai

**Taisyklė:** Vaizdas neturi turėti nesuprantamo teksto, nenormalios anatomijos ar akivaizdžių AI klaidų.

- ✓ Priimti: Tuščias lapas, abstrakti figūra, natūralus interjeras.
- ⛔ Atmesti: Telefonas su neperskaitomu pseudotekstu ekrane.
- ◆ Pastaba: Teksto buvimas nėra klaida — klaida yra neskaitomas, beprasmis tekstas.

### V1.3 Kultūrinis šališkumas

**Taisyklė:** Vaizdas turi būti interpretuojamas be kultūrinių žinių.

- ✓ Priimti: Tuščias stalas, atviros durys, žmogus prie lango.
- ⛔ Atmesti: Specifiniai kultūriniai simboliai (religiniai ženklai, tradiciniai drabužiai).
- ◆ Ribinis atvejis: Biuro aplinka — leistina su žyma `context: office`.

### V1.4 Lyties, amžiaus ir statuso signalai

**Taisyklė:** Figūros turi būti neutralios arba jų lytis/amžius/statusas neturi būti aiškiai matomas.

- ✓ Priimti: Siluetas be veidų. Figūra nugara. Tamsios neidentifikuojamos figūros.
- ⛔ Atmesti: Ryškiai matomas veidas su aiškia lytimi. Uniforma nurodanti statusą.
- ◆ Ribinis atvejis: Profesija leistina jei matuojamas darbo kontekstas — su žyma.

### V1.5 Neapibrėžtumo lygis

**Taisyklė:** Optimalus neapibrėžtumo lygis — 20–70%.

| Lygis | Aprašymas | Vertinimas |
|---|---|---|
| < 20% | Visi supranta vienodai | ⛔ Atmesti |
| 20–70% | Kelios pagrįstos interpretacijos | ✓ Priimti |
| > 70% | Per abstraktus | ◆ Peržiūrėti |

---

## V2. Psichologinė validacija

### V2.1 Reakcija, ne nuomonė

**Taisyklė:** Variantai turi aprašyti momentinę reakciją, ne reflektuotą nuomonę.

- ✓ Priimti: `"Iš karto pagalvojau apie žinutę"` — reakcija.
- ⛔ Atmesti: `"Manau, kad kolega elgiasi neprofesionaliai"` — nuomonė.
- ◆ Testas: Ar variantas galėjo kilti per pirmąsias 2 sekundes?

### V2.2 Socialiai pageidaujamas atsakymas

**Taisyklė:** Nė vienas variantas neturi būti akivaizdžiai "geresnis" socialiniu požiūriu.

- ✓ Priimti: `"Laukimas — normalu"` / `"Norėjosi greitai reaguoti"` — lygiaverčiai.
- ⛔ Atmesti: `"Išlikau ramus ir racionalus"` vs `"Supanikiavau"`.
- ◆ Pavojingiausi žodžiai: "normalus", "ramus", "racionalus", "kontroliuojamas", "profesionalus".

### V2.3 Moralinis pasirinkimas

**Taisyklė:** Nė vienas variantas neturi turėti moralinės konotacijos.

- ✓ Priimti: `"Norėjosi ignoruoti"` / `"Norėjosi reaguoti"` — moraliniu požiūriu neutralūs.
- ⛔ Atmesti: `"Supratau, kad elgiausi neteisingai"` — moralinis vertinimas.
- ◆ Testas: Ar variantas implikuoja kaltę, gėdą ar pareigą?

### V2.4 Projekcija į vaizdą

**Taisyklė:** Variantai turi būti pirmo asmens — ne projekcija į figūros emociją.

- ✓ Priimti: `"Norėjosi atsitraukti"` — žiūrovas apie save.
- ⛔ Atmesti: `"Jis / Ji jaučiasi vienišas"` — projekcija į figūrą.
- ◆ Ribinis atvejis: `"Pagalvojau, kad jam reikia pagalbos"` — empatijos reakcija (aw+), priimtina.

### V2.5 Akivaizdžiai teisingas variantas

**Taisyklė:** Visi trys variantai turi būti pagrįsti kaip tikros pirmosios reakcijos.

- ✓ Priimti: Trys skirtingos, bet vienodai tikėtinos reakcijos.
- ⛔ Atmesti: Du absurdiški ir vienas logiškas variantas.
- ◆ Testas: Ar galite įsivaizduoti realų žmogų kuris rinktų kiekvieną variantą?

---

## V3. Konstrukto validacija

### V3.1 Pirminė ašis

**Taisyklė:** Stimulo pirminė ašis turi turėti didžiausius absoliučius svorius bent dviejuose variantuose.

- ✓ Priimti: cs stimulas — cs variantai = ±0.45–0.55. aw ir cr < 0.20.
- ⛔ Atmesti: Stimulas deklaruotas kaip aw, bet cs svoriai didesni.

### V3.2 Ašių diferenciacija

**Ašių apibrėžimai:**

| Ašis | Teigiamas polius (+) | Neigiamas polius (-) |
|---|---|---|
| `approach_withdrawal` (aw) | Artėjimas, įsitraukimas, kontaktas | Atsitraukimas, distancija, izoliacija |
| `certainty_seeking` (cs) | Aiškumo siekimas, struktūros poreikis | Neapibrėžtumo tolerancija, atvirumas |
| `control_release` (cr) | Kontrolės siekimas, struktūravimas | Paleidimas, perdavimas, srautas |

**Kritinis skirtumas:** aw- (atsitraukimas) ≠ cr- (paleidimas). Dažna supainiojimo vieta.

### V3.3 Mišrūs signalai

**Taisyklė:** Mišrūs signalai leistini kai psichologiškai pagrįsti. Antrinė ašis negali viršyti pirminės.

- ✓ Priimti: `"Rašyti dar kartą"` → cs+(0.50) + cr+(0.60). Logiškai pagrįsta.
- ⛔ Atmesti: cs stimulas su cr dominuojančiu svoriu.
- ◆ Mišraus signalo pagrindimas turi būti dokumentuojamas `stimulus.yaml` faile.

### V3.4 Variantų svorių simetrija

**Taisyklė:** Turėti bent vieną X+ ir vieną X- variantą pirminei ašiai.

- ✓ Priimti: cs stimulas: A(cs+0.65), B(cs-0.40), C(cs-0.05).
- ⛔ Atmesti: cs stimulas: A(cs+0.65), B(cs+0.50), C(cs-0.10). Du cs+ — skersvėjas.

---

## V4. Daugiateorinė validacija

**Esminis principas:** Teorijos validuoja stimulą — ne žmogų.

### V4.1 Kaip teorijos naudojamos

Kiekviena teorija yra "lęšis" per kurį žiūrima į stimulą. Klausimas:
> "Ar šis stimulas yra metodologiškai teisingas per šios teorijos perspektyvą?"

**Ne:** "Ką ši teorija sako apie žmogų."

### V4.2 Kaip teorijos NETURĖTŲ būti naudojamos

- ⛔ Teorijos nėra naudojamos žmogaus reakcijos interpretacijai.
- ⛔ Teorijos nėra naudojamos stimulo rezultatų aiškinimui vartotojui.
- ⛔ Teorija nėra "teisingesnė" už kitą.

### V4.3 Minimalus teorijų skaičius

**Taisyklė:** Kiekvienas stimulas turi būti peržiūrėtas per bent 3 nepriklausomas teorijas.

- ✓ Priimti: 3+ teorijų peržiūra su dokumentuotais rezultatais.
- ⛔ Atmesti: 1 teorijos peržiūra.

### V4.4 Teorinių prieštaravimų valdymas

Prieštaravimai tarp teorijų yra SIGNALAS, ne klaida. Stimulas gali būti priimtas su žyma.

---

## V5. Bibliotekos validacija

### V5.1 Dublikatų tikrinimas

**Taisyklė:** Naujas stimulas neturi dubliuoti esamo vizualiai AR konstruktyviai.

- ✓ Priimti: Naujas koridoriaus vaizdas su skirtingais variantais.
- ⛔ Atmesti: Du vaizdai rodantys tuščią salę su identiškais variantais.

### V5.2 Ašių balansas

| Rodiklis | Minimalas | Optimalus | Maksimalus |
|---|---|---|---|
| Stimulai vienai ašiai | 25% | 33% | 40% |
| Stimulai vienam poliui | 30% ašies | 50% ašies | 70% ašies |
| Neutralūs stimulai | 5% | 10% | 20% |

### V5.3 Kontekstų įvairovė

| Kontekstas | Rekomenduojama dalis |
|---|---|
| Darbo aplinka | 20–30% |
| Tarpasmeniniai santykiai | 20–30% |
| Vidinė erdvė | 15–25% |
| Gamta / abstrakti aplinka | 10–20% |
| Technologinis kontekstas | 10–20% |

---

## V6. Empirinė validacija

### V6.1 Minimalus testavimo protokolas

| Etapas | Imtis | Tikslas |
|---|---|---|
| Beta | 5–10 žmonių | Grubūs defektai |
| Pilotinis | 30–50 žmonių | Statistinis pasiskirstymas |
| Patvirtinimas | 100+ žmonių | Subgrupių analizė |

### V6.2 Gero stimulo rodikliai

- ✓ Variantų pasiskirstymas: nė vienas variantas >60% atvejų.
- ✓ Reakcijos laikas: vidutinis pasirinkimas <8 sekundžių.
- ✓ Atpažinimas: >70% supranta vaizdą.
- ✓ Rezonansas: >40% patvirtina refleksiją kaip "atpažįstu".
- ✓ Subgrupių homogeniškumas: nėra statistiškai reikšmingų skirtumų pagal lytį/amžių.

### V6.3 Pašalinimo kriterijai

- ⛔ Vienas variantas >70% atvejų.
- ⛔ Statistiškai reikšmingi demografiniai skirtumai.
- ⛔ Reakcijos laikas >15 sekundžių.
- ⛔ >30% sako "nesuprantu vaizdo".
- ⛔ >10% patiria emocinį diskomfortą.

---

## Stimulo vertinimo kortelė

| Kriterijus | Svoris | Min. balas |
|---|---|---|
| V1.1 Neutralumas | 15% | 3/5 |
| V1.2 AI artefaktai | 10% | 5/5 |
| V1.3 Kultūrinis neutralumas | 10% | 3/5 |
| V1.4 Lyties/statuso neutralumas | 10% | 4/5 |
| V2.1 Reakcija, ne nuomonė | 15% | 4/5 |
| V2.2 Socialinis neutralumas | 15% | 4/5 |
| V3.1 Pirminė ašis | 10% | 4/5 |
| V3.4 Svorių simetrija | 10% | 3/5 |
| V4 Teorijų validacija | 5% | 3/5 |

**Minimali bendra reikšmė priėmimui: 70/100**

Bet kurio kriterijaus "Min. balas" nepassiekimas → automatinis atmetimas nepriklausomai nuo bendro balo.

---

## Dokumento valdymas

| Laukas | Reikšmė |
|---|---|
| Versija | 1.0 |
| Statusas | Aktyvus standartas |
| Peržiūros ciklas | Kas 12 mėnesių |
| Galioja nuo | Bibliotekos versija 1.0 |
