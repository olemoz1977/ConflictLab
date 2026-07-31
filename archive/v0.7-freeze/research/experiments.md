# Eksperimentai

## ⚠️ Neatlikti / nepagrįsti skaičiai V2 architektūroje

Šie skaičiai šiuo metu naudojami `docs/principles.md` (II principas) ir `engine/analysis_pipeline.md` specifikacijose, tačiau **nėra pagrįsti jokiu ConflictLab atliktu eksperimentu ar konkrečia moksline citata**. Pagal `docs/principles.md` V principą ("Mokslas ir hipotezės yra atskiriami"), jie turi būti aiškiai laikomi **hipotezėmis**, kol nepatvirtinti:

| Parametras | Dabartinė reikšmė | Statusas |
|---|---|---|
| Latency riba "spontaniškam" atsakui | < 1.5 s | Hipotezė — reikia validuoti |
| Latency riba "racionalizuotam" atsakui | > 4.0 s | Hipotezė — reikia validuoti |
| Trianguliacijos Confidence Score slenkstis | ≥ 0.80 | Hipotezė — savavališkai pasirinktas skaičius, reikia pagrįsti arba testuoti empiriškai |

## Kas reikalinga prieš šiuos skaičius laikant patikimais

1. Literatūros apžvalga (`research/bibliography.md`) dėl reakcijos laiko / implicit-association tyrimų metodologijų — pvz., IAT (Implicit Association Test) naudoja panašią latency logiką, verta palyginti jų slenksčius su čia pasirinktais.
2. Pilotinis eksperimentas su realiais vartotojais, matuojant pasiskirstymą, o ne remiantis intuicija.
3. Aiškus sprendimas, ar slenksčiai bus fiksuoti visiems vartotojams, ar individualiai kalibruojami (žmonių bazinis reakcijos greitis skiriasi).

## Tyrimo klausimai (žr. taip pat `research/research_questions.md`)

- (papildyti)
