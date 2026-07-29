# Belief Engine (Įrodymų ir Hipotezių Kauptuvo Algoritmas)

**Versija:** 1.0  
**Paskirtis:** Apibrėžti matematinį-loginį mechanizmą, kaip spontaniškos vartotojo mikro-reakcijos (vaizdai, audio, tekstas) konvertuojamos į hipotezių pasitikėjimo svorius ($Confidence\ Score$), kaip tvarkomasi su prieštaringais duomenimis ir kada pasiekiamas slenkstis parodyti įžvalgą.

---

## 🏗️ Modelio Logika ir Būsenos

Belief Engine kiekvienai hipotezei $H_k \in \{H001, H002, \dots, H_n\}$ palaiko dinaminį pasitikėjimo rodiklį $C(H_k) \in [0.0, 1.0]$.

### Pasitikėjimo Slenksčiai (Confidence Thresholds):
- **$0.00 - 0.35$ (Triukšmas / Nepakanka duomenų):** Hipotezė pasyvi. Stimulai parenkami atsitiktiniu/bendruoju būdu.
- **$0.36 - 0.79$ (Aktyvus Tikrinimas):** Hipotezė iškelta. `/adaptive` modulis perima valdymą ir siunčia tikslinius stimulus neapibrėžtumui sumažinti.
- **$\ge 0.80$ (Trianguliuota Įžvalga):** Hipotezė laikoma patvirtinta per $\ge 3$ skirtingas medijos formas. Sugeneruojama įžvalga (`Reflection Mirror`).

---

## 🧮 Įrodymų Sumavimo Algoritmas (Evidence Accumulation)

Kiekvienas vartotojo pasirinkimas $E_i$ (Event / Evidence) turi tris kintamuosius:
1. **Medijos Formą ($m \in \{\text{visual}, \text{audio}, \text{scenario}\}$)**
2. **Reakcijos Greičio Svorį ($W_{\Delta t}$):**
   $$W_{\Delta t} = \begin{cases}     1.5 & \text{jei } \Delta t < 1.5\text{ s (Spontaniška amigdalos reakcija)} \\    1.0 & \text{jei } 1.5\text{ s } \le \Delta t \le 4.0\text{ s (Standartinė reakcija)} \\    0.5 & \text{jei } \Delta t > 4.0\text{ s (Kognityvinis pervertinimas / Racionalizacija)}    \end{cases}$$
3. **Poveikio Vektorių ($\Delta C_{base}$):** Nustatytas `model/hypothesis_weights.md` faile (pvz., $+0.20$ arba $-0.15$).

### Formulė: Naujo Pasitikėjimo Apskaičiavimas

Naujas pasitikėjimas $C_{new}(H_k)$ po atsakymo $E_i$ apskaičiuojamas taip:

$$C_{new}(H_k) = \text{Clamp}\left( C_{old}(H_k) + (\Delta C_{base} \cdot W_{\Delta t}), \ 0.0, \ 1.0 \right)$$

---

## ⚡ Prieštaravimų Valdymas (Contradiction Rules)

Jei vartotojas siunčia priešingus signalus (pvz., Vizualiniame stimule renkasi *Atsitraukimą* ($\Delta C = +0.25$), o Audio stimule – *Dominavimą / Kovą* ($\Delta C = -0.30$)):

1. **Prieštaravimo Indekso Didėjimas ($D_{index}$):**
   - Sistema padidina Prieštaravimo Indeksą: $D_{index} = D_{index} + 1$.
2. **Triukšmo Slopinimas:**
   - Jei $D_{index} \ge 2$, pasitikėjimo rodiklis $C(H_k)$ dirbtinai traukiamas link neutralaus $0.50$.
3. **Adaptyvus Reagavimas (`/adaptive`):**
   - Sistema konstatuoja **Kontekstinį Prieštaravimą** ir inicijuoja specialų gilinamąjį scenarijų, tikrinantį, ar elgesys skiriasi priklausomai nuo aplinkos (pvz., Darbas vs. Šeima).

---

## 📐 Trianguliacijos Taisyklė (The Rule of 3 Media Types)

Net jeigu matematinis $C(H_k)$ pasiekia $0.80$, hipotezė **NENUSIUNČIAMA** į įžvalgų variklį (`engine/synthesis.md`), kol neįvykdyta sąlyga:

$$\text{ConfirmedMediaTypes}(H_k) = \{\text{visual}, \text{audio}, \text{scenario}\}$$

Tik kai bent po vieną teigiamą patvirtinimą gauta iš **visų trijų skirtingų medijos šaltinių**, $Confidence\ Score$ oficialiai užfiksuojamas kaip patikimas.

---

## 🔄 Triukšmo ir Neapibrėžtumo Mažinimo Ciklas

```text
[ Naujas Stimulas ]
        │
        ▼
[ Fiksuojamas Atsakas + Δt ]
        │
        ▼
[ Apskaičiuojamas C_new(H_k) ]
        │
        ├─► C < 0.80 ARBA MediaTypes < 3 ──► Parinkti kitą modulio /adaptive stimulą
        │
        └─► C ≥ 0.80 IR MediaTypes = 3   ──► Perduoti į engine/synthesis.md (Sugeneruoti Įžvalgą)
        
