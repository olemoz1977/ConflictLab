# ConflictLab — Timing Research Privacy Notice v0.3

**Date:** 2026-08-15  
**Status:** DRAFT FOR ACTIVATION / DO NOT MARK ACTIVE UNTIL FINAL LIVE CHECKS PASS  
**Applies to:** first external ConflictLab mechanical timing / UX calibration study only  
**Controller:** Oleg Mozochin · info@omesg360.eu

> This notice covers only mechanical timing research. It does not authorize Gate D, Gate E, psychological profiling, reflection-content research, participant scoring, employment decisions, health decisions, or personality claims.

---

# LT — Privatumo pranešimas

## 1. Duomenų valdytojas

Duomenų valdytojas: **Oleg Mozochin**  
Privatumo kontaktas: **info@omesg360.eu**  
Projektas: **ConflictLab**

## 2. Tyrimo tikslas

Šiuo etapu tikrinama tik sąsajos mechanika: ar trijų nuoseklių vaizdų porų pasirinkimo blokas su bendru 6000 ms kandidatuojančiu laiko biudžetu techniškai veikia priimtinai palaikomuose įrenginiuose.

6000 ms yra eksperimentinis techninis parametras, o ne psichologinis standartas.

Šis tyrimas **nevertina jūsų asmenybės, psichologinių savybių, tinkamumo darbui, sveikatos ar kitų asmeninių charakteristikų**.

## 3. Savanoriškas dalyvavimas ir amžiaus riba

Išorinis timing tyrimas skirtas tik **18 metų ir vyresniems** dalyviams. Gimimo datos ar asmens dokumento dėl to nerenkame; naudojama paprasta 18+ deklaracija.

Prieš pagrindinį bloką galite:

- patvirtinti 18+ ir savanoriškai sutikti su timing tyrimo duomenų įkėlimu; arba
- tęsti be tyrimo duomenų įkėlimo.

Varnelės nėra pažymėtos iš anksto. Atsisakymas nėra interpretuojamas kaip nesėkmė, psichologinis signalas ar rezultatas.

## 4. Kokius tyrimo duomenis renkame

Jei aiškiai sutinkate dalyvauti ir pagrindinis blokas užbaigiamas taip, kad įvyksta upload, į izoliuotą timing tyrimo DB gali būti perduodami:

- atsitiktiniai sesijos / techninio įkėlimo UUID;
- serverio priskirtas run tipas;
- sutikimo versija ir teigiamo sutikimo / 18+ deklaracijos faktas;
- release, protokolo, stimulų rinkinio ir formos versijos;
- techninis poros raktas, pateikimo eilė ir pozicija;
- vizualinio pasirinkimo reakcijos laikas;
- bloko praėjęs ir likęs laikas;
- timeout / nepateikto stimulo būsena;
- retry / page-hidden diagnostika;
- apibendrinta įrenginio kategorija;
- techninės būsenos informacija;
- įrašo sukūrimo laikas;
- SHA-256 hash reikšmė, sukurta iš atsitiktinio duomenų ištrynimo kodo.

Į timing tyrimo DB **nerenkame**:

- vardo, el. pašto, telefono ar darbdavio;
- gimimo datos ar asmens dokumento;
- tikslios buvimo vietos;
- IP adreso kaip tyrimo lauko;
- pilno User-Agent / browser fingerprint;
- atviro refleksijos teksto;
- pasirinkimo priežasčių;
- reakcijos intensyvumo;
- priežasties ar intensyvumo response-time;
- psichologinio / kryptinio rezultato;
- nuolatinio cross-study participant ID.

Refleksijos priežastys, optional free text, intensyvumas ir jų response-time duomenys šiame etape lieka lokaliai naršyklėje ir nėra timing tyrimo serverio datasetas.

## 5. Duomenų ištrynimo kodas ir naršyklės vietinis saugojimas

Jei savanoriškai pasirenkate timing tyrimo upload, **prieš pagrindinį matuojamą bloką** jūsų naršyklė sugeneruoja atsitiktinį 32 šešioliktainių simbolių duomenų ištrynimo kodą.

Kodas:

- parodomas jums prieš pagrindinį bloką;
- jei naršyklės `localStorage` prieinamas, automatiškai išsaugomas **tik tame įrenginyje / naršyklės profilyje** kaip ištrynimo ir sutikimo atšaukimo patogumo priemonė;
- nėra siunčiamas į tyrimo serverį plaintext forma;
- nėra įtraukiamas į timing CSV eksportą ar tyrimo analizę;
- serverio DB sėkmingo upload atveju saugo tik jo **SHA-256 hash**.

