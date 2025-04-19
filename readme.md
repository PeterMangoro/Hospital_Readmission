# 🏥 Hospital Readmission Analysis & ETL Pipeline (PostgreSQL + Python)

This project is a Master's-level data analytics case study focused on hospital readmissions. It uses PostgreSQL as the OLTP database and Python for ETL (Extract, Transform, Load), exploration, and visualization.

---

## 📌 Project Objectives

- Build a mini hospital data model in PostgreSQL
- Populate realistic synthetic patient, doctor, and admission data
- Use Python to extract and transform admission records
- Perform readmission analysis and visualize trends
- Prepare the dataset for future predictive modeling

---

## 📊 Tech Stack

- **Python 3**
  - `pandas`, `SQLAlchemy`, `psycopg2`, `matplotlib`, `seaborn`
- **PostgreSQL**
  - Tables: `patients`, `doctors`, `admissions`, `diagnoses`, etc.
- **SQLAlchemy**: for Python-PostgreSQL integration
- **VSCode** + local PostgreSQL server on Windows 11

---

## 🚀 Features

- Generate and populate normalized patient & admission data
- Extract data into Python for analysis
- Clean and transform data (ETL process)
- Engineer new features like:
  - Length of stay groups
  - Monthly trends
  - Readmission flags
- Visualize readmission statistics

---

## 🛠️ Project Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/hospital-readmission-etl.git
cd hospital-readmission-etl
```

### 2. Install dependencies
```
python -m pip install -r requirements.txt
```
or just run
```
python -m pip install pandas sqlalchemy psycopg2-binary matplotlib seaborn
```
### 4. Setup the Database
Create a PostgreSQL database called hospital_data

Run your table creation and sample data SQL scripts

You can use PgAdmin or psql to run the SQL.

### 5. Configure Connection
Update connect_pg.py with your local PostgreSQL credentials:
Copy and Paste the connect_pg_sample to a new connect_pg.py file
setup the environment to your credentials
```
#create connect_pg.py

from sqlalchemy import create_engine

# Replace with your actual PostgreSQL credentials
username = 'postgres'
password = 'your_password'
host = 'localhost'
port = '5432'
database = 'your_database_name'

# SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

```
### 6. Run ETL & Analysis

python explore_admissions.py