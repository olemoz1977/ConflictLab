# 2Pair — Integrated Pilot Privacy Notice v0.1

**Date:** 2026-08-29  
**Status:** DRAFT FOR TECHNICAL DEPLOYMENT / NOT ACTIVE  
**Applies to:** `2pair-integrated-v0.1` timing / UX + stimulus-validation pilot only  
**Controller:** Oleg Mozochin · info@omesg360.eu

> This notice expands the former timing-only Calibration scope. It covers pseudonymous rapid-choice/timing data and optional Wave 1-style reflection data. It does not authorize Gate D/E, psychological profiling, personality diagnosis, employment decisions, health decisions, or a claim that rapid choices reveal the subconscious.

---

# LT — Privatumo pranešimas

## 1. Duomenų valdytojas

Duomenų valdytojas: **Oleg Mozochin**  
Privatumo kontaktas: **info@omesg360.eu**  
Projektas: **2Pair**

## 2. Tyrimo tikslas

Šio piloto tikslas yra kartu tikrinti dvi jau atskirai naudotas tyrimo dalis:

1. greito trijų porų pasirinkimo bloko mechaniką / UX, įskaitant 6000 ms bendro laiko kandidato veikimą; ir
2. šešių vaizdų porų stimulus-validation duomenis: ką dalyvis pasirinko ir, jei nori, kaip pats paaiškina savo pasirinkimą.

6000 ms yra eksperimentinis techninis parametras, o ne psichologinis standartas. Pasirinkimo laikas nėra interpretuojamas kaip impulsyvumas, pasitikėjimas, asmenybės bruožas ar „pasąmonės matas“.

Šis pilotas **nėra asmenybės testas, diagnostika, tinkamumo darbui ar sveikatos vertinimas**.

## 3. Savanoriškas dalyvavimas ir amžiaus riba

Tyrimo duomenų įkėlimas skirtas tik **18 metų ir vyresniems** dalyviams. Gimimo datos ar asmens dokumento nerenkame; naudojama 18+ deklaracija.

Po vietinės treniruotės galite:

- patvirtinti 18+ ir savanoriškai sutikti su tyrimo duomenų įkėlimu; arba
- tęsti tik lokaliai be tyrimo duomenų įkėlimo.

Varnelės nėra pažymėtos iš anksto. Atsisakymas nėra laikomas psichologiniu signalu ar rezultatu.

## 4. Kokius duomenis renkame, jei sutinkate

Į integruoto piloto DB gali būti perduodami:

- atsitiktinis pseudoniminis sesijos UUID;
- serverio priskirtas `TECHNICAL` arba `RESEARCH` tipas;
- release, protokolo, stimulų rinkinio ir treniruotės versijos;
- pasirinkta sąsajos kalba;
- apibendrinta įrenginio kategorija;
- sutikimo versija, teigiamo sutikimo faktas ir 18+ deklaracija;
- dviejų trijų porų blokų techninis formos / eilės identifikavimas;
- techniniai porų raktai ir A/B vaizdų pateikimo top/bottom pozicijos;
- ar pora buvo pateikta;
- faktinis A, B arba `no_clear_choice` pasirinkimas;
- vizualinio pasirinkimo reakcijos laikas nuo aktyvios poros iki pasirinkimo veiksmo;
- bloko praėjęs laikas ir likęs biudžetas;
- timeout, retry ir page-hidden diagnostika;
- neprivalomas jūsų parašytas trumpas pasirinkimo paaiškinimas;
- neprivalomas reakcijos stiprumas 1–5 po A/B pasirinkimo;
- `hard_to_identify` faktas, jei pažymite, kad sunku įvardyti priežastį;
- įrašo sukūrimo laikas;
- SHA-256 hash, sukurtas iš atsitiktinio duomenų ištrynimo kodo.

Treniruotės pasirinkimai į tyrimo DB nesiunčiami.

Retry bandymai saugomi kaip timing / UX diagnostika. Stimulus-validation refleksijos serveryje siejamos tik su pirmo (primary) bandymo užbaigtais atsakymais; retry-only pasirinkimo refleksija į Wave 1 analizės duomenis neįtraukiama.

## 5. Ko tyrimo DB nerenkame

Nerenkame kaip tyrimo laukų:

- vardo, el. pašto, telefono ar darbdavio;
- gimimo datos ar asmens dokumento;
- tikslios buvimo vietos;
- IP adreso kaip tyrimo kintamojo;
- pilno User-Agent / browser fingerprint;
- nuolatinio cross-study participant ID;
- Gate D / Gate E rezultato;
- asmenybės tipo ar psichologinės diagnozės;
- struktūruotų „teisingų“ priežasčių iš `reason-map-v1`.

## 6. Kada duomenys gali būti išsaugoti