Dabartinė sąsaja gali lokaliai laikyti iki 12 paskutinių ConflictLab Calibration deletion kodų, kad nauja sesija automatiškai neperrašytų ankstesnio kodo. Sėkmingai pasinaudojus savitarnos ištrynimu, pateiktas kodas pašalinamas iš šio vietinio sąrašo. Jūs taip pat galite pats išvalyti naršyklės svetainės duomenis; tada vietiniai kodai gali būti prarasti.

Jei vietinis saugojimas neprieinamas, sąsaja apie tai informuoja ir kodą reikia išsisaugoti pačiam prieš tęsiant.

**Svarbi riba:** `localStorage` deletion kodas yra dalyvio teisėms / ištrynimui palengvinti skirtas local-only mechanizmas. Jis nėra ConflictLab research datasetas.

Vietinis kodas įrašomas tik po to, kai pats pasirenkate dalyvauti timing tyrime; prieš research opt-in jis nekuriamas ir nerašomas.

## 6. Sutikimo atšaukimas ir ištrynimas

Timing tyrimo duomenų teisinis pagrindas yra jūsų **sutikimas pagal BDAR 6 straipsnio 1 dalies a punktą**.

Sutikimą galite atšaukti. Atšaukimas nepanaikina iki atšaukimo teisėtai atlikto tvarkymo.

Savo aktyvios ConflictLab timing sesijos duomenis galite ištrinti:

1. per ConflictLab savitarnos ištrynimo puslapį, naudodami deletion kodą; arba
2. parašę **info@omesg360.eu** ir pateikę kodą.

Jei deletion kodas prarastas ir jo nebėra vietinėje naršyklės saugykloje, dėl sąmoningo tiesioginių identifikatorių nerinkimo gali nebūti įmanoma patikimai nustatyti, kuris pseudoniminis įrašas yra jūsų.

## 7. Kada duomenys nesiunčiami

Jei pasirenkate tęsti be research upload, pagrindinio bloko timing telemetrija į tyrimo DB nesiunčiama.

Jei consented sesija nutrūksta iki to taško, kuriame užbaigto bloko timing payload sėkmingai įkeliamas, dalinis pasirinkimų srautas realiu laiku į tyrimo DB nesiunčiamas.

## 8. Saugojimo trukmė

Aktyvios pseudoniminės timing tyrimo DB sesijos saugomos **ne ilgiau kaip 90 dienų nuo surinkimo**, nebent jos ištrinamos anksčiau.

Kasdienis CLI retention procesas skirtas pašalinti pasibaigusio termino run ir susijusius attempt / pair-event įrašus iš aktyvios DB.

Tik iš tiesų anoniminė, su konkrečia sesija ar asmeniu nebesiejama suvestinė statistika gali būti saugoma ilgiau metodologijos dokumentavimui.

### Hostinger atsarginės kopijos

Dabartinis OMESG360 Premium Web Hosting planas naudoja savaitines Hostinger atsargines kopijas. Pagal 2026-08-15 peržiūrėtą Hostinger informaciją savaitinės web/cloud hosting kopijos laikomos iki **6 savaičių**.

Todėl individualus ar retention ištrynimas pašalina įrašą iš **aktyvios ConflictLab tyrimo DB**, tačiau anksčiau sukurtoje apsaugotoje Hostinger backup kopijoje likutinė kopija gali laikinai išlikti iki normalios backup rotacijos.

Backup kopijos nenaudojamos ConflictLab tyrimo analizei. Jei backup atkūrimas sugrąžintų anksčiau ištrintą aktyvų įrašą ir jį techniškai galima identifikuoti, ištrynimas turi būti pakartotinai pritaikytas.

## 9. Hostinger techniniai žurnalai

Hostingo infrastruktūra gali automatiškai apdoroti IP adresą, užklausos laiką / adresą, User-Agent kilusią techninę informaciją, IP pagrindu nustatomą šalį ir kitą tinklo veikimui ar saugumui reikalingą informaciją.

Šie Hostinger prieigos / saugumo žurnalai yra atskiras techninis sluoksnis ir **nejungiami su ConflictLab timing tyrimo duomenimis psichologinei ar elgesio analizei**.

Siaurai būtinas svetainės / serverio saugumo ir vientisumo tvarkymas gali būti grindžiamas duomenų valdytojo teisėtu interesu saugiai eksploatuoti sistemą, kaip dokumentuota atskirame techninio saugumo LIA.

## 10. Duomenų tvarkytojas ir perdavimai

ConflictLab naudoja **Hostinger** hostingo infrastruktūrą.

Dabartiniam planui patikrinta:

```text
pagrindinis serveris: Lietuva
atsarginių kopijų vieta: Prancūzija
```

