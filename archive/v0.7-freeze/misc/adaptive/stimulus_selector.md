# Adaptive Loop — Stimulus Selector

**Statusas:** 🟡 Juodraštis / TODO (nurodytas `engine/analysis_pipeline.md` Etape 3, bet dar neaprašytas detaliai)

**Paskirtis:** Kai aktyvios hipotezės (`/hypotheses`) pasitikėjimo laipsnis (`Confidence Score`, žr. `engine/confidence_score.md`) yra žemesnis nei slenkstis (šiuo metu numatyta ≥ 0.80, žr. `docs/principles.md` III principą), šis modulis nusprendžia, koks kitas stimulas turi būti pateiktas vartotojui, kad hipotezė būtų patikrinta per kitą medijos formą (trianguliacija).

## Įvestis
- Aktyvi hipotezė ir jos dabartinis Confidence Score.
- Jau panaudotų medijos formų sąrašas šioje sesijoje (vizualinė / audio / tekstinė).
- `/stimuli` katalogo turinys (galimų stimulų banko).

## Numatoma logika (reikia detalizuoti)
1. Patikrinti, kurios medijos formos dar nebuvo panaudotos trianguliacijai patvirtinti.
2. Iš `/stimuli` atrinkti stimulą, kuris tikrina *tą pačią* hipotezę, bet *kita* forma.
3. Grąžinti pasirinktą stimulą `/perception` sluoksniui pateikimui vartotojui.

## Kas dar neapibrėžta
- Atrankos algoritmas, kai kelios hipotezės turi panašų Confidence Score (prioritizavimo taisyklė).
- Elgesys, kai visos 3 medijos formos jau išnaudotos, o Confidence vis dar < 0.80 (ar sesija baigiama neapibrėžtu rezultatu, ar generuojamas naujas stimulas toje pačioje formoje?).
- Ryšys su `ideas/backlog.md` (šiuo metu tuščias) — ar čia turėtų atsirasti idėjos apie stimulų banko plėtimą.

---
*Šis failas sukurtas kaip struktūrinė vieta, kad `engine/analysis_pipeline.md` nuorodos neliktų "kabančios". Turinys turi būti išplėtotas prieš pradedant programavimą (žr. `docs/principles.md`, "Kūrimo taisyklė").*
