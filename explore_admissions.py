import matplotlib.pyplot as plt
import seaborn as sns
from extract import extract_admissions
from transform import transform_admissions
from load import load_to_csv,load_to_db
from enriched_admissions import get_enriched_admissions

df_raw  = extract_admissions()
df_clean = transform_admissions(df_raw)
df_enriched = get_enriched_admissions()

load_to_db(df_clean)
load_to_csv(df_clean)

load_to_db(df_enriched,'admission_enriched')
load_to_csv(df_enriched,'admission_enriched')
# load_to_csv()
# Quick Stats
# print(
#     df_clean[['length_of_stay','admission_month','stay_length_group','readmission_label']].head()
# )

# plots
# Readmission count
# sns.countplot(x='readmitted', data=df_admissions)
# plt.title('Readmission Distribution')
# plt.xlabel('Readmitted')
# plt.ylabel('Number of Admissions')
# plt.show()

# length of stay distribution
# sns.histplot(df_admissions['length_of_stay'],kde=True)
# plt.title('Length of Stay Distribution')
# plt.xlabel('Days')
# plt.ylabel('Frequency')
# plt.show()