Hostinger veikia kaip hostingo / Customer Data infrastruktūros tvarkytojas pagal taikomas DPA sąlygas ir gali naudoti autorizuotus subtvarkytojus. Jei konkrečiam Customer Data tvarkymui būtų taikomas perdavimas už EEE ribų į šalį be tinkamumo sprendimo, turi būti naudojamos taikomos perdavimo apsaugos priemonės, įskaitant ES standartines sutarčių sąlygas, kai jos taikomos.

Todėl ConflictLab nežada, kad joks techninis apdorojimas niekada nevyks už EEE ribų, nors dabartinės pagrindinės saugyklos ir backup vietos yra EEE.

## 11. GitHub riba

GitHub naudojamas ConflictLab kodui, konfigūracijoms, metodologijos dokumentams ir versijų istorijai. Dalyvių timing research datasetas, deletion kodai, session telemetry, refleksijos tekstas ar participant identifiers į GitHub nesiunčiami.

## 12. Sekimo / reklamos įrankiai

Šiam ConflictLab timing tyrimui OMESG360 kode nenaudojami Google Analytics, Meta Pixel, reklaminiai pikseliai ar kitos nebūtinos rinkodaros sekimo technologijos.

Hostinger serverio prieigos žurnalai nėra reklamos profilis ir nėra naudojami timing tyrimo psichologinei analizei.

## 13. Automatizuoti sprendimai

Timing tyrimo duomenys nenaudojami automatizuotiems sprendimams, turintiems teisinių ar panašiai reikšmingų pasekmių.

Jie nenaudojami darbo atrankai, reitingavimui, sveikatos sprendimams, asmenybės diagnozei ar tinkamumo vertinimui.

## 14. Jūsų teisės

Priklausomai nuo aplinkybių pagal BDAR galite turėti teisę:

- gauti informaciją ir prieigą;
- prašyti ištaisyti duomenis;
- prašyti ištrinti duomenis;
- prašyti apriboti tvarkymą;
- gauti duomenis perkeliamu formatu, kai ši teisė taikoma;
- atšaukti sutikimą dėl būsimo sutikimu grindžiamo tvarkymo;
- pateikti skundą priežiūros institucijai.

Privatumo kontaktas: **info@omesg360.eu**.

Lietuvoje skundą galite pateikti **Valstybinei duomenų apsaugos inspekcijai (VDAI)**.

---

# EN — Privacy Notice

## 1. Data controller

Data controller: **Oleg Mozochin**  
Privacy contact: **info@omesg360.eu**  
Project: **ConflictLab**

## 2. Study purpose

This phase tests only interaction mechanics: whether a three-pair rapid visual-choice block with a candidate shared 6000 ms budget produces acceptable technical completion/missingness mechanics on supported devices.

6000 ms is an experimental engineering parameter, not a psychological standard.

This study **does not assess personality, psychological traits, employment suitability, health or other personal characteristics**.

## 3. Voluntary participation and age limit

The external timing study is intended only for participants aged **18 or older**. We do not collect date of birth or identity documents for this; a simple 18+ declaration is used.

Before the main block, you may either:

- confirm 18+ and voluntarily opt in to timing-research upload; or
- continue without research upload.

Checkboxes are unticked by default. Refusal is not interpreted as failure, a psychological signal, or a result.

## 4. Research data collected

If you explicitly opt in and the main block reaches the point where upload occurs, the isolated timing-research database may receive:

- random session / ingestion UUIDs;
- server-assigned run type;
- consent version and evidence of affirmative consent / 18+ declaration;
- release, protocol, stimulus-set and form versions;
- technical pair key, presentation order and position;
- visual-choice response time;
- block elapsed / remaining time;
- timeout / never-presented state;
- retry / page-hidden diagnostics;
- coarse device category;
- technical status information;
- collection timestamp;
- a SHA-256 hash derived from the random deletion code.

The timing-research DB does **not** collect:

- name, email, phone or employer;
- date of birth or identity document;
- precise location;
- IP address as a research field;
- full User-Agent / browser fingerprint;
- open reflection text;
- reason responses;
- reaction intensity;
- reason/intensity response timing;
- psychological/directional result;
- persistent cross-study participant ID.

Reflection reasons, optional free text, intensity and their response times remain local in this phase and are not part of the timing research server dataset.

## 5. Deletion code and browser local storage

If you voluntarily opt in to timing-research upload, **before the main measured block** your browser creates a random 32-hex-character deletion code.

The code:

- is shown to you before the main block;
- where browser `localStorage` is available, is automatically stored **only on that device / browser profile** as a withdrawal/deletion convenience;
- is not sent to the research server in plaintext form;
- is not included in timing CSV export or research analysis;
- after a successful upload, only its **SHA-256 hash** is stored in the research database.

