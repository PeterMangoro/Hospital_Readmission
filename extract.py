import pandas as pd
from connect_pg import engine

def extract_admissions():
    query = "Select * from admissions"
    df = pd.read_sql(query,engine)
    return df