# ConflictLab Product Experience Audit v1.0

**Data:** 2026-07-30
**Paskirtis:** Produkto patirties auditas — ne kodo, o žmogaus kelio auditas.
**Klausimas:** Ar žmogus po eksperimento jaučiasi, kad geriau suprato save?

---

## 1. Vartotojo kelio auditas

### Pilnas kelias

```
INTRO → STIMULUS (×4) → LOADING → REFLECTION → FEEDBACK → THANKS/PATTERN
```

### Kur žmogus tampa testo dalyviu

**Intro ekranas:**
> "Sistema renka signalus ir po 3 sesijų parodo pastebėtą trajektoriją."

Problema: žodis "sistema renka signalus" iš karto sukuria stebėjimo jausmą.
Žmogus pradeda galvoti: *"ką sistema apie mane sužinos?"* — tai yra testo dalyvio mentalitetas.

**Stimulo klausimas:** nėra — tai GERAI. Vaizdas rodomas be klausimo.

**Pasirinkimų mygtukas:** "Toliau" po pasirinkimo — tai GERAI. Suteikia pauzę.

**Loading:** "Analizuojama trajektorija..." — PROBLEMA. Žodis "analizuojama" sukuria jausmą kad kažkas tave analizuoja.

### Kur žmogus spėlioja teisingą atsakymą

**Choices tekstai** — mišri kokybė. Kai kurie variantai vis dar skamba kaip "teisingesni":
- "Ar atsakė?" — natūralus
- "Telefonas nutylęs — ir gerai" — skamba kaip "suaugęs" atsakymas
- Žmogus jaučia: B yra "geriau kontroliuojantis" atsakymas

**Reflection ekranas** — tai yra KRITINĖ VIETA kur refleksija sustoja:
Žmogus mato skaičius `aw=-0.09` ir pradeda galvoti apie skaičius, ne apie save.

### Kur žmogus nustoja reflektuoti

**Iš karto po skaičių** — žmogus pereina į analitinį režimą:
*"Kas tas aw? Kodėl -0.09? Ar tai gerai ar blogai?"*

Tai yra tiksliai priešinga refleksijai.

---

## 2. Reflection ekrano auditas

### Dabartinė struktūra

```
[Ašių juostos] aw=-0.09 | cs=-0.18 | cr=-0.01
[Pastebėta trajektorija] — tekstas
[Ko sistema negali žinoti] — tekstas
[Refleksinis klausimas] — tekstas
[Atpažįstu / Nepanašu]
```

### Ar žmogui reikia matyti aw=-0.09?

**Ne.**

Argumentai:

1. Žmogus nežino ką reiškia aw skalė. -0.09 yra beveik nulis — bet jis to nežino. Gali interpretuoti kaip "atsitraukimas" kai iš tikrųjų tai "neutralu".

2. Skaičiai aktyvuoja analitinį mąstymą. Tai priešinga refleksijos tikslui.

3. Vizualinės juostos suteikia informacijos — bet ta informacija yra sistemos kalba, ne žmogaus kalba.

4. Jei juosta rodo "0.09 artėjimo kryptimi" — ką žmogus su tuo daro? Nieko. Jis neturi konteksto.

**Kas galėtų būti vietoje skaičių:**

Variantas A — tik kryptis, be skaičių:
```
Šios sesijos reakcijų kryptis:
→ Artėjimo pusė (silpnas signalas)
→ Aiškumo siekimo pusė (vidutinis signalas)
→ Neutralu
```

Variantas B — visai be ašių, tik klausimas:
Ašys lieka sistemoje (localStorage), bet vartotojas jų nemato.
Žmogus gauna tik refleksinio klausimo tekstą.

Variantas C — metafora vietoj skaičių:
```
Šioje sesijoje tavo dėmesys krypo link aiškumo —
situacijos, kuriose reikia žinoti kas vyksta.
```

---

## 3. Sistemos ir žmogaus atskyrimas

### Kas skirta sistemai (žmogui NEREIKIA matyti)

- aw/cs/cr reikšmės kaip skaičiai
- "Signalų kryptys šioje sesijoje" antraštė
- Ašių juostos su decimal reikšmėmis
- localStorage sesijų istorija su skaičiais (hist-axes span)
- "Sesija X išsaugota. Dar Y sesijų iki dėsningumo" — alert()

### Kas skirta žmogui (PALIKTI arba PAGERINTI)

- Stimulo vaizdas — palikti
- Pasirinkimų mygtukai — palikti, galbūt retoriškai patobulinti
- "Pastebėta trajektorija" tekstas — palikti bet tobulinti
- "Ko sistema negali žinoti" — palikti, tai svarbu
- Refleksinis klausimas — tai yra branduolys, PALIKTI
- "Atpažįstu / Nepanašu" — palikti

### Kas turi būti pašalinta arba paslėpta

- Skaičiai prie ašių (`ax-aw-v`, `ax-cs-v`, `ax-cr-v`)
- Ašių juostos kaip vizualinis elementas (arba supaprastinti iki tik krypties)
- `alert()` tarp sesijų — tai laužo patirtį
- Istorija su aw/cs/cr skaičiais intro ekrane

---

## 4. Choice auditas

### Problema: kas skamba kaip AI, ne kaip žmogus

