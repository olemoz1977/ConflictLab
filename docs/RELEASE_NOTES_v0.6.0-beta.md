# ConflictLab v0.6.0-beta — Release Notes

**Data:** 2026-07-30
**Versija:** v0.6.0-beta
**Tikslas:** Pirmųjų realių testuotojų bandymai

---

## Įgyvendinta

### ConflictLab Voice
Visas UI perrašytas pagal `conflictlab_voice_v1.md`:
- Intro: "Pamatysi keletą vaizdų. Po kiekvieno — pasirink pirmą mintį. Ne teisingą."
- Loading: tik spinner, jokio teksto
- Reflection: "Pasirodė" / "Ko sesija nematė" — ne algoritmo kalba
- Feedback: "Ar tai atspindi ką nors tikro?" / "Taip, kažką palietė" / "Ne, čia kitaip"
- Nesutarimas: "Šį kartą mūsų matymas nesutapo."
- Pabaiga: "Kita sesija gali atskleisti kažką kito."

### Skaičiai pašalinti
Reflection ekrane daugiau nėra `aw=-0.09 cs=-0.18 cr=-0.01`.
Vietoje jų — taškas ant linijos: kryptis be skaičių.
Istorija rodo žodžius: "artėjimo · aiškumo · neutrali" — ne skaičius.

### alert() pašalinti
Visi `alert()` pakeisti į UI ekranus.
Sesijų skaičius rodomas be pertraukos sesijoje.

### Stimulų biblioteka išvalyta
Pašalinta iš aktyvaus naudojimo:
- L06 — pokalbio ekranas su tekstu (AI artefaktai)
- L08 — knygelė su tekstu (AI artefaktai)
Failai palikti, bet nenaudojami.

### Choice tekstai
Perrašyti pagal Voice principą — spontaniška mintis, ne etiketė:
- "Artumas — kažkas sprendžiasi" → "Kažkas čia vyksta"
- "Galimybė — rašyti bet ką" → "Iš karto pagalvojau ką čia galėčiau daryti"
- "Tyla — nieko nereikia" → "Nieko nekyla"
- "Darbas — viskas tvarkoje" → "Darbas — viskas gerai"

### Claude API prompt
Perrašytas pagal Voice principus:
- DRAUDŽIAMA sąrašas įtrauktas tiesiai į promptą
- Subjektas = žmogaus dėmesys, ne sistema
- Tono reikalavimas: ramus, smalsus, kuklus

---

## Sąmoningai neįgyvendinta

**Naujų stimulų:** bibliotekos auditas baigtas, bet naujų stimulų (konfliktas, praradimas, gamta) nekuriama prieš pirmuosius testuotojus.

**Theory Context UI:** teorijų rodimas vartotojui nukeltas į V2.

**Backend/server:** localStorage pakanka pirmiesiems 50-100 vartotojams.

**GDPR eksportas:** V2.

**Pattern po kiekvienos sesijos:** sistema rodo dėsningumą tik po 3 sesijų — sąmoningas sprendimas.

---

## Žinomi apribojimai

**Biblioteka per maža adaptyvumui.** 9 aktyvūs stimulai — per mažai kad adaptyvus pasirinkimas būtų tikrai jautrus. Po 3 sesijų sistema gali naudoti tuos pačius stimulus.

**cs ašis nepakankamai reprezentuota.** 2 iš 9 stimulų (22%) — teorinis optimumas 33%.

**ST-001 ir ST-006 panašūs.** Abu aw- su vienu žmogumi. Gali sukelti monotoniją.

**Micro-pause neišmatuotas empiriškai.** Reakcijos laikas saugomas localStorage, bet dar neanalizuotas.

**GitHub Pages API key.** Anthropic API kviečiamas tiesiai iš naršyklės — tinka demo, ne produkcijai.

---

## Rekomendacija

**Ar ši versija tinkama pirmiesiems 10-15 testuotojams?**

**Taip.**

Argumentai:
1. Žmogus daugiau galvos apie save, ne apie sistemą — skaičiai pašalinti
2. Voice principai įgyvendinti visame kelyje
3. Stimulų biblioteka pakankama pirmai bangai
4. Grįžtamojo ryšio mechanizmas veikia

**Ką stebėti pirmos bangos metu:**
- Ar žmogus po sesijos pasakys "kažką palietė" ar "įdomūs skaičiai"?
- Ar kas nors grįžta antrai sesijai?
- Kur reakcijos laikas ilgas (>10s) — tai micro-pause arba sumaišties ženklas
- Ką žmonės rašo "Ne, čia kitaip" laukelyje

**Testuotojų instrukcija:** `docs/tester_instructions.md`

---

*ConflictLab v0.6.0-beta*
*"Ar po šių pakeitimų žmogus daugiau galvos apie save, ar apie sistemą?"*
*Atsakymas: apie save.*
