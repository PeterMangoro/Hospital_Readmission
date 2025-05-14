from config.connect_pg import engine # Updated import
import pandas as pd

def get_enriched_admissions() -> pd.DataFrame:
    """Retrieves enriched admission data by joining admissions, patients, doctors, and diagnoses tables.

    Returns:
        pd.DataFrame: A DataFrame containing the enriched admission records.
                      Returns an empty DataFrame if an error occurs.
    """
    query = """
    SELECT
        a.admission_id,
        a.patient_id,
        p.first_name || ' ' || p.last_name AS patient_name,
        p.gender,
        DATE_PART('year', AGE(p.date_of_birth)) AS age,
        a.admission_date,
        a.discharge_date,
        a.length_of_stay,
        a.readmitted,
        d.doctor_id,
        d.first_name || ' ' || d.last_name AS doctor_name,
        d.specialty,
        dg.diagnosis_code,
        dg.description
    FROM admissions a
    JOIN patients p ON p.patient_id = a.patient_id
    LEFT JOIN diagnoses dg ON a.admission_id = dg.admission_id
    LEFT JOIN admission_doctors ad ON a.admission_id = ad.admission_id
    LEFT JOIN doctors d ON ad.doctor_id = d.doctor_id;
    """
    print(f"Executing enrichment query...")
    try:
        df = pd.read_sql(query, engine)
        print(f"Successfully retrieved {len(df)} enriched admission records.")
        return df
    except Exception as e:
        print(f"Error retrieving enriched admissions data: {e}")
        return pd.DataFrame() # Return empty DataFrame on error

