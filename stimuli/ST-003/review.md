# ST-003 — Stimulus Review

**Stimulo ID:** ST-003
**Vaizdo versija:** v1
**Peržiūros data:** 2026-07-30
**Recenzentas:** Claude (ConflictLab auditas)
**Remtasi:** `docs/methodology/stimulus_validation_protocol.md` v1.0.1
**Statusas po peržiūros:** review

---

## IMAGE — Vaizdo validacija (V1)

*Vaizdas: tuščias baltas lapas ant tamsaus paviršiaus, šviesa iš šono.*

### V1.1 Neutralumas
**Įvertinimas:** 4/5
**Paaiškinimas:** Tuščias lapas leidžia bent tris lygiavertes interpretacijas: galimybė (dar nieko neparašyta), spaudimas (reikia parašyti), tyla (nereikia nieko). Jokios figūros, jokio konteksto — interpretacija visiškai žiūrovo projekcija.
**Rastos problemos:** Akademinis ar profesinis kontekstas gali sukelti "reikia užpildyti" schemą žmonėms su stipria pareigos kultūra. Nereikšminga, bet stebėtina.
**Rekomendacija:** Priimti

### V1.2 AI artefaktai
**Įvertinimas:** 5/5
**Paaiškinimas:** Vaizdas fotografinis arba labai tikroviškas. Tuščias lapas — jokių artefaktų galimybės. Šviesos ir šešėlių žaismas natūralus.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V1.3 Kultūrinis šališkumas
**Įvertinimas:** 5/5
**Paaiškinimas:** Tuščias lapas yra vienas universaliausių simbolių. Popierius naudojamas beveik visose kultūrose. Jokio specifinio kultūrinio konteksto.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V1.4 Lyties / amžiaus / statuso signalai
**Įvertinimas:** 5/5
**Paaiškinimas:** Vaizdas — tik popierius ir paviršius. Jokių žmonių, jokių figūrų. Visiškas neutralumas.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V1.5 Neapibrėžtumo lygis
**Įvertinimas:** 20–70% (optimalus)
**Paaiškinimas:** Vaizdas suprantamas visiems — tuščias lapas. Bet jo reikšmė interpretuojama skirtingai. Geras neapibrėžtumo balansas.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

---

## CHOICES — Variantų validacija (V2)

### V2.1 Reakcija, ne nuomonė
**Įvertinimas:** 3/5
**Paaiškinimas:** A ("galimybė — galima rašyti bet ką") yra sąvokinė reakcija — reikalauja kognityvinės operacijos "tai = galimybė". B ("nerimas") ir C ("tyla") yra artimesnės momentinei reakcijai.
**Rastos problemos:** A variantas yra interpretacija, ne gryna reakcija. Pažeidžia V2.1 ribą.
**Rekomendacija:** Perrašyti A variantą. Siūloma: *"Iš karto pagalvojau ką čia galėčiau daryti"* — tai yra reakcija, ne vertinimas.

### V2.2 Socialiai pageidaujamas atsakymas
**Įvertinimas:** 3/5
**Paaiškinimas:** A ("galimybė") skamba optimistiškai ir gali būti renkamas kaip socialiai pageidaujamas. B ("nerimas") gali būti vengiamas kaip "silpnybės" ženklas. Asimetrija reikšminga.
**Rastos problemos:** A variantas turi pozityvumo šališkumą. B variantas gali būti vengiamas.
**Rekomendacija:** Perrašyti A — pašalinti "galimybė" žodį iš teksto.

### V2.3 Moralinis pasirinkimas
**Įvertinimas:** 5/5
**Paaiškinimas:** Nė vienas variantas neturi moralinės konotacijos.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V2.4 Projekcija į vaizdą
**Įvertinimas:** 5/5
**Paaiškinimas:** Visi variantai aprašo žiūrovo vidinę reakciją, ne vaizdo turinį. Nėra figūrų į kurias projektuoti.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V2.5 Akivaizdžiai teisingas variantas
**Įvertinimas:** 4/5
**Paaiškinimas:** Galima įsivaizduoti realų žmogų kiekvienam variantui. Tačiau A ir C abu yra cs- krypties — žr. V3.4.
**Rastos problemos:** A ir C abu matuoja cs- — asimetrija SIGNALS lygmeniu.
**Rekomendacija:** Priimti variantus, bet koreguoti svorius.

---

## SIGNALS — Signalų validacija (V3)

### V3.1 Pirminė ašis
**Deklaruota ašis:** cs (certainty_seeking), polius: neigiamas (-)
**Įvertinimas:** 4/5
**Paaiškinimas:** B: cs+0.55 (aiškumo siekimas). A: cs-0.45. C: cs-0.50. Pirminė ašis dominuoja visuose variantuose. Tačiau du variantai cs- pusėje prieš vieną cs+.
**Rastos problemos:** Asimetrija — du cs- prieš vieną cs+. Žr. V3.4.
**Rekomendacija:** Priimti — asimetrija pažymėta.

### V3.2 aw/cs/cr diferenciacija
**Įvertinimas:** 5/5
**Paaiškinimas:** cs ir cr nesupainiotos. C variante cs- ir cr- abu stiprūs — abu matuoja neapibrėžtumo toleranciją skirtingomis dimensijomis. Pagrindimas dokumentuotas.
**Rastos problemos:** Nėra.
**Rekomendacija:** Priimti

### V3.3 Mišrūs signalai
**Ar yra:** Taip (visi trys variantai)
**Paaiškinimas:** Visi pagrįsti ir dokumentuoti `stimulus.yaml`. A: cs- + cr- (galimybė → kontrolės paleidimas). B: cs+ + cr+ (nerimas → kontrolės siekimas). C: cs- + cr- (tyla → visiškas paleidimas).
**Rastos problemos:** C variante cr- (-0.45) yra labai stiprus — artimas pirminės cs- (-0.50) stiprumui. Ribinis, bet pagrįstas.
**Rekomendacija:** Priimti

