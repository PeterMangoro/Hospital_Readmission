from sqlalchemy import create_engine

# Replace with your actual PostgreSQL credentials
username = 'postgres'
password = 'your_password'
host = 'localhost'
port = '5432'
database = 'your_database_name'

# SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
