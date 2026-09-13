# Code review

## Fynd 1 – Hela programmet körs på modulnivå

**Observation:**
Hela arbetsflödet körs direkt när modulen körs eller importeras. Det finns ingen `main()`-funktion som styr programstarten.

**Konsekvens:**
Om filen importeras från en annan modul kommer programmet direkt att läsa data, skapa rapporter och skriva filer. Det gör koden svårare att återanvända och testa.

**Förslag:**
Lägg programmets huvudflöde i en `main()`-funktion och använd en main guard för att styra när programmet ska starta.

## Fynd 2 – Flera ansvar är blandade i samma fil

**Observation:**
Samma script ansvarar för flera olika delar av programmet, till exempel filinläsning, validering, datastädning, beräkningar, rapportering och filsparning.

**Konsekvens:**
Koden blir svårare att överblicka, testa och återanvända. Om en del av programmet behöver ändras kan det också påverka andra delar i samma script.

**Förslag:**
Dela upp koden efter ansvar, så att exempelvis inläsning och bearbetning av data separeras från skapandet av rapporter och programmets huvudflöde.

## Fynd 3 – Felhanteringen är för generell

**Observation:**
Programmet använder ett generellt `Exception` med meddelandet `"Fel data"` när obligatoriska kolumner saknas. Dessutom fångas alla fel med `except Exception`.

**Konsekvens:**
Det blir svårt att förstå vad som faktiskt har gått fel. Till exempel framgår det inte vilken kolumn som saknas, och olika typer av fel hanteras på samma sätt.

**Förslag:**
Använd mer specifika fel, till exempel `ValueError` vid felaktig data och `FileNotFoundError` om filen saknas. Felmeddelanden bör också tydligt beskriva vad som är fel.

## Fynd 4 – Programmet använder print() för loggning

**Observation:**
Programmet använder `print()` för att visa information om vad som händer under körningen, till exempel när programmet startar, data läses in och rapporter sparas.

**Konsekvens:**
Det blir svårare att skilja mellan vanlig information, varningar och fel. `print()` ger inte heller samma möjlighet att styra vilken information som ska visas.

**Förslag:**
Ersätt `print()` som beskriver programmets körning med Python-modulen `logging` och använd lämpliga loggnivåer, till exempel `INFO`, `WARNING` och `ERROR`.

## Fynd 5 – Samma rapportlogik upprepas

**Observation:**
Rapporterna för försäljning per produktkategori och försäljning per region använder nästan samma kod. Skillnaden är främst vilken kolumn datan grupperas efter.

**Konsekvens:**
Upprepad kod gör programmet längre och svårare att underhålla. Om rapportlogiken behöver ändras måste samma ändring göras på flera ställen.

**Förslag:**
Flytta den gemensamma rapportlogiken till en återanvändbar funktion som tar emot vilken kolumn datan ska grupperas efter.

## Fynd 6 – Sökvägar och mappar hanteras inte robust

**Observation:**
Sökvägarna till indata och output är fasta, och programmet förutsätter att `data/orders.csv` och mappen `output` redan finns.

**Konsekvens:**
Programmet kan misslyckas om det körs från fel plats, om datafilen saknas eller om output-mappen inte har skapats.

**Förslag:**
Hantera sökvägar tydligare och kontrollera att datafilen finns. Skapa output-mappen automatiskt om den saknas.

## Fynd 7 – Vissa variabelnamn är otydliga

**Observation:**
Variabler som `result1` och `result2` beskriver inte tydligt vad resultaten innehåller.

**Konsekvens:**
Det blir svårare att följa dataflödet och förstå vilken rapport en variabel representerar.

**Förslag:**
Använd mer beskrivande namn, till exempel `sales_by_category` och `sales_by_region`.


## Prioritering

### Hög prioritet

* **Fynd 1 – Hela programmet körs på modulnivå**
* **Fynd 2 – Flera ansvar är blandade i samma fil**
* **Fynd 3 – Felhanteringen är för generell**

### Medelprioritet

* **Fynd 4 – Programmet använder `print()` för loggning**
* **Fynd 5 – Samma rapportlogik upprepas**
* **Fynd 6 – Sökvägar och mappar hanteras inte robust**

### Låg prioritet

* **Fynd 7 – Vissa variabelnamn är otydliga**

