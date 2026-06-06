# Oncology Data Quality Risk Review

## Purpose

This document identifies potential data quality risks within the oncology data pipeline and outlines mitigation strategies.

---

## Missing Stage

Risk:
Patients may be missing stage information.

Impact:
Incorrect cohort selection, inaccurate analytics, and reporting errors.

Mitigation:
Flag records with missing stage values during validation.

---

## Invalid Age at Diagnosis

Risk:
Age at diagnosis may be negative, missing, or unrealistically high.

Impact:
Can distort cohort definitions and outcomes analyses.

Mitigation:
Validate age_at_diagnosis is between 0 and 120.

---

## Duplicate Patient IDs

Risk:
Multiple records may exist for the same patient.

Impact:
Inflated patient counts and inaccurate metrics.

Mitigation:
Check for duplicate patient identifiers during validation.

---

## Invalid Stage Values

Risk:
Stage values may not conform to accepted categories.

Impact:
Incorrect disease severity reporting.

Mitigation:
Restrict stage values to I, II, III, and IV.

---

## Future Risks

Potential future risks include:

- Missing biomarker data
- Invalid diagnosis dates
- Histology coding inconsistencies
- NLP abstraction errors
- Human review discrepancies
