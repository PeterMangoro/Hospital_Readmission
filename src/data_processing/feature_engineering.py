import pandas as pd
from config.connect_pg import engine

def extract_features():
    query = """
    SELECT 
        a.admission_id,
        p.gender,
        DATE_PART('year', AGE(p.date_of_birth)) AS age,
        a.length_of_stay,
        a.readmitted,
        d.specialty,
        dg.diagnosis_code
    FROM admissions a
    join patients p on a.patient_id = p.patient_id
    left join diagnoses dg on a.admission_id = dg.admission_id
    left join admission_doctors ad on a.admission_id = ad.admission_id
    left join doctors d on ad.doctor_id = d.doctor_id ;
    """

    df = pd.read_sql(query,engine)

    # Group by admission_id to count diagnoses
    diag_count = df.groupby('admission_id')['diagnosis_code'].nunique().reset_index()
    diag_count.columns = ['admission_id','number_of_diagnosis']

    # Merge back
    df  = df.drop(columns=['diagnosis_code'])
    df = df.drop_duplicates()
    df = df.merge(diag_count,on='admission_id',how='left')
    
    # One-hot encode gender and specialty
    df = pd.get_dummies(df,columns=['gender','specialty'],drop_first=True)

    return df

if __name__ == "__main__":
    df = extract_features()
    print(df.head())
    df.to_csv("features.csv", index=False)
    print("Feature dataset saved to features")