Jei pasirinkote research upload, kiekvienas užbaigtas arba po maksimalių retry terminalus pasiekęs 3 porų blokas gali būti išsaugotas iš karto. Todėl sesijai nutrūkus po pirmo bloko, pirmo bloko duomenys gali likti DB kaip nepilnos sesijos įrašas.

Po greitų blokų pasirinkta neprivaloma refleksija saugoma po vieną porą, kai ją išsaugote. Jei sesija nutrūksta refleksijos metu, dalis jau išsaugotų refleksijų gali likti DB.

Jei pasirinkote tęsti tik lokaliai, nei greitų blokų, nei refleksijos tyrimo payload į integruoto piloto DB nesiunčiamas.

## 7. Duomenų ištrynimo kodas

Po research opt-in naršyklė sugeneruoja atsitiktinį 32 šešioliktainių simbolių kodą, parodo jį **prieš pirmą matuojamą bloką** ir gali jį išsaugoti toje pačioje naršyklėje `localStorage`, jei ši funkcija prieinama.

Į serverį siunčiamas tik kodo **SHA-256 hash**. Plaintext kodas serverio DB nesaugomas.

Kodas nenaudojamas tyrimo analizei.

## 8. Sutikimo atšaukimas ir ištrynimas

Tyrimo duomenų teisinis pagrindas yra jūsų **sutikimas pagal BDAR 6 straipsnio 1 dalies a punktą**.

Sutikimą galite atšaukti. Aktyvios integruotos sesijos duomenis galima ištrinti per savitarnos ištrynimo puslapį arba susisiekus **info@omesg360.eu** ir pateikus deletion kodą.

Ištrynimas pašalina sesiją, abu blokus, attempt įrašus, pair-event įrašus ir išsaugotas refleksijas iš aktyvios DB.

Jei kodas prarastas, dėl sąmoningo tiesioginių identifikatorių nerinkimo gali nebūti įmanoma patikimai nustatyti, kuris pseudoniminis įrašas yra jūsų.

## 9. Saugojimo trukmė ir Hostinger backup

Aktyvūs pseudoniminiai integruoto piloto įrašai saugomi **ne ilgiau kaip 90 dienų**, nebent ištrinami anksčiau.

Kasdienis CLI retention procesas skirtas iš aktyvios DB pašalinti pasibaigusio termino sesiją ir visus susijusius blokus, attempt, pair-event ir reflection įrašus.

OMESG360 Hostinger plano backup rotacija yra atskiras infrastruktūros sluoksnis. Individualus aktyvios DB ištrynimas gali ne iš karto pašalinti ankstesnėje apsaugotoje backup kopijoje esančią likutinę kopiją iki normalios backup rotacijos. Backup kopijos nenaudojamos 2Pair tyrimo analizei.

## 10. Hostinger techniniai žurnalai

Hostingo infrastruktūra gali automatiškai apdoroti IP adresą, užklausos laiką, User-Agent kilusią techninę informaciją ir kitą saugumui / tinklo veikimui reikalingą informaciją. Šie žurnalai nėra integruoto 2Pair tyrimo datasetas ir nėra jungiami su pasirinkimų duomenimis psichologinei analizei.

## 11. Duomenų tvarkytojas ir GitHub riba

2Pair naudoja Hostinger infrastruktūrą. Dabartiniame OMESG360 kontekste pagrindinė serverio vieta yra Lietuva, backup vieta – Prancūzija, kaip dokumentuota ankstesniame aktyvavimo patikrinime.

GitHub naudojamas kodui, metodologijai ir versijų istorijai. Dalyvių DB įrašai, session UUID eksportai, refleksijos tekstai ar deletion kodai į GitHub nesiunčiami.

## 12. Automatizuoti sprendimai ir rezultatų riba

Integruoto piloto duomenys nenaudojami automatizuotiems sprendimams, turintiems teisinių ar panašiai reikšmingų pasekmių.

Gate D ir Gate E lieka `NONE`. Dalyviui nerodomas psichologinis / kryptinis rezultatas. Choice Trace yra tik jo paties šios sesijos pasirinkimų atvaizdavimas.

## 13. Jūsų teisės

Priklausomai nuo aplinkybių pagal BDAR galite turėti teisę gauti informaciją ir prieigą, prašyti ištaisyti ar ištrinti duomenis, apriboti tvarkymą, pasinaudoti duomenų perkeliamumo teise, kai ji taikoma, atšaukti sutikimą ir pateikti skundą priežiūros institucijai.

Privatumo kontaktas: **info@omesg360.eu**. Lietuvoje skundą galima pateikti **Valstybinei duomenų apsaugos inspekcijai (VDAI)**.

---

# EN — Privacy Notice

## 1. Data controller

Data controller: **Oleg Mozochin**  
Privacy contact: **info@omesg360.eu**  
Project: **2Pair**

## 2. Study purpose

This pilot combines two research functions that were previously run separately:

