import pandas as pd
from connect_pg import engine

def load_fact_admissions():
    query = """
    SELECT 
        a.admission_id,
        a.patient_id,
        ad.doctor_id,
        dg.diagnosis_code,
        a.admission_date::date AS date_id,
        a.length_of_stay,
        a.readmitted
    FROM admissions a
    LEFT JOIN diagnoses dg ON a.admission_id = dg.admission_id
    LEFT JOIN admission_doctors ad ON a.admission_id = ad.admission_id;
    """
    df = pd.read_sql(query, engine)
    df.to_sql("fact_admissions", engine, index=False, if_exists="replace")
    print("fact_admissions loaded")

if __name__ == "__main__":
    load_fact_admissions()
