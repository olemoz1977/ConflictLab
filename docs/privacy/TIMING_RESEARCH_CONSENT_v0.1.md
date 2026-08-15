# ConflictLab — Timing Research Consent v0.1

**Date:** 2026-08-15  
**Status:** DRAFT ALIGNED WITH LIVE TECHNICAL FLOW / NOT AUTHORIZED FOR EXTERNAL CALIBRATION YET  
**Purpose:** explicit opt-in consent for the first external mechanical timing / UX calibration study.

---

# LT — dalyvio sutikimo tekstas

## Trumpa informacija prieš pasirinkimą

ConflictLab šiuo etapu tikrina tik techninę sąsajos mechaniką: ar trijų nuoseklių vaizdų porų bloką galima patikimai atlikti per nustatytą laiko biudžetą.

Šis tyrimas **nevertina jūsų asmenybės, psichologinių savybių, tinkamumo darbui ar sveikatos**.

Jei sutinkate dalyvauti, į tyrimų serverį bus perduodami tik minimalūs pseudoniminiai techniniai duomenys: atsitiktinis sesijos ID, protokolo/formos informacija, pateikimo eilė/pozicija, reakcijos laikas, timeout/missingness, retry/page-hidden diagnostika, apibendrinta įrenginio kategorija ir techninės būsenos informacija.

Į tyrimų DB nebus siunčiami jūsų vardas, el. paštas, darbdavys, gimimo data, atviras refleksijos tekstas, pasirinkimo priežasčių tekstai, intensyvumo įverčiai ar psichologinis rezultatas.

Duomenų valdytojas: **Oleg Mozochin**  
Kontaktas: **info@omesg360.eu**

Pseudoniminiai timing tyrimo įvykiai aktyvioje tyrimo DB planuojami saugoti ne ilgiau kaip **90 dienų**, nebent jie būtų ištrinti anksčiau. Hostinger atsarginėse kopijose likutinė kopija gali išlikti iki įprastos backup rotacijos, kaip paaiškinta pilname privatumo pranešime.

Dalyvavimas yra savanoriškas. Sutikimą dėl būsimo sutikimu grindžiamo tvarkymo galite atšaukti.

Jei pasirenkate dalyvauti, **prieš pagrindinį timing bloką** jūsų naršyklė sugeneruoja atsitiktinį 32 simbolių duomenų ištrynimo kodą. Kodas parodomas jums ir, jei vietinis naršyklės saugojimas prieinamas, išsaugomas tik tame įrenginyje kaip ištrynimo / atšaukimo patogumo priemonė. Šis plaintext kodas nėra siunčiamas į tyrimo DB; sėkmingo upload atveju serveris saugo tik jo SHA-256 hash.

Kodu galima pasinaudoti per savitarnos ištrynimo puslapį arba pateikti jį el. paštu `info@omesg360.eu`. Jei vietinis saugojimas neprieinamas, kodą reikia išsisaugoti pačiam prieš tęsiant.

Pilną informaciją pateikia `Timing Research Privacy Notice v0.3`.

### Dalyvio veiksmai

```text
[ ] Patvirtinu, kad man yra 18 metų arba daugiau.

[ ] Perskaičiau informaciją ir SAVANORIŠKAI SUTINKU,
    kad aukščiau aprašyti pseudoniminiai techniniai duomenys
    būtų naudojami ConflictLab timing/UX mechanikos tyrimui.
```

Primary action:

```text
Sutinku ir dalyvauju timing tyrime
```

Alternative action:

```text
Tęsti be tyrimo duomenų įkėlimo
```

Rules:
- boxes are empty by default;
- consent is not bundled with general site terms;
- no countdown, visual coercion or guilt language around refusal;
- the research upload must not begin before affirmative consent;
- deletion-code local storage must not occur before affirmative research opt-in;
- local deletion-code storage is not a research-data channel and must not be uploaded/exported/analyzed;
- store the exact consent version/state with the research run;
- refusal must not be encoded as a psychological result.

---

# EN — participant consent copy

## Short information before you decide

At this stage ConflictLab tests only the technical interaction mechanics: whether a three-pair rapid-choice block can be completed reliably within the defined time budget.

This study **does not assess your personality, psychological traits, employment suitability, or health**.

If you agree to participate, only minimal pseudonymous technical data will be uploaded to the research server: a random session ID, protocol/form information, presentation order/position, response timing, timeout/missingness, retry/page-hidden diagnostics, coarse device category, and technical status information.

The research database will not receive your name, email address, employer, date of birth, open reflection text, reason text, intensity ratings, or a psychological result.

Data controller: **Oleg Mozochin**  
Contact: **info@omesg360.eu**

Pseudonymous timing-study event data are planned to remain in the active research database for no more than **90 days**, unless deleted earlier. Residual copies may remain in Hostinger backups until normal backup rotation, as described in the full privacy notice.

Participation is voluntary. You may withdraw consent for future consent-based processing.

If you choose to participate, **before the main timing block** your browser creates a random 32-character deletion code. The code is shown to you and, where browser local storage is available, is stored only on that device as a withdrawal/deletion convenience. The plaintext code is not sent to the research database; after a successful upload the server stores only its SHA-256 hash.

The code can be used through the self-service deletion page or provided by email to `info@omesg360.eu`. If local storage is unavailable, you should save the code yourself before continuing.

Full information is provided in `Timing Research Privacy Notice v0.3`.

### Participant actions

```text
[ ] I confirm that I am 18 years old or older.

[ ] I have read the information and I VOLUNTARILY CONSENT
    to the pseudonymous technical data described above being used
    for ConflictLab timing/UX mechanics research.
```

Primary action:

```text
I consent and participate in timing research
```

Alternative action:

```text
Continue without research upload
```

Rules:
- checkboxes are unticked by default;
- consent is separate from general terms;
- no countdown, visual coercion, or guilt language around refusal;
- research upload starts only after affirmative consent;
- deletion-code local storage must not occur before affirmative research opt-in;
- local deletion-code storage is not a research-data channel and must not be uploaded/exported/analyzed;
- store exact consent version/state with the run;
- refusal is never encoded as a psychological result.

---

## Release blockers

This participant copy is not authorized for external CALIBRATION collection until:

```text
Privacy Notice v0.3 is frozen and reflected in live /privacy.html
Hostinger processor/transfer review is closed
technical/security LIA is complete
withdrawal/deletion code works end-to-end
90-day retention control is operational
exact research payload is verified
final LT/EN + local-only smoke checks pass
activation record is created
owner explicitly authorizes CALIBRATION
```
