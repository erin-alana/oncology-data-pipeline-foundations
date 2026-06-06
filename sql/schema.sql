CREATE TABLE patients (
    patient_id TEXT PRIMARY KEY,
    age_at_diagnosis INTEGER,
    sex TEXT,
    primary_site TEXT,
    histology TEXT,
    stage TEXT,
    vital_status TEXT,
    is_advanced_stage BOOLEAN,
    age_group_at_diagnosis TEXT
);
