# ST-002 — Stimulus Review

**Stimulo ID:** ST-002
**Peržiūros data:** 2026-07-30
**Recenzentas:** Claude (ConflictLab v0.6 auditas)
**Remtasi:** `docs/methodology/stimulus_validation_protocol.md` v1.0.1
**Statusas po peržiūros:** beta_po_pataisymo

---

## IMAGE — Vaizdo validacija (V1)

*Vertinamas tik vaizdas. Variantai ir signalai dar nevertinami.*

### V1.1 Neutralumas
**Įvertinimas:** 3/5
**Paaiškinimas:** Vaizdas leidžia kelias interpretacijas: derybos, konfliktas, susitikimas, atsitiktinis susidūrimas. Tačiau du žmonės veidu į veidą koridoriuje sukuria stiprų "konfrontacijos" lūkestį — viena interpretacija gali dominuoti.
**Rastos problemos:** Konfrontacijos interpretacija gali viršyti 50% — ribinė neutralumo zona.
**Rekomendacija:** Priimti su žyma `interpretacijos_skersvėjas: konfrontacija`

### V1.2 AI artefaktai
**Įvertinimas:** 4/5
**Paaiškinimas:** Vaizdas yra AI generuotas, tačiau artefaktų nėra — figūros anatomiškai teisingos, aplinka natūrali, apšvietimas logiškas.
**Rastos problemos:** Šiek tiek per "tobulas" — gali atrodyti kaip reklama, o ne gyvenimiškas kadras.
**Rekomendacija:** Priimti

### V1.3 Kultūrinis šališkumas
**Įvertinimas:** 3/5
**Paaiškinimas:** Biuro koridoriaus aplinka yra pakankamai universali, tačiau specifinė darbo kontekstui. Distancija tarp figūrų (apie 1 metras) turi kultūrinę reikšmę — Vakarų kultūroje tai "asmeninė erdvė", kitur gali būti kitaip.
**Rastos problemos:** Asmeninės erdvės koncepcija kultūriškai specifinė.
**Rekomendacija:** Priimti su žyma `cultural_flag: asmenine_erdve`

### V1.4 Lyties / amžiaus / statuso signalai
**Įvertinimas:** 2/5
**Paaiškinimas:** Nuotraukoje matomi vyras ir moteris veidu į veidą. Lyties signalas yra tikra problema, tačiau nepriklausomo audito metu nustatytas dar svarbesnis reiškinys — žr. Naratyvinio šališkumo pastabą žemiau.
**Rastos problemos:** Lyties signalas gali aktyvuoti lyčių dinamikos schemas nesusijusias su aw konstruktu.
**Rekomendacija:** Taisyti stimulą — ne review.

### V1.4a Naratyvinis šališkumas (FC-001)
**Įvertinimas:** ⚠ Pastaba (ne Protocol kriterijus — žr. `future_considerations.md`)
**Paaiškinimas:** Vaizdas labai skatina žiūrovą kurti santykių istoriją: vadovas/darbuotojas, kolegos, pora, derybos, konfliktas. Šis naratyvinis sluoksnis gali nustelbti aw signalą — žmogus reaguoja į tariamą santykį, o ne į artėjimo/atsitraukimo dimensiją. Tai skiriasi nuo lyties signalo — problema atsiras net su neutraliomis figūromis jei jos yra aiškioje socialinėje situacijoje.
**Rastos problemos:** Santykio neapibrėžtumas (relationship ambiguity) gali dominuoti prieš aw konstruktą.
**Rekomendacija:** Taisyti stimulą — figūros turėtų būti mažiau individualizuotos, be aiškių santykio užuominų.

### V1.5 Neapibrėžtumo lygis
**Įvertinimas:** 20–70% (optimalus, bet ribinis)
**Paaiškinimas:** Vaizdas yra suprantamas — žmonės koridoriuje. Bet du žmonės veidu į veidą be konteksto sukuria didelę interpretacijų įvairovę. Optimalus diapazonas pasiektas, bet V1.1 ir V1.4 problemos gali jį siaurinti.
**Rastos problemos:** Lyties signalas gali siaurinti interpretacijų erdvę.
**Rekomendacija:** Priimti

---

## CHOICES — Variantų validacija (V2)

*Vertinami tik trijų variantų tekstai.*

### V2.1 Reakcija, ne nuomonė
**Įvertinimas:** 4/5
**Paaiškinimas:** A ("artumas — kažkas sprendžiasi") ir B ("įtampa — per arti") yra momentinės reakcijos. C ("neutralu — tiesiog du žmonės") yra šiek tiek racionalizuotas — reikalauja "tiesiog" neutralizavimo gesto.
**Rastos problemos:** C variantas yra racionalizacija, ne gryna reakcija.
**Rekomendacija:** Priimti — C yra ribinis bet priimtinas.

