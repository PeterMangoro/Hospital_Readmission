import pandas as pd
from connect_pg import engine
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import insert

def load_dim_diagnosis():
    query = """
    select
        diagnosis_code,
        concat('Description of ', diagnosis_code) as description,
        'General' as category
    from diagnoses;
    """

    df = pd.read_sql(query,engine)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    dim_diagnosis = metadata.tables['dim_diagnosis']

    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = insert(dim_diagnosis).values(**row.to_dict())
            stmt = stmt.on_conflict_do_update(
                index_elements=['diagnosis_code'],
                set_={'description': stmt.excluded.description}
            )
            conn.execute(stmt)

if __name__=="__main__":
    load_dim_diagnosis()