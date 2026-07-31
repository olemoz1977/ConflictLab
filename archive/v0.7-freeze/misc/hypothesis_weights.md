# Hipotezių Svorių Matrica (Hypothesis Weight Matrix)

**Versija:** 1.0  
**Paskirtis:** Apibrėžti pradines kintamųjų reikšmes, poveikio vektorius ($\Delta C_{base}$) ir daugiklius, kurie naudojami `model/belief_engine.md` algoritme apskaičiuojant hipotezių pasitikėjimo svorį.

---

## 1. Laiko Daugikliai (Latency Multipliers - $W_{\Delta t}$)

Reakcijos greitis parodo, kuris smegenų apdorojimo sluoksnis (amigdala vs. prefrontalinė žievė) priėmė sprendimą:

| Reakcijos laikas ($\Delta t$) | Sluoksnis | Daugiklis ($W_{\Delta t}$) | Interpretacija |
| :--- | :--- | :--- | :--- |
| **$< 1.5\text{ s}$** | Amigdala / ANS | **$1.5$** | Grynas spontaniškas impulsas (Didelis patikimumas) |
| **$1.5\text{ s} - 4.0\text{ s}$** | Standartinis | **$1.0$** | Normatyvus atsakymo laikas |
| **$> 4.0\text{ s}$** | Prefrontalinė žievė | **$0.5$** | Racionalizacija / Kognityvinis gynybinis filtras |

---

## 2. Medijos Svorio Daugikliai ($W_{media}$)

Kadangi ne visos medijų formos yra vienodai atsparios gynybiškumui, įvedamas medijos patikimumo koeficientas:

* **Vizualiniai stimulai (Images):** $W_{media} = 1.2$ (Mažiausiai racionalizuojama)
* **Audio / Pseudokalba (Intonacijos):** $W_{media} = 1.1$ (Tiesioginis emociškai palaikomo fono trigeris)
* **Tekstiniai scenarijai (Scenarios):** $W_{media} = 0.9$ (Lengviau racionalizuoti ir parinkti „teisingą“ atsakymą)

---

## 3. Hipotezių Poveikio Matrica ($\Delta C_{base}$)

Ši lentelė apibrėžia, kaip konkretus pasirinkimas tam tikrame stimule pakeičia bazinį pasitikėjimą hipoteze ($\Delta C_{base}$):

### Hipotezė H001: Autonomijos praradimo baimė ir gynybinė kontrolė
- **Pasirinkimas: Dominavimas / Reikalavimas perimti valdymą**
  - $\Delta C_{base} = +0.25$
- **Pasirinkimas: Atsitraukimas / Pasyvus prisitaikymas**
  - $\Delta C_{base} = -0.20$

### Hipotezė H002: Nerimastingas prisirišimas ir neigiamas šališkumas
- **Pasirinkimas: Neutralų / dviprasmišką signalą interpretuoti kaip atstūmimą**
  - $\Delta C_{base} = +0.30$
- **Pasirinkimas: Neutralų signalą interpretuoti kaip saugų / neapibrėžtą**
  - $\Delta C_{base} = -0.25$

### Hipotezė H003: Išorinis valdymo lokusas ir Kaltinimas
- **Pasirinkimas: Kito asmens motyvų teisimas („jis tyčia mane erzina“)**
  - $\Delta C_{base} = +0.20$
- **Pasirinkimas: Asmeninio indėlio / poreikio įvardijimas**
  - $\Delta C_{base} = -0.30$

### Hipotezė H004: Vengiantis prisirišimas ir emocinis atsiribojimas
- **Pasirinkimas: Konflikto nutraukimas / Fizinis arba emocinis pasitraukimas**
  - $\Delta C_{base} = +0.25$
- **Pasirinkimas: Eiti į pažeidžiamą dialogą**
  - $\Delta C_{base} = -0.35$

---

## 4. Pilna Formulė su Medijos Daugikliu

Galinė vieno įvykio ($E_i$) įtaka pasitikėjimo rodikliui skaičiuojama taip:

$$\Delta C = \Delta C_{base} \cdot W_{\Delta t} \cdot W_{media}$$

### Pavyzdys:
Vartotojas per **$1.1\text{ s}$** ($W_{\Delta t} = 1.5$) **vizualiniame stimule** ($W_{media} = 1.2$) pasirenka dviprasmiško vaizdo interpretaciją kaip atstūmimą ($\Delta C_{base} = +0.30$ dėl **H002**):

$$\Delta C = 0.30 \cdot 1.5 \cdot 1.2 = +0.54$$

*Šis vienas spontaniškas vizualinis pasirinkimas akimirksniu pakelia H002 pasitikėjimą iki $0.54$, kas aktyvuoja `/adaptive` modulį siųsti audio stimulą patikrinimui.*
