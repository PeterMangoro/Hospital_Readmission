# Project Overview

## 1. Introduction

This project undertakes a comprehensive analysis of hospital readmission data. The primary objective is to identify key factors influencing patient readmissions within a specified timeframe after discharge. By leveraging a dataset encompassing patient demographics, admission details, medical history, and treatment information, the project aims to build a robust ETL (Extract, Transform, Load) pipeline, perform in-depth exploratory data analysis (EDA), and engineer relevant features. The ultimate goal is to prepare a clean, well-structured dataset that can be used for developing predictive models to forecast the likelihood of hospital readmission. Such models can aid healthcare providers in proactively identifying at-risk patients and implementing targeted interventions to reduce readmission rates, thereby improving patient outcomes and reducing healthcare costs.

The project involves several key stages:
*   **Data Modeling:** Designing a relational database schema in PostgreSQL to store and manage the hospital data effectively.
*   **ETL Pipeline Development:** Creating Python scripts to extract data from the source (PostgreSQL), perform necessary transformations (cleaning, formatting, deriving new attributes), and load the processed data into analytical tables or flat files (CSVs).
*   **Data Enrichment:** Combining data from various sources or tables to create a richer dataset for analysis.
*   **Feature Engineering:** Developing new features from the existing data that might have predictive power for readmission.
*   **Exploratory Data Analysis (EDA):** Utilizing statistical summaries and visualizations to uncover patterns, trends, and correlations within the data, particularly focusing on factors associated with readmission.
*   **Code Restructuring and Documentation:** Organizing the codebase into a modular and maintainable structure, and providing comprehensive documentation for clarity and ease of use.

## 2. Problem Statement

Hospital readmissions, particularly those occurring shortly after discharge, are a significant concern in the healthcare industry. They often indicate potential gaps in patient care, discharge planning, or post-discharge support. High readmission rates can lead to increased healthcare costs, reduced hospital efficiency, and negatively impact patient well-being. Understanding the drivers of readmission is crucial for developing effective strategies to mitigate this problem.

This project addresses this challenge by:
*   Analyzing historical patient and admission data to identify statistically significant factors correlated with readmission.
*   Developing a dataset that is well-suited for building machine learning models to predict readmission risk.

## 3. Data Sources

The primary data source for this project is a PostgreSQL relational database named `hospital_data`. This database is designed to simulate a hospital's information system and contains several interconnected tables, including:
*   `patients`: Information about individual patients (e.g., patient ID, name, date of birth, gender).
*   `doctors`: Information about medical doctors (e.g., doctor ID, name, specialty).
*   `admissions`: Details of each hospital admission (e.g., admission ID, patient ID, admission date, discharge date, length of stay, readmission status).
*   `diagnoses`: Diagnosis information linked to admissions (e.g., diagnosis code, description).
*   `admission_doctors`: Linking table for admissions and the doctors involved.

Synthetic data is used to populate these tables, reflecting realistic scenarios and distributions found in hospital admission records. The SQL script `src/database/hospital_readmission.sql` contains the DDL (Data Definition Language) for creating these tables and DML (Data Manipulation Language) for inserting sample data.

## 4. Methodology

The project follows a structured data analytics workflow:

1.  **Project Setup & Environment Configuration:** Cloning the repository, setting up a Python virtual environment, installing dependencies, and configuring the PostgreSQL database connection.
2.  **Data Extraction:** Python scripts connect to the PostgreSQL database using SQLAlchemy and extract raw data from the relevant tables (primarily `admissions`, `patients`, `doctors`, `diagnoses`).
3.  **Data Transformation & Cleaning:**
    *   Handling missing values (e.g., dropping rows with critical missing data).
    *   Converting data types (e.g., ensuring date columns are in datetime format).
    *   Data validation (e.g., ensuring `length_of_stay` is non-negative).
    *   Creating derived attributes like `admission_month`.
4.  **Feature Engineering:**
    *   Creating categorical features like `stay_length_group` based on `length_of_stay`.
    *   Mapping boolean `readmitted` flags to more descriptive labels (`Yes`/`No`).
5.  **Data Enrichment:** Joining data from multiple tables (e.g., `admissions`, `patients`, `doctors`, `diagnoses`) using SQL queries executed via Python to create a comprehensive analytical dataset (`admission_enriched.csv`).
6.  **Data Loading:** The transformed and enriched datasets are loaded into CSV files (`transformed_admissions.csv`, `admission_enriched.csv`) and potentially back into new tables in the PostgreSQL database for further analysis or reporting.
7.  **Exploratory Data Analysis (EDA):
    *   Generating descriptive statistics for key variables.
    *   Visualizing distributions of variables (e.g., length of stay).
    *   Analyzing readmission rates across different patient segments (e.g., by age group, gender, medical specialty).
    *   Identifying potential correlations between features and readmission status.
    *   EDA is performed using Python scripts (`src/analysis/exploratory_analysis.py`) and an interactive Jupyter Notebook (`notebooks/eda_analysis.ipynb`). Visualizations are saved as image files.
8.  **Code Refactoring and Documentation:** The entire codebase is structured into logical modules for better organization. Comprehensive documentation, including README files, code comments, docstrings, a data dictionary, and this project overview, is created.
9.  **Testing (Future Scope):** Implementation of unit tests using `pytest` to ensure the reliability of data processing and ETL functions.

## 5. Expected Outcomes and Deliverables

*   A fully restructured and well-documented Python project.
*   A robust ETL pipeline capable of processing hospital admission data.
*   Cleaned, transformed, and enriched datasets saved as CSV files (`transformed_admissions.csv`, `admission_enriched.csv`, `features.csv`).
*   A detailed exploratory data analysis report (`reports/analysis_report.md`) with supporting visualizations (`reports/figures/`).
*   A Jupyter Notebook (`notebooks/eda_analysis.ipynb`) for interactive EDA.
*   Comprehensive project documentation, including:
    *   Main `README.md` with setup and usage instructions.
    *   `docs/project_overview.md` (this file).
    *   `docs/data_dictionary.md`.
    *   Module-level READMEs and extensive code comments/docstrings.
*   A codebase that is prepared for future development, such as building and evaluating predictive models for hospital readmission.

## 6. Tools and Technologies

*   **Programming Language:** Python 3.x
*   **Core Python Libraries:** `pandas`, `SQLAlchemy`, `psycopg2-binary`, `matplotlib`, `seaborn`, `python-dotenv`.
*   **Database:** PostgreSQL
*   **Version Control:** Git and GitHub (or a similar platform)
*   **IDE/Editor:** VSCode (or any preferred Python IDE)
*   **Virtual Environment:** `venv`
*   **Notebook Environment:** Jupyter Notebook

This project aims to provide a solid foundation for understanding hospital readmission patterns and serves as a practical example of a data analytics project lifecycle, from data extraction to analysis and documentation.
