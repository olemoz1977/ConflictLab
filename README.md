# ConflictLab

**ConflictLab** – tai adaptyvus kognityvinės elgsenos modeliavimo ir „aklojo taško“ (*Blind Spot*) diagnostikos karkasas. 

Skirtingai nuo tradicinių testų ar stacionarių anketų, sistema remiasi ne žmogaus deklaracijomis (kurioms būdinga racionalizacija ir gynybinis šališkumas), o **pasikartojančiais spontaniškų reakcijų dėsningumais**, išgaunamais per multimodalinius mikro-stimulus.

---

## 🎯 Esminė Filosofija ir Principas

> *„Žmonės dažnai negali patikimai papasakoti, kodėl elgiasi vienaip ar kitaip. Todėl sistema remiasi ne pasakojimais apie elgesį, o spontaniškų reakcijų stebėjimu per skirtingas medijos formas.“*

Kai žmogus atsako į tekstinį klausimą, jame įsijungia kognityviniai filtrai ir gynybiniai mechanizmai. Naudojant **ne-tekstinius stimulus (vaizdus, pseudokalbos intonacijas, mikro-pasirinkimus laike)**, sistema fiksuoja grynąją pirminę reakciją, praleisdama ją pro smegenų amigdalos ir autonominės nervų sistemos lygmenį.

---

## 🏗️ Architektūra ir Duomenų Srautas

Sistema veikia per 4 sąveikaujančius sluoksnius:
[ Multimodaliniai Stimulai ] (/stimuli)
├─ Vizualiniai trigeriai
├─ Audio / Pseudokalbos intonacijos
└─ Micro-scenarijai (greiti pasirinkimai)
│
▼
[ Stebėjimo Sluoksnis ] (/perception)
├─ Reakcijos greitis (Latency < 1.5s)
└─ Pasirinkimo šališkumo fiksavimas
│
▼
[ Adaptyvusis Variklis ] (/adaptive)
├─ Hipotezių tikrinimas (A/B testing ant elgesio)
└─ Kito tikslinio stimulo parinkimas
│
▼
[ Kognityvinis Variklis ] (/theories & /core)
├─ Teorijų atitikimas (SCARF, Polyvagal, Karpman ir kt.)
└─ Blind Spots identifikavimas & Transformacija

---

## 📁 Projekto Struktūra

- **`/core`**: Pagrindinis žmogaus reagavimo grandinės modelis (`human_model.md`), interpretacijos filtrai ir transformacijos kelias.
- **`/stimuli`**: Multimodalinių trigerių katalogas (vizualiniai atstumai, kūno kalba, balso intonacijos, greitojo pasirinkimo situacijos).
- **`/perception`**: Mikro-reakcijų ir pasąmoninių dėsningumų fiksavimo mechanizmas (objektyvus stebėjimas be teisimo).
- **`/adaptive`**: Dinaminis interviu / patirties generatorius, parenkantis kitą stimulą pagal iškeltą hipotezę.
- **`/theories`**: 15 mokslinių teorijų bazė (neurologinės, kognityvinės, socialinės-santykių).
- **`/hypotheses`**: Patikrinamų elgsenos hipotezių katalogas (H001–H004 ir kt.).
- **`/engine`**: Analizės pipeline, sintezės ir išvesčių schemos.

---

## ⚖️ Bešališkumo Garantija (Trianguliacija)

Sistema neklijuoja etikečių pagal 1 ar 2 atsakymus. Hipotezė patvirtinama tik atlikus **trianguliaciją tarp 3 skirtingų medijos formų**:
1. Abstraktus vaizdas / vizualinė situacija.
2. Garso intonacija (pseudokalba).
3. Sąmoningas elgesio pasirinkimas scenarijuje.

Gauta išvada pateikiama ne kaip verdiktas, o kaip **veidrodis refleksijai**:  
*„3 skirtingose situacijose pasirinkai atsitraukimą, kai išgirdai neaiškų balso toną. Ar pastebi šį dėsningumą savo kasdienybėje?“*
