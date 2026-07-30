# ADR-009 — Behavior Translation Engine

**Status:** Accepted

**Date:** 2026-07-30

---

# Context

Iki šiol ConflictLab rezultatų sluoksnis daugiausia vertė signalus į refleksinius teiginius.

Pavyzdžiai:

- „Dažniau atsitraukei.“
- „Siekei daugiau kontrolės.“
- „Buvai neutralus.“

Nors šie teiginiai atitiko vidinę metodologiją, vartotojų testavimo metu paaiškėjo esminė problema.

Rezultatai:

- nekuria AHA momento;
- nepaaiškina, kas vyksta;
- atrodo kaip dar vienas psichologinis testas;
- pernelyg primena vidinius sistemos signalus.

ConflictLab tikslas nėra parodyti signalus.

ConflictLab tikslas yra padėti žmogui suprasti savo reakcijų dėsningumus.

---

# Decision

Įvedamas naujas produkto branduolys:

## Behavior Translation Engine

Signalai daugiau nebus pateikiami tiesiogiai vartotojui.

Jie tampa tik vidiniu analizės sluoksniu.

Vartotojui pateikiamas:

Signalai

↓

Dėsningumai

↓

Psichologinis reiškinys

↓

Žmogui suprantamas paaiškinimas

↓

Refleksijos klausimas

---

# New Result Structure

Kiekviena sesija turi keturias dalis.

## 1. Ką pastebėjome?

Tik objektyvus pastebėtas dėsningumas.

Be teorijų.

Be etikečių.

---

## 2. Kodėl taip galėjo nutikti?

Trumpas žmogui suprantamas paaiškinimas.

Psichologinės teorijos naudojamos tik kaip vidinis pagrindas.

Teorijų pavadinimai nerodomi.

---

## 3. Ką tai gali reikšti praktiškai?

Galimi privalumai.

Galimos rizikos.

Be absoliučių teiginių.

---

## 4. Refleksijos klausimas

Vienas klausimas.

Jo tikslas – pratęsti mąstymą už eksperimento ribų.

---

# Product Principle

ConflictLab neatsako:

> Kas tu esi?

ConflictLab padeda suprasti:

> Kas įvyko šios sesijos metu?

---

# Theoretical Role

Psichologinės teorijos daugiau nebėra galutinis rezultatas.

Jos tampa:

- paaiškinimo pagrindu;
- interpretacijos ribomis;
- AI apsauga nuo fantazavimo.

Teorijos nėra rodomos kaip etiketės.

Jos naudojamos tik tam, kad žmogui būtų paaiškintas pastebėtas reiškinys.

---

# Success Metric

Pagrindinis produkto KPI tampa ne algoritmo tikslumas.

Pagrindinis KPI:

## Reflection Resonance

Po sesijos žmogus turi pagalvoti:

> „Apie tai niekada nebuvau susimąstęs.“

Jeigu ši reakcija neįvyksta, rezultatas laikomas nepakankamai vertingu.

---

# Consequences

Teigiami:

- suprantamesni rezultatai;
- didesnė emocinė vertė;
- mažesnė diagnostikos iliuzija;
- aiškesnis ryšys tarp teorijos ir praktikos.

Neigiami:

- reikės visiškai perrašyti rezultatų generatorių;
- reikės sukurti Theory Translation Map;
- reikės naujo AHA Engine sluoksnio.
