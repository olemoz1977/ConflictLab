# ConflictLab — Stimulus Cue Writing Rules v1.0

**Data:** 2026-07-31
**Statusas:** Užšaldyta — taikoma visai bibliotekai
**Priklauso:** Stimulus Validation Protocol v1.0.1

> Šios taisyklės užtikrina, kad Reflection Engine gauna
> švarų pirmosios reakcijos signalą — ne žmogaus interpretaciją.

---

## Kas yra attention cue

Attention cue yra trumpa frazė arba žodis, kuris:

- fiksuoja **pirmą spontanišką dėmesio kryptį**
- nekviečia kurti istorijos ar planavimo
- leidžia skirtingiems žmonėms pasirinkti jį **dėl skirtingų priežasčių**

Cue nėra pasirinkimo paaiškinimas. Jis yra **dėmesio objektas**.

---

## Keturi privalomi filtrai

### Filtras 1 — Ne interpretacija

Cue neturi pasakyti žmogui, **ką tai reiškia**.

```
❌ vienatvė       → jau pasakyta, ką žmogus jaučia
✓  būti vienam    → fiksuoja būseną be vertinimo

❌ tuštuma         → interpretacija
✓  tuščia erdvė   → fizinis faktas

❌ susitikimas     → išvada apie tai, kas vyksta
✓  artėjimas      → matomas procesas
```

### Filtras 2 — Ne emocija

Cue neturi apibūdinti **jausmo**.

```
❌ nerimas
❌ palengvėjimas
❌ smalsumas
✓  laukimas
✓  tyla
✓  žinutė
```

### Filtras 3 — Ne diagnozė, ne vertinimas

Cue neturi siūlyti **kokia reakcija yra teisinga**.

```
❌ viskas gerai
❌ norėjosi pabėgti
❌ per arti
✓  atstumas
✓  tvarka
✓  artėjimas
```

### Filtras 4 — Skirtingos prasmės skirtingiems žmonėms (svarbiausias)

**Cue testas:** Ar du skirtingi žmonės gali pasirinkti tą patį cue dėl visiškai skirtingų priežasčių?

Jei **taip** — cue geras. Reflection Engine turi darbo.
Jei **ne** — cue jau turi vieną aiškią reikšmę. Pakeisti.

```
✓  "artėjimas"
   Žmogus A: "Pagaliau ateina kažkas."
   Žmogus B: "Geriau pasitrauksiu."
   → Tas pats cue, skirtinga vidinė reakcija. GERAS.

❌ "vienatvė"
   Pasirinkus šį cue, žmogus jau beveik pasakė, ką galvojo.
   → Cue praranda prasmę. BLOGAS.

✓  "laukimas"
   Žmogus A: nerimastingas laukimas
   Žmogus B: ramus laukimas
   Žmogus C: erzinantis laukimas
   → Trys visiškai skirtingos reakcijos į tą patį cue. GERAS.
```

---

## Papildomi kriterijai

### Cue kyla iš vaizdo

Cue turi natūraliai kilti iš to, kas matoma — ne iš teorijos, ne iš SignalOrientation ašių.

```
Vaizdas: Telefonas ant stalo.
✓  žinutė      ← matomas objektas / kontekstas
✓  tyla        ← matoma/jaučiama situacija
✓  patikrinti  ← spontaniška reakcija į objektą
❌ kontrolė    ← SignalOrientation terminas, ne vaizdo elementas
```

### Cue negali kviesti planavimo

Cue turi fiksuoti **pirmą mintį** — ne **planą**.

```
❌ "ką daryti toliau"  → jau planuojama
✓  "patikrinti"        → spontaniška reakcija
✓  "žinutė"           → dėmesio objektas
```

### Cue negali kviesti kurti istorijos

Cue neturi kviesti fantazuoti kas vyko ar vyksta už kadro.

```
❌ "kas čia buvo"    → kuria pasakojimą
✓  "palikta vieta"  → fiksuoja tai, kas matoma
```

---

## Leistini cue tipai

| Tipas | Pavyzdys | Kodėl tinka |
|---|---|---|
| Fizinis objektas | žinutė, telefonas, langas | Konkretu, matoma |
| Fizinė savybė | tuščia erdvė, atstumas, tvarka | Aprašo, ne vertina |
| Matomas procesas | artėjimas, laukimas, judėjimas | Veiksmas be interpretacijos |
| Spontaniška veikla | patikrinti, pažiūrėti, pasitraukti | Reakcija, ne planas |
| Būsena/situacija | būti vienam, kas lauke, tyla | Fiksuoja momentą |

---

## Draudžiami cue tipai

| Tipas | Pavyzdys | Kodėl netinka |
|---|---|---|
| Emocija | nerimas, palengvėjimas, smalsumas | Jau interpretacija |
| Interpretacija | vienatvė, tuštuma, susitikimas | Žmogus jau padarė išvadą |
| Vertinimas | viskas gerai, per arti, blogai | Siūlo "teisingą" atsakymą |
| Planavimas | ką daryti, kaip elgtis | Ne pirma mintis |
| Pasakojimas | kas čia buvo, kas nutiko | Kviečia fantazuoti |
| Teorinis terminas | kontrolė, atsitraukimas, orientacija | Ne vaizdo kalba |

---

## Cue rašymo procesas

1. Žiūrėk į vaizdą — ne į SignalOrientation ašis
2. Surašyk 10 pirmų asociacijų
3. Pašalink visas, kurios pereina per interpretaciją
4. Iš likusių pasirink 3, kurios **gali turėti skirtingas prasmes**
5. Patikrink kiekvieną pagal 4 filtrus
6. Patikrink rinkinį: ar trijų cue nė vienas nėra socialiai "geresnis"?

---

## Sąsaja su Reflection Engine

Cue yra tik UI reprezentacija. Sistema mato `choice_id` su svoriais.

```
Vartotojas:  "artėjimas"
Sistema:     choice_id: L02_A → {aw:+0.50, cs:+0.20, cr:+0.15}
```

**Svarbu:** tas pats žodis skirtinguose stimuluose gali turėti visiškai skirtingus svorius. Cue nėra signalo pavadinimas.

---

## Bibliotekos taikymas

Šios taisyklės taikomos:
- Naujiems stimulams nuo 2026-07-31
- Esamų stimulų peržiūrai po beta etapo

Pirmi 5 stimulus (L01, L02, L05, L10, L12) atnaujinti pagal šias taisykles.
Likę 5 stimulus (L03, L04, L07, L09, L11) — peržiūrėti po pirmų beta sesijų.

---

*Stimulus Cue Writing Rules v1.0*
*ConflictLab — pirmoji reakcija, ne interpretacija*