### V2.2 Socialiai pageidaujamas atsakymas
**Įvertinimas:** 4/5
**Paaiškinimas:** A ("artumas") ir C ("neutralu") gali atrodyti "pozityvesni" nei B ("įtampa"). Tačiau B yra legitimiai tikėtina reakcija — "per arti" nėra moraliniu požiūriu negatyvu.
**Rastos problemos:** A ir C šiek tiek "geresni" socialiniu požiūriu nei B, bet skirtumas nėra kritinis.
**Rekomendacija:** Priimti

### V2.3 Moralinis pasirinkimas
**Įvertinimas:** 5/5
**Paaiškinimas:** Nė vienas variantas neturi moralinės konotacijos. "Artumas", "įtampa", "neutralu" — visi moraliniu požiūriu neutralūs.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V2.4 Projekcija į vaizdą
**Įvertinimas:** 4/5
**Paaiškinimas:** Visi variantai aprašo žiūrovo reakciją — ne figūrų emocijas. "Jaučiau artumą", "jaučiau įtampą", "mačiau neutralią sceną" — visi pirmo asmens reakcijos.
**Rastos problemos:** "Kažkas sprendžiasi" (A variante) yra projekcija į situaciją — bet ne į figūrą. Ribinai priimtina.
**Rekomendacija:** Priimti

### V2.5 Akivaizdžiai teisingas variantas
**Įvertinimas:** 4/5
**Paaiškinimas:** Galima įsivaizduoti realų žmogų kiekvienam variantui. A — ekstravertas ar empatas. B — asmuo jautrus asmeninei erdvei. C — analitiškai mąstantis žmogus.
**Rastos problemos:** C variantas yra mažiau tikėtinas kaip pirma reakcija.
**Rekomendacija:** Priimti

---

## SIGNALS — Signalų validacija (V3)

*Vertinami tik aw/cs/cr svoriai.*

### V3.1 Pirminė ašis
**Deklaruota ašis:** aw (approach_withdrawal)
**Įvertinimas:** 5/5
**Paaiškinimas:** A: aw+0.50 (stiprus artėjimas). B: aw-0.25 (atsitraukimas). C: aw+0.05 (neutralus). Pirminė ašis dominuoja. Ir X+ (A) ir X- (B) variantai yra.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V3.2 aw/cs/cr diferenciacija
**Įvertinimas:** 4/5
**Paaiškinimas:** aw ir cr nesupainiotos. B variante aw- (-0.25) + cs+ (+0.35) + cr+ (+0.25) — tai yra dokumentuotas mišrus signalas. Logika: įtampa → atsitraukimas + aiškumo poreikis + kontrolės siekimas. Psichologiškai pagrįsta.
**Rastos problemos:** B variante cs ir cr svoriai reikšmingi — bet žemiau pirminės aw ašies.
**Rekomendacija:** Priimti

### V3.3 Mišrūs signalai
**Ar yra mišrūs signalai:** Taip (A ir B variantai)
**Paaiškinimas:** Abu pagrįsti ir dokumentuoti `stimulus.yaml → mixed_signal_justification`. A: artumas → struktūros lūkestis (cs+, cr+). B: įtampa → aiškumo ir kontrolės poreikis (cs+, cr+).
**Rastos problemos:** Nėra — pagrindimas tinkamas.
**Rekomendacija:** Priimti

### V3.4 Variantų svorių simetrija
**Įvertinimas:** 4/5
**Paaiškinimas:** A: aw+0.50. B: aw-0.25. C: aw+0.05. Yra tiek aw+ tiek aw- variantai. Simetrija pakankama, nors A polius kiek stipresnis nei B.
**Rastos problemos:** A (aw+0.50) stipresnis nei B (aw-0.25) — asimetrija priimtina bet pastebėta.
**Rekomendacija:** Priimti

---

## Daugiateorinė validacija (V4)

*Teorijos validuoja stimulą — ne žmogų.*

### Teorija 1: Dual Process Theory (Kahneman)
**Validacijos klausimas:** Ar stimulas sukelia momentinę (System 1) reakciją?
**Įvertinimas:** Patvirtina
**Paaiškinimas:** Visi trys variantai gali kilti per pirmąsias 2 sekundes. "Artumas", "įtampa", "neutralu" — visi System 1 lygio reakcijos.

### Teorija 2: Attachment Theory (Bowlby)
**Validacijos klausimas:** Ar stimulas gali aktyvuoti prisirišimo schemas? Ar aw ašis tinkama?
**Įvertinimas:** Patvirtina — su pastaba
**Paaiškinimas:** Du žmonės veidu į veidą yra klasikinis prisirišimo konteksto stimulas. aw ašis visiškai tinkama. Pastaba: lyties signalas (V1.4) gali aktyvuoti romantinius prisirišimo scenarijus — ne universalų aw konstruktą.

