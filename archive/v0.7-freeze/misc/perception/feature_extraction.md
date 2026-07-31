# Perception Layer — Feature Extraction

**Statusas:** 🟡 Juodraštis / TODO (nurodytas `engine/analysis_pipeline.md` Etapuose 1–2, bet dar neaprašytas detaliai)

**Paskirtis:** Priimti žalią vartotojo atsaką į `/stimuli` stimulą ir paversti jį struktūrizuotu, objektyviu duomenų vektoriumi — dar be jokios interpretacijos ar teorijos taikymo (žr. `docs/principles.md`, I principas — griežtas Stebėjimo/Hipotezės/Išvados atskyrimas).

## Įvestis
- Stimulo ID ir tipas (vizualinis / audio / mikro-scenarijus), žr. `/stimuli`.
- Vartotojo pasirinkimas / veiksmas.
- Laiko žyma nuo stimulo parodymo iki atsako (raw timestamp).

## Numatomos funkcijos (reikia detalizuoti)
1. **Latency skaičiavimas** — Δt tarp stimulo ir atsako, pagal `docs/principles.md` II principą (< 1.5s / > 4.0s slenksčiai).
   - ⚠️ TODO: šie slenksčiai šiuo metu nėra pagrįsti jokiu eksperimentu `/research/experiments.md` faile — žr. pastabą ten.
2. **Pasirinkimo vektoriaus normalizavimas** — atsako suvedimas į standartizuotą kategoriją (kova / bėgimas / sustingimas / kontrolė / atsitraukimas).
3. **Duomenų perdavimas** į `/hypotheses` sluoksnį tolimesniam dėsningumų (pattern) skaičiavimui.

## Kas dar neapibrėžta
- Tiksli duomenų schema (JSON contract) tarp `/stimuli` → `/perception` → `/hypotheses`.
- Kaip elgiamasi su triukšmingais / dviprasmiškais atsakymais (pvz., vartotojas nepaspaudė nieko per numatytą laiką).
- Ar latency matuojamas kliento (browser/app), ar serverio pusėje — turi įtakos tikslumui.

---
*Šis failas sukurtas kaip struktūrinė vieta, kad `engine/analysis_pipeline.md` nuorodos neliktų "kabančios". Turinys turi būti išplėtotas prieš pradedant programavimą (žr. `docs/principles.md`, "Kūrimo taisyklė").*