### V3.4 Variantų svorių simetrija
**Įvertinimas:** 2/5
**Paaiškinimas:** A: cs-0.45. B: cs+0.55. C: cs-0.50. Du cs- variantai prieš vieną cs+. Tai yra V3.4 pažeidimas — Protocol reikalauja bent vieno X+ ir vieno X-. Techniškai įvykdyta (B yra cs+), bet santykis 2:1 sukuria skersvėją.
**Rastos problemos:** Skersvėjas cs- kryptimi. Bibliotekoje šis stimulas bus linkęs generuoti cs- signalus nepriklausomai nuo tikros žiūrovo reakcijos.
**Rekomendacija:** Perrašyti vieną cs- variantą į neutralesnį arba cs+.

---

## Daugiateorinė validacija (V4)

### Teorija 1: Dual Process Theory
**Įvertinimas:** Abejoja
**Paaiškinimas:** A variantas ("galimybė") reikalauja System 2 — sąvokinė interpretacija. B ir C yra System 1. A variantas pažeidžia momentinės reakcijos principą — tai patvirtina V2.1 problemą.

### Teorija 2: Cognitive Distortions (Beck/Burns)
**Įvertinimas:** Patvirtina
**Paaiškinimas:** B variantas ("nerimas — nežinau nuo ko pradėti") yra klasikinis "analysis paralysis" — kognityvinis iškraipymas dėl neapibrėžtumo. Stimulas teisingai matuoja cs konstruktą.

### Teorija 3: Self-Determination Theory (Deci/Ryan)
**Įvertinimas:** Patvirtina su pastaba
**Paaiškinimas:** Tuščias lapas aktyvuoja autonomijos dimensiją — ar žmogus jaučia laisvę (cs-) ar spaudimą (cs+). SDT patvirtina cs ašies tinkamumą. Pastaba: A variantas ("galimybė") per daug susietas su SDT autonomijos sąvoka — tai akademinė interpretacija, ne momentinė reakcija.

### Teoriniai prieštaravimai
**Ar yra:** Taip — Dual Process ir SDT abi identifikuoja A variantą kaip per sąvokinį.
**Rekomendacija:** Perrašyti A variantą — tai patvirtina V2.1 ir V2.2 problemas.

---

## Bibliotekos validacija (V5)

### V5.1 Dublikatai
**Ar yra panašių:** Taip — L07 (identiškas stimulas senoje bibliotekoje)
**Rekomendacija:** ST-003 pakeičia L07.

### V5.2 Ašių balansas
- aw: 2/3 (67%) — laikinas disbalansas, normalizuosis
- cs: 1/3 (33%) — pirmasis cs stimulas
- cr: 0/3 (0%)

**Rekomendacija:** Priimti — pirmasis cs stimulas, reikalingas.

### V5.3 Kontekstų įvairovė
**Kontekstas:** vidine_erdve
**Pastaba:** ST-001 taip pat vidine_erdve, bet ST-001 yra figūra, ST-003 yra objektas. Skirtingos situacijų klasės.
**Rekomendacija:** Priimti

---

## Empirinė validacija (V6)

*(Nepildyta — laukiama)*

### Stebėsenos punktai
- Ar A variantas renkamas statistiškai dažniau dėl pozityvumo šališkumo?
- Ar akademinio konteksto žmonės reaguoja kitaip?
- Ar cs- skersvėjas matomas rezultatuose?

---

## Galutinis vertinimas

| Kriterijus | Objektas | Svoris | Balas | Svertinis |
|---|---|---|---|---|
| V1.1 Neutralumas | IMAGE | 15% | 4/5 | 12 |
| V1.2 AI artefaktai | IMAGE | 10% | 5/5 | 10 |
| V1.3 Kultūrinis neutralumas | IMAGE | 10% | 5/5 | 10 |
| V1.4 Lyties/statuso neutralumas | IMAGE | 10% | 5/5 | 10 |
| V2.1 Reakcija, ne nuomonė | CHOICES | 15% | 3/5 | 9 |
| V2.2 Socialinis neutralumas | CHOICES | 15% | 3/5 | 9 |
| V3.1 Pirminė ašis | SIGNALS | 10% | 4/5 | 8 |
| V3.4 Svorių simetrija | SIGNALS | 10% | 2/5 | 4 |
| V4 Teorijų validacija | VISI | 5% | 3/5 | 3 |
| **VISO** | | **100%** | | **75/100** |

**Gautas balas: 75/100** ✓ (min 70)

**Sprendimas:** 🟡 Beta po pataisymo

**Reikalingi pataisymai (CHOICES):**
1. **A variantas** — perrašyti: pašalinti "galimybė", paversti momentine reakcija
2. **Svorių balansas** — po A perrašymo patikrinti V3.4

**IMAGE — puiki** (5/5 trijuose iš penkių kriterijų). Vaizdas nekeičiamas.

**Žymos:** `choices_rewrite_required` · `cs_skersvėjas_stebimas` · `replaces:L07`

---

## Bibliotekos įnašo suvestinė

- ✓ Pirmas cs ašies stimulas bibliotekoje
- ✓ Pirmas "objektas be žmonių" (ST-001 ir ST-002 turėjo figūras)
- ✓ Naujas kontekstų poklasis: abstraktus objektas → vidinė erdvė
- ⚠ CHOICES reikalauja perrašymo prieš beta

**Sprendimas:** 🟡 Beta po CHOICES pataisymo

---

*Review užpildyta pagal: `docs/methodology/stimulus_validation_protocol.md` v1.0.1*
