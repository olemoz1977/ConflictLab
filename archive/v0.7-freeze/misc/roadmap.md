# ConflictLab Roadmap

> **Tikslas nėra kuo greičiau sukurti produktą.**
>
> **Tikslas – sukurti patikimą savirefleksijos platformą, kuri auga kartu su mokslo žiniomis ir vartotojų patirtimi.**

---

# 1 etapas – Projekto pamatai ✅

Tikslas:

Sukurti aiškią projekto filosofiją.

Rezultatas:

- README
- Manifestas
- Principles
- Roadmap
- GitHub struktūra

Statusas:

🟢 Vykdoma

---

# 2 etapas – Žinių bazė

Tikslas:

Sukurti mokslinį projekto pagrindą.

Veiksmai:

- surinkti psichologines teorijas;
- išanalizuoti jų stiprybes ir ribas;
- aprašyti jų pritaikymą ConflictLab.

Rezultatas:

/theories katalogas.

Statusas:

🟢 Vykdoma


---

# 3 etapas – Hipotezių biblioteka

Tikslas:

Atskirti tai, ką žinome, nuo to, ką dar tik norime patikrinti.

Veiksmai:

- sukurti H001, H002...
- aprašyti kiekvieną hipotezę;
- numatyti, kaip ji bus tikrinama.

Rezultatas:

/hypotheses katalogas.

Statusas:

🟢 Vykdoma


---

# 4 etapas – Reakcijų modelis

Tikslas:

Sukurti bendrą žmogaus reakcijos modelį.

Galimi elementai:

- stimulas;
- emocija;
- mintis;
- impulsas;
- elgesys;
- pasekmė;
- savirefleksija.

Rezultatas:

Pirmasis ConflictLab modelis.

Statusas:
🟢 Vykdoma

---

# 5 etapas – Stimulų biblioteka (multimodalinė)

> ⚙️ Atnaujinta pagal V2 architektūrą (žr. `README.md`, `docs/manifesto.md`).

Tikslas:

Sukurti multimodalinių mikro-stimulų katalogą (/stimuli), skirtą fiksuoti spontaniškas reakcijas, o ne tekstinius aprašymus.

Formos:

- vizualiniai trigeriai (`stimuli/visual_patterns.md`);
- audio / pseudokalbos intonacijos (`stimuli/audio_intonations.md`);
- greiti mikro-scenarijai (`stimuli/micro_scenarios.md`).

Kiekvienas stimulas turi būti susietas su konkrečia hipoteze (`/hypotheses`), kurią jis padeda patikrinti.

Rezultatas:

Pirmoji multimodalinių stimulų duomenų bazė.

Statusas:

⚪ Nepradėta

---

# 6 etapas – Suvokimo ir Adaptyvusis sluoksniai

Tikslas:

Įgyvendinti `/perception` (mikro-reakcijų fiksavimas: latency, pasirinkimo vektorius) ir `/adaptive` (kito stimulo parinkimas pagal Confidence Score) modulius, aprašytus `engine/analysis_pipeline.md`.

Veiksmai:

- detalizuoti `perception/feature_extraction.md` ir `adaptive/stimulus_selector.md` (šiuo metu juodraščiai);
- pagrįsti arba empiriškai patikrinti latency ir Confidence Score slenksčius (žr. `research/experiments.md`);
- apibrėžti duomenų schemą tarp sluoksnių.

Statusas:

⚪ Nepradėta

---

# 7 etapas – MVP

Tikslas:

Sukurti pirmą veikiančią ConflictLab versiją pagal V2 architektūrą.

Galimos funkcijos:

- multimodalinio stimulo pateikimas ir atsako fiksavimas;
- adaptyvus hipotezės tikrinimo ciklas (trianguliacija per 3 medijos formas);
- veidrodinė įžvalga (be etikečių, be diagnozės) vartotojui.

Rezultatas:

Veikiantis prototipas.

Statusas:

⚪ Nepradėta

---

# 8 etapas – Eksperimentiniai moduliai

Galimos kryptys:

- DI pokalbiai / dinaminis interviu;
- balso emocijų atpažinimas;
- ilgalaikio dėsningumų sekimo (longitudinal) ataskaitos.

Visi moduliai kuriami tik po teorinio pagrindimo.

---

# 9 etapas – Tyrimai

Tikslas:

Patikrinti projekto hipotezes naudojant anoniminius duomenis.

Galimos veiklos:

- statistinė analizė;
- vartotojų grįžtamasis ryšys;
- hipotezių tikrinimas;
- modelio tobulinimas.

---

# Pagrindinis kūrimo principas

ConflictLab vystomas tokia tvarka:

Idėja

↓

Hipotezė

↓

Teorinis pagrindas

↓

Architektūra

↓

Programavimas

↓

Testavimas

↓

Vertinimas

↓

Tobulinimas

---

# Projekto vizija

ConflictLab nėra vienkartinis testas.

Tai ilgalaikė savirefleksijos platforma, kuri padeda žmonėms geriau suprasti savo emocinių reakcijų dėsningumus ir sąmoningiau kurti santykius su kitais bei savimi.

---

> **Kiekvienas etapas turi palikti projektą aiškesnį nei jis buvo prieš tai.**
