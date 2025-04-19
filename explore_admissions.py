import matplotlib.pyplot as plt
import seaborn as sns
from extract import extract_admissions
from transform import transform_admissions
from load import load_transformed_to_csv

df_raw  = extract_admissions()
df_clean = transform_admissions(df_raw)

# Quick Stats
print(
    df_clean[['length_of_stay','admission_month','stay_length_group','readmission_label']].head()
)

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