### Teorija 3: SCARF Model (Rock)
**Validacijos klausimas:** Ar stimulas aktyvuoja Status ar Relatedness grėsmę?
**Įvertinimas:** Abejoja
**Paaiškinimas:** Du žmonės koridoriuje gali aktyvuoti Status dinamiką (kas turi galią?) ir Relatedness (ar jie pažįstami?). Jei Status dominuoja — stimulas matuoja ne aw, o hierarchijos reakciją. SCARF signalizuoja potencialą konstrukto supainiojimui.

### Teoriniai prieštaravimai
**Ar yra:** Taip (ribinis)
**Aprašymas:** SCARF abejoja ar aw yra dominuojantis konstruktas — gali būti Status signalas. Attachment patvirtina aw, bet su lyties signalo pastaba.
**Rekomendacija:** Priimti su žyma `teorinis_abejonimas: SCARF_status`

---

## Bibliotekos validacija (V5)

### V5.1 Dublikatai
**Ar yra panašių stimulų:** Taip — L02 (identiškas stimulas senoje bibliotekoje)
**Ar konstruktai skiriasi:** Ne — tas pats vaizdas, ta pati ašis
**Rekomendacija:** ST-002 pakeičia L02. L02 archyvuojamas.

### V5.2 Ašių balansas po ST-002 pridėjimo
- aw stimulai: 2/2 (100%) — kol kas tik aw stimulai, balansuosis toliau
- cs stimulai: 0/2 (0%)
- cr stimulai: 0/2 (0%)

**Ar laikomasi 25–40% ribų:** Ne — bet tik 2 stimulai iš planuojamų 12. Balansas vertintinas po pilno bibliotekos ciklo.
**Rekomendacija:** Priimti — disbalansas laukiamas pradinėje fazėje.

### V5.3 Kontekstų įvairovė
**Stimulo kontekstas:** tarpasmeniniai
**Ar per daug reprezentuotas:** Ne — ST-001 yra vidine_erdve, ST-002 yra tarpasmeniniai.
**Rekomendacija:** Priimti — kontekstai skiriasi.

---

## Empirinė validacija (V6)

*(Nepildyta — stimulas dar nebuvo testuotas su realiais žmonėmis)*

### Beta / Pilotinis
**Statusas:** Laukiama

### Pašalinimo kriterijai
- [ ] Nė vienas variantas >60%
- [ ] Reakcijos laikas <8 sek.
- [ ] >70% supranta vaizdą
- [ ] >40% rezonansas
- [ ] Nėra statistinių demografinių skirtumų

---

## Galutinis vertinimas

| Kriterijus | Objektas | Svoris | Balas | Svertinis |
|---|---|---|---|---|
| V1.1 Neutralumas | IMAGE | 15% | 3/5 | 9 |
| V1.2 AI artefaktai | IMAGE | 10% | 4/5 | 8 |
| V1.3 Kultūrinis neutralumas | IMAGE | 10% | 3/5 | 6 |
| V1.4 Lyties/statuso neutralumas | IMAGE | 10% | 2/5 | 4 |
| V2.1 Reakcija, ne nuomonė | CHOICES | 15% | 4/5 | 12 |
| V2.2 Socialinis neutralumas | CHOICES | 15% | 4/5 | 12 |
| V3.1 Pirminė ašis | SIGNALS | 10% | 5/5 | 10 |
| V3.4 Svorių simetrija | SIGNALS | 10% | 4/5 | 8 |
| V4 Teorijų validacija | VISI | 5% | 4/5 | 4 |
| **VISO** | | **100%** | | **73/100** |

**Minimalus balas: 70/100**
**Gautas balas: 73/100** ✓

**Sprendimas:** 🟡 Beta po pataisymo

**Žymos:**
- `taisyti_stimula: naratyvinis_sališkumas` — figūros per daug individualizuotos, santykio neapibrėžtumas nustelbia aw
- `taisyti_stimula: lyties_signalas` — rekomenduoti abstraktūs siluetai
- `cultural_flag: asmenine_erdve` — kultūriškai specifinė distancija
- `teorinis_abejonimas: SCARF_status` — SCARF abejoja dominuojančiu konstruktu
- `replaces: L02` — archyvuojamas senas stimulas
- `fc_001_stebima` — Naratyvinis šališkumas užregistruotas future_considerations.md

---

## Bibliotekos įnašo suvestinė

**Kas naujo bibliotekoje po ST-002:**
- ✓ Naujas kontekstas: `tarpasmeniniai` (ST-001 buvo `vidine_erdve`)
- ✓ Naujas situacijų klasė: dviejų žmonių dinamika (ST-001 buvo vienas žmogus)
- ✓ Naujas aw polius: `aw+` (artėjimas)
- ✓ Naujas signalų derinys: aw+ su cs+/cr+ (artėjimas + struktūros lūkestis)
- ⚠ Taisytina: naratyvinis šališkumas + lyties signalas

**Sprendimas:** 🟡 Beta po pataisymo — stimulas praturtina biblioteką, bet reikia geresnio vaizdo

---

*Review užpildyta pagal: `docs/methodology/stimulus_validation_protocol.md` v1.0.1*
