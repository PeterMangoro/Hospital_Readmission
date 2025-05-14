# 🏥 Hospital Readmission Analysis & ETL Pipeline (PostgreSQL + Python)

This project is a data analytics case study focused on hospital readmissions. It utilizes PostgreSQL as the OLTP database and Python for ETL (Extract, Transform, Load), data processing, exploratory data analysis (EDA), and feature engineering. The primary goal is to analyze factors contributing to hospital readmissions and prepare a dataset suitable for future predictive modeling.

---

## 📌 Project Objectives

-   **Data Modeling:** Design and implement a relational data model for hospital admissions in PostgreSQL.
-   **ETL Pipeline:** Develop a robust ETL pipeline using Python to extract data from PostgreSQL, transform it for analysis, and load it into various formats (CSV, database tables).
-   **Data Enrichment & Feature Engineering:** Create new, insightful features from the existing data to better understand readmission patterns.
-   **Exploratory Data Analysis (EDA):** Perform comprehensive EDA to identify trends, patterns, and correlations related to hospital readmissions.
-   **Visualization:** Generate clear and informative visualizations to communicate findings from the EDA.
-   **Code Restructuring & Documentation:** Refactor the codebase for improved modularity, readability, and maintainability, accompanied by thorough documentation.

---

## 📂 Project Structure

The project is organized into the following directories:

```
Hospital_Readmission/
├── .gitignore
├── .vscode/                    # VSCode specific settings
│   └── settings.json
├── config/                     # Configuration files
│   ├── connect_pg.py           # Script for PostgreSQL database connection
│   └── connect_pg.py.template  # Template for connect_pg.py
├── data/                       # Data files
│   ├── processed/              # Processed and enriched data files
│   │   ├── admission_enriched.csv
│   │   └── transformed_admissions.csv
│   └── features.csv            # Engineered features for modeling
├── docs/                       # Project documentation
│   ├── Hospital_Readmission.docx # Original project documentation (if any)
│   ├── data_dictionary.md      # Details of data schemas and fields
│   └── project_overview.md     # In-depth project description
├── notebooks/                  # Jupyter notebooks for analysis
│   └── eda_analysis.ipynb      # Interactive EDA notebook
├── reports/                    # Reports and generated figures
│   ├── figures/                # Saved plots and visualizations
│   │   ├── eda_admissions_by_month.png
│   │   ├── eda_los_vs_readmission.png
│   │   ├── eda_readmission_by_age_group.png
│   │   ├── eda_readmission_by_gender.png
│   │   └── eda_readmission_by_specialty.png
│   └── analysis_report.md      # Summary of analysis and findings
├── src/                        # Source code for the project
│   ├── __init__.py
│   ├── data_extraction/        # Scripts for extracting data
│   │   ├── __init__.py
│   │   └── extract.py
│   ├── data_processing/        # Scripts for transforming and cleaning data
│   │   ├── __init__.py
│   │   ├── transform.py
│   │   └── feature_engineering.py
│   ├── database/               # Database related scripts and utilities
│   │   ├── __init__.py
│   │   ├── hospital_readmission.sql # SQL script for DDL and DML
│   │   └── db_utils.py           # Database utility functions
│   ├── etl/                    # ETL pipeline scripts
│   │   ├── __init__.py
│   │   ├── etl_dimensions.py
│   │   ├── etl_facts.py
│   │   └── etl_main_pipeline.py  # Main orchestrator for ETL
│   ├── analysis/               # Scripts for data analysis and enrichment
│   │   ├── __init__.py
│   │   ├── data_enrichment.py
│   │   └── exploratory_analysis.py
│   ├── loading/                # Scripts for loading data to destinations
│   │   ├── __init__.py
│   │   └── load.py
│   └── utils/                  # Utility functions and helpers
│       ├── __init__.py
│       └── helpers.py
├── tests/                      # Test scripts for the project
│   ├── __init__.py
│   ├── test_data_processing.py
│   └── test_etl.py
├── main.py                       # Main script to run pipelines/analyses
├── requirements.txt              # Python package dependencies
└── README.md                     # This file: Project overview and setup
```

---

## 📊 Tech Stack