1. mechanical timing / UX of rapid three-pair visual-choice blocks using a candidate shared 6000 ms budget; and
2. stimulus-validation evidence across six image pairs, including what a participant chose and, optionally, how the participant explains that choice.

6000 ms is an experimental engineering parameter, not a psychological standard. Choice latency is not interpreted as impulsivity, confidence, a personality trait, or a measure of the subconscious.

This pilot is **not a personality test, diagnosis, employment-suitability assessment or health assessment**.

## 3. Voluntary participation and age limit

Research upload is intended only for participants aged **18 or older**. We do not collect date of birth or identity documents; a simple 18+ declaration is used.

After local practice, you may either opt in to research upload or continue locally without research upload. Checkboxes are not preselected. Refusal is not treated as a psychological signal or result.

## 4. Data collected if you opt in

The integrated pilot database may store:

- a random pseudonymous session UUID;
- a server-assigned `TECHNICAL` or `RESEARCH` run type;
- release, protocol, stimulus-set and training-set versions;
- interface language;
- coarse device category;
- consent version, affirmative consent state and 18+ declaration;
- the two three-pair block/form identities and presentation order;
- technical pair keys and A/B top/bottom positions;
- whether a pair was presented;
- the A, B or `no_clear_choice` response;
- visual-choice latency from an interactive pair to the response action;
- elapsed and remaining block time;
- timeout, retry and page-hidden diagnostics;
- optional free-text explanation of a choice;
- optional 1–5 reaction intensity after A/B choices;
- the `hard_to_identify` state when the participant indicates that the reason is hard to name;
- collection timestamps;
- a SHA-256 hash derived from a random participant deletion code.

Practice choices are not uploaded. Retry attempts are retained only as timing / UX diagnostics. Server-side stimulus-validation reflection is stored only for completed PRIMARY-attempt responses; retry-only reflection is not added to Wave 1 evidence.

## 5. Data not collected as research fields

The research dataset does not collect name, email, phone number, employer, date of birth, identity document, precise location, research-use IP field, full User-Agent/browser fingerprint, persistent cross-study participant ID, Gate D/E result, personality type, psychological diagnosis, or participant-facing structured `reason-map-v1` answers.

## 6. When data may be stored

If you opt in, each terminal rapid block may be uploaded as soon as that block ends. Therefore, if a session stops after block 1, block-1 data may remain as an incomplete-session record.

Optional reflection is stored pair-by-pair when saved. If the session stops during reflection, reflections already saved may remain.

If you continue locally only, neither rapid-block nor reflection research payloads are sent to the integrated pilot database.

## 7. Deletion code

After research opt-in, the browser creates a random 32-character hexadecimal deletion code, shows it **before the first measured block**, and may store that plaintext code locally in `localStorage` if available. Only its SHA-256 hash is sent to and stored by the server. The code is not used for analysis.

## 8. Withdrawal and deletion

The legal basis for the research data is **consent under GDPR Article 6(1)(a)**. Consent may be withdrawn. An active integrated session can be deleted using the self-service deletion page or by contacting **info@omesg360.eu** with the deletion code.

Deletion removes the session and its blocks, attempts, pair events and saved reflections from the active database. If the code is lost, deliberate avoidance of direct identifiers may make it impossible to reliably identify which pseudonymous record is yours.

## 9. Retention and backups

Active pseudonymous integrated-pilot records are retained for **no more than 90 days**, unless deleted earlier. A daily CLI retention process removes expired sessions and their related records from the active database.

Hostinger backup rotation is a separate infrastructure layer. Deletion from the active database may not immediately remove a residual copy contained in a previously created protected backup until normal backup rotation. Backups are not used for 2Pair research analysis.

## 10. Hosting logs

Hosting infrastructure may automatically process IP address, request time, User-Agent-derived technical information and other data required for network operation or security. These logs are not the integrated 2Pair research dataset and are not joined to choice data for psychological analysis.

## 11. Processor and GitHub boundary

2Pair uses Hostinger infrastructure. In the previously documented OMESG360 activation state, the primary server location is Lithuania and the backup location is France.

GitHub is used for code, methodology and version history. Participant database rows, session-UUID exports, reflection text and deletion codes are not committed to GitHub.

## 12. Automated decisions and result boundary

Integrated-pilot data are not used for automated decisions with legal or similarly significant effects. Gate D and Gate E remain `NONE`; no psychological/directional participant result is produced. Choice Trace is only a visual representation of the participant's own choices in that session.

## 13. Your rights

Depending on the circumstances, GDPR rights may include information/access, rectification, erasure, restriction, portability where applicable, withdrawal of consent and the right to lodge a complaint with a supervisory authority.

Privacy contact: **info@omesg360.eu**. In Lithuania, complaints may be submitted to the **State Data Protection Inspectorate (VDAI)**.
