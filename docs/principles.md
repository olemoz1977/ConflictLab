# ConflictLab Metodologiniai Principai

Šie principai apibrėžia architektūrinius ir algoritminius apribojimus, pagal kuriuos kuriami visi `/perception`, `/adaptive` ir `/engine` moduliai.

---

## I. Trijų Lygmenų Atskyrimo Principas
Kiekviename analizės žingsnyje sistema privalo griežtai atskirti 3 elementus:
1. **Stebėjimą (Observation):** Obyktyvūs duomenys (pasirinktas opcija X, reakcijos laikas $1.2\text{ s}$).
2. **Hipotezę (Hypothesis):** Galimas dėsningumas pagal teorijų karkasą (pvz., H002 – atmetimo baimė).
3. **Išvadą (Conclusion):** Sugeneruota įžvalga, pateikiama vartotojui TIK pasiekus pakankamą įrodymų trianguliaciją.

## II. Greičio Filtro Principas (Latency Rule)
- Reakcija, atlikta per **$< 1.5\text{ s}$**, laikoma spontanišku autonominės nervų sistemos atsaku (amigdalos lygmuo).
- Reakcija, atlikta per **$> 4.0\text{ s}$**, rodo įsijungusį kognityvinį pervertinimą, abejonę arba racionalizaciją.
- Sistema naudoja laiko matmenį kaip kintamąjį atpažįstant tikrąsias emocines reakcijas.

## III. Adaptyvaus Stimulo Principas
Kiekvienas vartotojo pasirinkimas pakeičia kito stimulo pobūdį. Sistema veikia ne pagal fiksuotą klausimyną, o kaip **mokslinis hipotezių tikrinimo algoritmas**:
- Jei pastebima vengimo tendencija $\rightarrow$ generuojamas stimulas, tikrinantis ar vengimas kyla dėl *Statuso* ar *Saugumo* grėsmės (SCARF modelis).

## IV. Ne-vertinančios Kalbos Principas
Visi sisteminiai tekstai, interpretacijos ir įžvalgos turi būti parašyti nenaudojant teisiamųjų, diagnostinių ar klinikinio pobūdžio terminų. Naudojama tyrinėjanti, dialogiška ir atsakomybę grąžinanti kalba.