-   **Python 3.x**
    -   `pandas`: For data manipulation and analysis.
    -   `SQLAlchemy`: For ORM and database interaction with PostgreSQL.
    -   `psycopg2-binary`: PostgreSQL adapter for Python.
    -   `matplotlib` & `seaborn`: For data visualization.
    -   `python-dotenv` (recommended): For managing environment variables.
-   **PostgreSQL**: Relational database management system.
-   **Jupyter Notebooks**: For interactive data exploration.
-   **Git**: For version control.

---

## 🚀 Features

-   **Modular ETL Pipeline:** Separate modules for extraction, transformation, and loading.
-   **Data Enrichment:** SQL-based data enrichment joining multiple tables.
-   **Feature Engineering:** Creation of new features like length of stay groups, admission month, and readmission labels.
-   **Comprehensive EDA:** Visualizations and statistical summaries of readmission trends by various factors (age, gender, specialty, length of stay).
-   **Structured Project Layout:** Organized folder structure for better maintainability and scalability.
-   **Configuration Management:** Centralized database connection configuration.

---

## 🛠️ Project Setup

### 1. Clone the Repository

```bash
git clone <repository_url> # Replace <repository_url> with the actual URL
cd Hospital_Readmission
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Ensure you have Python 3.x installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Setup the PostgreSQL Database

-   Ensure you have PostgreSQL installed and running.
-   Create a new database (e.g., `hospital_data`).
-   Execute the SQL script `src/database/hospital_readmission.sql` to create the necessary tables and populate initial data. You can use tools like `psql` or PgAdmin.

    ```bash
    psql -U your_username -d hospital_data -f src/database/hospital_readmission.sql
    ```

### 5. Configure Database Connection

-   Navigate to the `config/` directory.
-   Rename `connect_pg.py.template` to `connect_pg.py`.
-   Open `connect_pg.py` and update the database connection details (username, password, host, port, database name). **It is highly recommended to use environment variables for sensitive credentials instead of hardcoding them.**

    Example using `python-dotenv` (add `python-dotenv` to `requirements.txt`):

    Create a `.env` file in the project root with your credentials:
    ```env
    DB_USERNAME=your_postgres_username
    DB_PASSWORD=your_postgres_password
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=hospital_data
    ```

    Modify `config/connect_pg.py` to load these variables:
    ```python
    import os
    from sqlalchemy import create_engine
    from dotenv import load_dotenv

    load_dotenv() # Load variables from .env file

    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    if not all([username, password, host, port, database]):
        raise ValueError("One or more database connection environment variables are not set.")

    # SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
    ```

---

## ⚙️ Running the Project

The main entry point for running the ETL pipeline and analyses is `main.py`.

### Running the Full ETL Pipeline and Analysis

```bash
python main.py
```

This script will typically orchestrate the following steps:
1.  Extract data from the PostgreSQL database.
2.  Transform and clean the extracted data.
3.  Perform feature engineering.
4.  Load the processed data to CSV files and/or new database tables.
5.  Execute data enrichment queries.
6.  Generate EDA plots (saved in `reports/figures/`).

### Running Individual Components

You can also run individual scripts if needed, but ensure dependencies and data flow are managed correctly. Refer to the `main.py` script to understand the sequence of operations.

### Exploratory Data Analysis (Notebook)

For interactive EDA, you can use the Jupyter Notebook:

```bash
jupyter notebook notebooks/eda_analysis.ipynb
```

---

## 📝 Documentation

-   **This `README.md`**: Provides an overview, setup, and execution instructions.
-   **`docs/data_dictionary.md`**: Contains descriptions of database tables and CSV file columns.
-   **`docs/project_overview.md`**: Offers a more detailed explanation of the project, its components, and methodologies.
-   **Code Comments & Docstrings**: The source code in `src/` is commented, and functions/modules include docstrings explaining their purpose and usage.

---

## 🧪 Testing

Unit tests are located in the `tests/` directory. To run tests (assuming `pytest` is installed and configured):

```bash
pytest
```

---

## 🤝 Contributing

(Optional: Add guidelines for contributing if this is an open project.)

---

## 📜 License

(Optional: Specify the project license, e.g., MIT, Apache 2.0.)

