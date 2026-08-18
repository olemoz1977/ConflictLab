# ConflictLab — Timing Research Privacy Notice v0.2

**Date:** 2026-08-15  
**Status:** DRAFT FOR ACTIVATION / DO NOT MARK ACTIVE UNTIL LIVE TECHNICAL CHECKLIST PASSES  
**Applies to:** first external ConflictLab mechanical timing / UX calibration study only.  
**Controller:** Oleg Mozochin · info@omesg360.eu

> This notice covers only mechanical timing research. It does not authorize Gate D, Gate E, psychological profiling, reflection-content research, participant scoring or employment/health decisions.

---

# LT — Privatumo pranešimas

## 1. Duomenų valdytojas

Duomenų valdytojas: **Oleg Mozochin**  
Kontaktas privatumo klausimais: **info@omesg360.eu**  
Projektas: **ConflictLab**

## 2. Tyrimo tikslas

Šio etapo tikslas yra patikrinti tik sąsajos mechaniką: ar trijų nuoseklių vaizdų porų pasirinkimo blokas su bendru 6000 ms kandidatuojančiu laiko biudžetu techniškai veikia priimtinai palaikomuose įrenginiuose.

Šis tyrimas **nevertina jūsų asmenybės, psichologinių savybių, tinkamumo darbui, sveikatos ar kitų asmeninių charakteristikų**.

6000 ms yra eksperimentinis techninis parametras, o ne psichologinis standartas.

## 3. Savanoriškas dalyvavimas

Timing tyrimo duomenų įkėlimas yra savanoriškas.

Prieš pagrindinį bloką galite:

- patvirtinti, kad jums 18 metų arba daugiau, ir savanoriškai sutikti su timing tyrimo duomenų įkėlimu; arba
- tęsti be tyrimo duomenų įkėlimo.

Atsisakymas įkelti tyrimo duomenis nėra interpretuojamas kaip nesėkmė, psichologinis signalas ar rezultatas.

## 4. Kokius tyrimo duomenis renkame

Jei aiškiai sutinkate dalyvauti, į izoliuotą timing tyrimo duomenų bazę gali būti perduodami:

- atsitiktiniai sesijos / techninio įkėlimo UUID;
- tyrimo paskirtis / serverio priskirtas run tipas;
- sutikimo versija ir teigiamo sutikimo / 18+ deklaracijos faktas;
- release, protokolo, stimulų rinkinio ir formos versijos;
- techninis poros raktas, pateikimo eilė ir pozicija, kai to reikia timing diagnostikai;
- vizualinio pasirinkimo reakcijos laikas;
- bloko praėjęs ir likęs laikas;
- timeout / nepateikto stimulo būsena;
- retry / page-hidden diagnostika;
- apibendrinta įrenginio kategorija;
- techninės būsenos informacija;
- įrašo sukūrimo laikas;
- SHA-256 hash reikšmė, sukurta iš jūsų atsitiktinio duomenų ištrynimo kodo.

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

## 5. Techniniai Hostinger žurnalai

Svetainės hostingo infrastruktūra gali automatiškai apdoroti IP adresą, užklausos laiką / adresą, User-Agent kilusią techninę informaciją, IP pagrindu nustatomą šalį ir kitą tinklo veikimui ar saugumui reikalingą informaciją.

Šie Hostinger prieigos / saugumo žurnalai yra atskiras techninis sluoksnis ir **nejungiami su ConflictLab timing tyrimo duomenimis psichologinei ar elgesio analizei**.

## 6. Teisinis pagrindas

Savanoriško timing tyrimo duomenys tvarkomi pagal jūsų **sutikimą, BDAR 6 straipsnio 1 dalies a punktą**.

Sutikimą galite atšaukti. Atšaukimas nepanaikina iki atšaukimo teisėtai atlikto tvarkymo.

Atskirai nuo tyrimo, siaurai būtinas svetainės / serverio saugumo ir vientisumo tvarkymas gali būti grindžiamas duomenų valdytojo teisėtu interesu saugiai eksploatuoti sistemą, kai toks interesas yra dokumentuotas ir taikomas tik būtinai techninei apimčiai.

## 7. Duomenų ištrynimo kodas ir sutikimo atšaukimas

Po **sėkmingo** sutikimu pagrįsto timing duomenų įkėlimo sistema parodo atsitiktinį 32 šešioliktainių simbolių duomenų ištrynimo kodą.

Svarbu:

- plaintext kodas rodomas jums;
- serverio DB plaintext kodo nesaugo;
- serveris saugo tik SHA-256 hash, leidžiantį rasti atitinkančią pseudoniminę sesiją;
- jūsų vardas ar el. paštas dėl to netampa tyrimo identifikatoriumi.

Savo aktyvios ConflictLab timing sesijos duomenis galite ištrinti:

