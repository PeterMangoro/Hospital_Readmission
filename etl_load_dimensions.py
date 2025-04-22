from etl_dim_patient import load_dim_patient
from etl_dim_doctor import load_dim_doc
from etl_dim_diagnosis import load_dim_diagnosis
from etl_dim_date import load_dim_date
from etl_fact_admissions import load_fact_admissions

if __name__ == "__main__":
    load_dim_patient()
    load_dim_doc()
    load_dim_diagnosis()
    load_dim_date()
    load_fact_admissions()
    print(" All dimension ETL jobs completed.")
