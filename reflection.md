# Reflektion

## 1. Vilka var de viktigaste problemen i originalkoden?

Ett av de största problemen var att nästan all kod låg samlad i samma fil. Inläsning av data, validering, bearbetning, rapportskapande och sparande skedde på samma ställe, vilket gjorde koden svårare att överblicka och testa.

Programmet kördes också direkt när filen importerades och använde `print()` för statusmeddelanden. Felhanteringen bestod av en generell `try/except`, vilket gjorde det svårt att se vad som faktiskt hade gått fel.

Det fanns även duplicerad kod för rapporterna och vissa variabelnamn, till exempel `result1` och `result2`, beskrev inte tydligt vad de innehöll.


## 2. Vilka är de största förbättringarna efter refaktoreringen?

Den största förbättringen är att programmet nu är uppdelat i mindre moduler med tydliga ansvarsområden för bland annat inläsning, validering, transformation, rapportskapande och sparande.

Programmet har också fått tydligare felhantering, central konfiguration av logging och en tydlig startpunkt med `main()`.

En annan viktig förbättring är att de olika delarna nu går att testa separat med pytest.


## 3. Varför valde du den här modulstrukturen?

Jag valde att dela upp programmet efter ansvar. Varje modul har därför en tydlig uppgift.

Till exempel ansvarar `io.py` för filer, `validation.py` för validering, `transform.py` för bearbetning av data och `reports.py` för att skapa rapporterna. `pipeline.py` binder sedan ihop de olika delarna och styr i vilken ordning de ska köras.

Jag valde denna struktur eftersom den gör det lättare att förstå var olika delar av koden hör hemma. Det gör också funktionerna enklare att testa och programmet lättare att ändra eller bygga vidare på.


## 4. Var och varför använde du OOP eller dataclass?

Jag använde en dataclass, `ReportConfig`, för att samla sökvägarna till programmets inputfil och outputmapp.

En dataclass passade bra här eftersom sökvägarna är information som hör ihop och tillsammans beskriver programmets konfiguration. Istället för att hantera dem som separata värden kan de samlas i ett `ReportConfig`-objekt och skickas vidare till programmets pipeline.

Övriga delar, som validering, transformation och rapportskapande, passade bättre som vanliga funktioner. De tar emot data, utför en uppgift och behöver inte spara någon information mellan körningarna.


## 5. Vad skyddar dina tester?

Testerna hjälper till att kontrollera att de viktigaste delarna av programmet fortsätter fungera som de ska.

De kontrollerar bland annat att valideringen reagerar på tom data och saknade kolumner, att orderdata städas och omvandlas korrekt och att felaktiga numeriska värden hanteras.

Jag testar också att transformationen inte ändrar den ursprungliga DataFramen och att rapporternas beräkningar blir rätt.

IO-testerna kontrollerar att programmet kan läsa och spara CSV-filer, skapa outputmappen vid behov och ger ett tydligt fel om inputfilen saknas.


## 6. Vad var svårast i arbetet?

Det svåraste för mig har varit alla nya begrepp och att förstå när de olika delarna ska användas. Det är inte själva syntaxen som är svårast, utan att veta vilka val som är lämpliga i olika situationer.

Till exempel tyckte jag att det var svårt att avgöra vad som bör loggas och när, vilka delar av ett program som är viktiga att testa och vilka tester som faktiskt tillför något. Samma sak gäller OOP – när passar en klass och när räcker det med en vanlig funktion?

## 7. Vad skulle du förbättra vidare om du hade mer tid?

Om projektet skulle utvecklas vidare skulle jag kunna lägga till mer validering av datan, till exempel kontrollera negativa antal eller priser och att rabatt ligger inom ett rimligt intervall.

Felhanteringen skulle också kunna utvecklas, till exempel för en helt tom CSV-fil utan kolumnrubriker.

Jag skulle även kunna göra input- och outputsökvägarna konfigurerbara vid körning istället för att endast använda standardsökvägarna i `ReportConfig`.