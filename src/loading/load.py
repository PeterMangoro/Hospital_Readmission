from config.connect_pg import engine # Updated import
import pandas as pd

def load_to_csv(df: pd.DataFrame, path: str = 'transformed_admissions'):
    """Saves a DataFrame to a CSV file.

    Args:
        df: The DataFrame to save.
        path: The base path (without .csv extension) for the output file.
              The .csv extension will be appended automatically.
              The path should be relative to the project root if not absolute.
    """
    full_path = path + ".csv"
    try:
        df.to_csv(full_path, index=False)
        print(f"Data successfully saved to {full_path}")
    except Exception as e:
        print(f"Error saving data to CSV {full_path}: {e}")

def load_to_db(df: pd.DataFrame, table_name: str = 'admission_cleaned'):
    """Loads a DataFrame into a specified table in the PostgreSQL database.

    Args:
        df: The DataFrame to load.
        table_name: The name of the target table in the database.
    """
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data successfully loaded into table: {table_name}")
    except Exception as e:
        print(f"Error loading data to table {table_name}: {e}")