The current interface may retain up to 12 recent ConflictLab Calibration deletion codes locally so a new session does not silently replace the previous code. After successful self-service deletion, the submitted local code is removed from that local list. You may also clear browser site data yourself, which can remove locally retained codes.

If local storage is unavailable, the interface tells you and you should save the code yourself before continuing.

**Boundary:** the localStorage deletion code is a local-only mechanism to make withdrawal/deletion easier. It is not part of the ConflictLab research dataset.

The local code is written only after you choose to participate in timing research; it is not created or stored before research opt-in.

## 6. Withdrawal and deletion

The legal basis for voluntary timing-research data is your **consent under GDPR Article 6(1)(a)**.

You may withdraw consent. Withdrawal does not affect processing that was lawful before withdrawal.

You can delete active ConflictLab timing-session data either:

1. through the ConflictLab self-service deletion page using the deletion code; or
2. by emailing **info@omesg360.eu** and providing the code.

If the deletion code is lost and no longer available in browser local storage, deliberately not collecting direct identifiers may make it impossible to reliably determine which pseudonymous record is yours.

## 7. When data are not uploaded

If you continue without research upload, main-block timing telemetry is not sent to the research database.

If a consented session is abandoned before the completed-block timing payload is successfully uploaded, partial choices are not streamed in real time to the research database.

## 8. Retention

Active pseudonymous timing-research database sessions are retained for **no longer than 90 days from collection**, unless deleted earlier.

A daily CLI retention process is intended to remove expired runs and their related attempt / pair-event records from the active database.

Only genuinely anonymous aggregate statistics that can no longer be linked to a particular session or person may be retained longer for methodology documentation.

### Hostinger backups

The current OMESG360 Premium Web Hosting plan uses weekly Hostinger backups. According to Hostinger information reviewed on 2026-08-15, weekly web/cloud-hosting backups are retained for up to **6 weeks**.

Individual or retention deletion removes a record from the **active ConflictLab research database**, but a residual copy may temporarily remain in a previously created protected Hostinger backup until normal backup rotation.

Backups are not used for ConflictLab research analysis. If a backup restore reintroduced a previously deleted active record and the record can technically be identified, deletion must be re-applied.

## 9. Hostinger technical logs

Hosting infrastructure may automatically process IP address, request time/resource, User-Agent-derived technical information, IP-derived country and other information needed for network operation/security.

These Hostinger access/security logs are a separate technical layer and **are not joined to ConflictLab timing-research data for psychological or behavioural analysis**.

Narrowly necessary website/server security and integrity processing may rely on the controller's legitimate interests in secure operation as documented in a separate technical-security LIA.

## 10. Processor and transfers

ConflictLab uses **Hostinger** hosting infrastructure.

The current plan has been checked as:

```text
primary server: Lithuania
backup location: France
```

Hostinger acts as hosting / Customer Data infrastructure processor under applicable DPA terms and may use authorized subprocessors. Where a specific Customer Data processing route involves transfer outside the EEA to a country without an adequacy decision, applicable transfer safeguards must be used, including EU Standard Contractual Clauses where applicable.

ConflictLab therefore does not promise that no technical processing can ever occur outside the EEA, even though the current primary and backup storage locations are in the EEA.

## 11. GitHub boundary

GitHub is used for ConflictLab code, configuration, methodology documents and version history. Participant timing-research datasets, deletion codes, session telemetry, reflection text and participant identifiers are not sent to GitHub.

## 12. Tracking / advertising tools

The OMESG360 code for this ConflictLab timing study does not use Google Analytics, Meta Pixel, advertising pixels, or other non-essential marketing tracking technologies.

Hostinger server access logs are not an advertising profile and are not used for psychological analysis of the timing study.

## 13. Automated decisions

Timing-research data are not used for automated decisions producing legal or similarly significant effects.

They are not used for employment selection, ranking, health decisions, personality diagnosis, or suitability assessment.

## 14. Your rights

Depending on the circumstances, the GDPR may give you rights to:

- information and access;
- rectification;
- erasure;
- restriction;
- portability where applicable;
- withdraw consent for future consent-based processing;
- lodge a complaint with a supervisory authority.

Privacy contact: **info@omesg360.eu**.

In Lithuania you may lodge a complaint with the **State Data Protection Inspectorate (VDAI)**.

---

## Activation boundary

This v0.3 notice is a release candidate, not evidence that external collection is already active.

Before activation:

```text
final current-artifact LT/EN smoke checks pass
local-only no-DB proof passes
admin fallback deletion smoke passes
retention scheduled execution evidence is captured or explicitly accepted as a monitored post-activation operational check
live /privacy.html is synchronized with this processing profile
activation record is created
owner explicitly authorizes CALIBRATION
```
