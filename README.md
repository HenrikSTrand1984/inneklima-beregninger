---
title: "Inneklima – Beregningsmoduler"
document_id: "INNEKLIMA-CALC-0001"
version: "1.0"
status: "Aktiv"
date: 2025-08-28
owner: "Hs"
contact: "hs@info.no"
path: "/projects/inneklima_beregninger/README.md"
tags: ["inneklima", "beregninger", "ventilasjon", "CO2", "varmelast", "python"]
license: "CC-BY-SA-4.0"
---

# 🌿 Inneklima – Beregningsmoduler

Python-implementasjon av formler fra **vedlegg A2 og A3** for inneklima-beregninger:  
- Ventilasjonsberegning  
- CO₂-nivå og luftkvalitet  
- Varmelast  

Prosjektet gir grunnlag for verifisering av prosjekteringsmål i ventilasjon og inneklima, og kan kobles videre mot simulering og dokumentasjon.

---

## 📦 Installasjon

1. **Installer Poetry**  
   ```bash
   pip install poetry
   ```

2. **Installer dependencies**  
   ```bash
   poetry install
   ```

---

## ▶️ Bruk

Kjør en beregningsfil, f.eks. ventilasjon:  
```bash
poetry run python src/a2/a2_ventilasjon.py
```

Alle scripts ligger under `src/` strukturert etter vedlegg (A2, A3 osv.).

---

## 🧪 Tester

Kjør alle tester med:  
```bash
poetry run pytest tests/
```

Testene dekker formelimplementasjoner og validering mot kjente eksempler.

---

## ⚙️ CI/CD (GitHub Actions)

Automatisk kjøring av scripts og tester via workflow:  
```
.github/workflows/ci_pipeline.yml
```

- Kjører pytest på alle commits og pull requests  
- Sikrer at beregningene forblir stabile  

---

## 📚 Videre arbeid

- Utvide med flere beregningsmoduler (f.eks. akustikk, fuktnivå, energibalanse).  
- Integrasjon mot dokumentasjonsfiler i repoet.  
- Eksport av resultater til Excel/CSV for prosjektdokumentasjon.  

---

## 📄 Lisens

© 2025 Hs – Licensed under **CC BY-SA 4.0**  
Se [LICENSE.md](../../LICENSE.md) for detaljer.

---
