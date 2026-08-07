# ConflictLab P0 — Progress & Known Issues

**Data:** 2026-08-04
**Statusas:** Funkcionalumas veikia. Vizualinis layout nestabilus. Ruošiamas pilnas perrašymas.

---

## Kas veikia (patvirtinta debug JSON eksportais)

- ✅ Layer 1 — porų rodymas, pozicijos randomizacija, latency matavimas
- ✅ Layer 2 mikro-srautas — cue pasirinkimas → refleksija, susieta su konkrečiu vaizdu
- ✅ Visi 3 pasirinkti vaizdai eina per mikro-srautą (ne tik dalis, kaip senoje `l2_indices` logikoje)
- ✅ Cue duomenys teisingi — `pair-cue-v0.1.json` A/B priskyrimas patikrintas prieš realius vaizdo failus
- ✅ Rezultatų ekranas rodo VISĄ Layer 1 seką, ne tik reflektuotus vaizdus
- ✅ Sesijos vektorius skaičiuojamas (`computeSessionVector`), saugomas, bet niekur nerodomas vartotojui
- ✅ Audio integracija — toggle, loop, fade-out feedback/done ekranuose
- ✅ Feedback duomenys normalizuojami (`null` vietoj `undefined`)
- ✅ localStorage namespace atskirtas (`cl_pair_p0_*`), nekonfliktuoja su v0.7

## Žinomos problemos (neišspręstos)

- ❌ **Layout nestabilus tarp naršyklių.** Chrome mobile: footer mygtukas dažnai apkarpomas apačioje (nematomas arba dalinis). Mi Browser: matomas geriau, bet irgi apkarpytas. Priežastis: `100dvh` + naršyklės dinaminė adresų juosta skaičiuojama nenuosekliai skirtinguose naršyklėse.
- ❌ Per šią sesiją rasti ir taisyti (bet gali kartotis su naujais pakeitimais): `.footer-fixed` CSS trūko, `.action-btn` CSS trūko, CSS eiliškumo klaida tarp `#app` ir `body.has-debug #app`, cache (fetch be `?v=` cache-bust).

## Diagnozuota, bet nepatikrinta realiai

- Šio pokalbio Claude instancija **negali pasiekti `olemoz1977.github.io`** iš savo bash aplinkos (egress proxy blokuoja `host_not_allowed`). Visi vizualiniai patikrinimai remiasi tik vartotojo atsiųstais screenshot'ais ir debug JSON eksportais — ne tiesioginiu naršyklės testavimu.

## Duomenų struktūra (galutinė, teisinga)

```json
{
  "image_id": "P0-002-B",
  "response_type": "cue",
  "cue_id": "P0-002-B-C1",
  "cue_text": "Čia saugiau",
  "custom_words": null,
  "reflection_text": "",
  "vector": {"aw": 0.45, "cs": 0.2, "cr": 0.2}
}
```

`response_type` reikšmės: `cue` | `custom` | `hard_to_say`

## Failai

```
docs/experiments/pair-p0/
  index.html              ← perrašomas iš naujo
  pair-set.json           ← 3 aktyvios poros, teisingas turinys
  pair-cue-v0.1.json      ← 18 cue, A/B patikrinta prieš realius vaizdus
  lang.json               ← LT/EN, pilnas
  audio/open-window.mp3
  images/                 ← 6 vaizdai (3 poros)
  archive/
    index_v1_before_rewrite.html  ← veikiantis, bet layout-nestabilus variantas
```

## Kito perrašymo principai

1. Jokio `dvh`/`vh` eksperimentavimo — naudoti paprastą `flex` su `min-height` apsaugomis visur
2. Kiekvieną naują CSS klasę HTML'e — iš karto patikrinti, ar ji apibrėžta CSS (automatinis auditas prieš push)
3. Visi `fetch()` — su cache-bust nuo pat pradžių
4. Testuoti debug JSON eksportu po kiekvieno žingsnio, ne tik vizualiai


---

## 2026-08-07 — prototype-nine-v1 FLOW STABLE

**Commit:** `b3dcbf69201d55aa209b9d3a5470a6e067f9e2b2`
**Tag:** `pair-p0-prototype-nine-v1-flow-stable`

### Patvirtinta realiu eksportu

- 3×3 srautas: 3 sesijos × 3 poros = 9 unikalūs pasirinkimai
- SESSION provenance: `set_id`, `qa_mode`, `radar_mode`, `build_id`, `radar_unlocked`
- choices[] ir reflections[] provenance veikia
- `reviewed` (3) ir `prototype_only` (6) vektoriai atskiriami
- `radar_unlocked`: sesija 1→false, sesija 2→false, sesija 3→true ✅

### Fix šiame etape

`fix(pair-p0): persist radar unlocked state after third session`
— P9 blokas perkeltas prieš `completed_sessions` išsaugojimą `completeSession()` viduje.

### Laukia

- Manual QA: OQ-002 (prototipo vektorių skaičius radare su "Sunku pasakyti")
- Antras radaro blokas (sesijos 4–6)
- N0-010–018 porų kūrimas
