from sqlalchemy import create_engine
import pandas as pd

# Replace with your actual PostgreSQL credentials
username = 'postgres'
password = 'your_password'
host = 'localhost'
port = '5432'
database = 'hospital_data'

# SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# Load the admissions table
df_admissions = pd.read_sql("SELECT * FROM admissions", engine)

# Preview data
print(df_admissions.head())