1. per ConflictLab savitarnos ištrynimo puslapį, įvesdami kodą; arba
2. parašę **info@omesg360.eu** ir pateikę kodą.

Jei kodas prarastas, dėl sąmoningo tiesioginių identifikatorių nerinkimo gali nebūti įmanoma patikimai nustatyti, kuris pseudoniminis įrašas yra jūsų.

## 8. Saugojimo trukmė

Aktyvios pseudoniminės timing tyrimo DB sesijos planuojamos saugoti **ne ilgiau kaip 90 dienų nuo surinkimo**, nebent jos ištrinamos anksčiau.

Pasibaigus terminui, event-level timing duomenys ištrinami iš aktyvios tyrimo DB. Tik iš tiesų anoniminė, su konkrečia sesija ar asmeniu nebesiejama suvestinė statistika gali būti saugoma ilgiau metodologijos dokumentavimui.

### Hostinger atsarginės kopijos

Dabartinis OMESG360 Premium Web Hosting planas naudoja savaitines Hostinger atsargines kopijas. Pagal 2026-08-15 peržiūrėtą Hostinger dokumentaciją savaitinės web/cloud hosting kopijos laikomos iki **6 savaičių**.

Todėl sėkmingas individualus ar retention ištrynimas pašalina įrašą iš **aktyvios ConflictLab tyrimo DB**, tačiau anksčiau sukurtoje apsaugotoje Hostinger backup kopijoje likutinė kopija gali laikinai išlikti iki normalios backup rotacijos.

Backup kopijos nenaudojamos ConflictLab tyrimo analizei. Jei atkuriant backup būtų grąžintas anksčiau ištrintas aktyvus įrašas ir jį techniškai galima identifikuoti, ištrynimas turi būti pakartotinai pritaikytas.

## 9. Duomenų tvarkytojas ir perdavimai

ConflictLab naudoja **Hostinger** hostingo infrastruktūrą.

Dabartiniam planui savininkas patikrino:

```text
pagrindinis serveris: Lietuva
atsarginių kopijų vieta: Prancūzija
```

Hostinger DPA nustato Hostinger kaip Customer Data tvarkytoją teikiant Covered Services ir leidžia naudoti autorizuotus subtvarkytojus pagal DPA sąlygas.

Hostinger DPA Appendix 3 nurodo autorizuotų subtvarkytojų sąrašą. Šis sąrašas nereiškia, kad kiekvienas nurodytas subtvarkytojas gauna konkretų ConflictLab įrašą.

Jei Customer Data būtų perduodami už EEE ribų į šalį be tinkamumo sprendimo, taikomos Hostinger DPA aprašytos perdavimo apsaugos priemonės, įskaitant ES standartines sutarčių sąlygas, kai jos taikomos.

Todėl ConflictLab nežada, kad joks techninis apdorojimas niekada nevyks už EEE ribų, nors pagrindinė dabartinio plano saugykla ir backup lokacijos yra EEE.

## 10. Sekimo / reklamos įrankiai

Šiam ConflictLab timing tyrimui OMESG360 kode nenumatyti Google Analytics, Meta Pixel, reklaminiai pikseliai ar kitos nebūtinos rinkodaros sekimo technologijos.

Hostinger serverio prieigos žurnalai nėra reklamos profilis ir nėra naudojami timing tyrimo psichologinei analizei.

## 11. Automatizuoti sprendimai

Timing tyrimo duomenys nenaudojami automatizuotiems sprendimams, turintiems teisinių ar panašiai reikšmingų pasekmių.

Jie nenaudojami darbo atrankai, reitingavimui, sveikatos sprendimams, asmenybės diagnozei ar tinkamumo vertinimui.

## 12. Jūsų teisės

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

## 13. Amžiaus riba

Išorinis timing tyrimas skirtas tik **18 metų ir vyresniems** dalyviams.

Naudojama paprasta pilnametystės deklaracija. Gimimo datos ar asmens dokumento dėl to nerenkame.

---

# EN — Privacy Notice

## 1. Data controller

Data controller: **Oleg Mozochin**  
Privacy contact: **info@omesg360.eu**  
Project: **ConflictLab**

## 2. Study purpose

This phase tests only interaction mechanics: whether a three-pair rapid visual-choice block with a candidate shared 6000 ms budget produces acceptable technical completion/missingness mechanics on supported devices.

This study **does not assess personality, psychological traits, employment suitability, health or other personal characteristics**.

6000 ms is an experimental engineering parameter, not a psychological standard.

## 3. Voluntary participation

Timing-research upload is voluntary.

Before the main block you can either:

- confirm that you are 18 or older and voluntarily opt in to timing-research upload; or
- continue without research upload.

Refusing research upload is not interpreted as failure, a psychological signal, or a result.

## 4. Research data collected

If you explicitly opt in, the isolated timing-research database may receive:

