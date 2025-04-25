import pandas as pd
from connect_pg import engine
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import insert

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

    # Reflect existing table
    metadata = MetaData()
    metadata.reflect(bind=engine)
    fact_admissions = metadata.tables['fact_admissions']

    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = insert(fact_admissions).values(**row.to_dict())
            stmt = stmt.on_conflict_do_update(
                index_elements=['admission_id'],
                set_={
                    'patient_id': stmt.excluded.patient_id,
                    'doctor_id': stmt.excluded.doctor_id,
                    'diagnosis_code': stmt.excluded.diagnosis_code,
                    'date_id': stmt.excluded.date_id,
                    'length_of_stay': stmt.excluded.length_of_stay,
                    'readmitted': stmt.excluded.readmitted
                }
            )
            conn.execute(stmt)
    print("fact_admissions loaded successfully")

if __name__ == "__main__":
    load_fact_admissions()
