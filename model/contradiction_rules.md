# Prieštaravimų Valdymo Taisyklės (Contradiction Rules)

**Versija:** 1.0  
**Paskirtis:** Apibrėžti sisteminį ir algoritminį atsaką, kai vartotojo mikro-reakcijos siunčia viena kitai prieštaraujančius signalus tarp skirtingų medijos formų ar reakcijos laikų.

---

## 1. Prieštaravimo Tipai ir Diagnostika

Prieštaravimas užfiksuojamas, kai po naujo įvykio $E_i$ hipotezės pokytis yra priešingos krypties nei ankstesnis trendas ($\text{Sign}(\Delta C_{new}) \neq \text{Sign}(\Delta C_{prev})$).

Sistemoje išskiriami du pagrindiniai prieštaravimų tipai:

### Tipas A: Reakcijos Greičio Prieštaravimas (Spontaneous vs. Rationalized)
* **Požymis:** Spontaniškoje reakcijoje ($\Delta t < 1.5\text{ s}$) pasirenkama gynybinė / atsitraukimo opcija, o lėtoje reakcijoje ($\Delta t > 4.0\text{ s}$) renkasi konstruktyvų / idealų elgesį.
* **Diagnozė:** Kognityvinė racionalizacija (Social Desirability Bias). Žmogus nori atrodyti atsparus / konstruktyvus, nors kūnas / amigdala jaučia grėsmę.
* **Algoritminis sprendimas:** 
  - **Svoris nemažinamas:** Spontaniškos reakcijos $C(H_k)$ svoris išlieka nepakitęs.
  - **Užfiksuojamas „Aklasis taškas“ (Blind Spot):** Sugeneruojama žyma `RATIONALIZATION_GAP`.

### Tipas B: Medijų ir Konteksto Prieštaravimas (Cross-Media Split)
* **Požymis:** Vizualiniame stimule renkasi *Kovą / Kontrolę*, o Audio (intonacijos) stimule – *Atsitraukimą / Freeze*.
* **Diagnozė:** Kontekstinė elgsenos poliarizacija. Skirtingi trigeriai aktyvuoja skirtingas nervų sistemos būsenas (pvz., vizualinis neapibrėžtumas kelia norą valdyti, o balso intonacija kelia atstumties baimę).
* **Algoritminis sprendimas:** 
  - Hipotezės pasitikėjimas $C(H_k)$ koreguojamas link neutralaus $0.50$.
  - Inicijuojamas **Konteksto Vektoriaus patikrinimas** per `/adaptive` modulinį scenarijų.

---

## 2. Prieštaravimo Indekso ($D_{index}$) Skaičiavimas

Kiekvienai aktyviai hipotezei palaikomas Prieštaravimo Indeksas $D_{index} \in \mathbb{N}_0$:

$$\text{Jei } \Delta C_{new} \cdot \Delta C_{prev} < 0 \implies D_{index} = D_{index} + 1$$

### Indekso Reikšmių Poveikis:

| $D_{index}$ Reikšmė | Sistemos Būsena | Algoritminis Veiksmas |
| :--- | :--- | :--- |
| **$D_{index} = 0$** | Vientisa elgsena | Standartinis įrodymų kauptuvo režimas. |
| **$D_{index} = 1$** | Mikro-triukšmas | Ignoruojama, laukiama kito patvirtinančio stimulo. |
| **$D_{index} = 2$** | Kontekstinis skėlimasis | Daugikliai $W_{media}$ sumažinami $50\%$. `/adaptive` parenka kontrastinį stimulą. |
| **$D_{index} \ge 3$** | Hipotezės Mutacija | Hipotezė $H_k$ anuliuojama arba padalinama į dvi **Kontekstines Hipotezes** (pvz., $H001_{darbas}$ ir $H001_{namai}$). |

---

## 3. Kontekstinių Hipotezių Padalinimo Taisyklė (Hypothesis Splitting)

Jei $D_{index} \ge 3$, sistema pripažįsta, kad bendras elgesio dėsningumas neegzistuoja ir elgesys yra stipriai priklausomas nuo konteksto.

Duomenų struktūroje sugeneruojamos sub-hipotezės:

```json
{
  "parent_hypothesis": "H001",
  "status": "SPLIT_BY_CONTEXT",
  "sub_hypotheses": {
    "H001_professional": {
      "confidence": 0.82,
      "dominant_response": "control_and_dominance"
    },
    "H001_interpersonal": {
      "confidence": 0.78,
      "dominant_response": "avoidance_and_withdrawal"
    }
  }
}

_______



'''text
4. Atsakas Vartotojui („Veidrodžio“ Integravimas)
Prieštaravimas sistemoje NĖRA traktuojamas kaip klaida. Tai yra vertingiausia informacija apie žmogaus vidinius konfliktus.
Gauta išvestis reframinama per atspindėjimo principą:
„Pastebėjome įdomų dėsningumą: kai matai vizualinį neapibrėžtumą, tavo pirmoji reakcija per 1.1 sek. yra siekis perimti kontrolę. Tačiau kai išgirsti šaltą balso toną, renkiesi atsitraukti. Ar pastebi, kad tavo elgesį labiau valdo ne pati situacija, o trigerio forma?“

