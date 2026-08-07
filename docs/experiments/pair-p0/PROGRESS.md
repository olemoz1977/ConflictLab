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


---

## 2026-08-08 — prototype-nine-v1 Radar UX STABLE

**Tag:** `pair-p0-prototype-nine-v1-radar-ux-stable`
**Head commit:** `ec6b7c0c6da8f3b4380bb0d4ec9b074b8e686e56`

### Šiame etape atlikta

- **Bipolar map** (commit `48bfcd25aa`): 6-spindulinis radaras P9 kelyje pakeistas į 3-ašių bipolarinį žemėlapį. Kiekviena iš 3 reikšmių → 1 signed taškas ant diametro → trikampė forma. Senas `renderRadarSVG()` (M0) nepakeistas.
- **Display calibration v1** (commit `d78fe6bbff`): įdiegtas `P9_DISPLAY_BOUND = 0.65`, `p9RawToDisplay()`. RAW reikšmės nepakeičiamos — transformacija tik SVG koordinatėms. Jokio pow(), MIN_VISIBLE_PX, per-axis scaling.
- **Attainable envelope audit** (commit `c39d6908b0`): `tests/pair_p0_attainable_envelope.py` — 9/9 envelope: AW ±0.372, CS [-0.294, +0.383], CR [-0.250, +0.333]. Visi assertions PASS.
- **Routing fix** (commit `ec6b7c0c6d`): radaras rodomas TIK po pilno 3-session bloko. Pašalinta `showP9RadarWithBlockProgress()` iš aktyvaus routing kelio. `hasUnlockedRadar()` nebebetriggerina radaro rodymo.
- **History routing fix** (commit `5a9fa707c4`): istorijos „View your current trace" mygtukas P9 kelyje perduodamas į `showP9BlockRadar()`.
- **UX copy** (keletas commit'ų): žmogaus kalba ašių pavadinimuose, automatiniai palyginimo sakiniai (7 atvejų logika), refleksijos klausimai.

### QA rezultatai

P9 sesijų 1→6 manual phone QA = **PASS**

- Session 1–2: progress ekranai, jokio radaro ✅
- Session 3: Radar 1 (bipolar map, Block 1) ✅
- Session 4–5: progress „X iš 3 iki kito palyginimo", jokio radaro ✅
- Session 6: Radar 2 + overlay (Block 1 pilkas + Block 2 žalias) + comparison ✅
- Comparison: warning, badge, 3 automatiniai sakiniai, refleksija, boundary ✅

### Laukia

- N0-010–018 naujų porų kūrimas (18 unikalių porų tikslas)
- N0-004–009 metodologiniai trūkumai
- prototype-nine-v2 planavimas
