from connect_pg import engine
import pandas as pd

def get_enriched_admissions():
    query = """
    Select
        a.admission_id,
        a.patient_id,
        p.first_name ||' ' || p.last_name AS patient_name,
        p.gender,
        DATE_PART('year', AGE(p.date_of_birth)) AS age,
        a.admission_date,
        a.discharge_date,
        a.length_of_stay,
        a.readmitted,
        d.doctor_id,
        d.first_name||' ' || d.last_name  AS doctor_name,
        d.specialty,
        dg.diagnosis_code,
        dg.description

        from admissions a
        join patients p on p.patient_id = a.patient_id
        left join diagnoses dg on a.admission_id = dg.admission_id
        left join admission_doctors ad on a.admission_id = ad.admission_id
        left join doctors d on ad.doctor_id = d.doctor_id;
    """
    df = pd.read_sql(query,engine)
    return df