| Stimulas | Variantas | Problema | Siūlymas |
|---|---|---|---|
| Telefonas | "Telefonas nutylęs — ir gerai" | "ir gerai" — per racionalizuotas | "Nieko — tai normalu" |
| Tuščia salė | "Tuoj prasidės — reikia pasiruošti" | "reikia" — pareigos jausmas | "Pagalvojau kas čia bus" |
| Durys | "Pagalvojau ar eiti ar likti" | geras, palikti | — |
| Kompiuteris | "Darbas — viskas tvarkoje" | antraštė, ne mintis | "Viskas gerai" |
| Figūros | "Artumas — kažkas sprendžiasi" | abstrakcija | "Kažkas vyksta" |

### Sisteminis pattern

Dažnai variantai yra: **[žodis] — [interpretacija]**
Pvz: "Artumas — kažkas sprendžiasi"

Tai yra AI struktūra. Realus žmogus taip negalvoja.
Realus žmogus galvoja vienu vientu sakiniu ar daline fraze.

**Taisyklė:** Jei variante yra brūkšnelis su dviem dalimis — tai yra ženklas kad reikia perrašyti.

---

## 5. Stimulų su tekstu auditas

### Dabartinė biblioteka UI (`docs/index.html`)

Peržiūrėjus LIB masyvą kode:

```javascript
{id:'L06',src:'media/p3_chat_screen.png'...}  // Pokalbio ekranas su tekstu
{id:'L08',src:'media/v2_p3_notebook.png'...}   // Knygelė su tekstu
```

Abu **vis dar aktyvūs** bibliotekoje. Jūsų instrukcija buvo juos nevertinti/neįtraukti.

**Problema:** Abu turi AI pseudotekstą (V1.2 — AI artefaktai, 0/5).

**Rekomendacija:** Pašalinti iš aktyvios LIB masyvo. Palikti failus, bet nebenaudoti.

---

## 6. Trys produkto kryptys

### Po viso eksperimento žmogus išeina su viena mintimi. Kokia?

---

**Kryptis A — "Veidrodis"**

> Žmogus išeina su vienu klausimu kuris jį seka dienos metu.

Produkto logika: ConflictLab nėra testas. Jis yra rytinio kavos puodukas su vienu klausimu. Trumpa. Intymi. Kasdienė.

Refleksija: vienas klausimas. Jokių skaičių. Jokio dėsningumo. Tik: *"Šiandien tavo dėmesys sustojo čia — kodėl?"*

Trūkumas: prarandamas sesijų kaupimo mechanizmas.

---

**Kryptis B — "Trajektorija"**

> Žmogus išeina su pastebėjimu apie savo reakcijų kryptį per laiką.

Produkto logika: ConflictLab yra dienoraštis be žodžių. Po 5-10 sesijų žmogus mato dėsningumą kurį pats anksčiau nepastebėdavo.

Refleksija: *"3 iš 4 kartų tavo dėmesys krypo ten kur yra neapibrėžtumas. Ar tai sutampa su tuo ką žinai apie save?"*

Trūkumas: reikia kantrybės. Pirma sesija nieko neduoda.

---

**Kryptis C — "Momentas"**

> Žmogus išeina su vienu atpažinimu apie konkretų šios dienos momentą.

Produkto logika: ConflictLab naudojamas tada kai kažkas nutiko. Ne kasdien — o tada kai žmogus jau jaučia kad kažkas vyksta viduje ir nori tai suprasti.

Refleksija: *"Šiandien tau buvo sunku dėl kažko. Ką pastebėjai žiūrėdamas į šiuos vaizdus?"*

Trūkumas: reikia situacijos konteksto iš vartotojo.

---

## Suvestinė

### Pašalinti dabar

| Elementas | Kodėl |
|---|---|
| aw/cs/cr skaičiai refleksijoje | Aktyvuoja analitinį mąstymą |
| `alert()` tarp sesijų | Laužo patirtį |
| L06 (pokalbio ekranas) iš LIB | AI artefaktai |
| L08 (knygelė) iš LIB | AI artefaktai |
| Istorija su skaičiais intro ekrane | Žmogui nereiškia nieko |

### Supaprastinti

| Elementas | Kaip |
|---|---|
| Ašių juostos | Tik kryptis (↑ artėjimas, ↓ atsitraukimas) — be skaičių |
| "Analizuojama trajektorija..." | → "Apmąstoma..." arba tiesiog spinner be teksto |
| Choices su brūkšneliu | Perrašyti kaip vieną frazę |
| Sesijų istorija | Paslėpti — tik sesijų skaičius, ne aw/cs/cr |

### Palikti

| Elementas | Kodėl |
|---|---|
| Stimulo vaizdas be klausimo | Veikia |
| "Ko sistema negali žinoti" | Epistemiškai svarbu |
| Refleksinis klausimas | Tai yra produkto branduolys |
| "Atpažįstu / Nepanašu" | Grįžtamasis ryšys |
| Sesijų kaupimas localStorage | Reikalingas trajektorijai |

### Rekomendacija dėl krypties

**Pradėti nuo A (Veidrodis)** — vienas klausimas, jokių skaičių.
Empiriškai patikrinti ar žmogus *"sustoja"*.
Jei taip — tada B (Trajektorija) yra natūralus sekantis žingsnis.
C (Momentas) yra ilgesnė kryptis — gali būti v2.

---

*ConflictLab Product Experience Audit v1.0*
*2026-07-30 — auditas prieš pirmuosius realius testuotojus*
