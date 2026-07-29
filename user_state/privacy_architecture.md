# Privatumo ir Duomenų Apsaugos Architektūra (Privacy & Compliance Spec)

**Versija:** 1.0  
**Atitiktis:** ES BDAR (GDPR Art. 6, 9, 25, 32), ES DI Aktas (EU AI Act - High-Risk Avoidance).

---

## 1. Kertinis Principas: „Privacy by Design & Local-First“

„ConflictLab“ nerenka, nesaugo ir netvarko asmenį identifikuojančios informacijos (PII). Visi elgsenos modeliai, reakcijos laikai ir diagnostiniai duomenys yra generuojami ir saugomi **TIK klijento pusėje (Client-Side Storage)**.

---

## 2. Ilgalaikio Profilio ir Pokyčio Laike Saugojimas (Progress Tracking)

Norint palyginti žmogaus pažangą (pvz., šiandien vs. prieš 6 mėnesius), naudojami šie mechanizmai:

1. **Local IndexedDB Vault:** Visi istoriniai sesijų įrašai saugomi lokaliai naršyklės atmintyje.
2. **Encrypted State Export/Import:** Vartotojas gali atsisiųsti savo šifruotą profilio būseną `.conflictlab` formatu ir ją įsikelti bet kada vėliau.
3. **Zero-Knowledge Sync (Pasirenkamas):** Jei naudojama debesų sinchronizacija, duomenys serveryje saugomi tik užšifruoti AES-256 algoritmu. Šifravimo raktas generuojamas vartotojo įrenginyje ir niekada nepasiekia serverio.

---

## 3. ES DI Akto (EU AI Act) Apsaugos Taisyklės

1. **Ne-manipuliacinis pobūdis:** Sistema neturi tikslo pakeisti elgesį prieš asmens valią. Visi elgesio eksperimentai yra pateikiami kaip *savanoriški pasiūlymai refleksijai*.
2. **Skaidrumo Reikalavimas (Transparency):** Vartotojui visada aiškiai atskleidžiama, kad sąveikaujama su algoritmu, o ne su žmogumi-psichologu.
3. **Teisinis Atribojimas:** „ConflictLab“ nėra medicinos ar psichoterapijos prietaisas.

---

## 4. Anonymized AI Gateway Interface

Kai užklausa siunčiama į Didįjį Kalbos Modelį (LLM API), taikomas anonimizavimo filtras:

$$\text{User Raw Impulse} \longrightarrow \text{[ Anonymizer Filter ]} \longrightarrow \text{Abstract Behavioral Vector} \longrightarrow \text{LLM API}$$

- **Ištrinama:** Visi vardai, vietovardžiai, specifinės asmeninės detalės.
- **Paliekama:** Tik abstraktus elgsenos kodas (pvz., `Trigger: Visual_03, Latency: 1.1s, Choice: Control`).
