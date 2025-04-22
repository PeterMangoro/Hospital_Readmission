import pandas as pd
from connect_pg import engine
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert

def load_dim_patient():
    query = """
    Select 
        patient_id,gender,date_of_birth,
        'Harare' as city, 'Zimbabwe' as country
    from patients;
    """

    df = pd.read_sql(query,engine)

    # Reflect the existing dim_patient table
    metadata = MetaData()
    metadata.reflect(bind=engine)
    dim_patient = metadata.tables['dim_patient']


    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = insert(dim_patient).values(**row.to_dict())
            stmt = stmt.on_conflict_do_update(
                index_elements=['patient_id'],  # primary key
                set_={
                    'gender': stmt.excluded.gender,
                    'date_of_birth': stmt.excluded.date_of_birth,
                    'city': stmt.excluded.city,
                    'country': stmt.excluded.country
                }
            )
            conn.execute(stmt)
    print("dim_patient loaded successfully")

if __name__ == "__main__":
    load_dim_patient()