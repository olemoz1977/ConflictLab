# [ST-XXX] — Stimulus Review

**Stimulo ID:** ST-XXX
**Peržiūros data:** YYYY-MM-DD
**Recenzentas:** [vardas arba įrankis]
**Remtasi:** `docs/methodology/stimulus_validation_protocol.md` v1.0.1
**Statusas po peržiūros:** [draft | review | beta | approved | archived]

---

> ⚠ Šis review užpildomas tik pagal Validation Protocol.
> Protocol > Review. Jei prieštaravimas — taisomas Review.

---

## IMAGE — Vaizdo validacija (V1)

*Vertinamas tik vaizdas. Variantai ir signalai dar nevertinami.*

### V1.1 Neutralumas
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Peržiūrėti variantus]

### V1.2 AI artefaktai
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti]

### V1.3 Kultūrinis šališkumas
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Priimti su žyma]

### V1.4 Lyties / amžiaus / statuso signalai
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Priimti su žyma]

### V1.5 Neapibrėžtumo lygis
**Įvertinimas:** [< 20% | 20–70% | > 70%]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Peržiūrėti]

---

## CHOICES — Variantų validacija (V2)

*Vertinami tik trijų variantų tekstai. Signalai dar nevertinami.*

### V2.1 Reakcija, ne nuomonė
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Perrašyti variantus]

### V2.2 Socialiai pageidaujamas atsakymas
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Perrašyti variantus]

### V2.3 Moralinis pasirinkimas
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti]

### V2.4 Projekcija į vaizdą
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Perrašyti variantus]

### V2.5 Akivaizdžiai teisingas variantas
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Perrašyti variantus]

---

## SIGNALS — Signalų validacija (V3)

*Vertinami tik aw/cs/cr svoriai. Vaizdas ir tekstai jau įvertinti.*

### V3.1 Pirminė ašis
**Deklaruota ašis:** [aw | cs | cr]
**Įvertinimas:** [1–5]
**Paaiškinimas:**
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Koreguoti svorius]

### V3.2 aw/cs/cr diferenciacija
**Įvertinimas:** [1–5]
**Paaiškinimas:** *(ar aw- ≠ cr-, ar ašys nesupainiotos)*
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Koreguoti]

### V3.3 Mišrūs signalai
**Ar yra mišrūs signalai:** [Taip | Ne]
**Paaiškinimas:** *(jei taip — ar pagrįsti, ar dokumentuoti yaml)*
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Dokumentuoti pagrindimą]

### V3.4 Variantų svorių simetrija
**Įvertinimas:** [1–5]
**Paaiškinimas:** *(ar yra X+ ir X- variantai pirminei ašiai)*
**Rastos problemos:**
**Rekomendacija:** [Priimti | Atmesti | Koreguoti svorius]

---

## Daugiateorinė validacija (V4)

*Vertinami IMAGE + CHOICES + SIGNALS kartu per teorijų lęšius.*
*Teorijos validuoja stimulą — ne žmogų.*

### Teorija 1: [pavadinimas]
**Validacijos klausimas:**
**Įvertinimas:** [Patvirtina | Abejoja | Prieštarauja]
**Paaiškinimas:**

### Teorija 2: [pavadinimas]
**Validacijos klausimas:**
**Įvertinimas:** [Patvirtina | Abejoja | Prieštarauja]
**Paaiškinimas:**

### Teorija 3: [pavadinimas]
**Validacijos klausimas:**
**Įvertinimas:** [Patvirtina | Abejoja | Prieštarauja]
**Paaiškinimas:**

### Teoriniai prieštaravimai
**Ar yra:** [Taip | Ne]
**Aprašymas:**
**Rekomendacija:** [Priimti su žyma | Atmesti | Peržiūrėti]

---

## Bibliotekos validacija (V5)

### V5.1 Dublikatai
**Ar yra panašių stimulų:** [Taip | Ne]
**Kurie:**
**Ar konstruktai skiriasi:** [Taip | Ne]
**Rekomendacija:** [Priimti | Atmesti | Priimti su diferenciacija]

### V5.2 Ašių balansas po pridėjimo
- aw stimulai: X/N (X%)
- cs stimulai: X/N (X%)
- cr stimulai: X/N (X%)

**Ar laikomasi 25–40% ribų:** [Taip | Ne]
**Rekomendacija:** [Priimti | Atidėti]

### V5.3 Kontekstų įvairovė
**Stimulo kontekstas:** [darbo_aplinka | tarpasmeniniai | vidine_erdve | gamta | technologinis]
**Ar per daug reprezentuotas:** [Taip | Ne]
**Rekomendacija:** [Priimti | Atidėti]

---

## Empirinė validacija (V6)

*(Pildoma po testavimo su realiais žmonėmis)*

### Beta (5–10 žmonių)
**Data:**
**Variantų pasiskirstymas:** A: X% | B: X% | C: X%
**Vidutinis reakcijos laikas:** X sek.
**Rastos problemos:**

### Pilotinis (30–50 žmonių)
**Data:**
**Variantų pasiskirstymas:** A: X% | B: X% | C: X%
**Rezonansas:** X%
**Rastos problemos:**

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
| V1.1 Neutralumas | IMAGE | 15% | /5 | |
| V1.2 AI artefaktai | IMAGE | 10% | /5 | |
| V1.3 Kultūrinis neutralumas | IMAGE | 10% | /5 | |
| V1.4 Lyties/statuso neutralumas | IMAGE | 10% | /5 | |
| V2.1 Reakcija, ne nuomonė | CHOICES | 15% | /5 | |
| V2.2 Socialinis neutralumas | CHOICES | 15% | /5 | |
| V3.1 Pirminė ašis | SIGNALS | 10% | /5 | |
| V3.4 Svorių simetrija | SIGNALS | 10% | /5 | |
| V4 Teorijų validacija | VISI | 5% | /5 | |
| **VISO** | | **100%** | | **/100** |

**Minimalus balas: 70/100**
**Gautas balas:**
**Sprendimas:** [Priimti | Atmesti | Grąžinti perrašymui]
**Žymos:**

---

*Review užpildyta pagal: `docs/methodology/stimulus_validation_protocol.md` v1.0.1*
