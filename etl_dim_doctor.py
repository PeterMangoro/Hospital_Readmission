import pandas as pd
from connect_pg import engine
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import insert

def load_dim_doc():
    query="""
    Select 
        doctor_id, specialty,
        'General Medicine' as department
    from doctors;
    """

    df = pd.read_sql(query,engine)
    
    metadata = MetaData()
    metadata.reflect(bind=engine)
    dim_doctor = metadata.tables['dim_doctor']

    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = insert(dim_doctor).values(**row.to_dict())
            stmt = stmt.on_conflict_do_update(
                index_elements=['doctor_id'],
                set_={
                    
                    'specialty': stmt.excluded.specialty
                }
            )
            conn.execute(stmt)
            
    print("dim_doctor loaded")

if __name__ == "__main__":
    load_dim_doc()