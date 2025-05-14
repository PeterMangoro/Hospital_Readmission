import matplotlib.pyplot as plt
import seaborn as sns
from src.data_extraction.extract import extract_admissions
from src.data_processing.transform import transform_admissions
from src.loading.load import load_to_csv, load_to_db
from src.analysis.data_enrichment import get_enriched_admissions

# It's good practice to wrap the main execution logic in a function or a main block
def main():
    print("Starting ETL and Analysis Pipeline...")

    print("Extracting raw admissions data...")
    df_raw = extract_admissions()
    print(f"Extracted {len(df_raw)} raw admission records.")

    print("Transforming admissions data...")
    df_clean = transform_admissions(df_raw.copy()) # Use .copy() to avoid SettingWithCopyWarning on slices
    print(f"Transformed data has {len(df_clean)} records.")

    print("Getting enriched admissions data...")
    df_enriched = get_enriched_admissions()
    print(f"Enriched data has {len(df_enriched)} records.")

    print("Loading cleaned data to database and CSV...")
    load_to_db(df_clean, table_name='admission_cleaned') # Specify table name as in original load.py
    load_to_csv(df_clean, path='data/processed/transformed_admissions') # Ensure path is correct

    print("Loading enriched data to database and CSV...")
    load_to_db(df_enriched, table_name='admission_enriched')
    load_to_csv(df_enriched, path='data/processed/admission_enriched') # Ensure path is correct

    print("Pipeline finished.")

    # Original commented out plotting code - can be moved to exploratory_analysis.py or a notebook
    # print("Generating visualizations (commented out by default)...")
    # Quick Stats
    # print(
    #     df_clean[[
    #         'length_of_stay',
    #         'admission_month',
    #         'stay_length_group',
    #         'readmission_label'
    #     ]].head()
    # )

    # plots
    # Readmission count
    # sns.countplot(x='readmitted', data=df_enriched) # Assuming df_enriched is the most complete for this
    # plt.title('Readmission Distribution')
    # plt.xlabel('Readmitted')
    # plt.ylabel('Number of Admissions')
    # plt.savefig('reports/figures/readmission_distribution.png') # Save plots instead of showing
    # plt.close()

    # length of stay distribution
    # sns.histplot(df_enriched['length_of_stay'], kde=True)
    # plt.title('Length of Stay Distribution')
    # plt.xlabel('Days')
    # plt.ylabel('Frequency')
    # plt.savefig('reports/figures/length_of_stay_distribution.png')
    # plt.close()

if __name__ == "__main__":
    # Note: For the imports to work correctly when running main.py directly from the project root,
    # the Python interpreter needs to be able to find the 'src' directory.
    # This usually means the project root directory should be in PYTHONPATH or you run it as a module.
    # Alternatively, ensure your IDE or environment handles this (e.g., by setting the correct working directory).
    # For simplicity in a script, one might add the project root to sys.path if needed, but this is often a sign of a more complex setup being required.
    # import sys
    # import os
    # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    # The above sys.path modification is generally not needed if running from the project root and 'src' is a package.

    main()