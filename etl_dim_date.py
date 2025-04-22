import pandas as pd
from connect_pg import engine
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import insert

def load_dim_date():
    query = """
    SELECT DISTINCT admission_date
    FROM admissions;
    """
    df = pd.read_sql(query, engine)
    df['date_id'] = df['admission_date']  # assuming this is the PK

    df['year'] = pd.to_datetime(df['admission_date']).dt.year
    df['month'] = pd.to_datetime(df['admission_date']).dt.month
    df['day'] = pd.to_datetime(df['admission_date']).dt.day
    df['weekday'] = pd.to_datetime(df['admission_date']).dt.day_name()

    df = df[['date_id', 'year', 'month', 'day', 'weekday']]

    metadata = MetaData()
    metadata.reflect(bind=engine)
    dim_date = metadata.tables['dim_date']

    with engine.begin() as conn:
        for _, row in df.iterrows():
            stmt = insert(dim_date).values(**row.to_dict())
            stmt = stmt.on_conflict_do_update(
                index_elements=['date_id'],
                set_={
                    'year': stmt.excluded.year,
                    'month': stmt.excluded.month,
                    'day': stmt.excluded.day,
                    'weekday': stmt.excluded.weekday
                }
            )
            conn.execute(stmt)
    print("dim_date loaded")

if __name__ == "__main__":
    load_dim_date()
