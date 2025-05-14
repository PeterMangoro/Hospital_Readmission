import pandas as pd
from config.connect_pg import engine # Updated import

def extract_admissions():
    """Extracts all admission records from the admissions table in the database."""
    query = "SELECT * FROM admissions"
    print(f"Executing query: {query}")
    try:
        df = pd.read_sql(query, engine)
        print(f"Successfully extracted {len(df)} records from admissions table.")
        return df
    except Exception as e:
        print(f"Error extracting admissions data: {e}")
        # Depending on the desired behavior, you might want to raise the exception,
        # return an empty DataFrame, or handle it in another way.
        return pd.DataFrame() # Return empty DataFrame on error