- random session / ingestion UUIDs;
- research purpose / server-assigned run type;
- consent version and evidence of affirmative consent / 18+ declaration;
- release, protocol, stimulus-set and form versions;
- technical pair key, presentation order and position where needed for timing diagnostics;
- visual-choice response time;
- block elapsed / remaining time;
- timeout / never-presented state;
- retry / page-hidden diagnostics;
- coarse device category;
- technical status information;
- collection timestamp;
- a SHA-256 hash derived from your random deletion code.

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

## 5. Hostinger technical logs

Hosting infrastructure may automatically process IP address, request time/resource, User-Agent-derived technical information, IP-derived country and other information needed for network operation/security.

These Hostinger access/security logs are a separate technical layer and **are not joined to ConflictLab timing-research data for psychological or behavioural analysis**.

## 6. Legal basis

Voluntary timing-research data are processed on the basis of your **consent under GDPR Article 6(1)(a)**.

You may withdraw consent. Withdrawal does not affect processing that was lawful before withdrawal.

Separately, narrowly necessary website/server security and integrity processing may rely on the controller's legitimate interests in secure operation where that interest is documented and limited to necessary technical processing.

## 7. Deletion code and withdrawal

After a **successful** consent-based timing upload, the system displays a random 32-hex-character deletion code.

- The plaintext code is shown to you.
- The research DB does not store the plaintext code.
- The server stores only a SHA-256 hash used to locate the matching pseudonymous session.
- Your name/email do not become study identifiers for this purpose.

You can delete the active ConflictLab timing session data either:

1. through the ConflictLab self-service deletion page by entering the code; or
2. by emailing **info@omesg360.eu** with the code.

If the code is lost, deliberate non-collection of direct identifiers may make it impossible to reliably identify which pseudonymous record is yours.

## 8. Retention

Active pseudonymous timing-study DB sessions are planned to be kept for **no more than 90 days from collection**, unless deleted earlier.

After the period, event-level timing records are deleted from the active research DB. Truly anonymous aggregate statistics that can no longer be linked to a person/session may be retained longer for methodology documentation.

### Hostinger backups

The current OMESG360 Premium Web Hosting account uses weekly Hostinger backups. Hostinger documentation reviewed on 15 August 2026 states that weekly web/cloud hosting backups are retained for up to **6 weeks**.

Therefore successful individual/retention deletion removes the record from the **active ConflictLab research DB**, while a residual copy may temporarily remain inside a previously created protected Hostinger backup until normal backup rotation expires.

Backup copies are not used for ConflictLab research analysis. If restoring a backup reintroduces a previously deleted active record and it can technically be identified, deletion must be re-applied.

## 9. Processor and transfers

ConflictLab uses **Hostinger** infrastructure.

Current account configuration verified by the owner:

```text
primary server: Lithuania
backup location: France
```

Hostinger's DPA describes Hostinger as Processor of Customer Data for Covered Services and permits authorized sub-processors under the DPA.

Appendix 3 provides the current authorized sub-processor list; this does not mean every listed sub-processor receives a particular ConflictLab record.

Where Customer Data are transferred outside the EEA to a jurisdiction without adequacy, the transfer safeguards described in Hostinger's DPA, including EU Standard Contractual Clauses where applicable, apply.

ConflictLab therefore does not promise that no technical processing can ever occur outside the EEA, even though the current primary storage and backup locations are in the EEA.

## 10. Tracking / advertising

The OMESG360 code for this timing study is designed without Google Analytics, Meta Pixel, advertising pixels, or other non-essential marketing trackers.

Hostinger access logs are not an advertising profile and are not used for psychological timing-research analysis.

## 11. Automated decisions

Timing-study data are not used for automated decisions producing legal or similarly significant effects, employment selection, ranking, health decisions, personality diagnosis or suitability assessment.

## 12. Your rights

Depending on the circumstances, GDPR rights may include information/access, rectification, erasure, restriction, portability where applicable, withdrawal of consent for future consent-based processing, and complaint to a supervisory authority.

Privacy contact: **info@omesg360.eu**.

In Lithuania, complaints may be lodged with the **State Data Protection Inspectorate (VDAI)**.

## 13. Age

The external timing study is for participants aged **18 or over**.

A simple age declaration is used; date of birth or identity documents are not collected for this purpose.

---

## Activation blockers remaining

This v0.2 is the source draft for the future active Calibration section / just-in-time notice. Do not mark it ACTIVE until:

```text
migrations 002/003 applied in live LAB
exact-head artifact deployed while TECHNICAL
consented + local-only + deletion + CSV TECHNICAL smoke tests pass
90-day retention cron configured/tested
legacy admin/security boundary reviewed/closed
technical/security LIA completed
public privacy.html aligned to the exact active implementation
activation record created
explicit owner authorization given
```
