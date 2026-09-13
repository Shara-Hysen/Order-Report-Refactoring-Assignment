# Order Report – Refactoring

## Beskrivning

Detta projekt är en refaktorering av ett befintligt Pythonprogram för orderrapportering.

Programmet läser orderdata från en CSV-fil, bearbetar datan och skapar rapporter över bland annat försäljning och returer.

Målet med uppgiften är att förbättra programmets struktur, läsbarhet, testbarhet och felhantering utan att förändra programmets resultat.

I refaktoreringen har programmet bland annat delats upp i mindre moduler med tydliga ansvarsområden. Jag har även lagt till validering, logging, tester med pytest samt en dataclass för programmets konfiguration.


## Funktionalitet

Programmet:

- läser in orderdata från CSV
- validerar att datan innehåller nödvändiga kolumner och rader
- städar och bearbetar orderdatan
- hanterar saknade och felaktiga numeriska värden
- beräknar ordervärde och rabatterat ordervärde
- skapar rapporter över försäljning och returer
- sparar rapporterna som CSV-filer
- använder logging för att visa programmets körflöde


## Rapporter

Programmet skapar följande rapporter i mappen `output/`:

- `overview.csv` – översikt över total försäljning, antal ordrar och antal returer
- `sales_by_category.csv` – försäljning och returer per produktkategori
- `sales_by_region.csv` – försäljning och returer per region
- `returns_by_category.csv` – returfrekvens per produktkategori


## Filstruktur

```text
data/
    orders.csv

src/
    order_report/
        __init__.py
        __main__.py
        config.py
        io.py
        logging_config.py
        pipeline.py
        reports.py
        transform.py
        validation.py

tests/
    test_io.py
    test_reports.py
    test_transform.py
    test_validation.py

output/
code_review.md
original_order_report.py
README.md
requirements.txt
pyproject.toml
```

Koden är uppdelad efter ansvar:

- `config.py` – konfiguration och sökvägar
- `io.py` – inläsning och sparande av CSV-filer
- `validation.py` – validering av orderdata
- `transform.py` – städning och bearbetning av data
- `reports.py` – skapande av rapporter
- `pipeline.py` – styr programmets arbetsflöde
- `logging_config.py` – central konfiguration av logging
- `__main__.py` – programmets startpunkt


## Miljö

Python 3.13.7


## Installation och körning

1. **Klona repositoryt:**

```bash
git clone https://github.com/Shara-Hysen/Order-Report-Refactoring-Assignment.git
cd Order-Report-Refactoring-Assignment
```

2. **Skapa och aktivera virtuell miljö:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. **Installera beroenden:**

```bash
pip install -r requirements.txt
```

4. **Installera projektet i editable mode:**

```bash
pip install -e .
```

5. **Kör programmet:**

```bash
python -m order_report
```

Programmet läser orderdata från `data/orders.csv` och sparar de färdiga rapporterna i mappen `output/`.


## Tester

Projektet innehåller automatiska tester med pytest.

Testerna kontrollerar bland annat:

- validering av tom data och saknade kolumner
- städning och transformation av orderdata
- hantering av felaktiga numeriska värden
- att originaldatan inte förändras vid transformation
- beräkningar och skapande av rapporter
- inläsning och sparande av CSV-filer
- hantering av saknad datafil

Kör samtliga tester med:

```bash
pytest
```


## Kodgranskning och refaktorering

En kodgranskning av originalprogrammet finns i `code_review.md`.

Där beskrivs identifierade problem i originalkoden, vilka konsekvenser de kan få och förslag på förbättringar.

Refaktoreringen har genomförts med målet att behålla programmets ursprungliga beteende samtidigt som koden har fått tydligare struktur och blivit enklare att testa och underhålla.


## Källor

Projektet är utvecklat som en examinationsuppgift med utgångspunkt i kursmaterial och laborationer, med stöd av AI-verktyg för kodgranskning och kodoptimering.