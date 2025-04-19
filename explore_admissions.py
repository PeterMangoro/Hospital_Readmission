import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from connect_pg import engine #importing from connection file

# load admission table
df_admissions = pd.read_sql("Select * from admissions",engine)

#Quick overview
print(df_admissions.head())
print(df_admissions.info())
print(df_admissions.describe())

# readmission rate
readmission_rate = df_admissions['readmitted'].mean() *100
print(f"\n Readmission rate: {readmission_rate:.2f}%")

# average length of stay
avg_los = df_admissions['length_of_stay'].mean()
print(f"Average Length Of Stay: {avg_los:.2f} days")

# plots
# Readmission count
sns.countplot(x='readmitted', data=df_admissions)
plt.title('Readmission Distribution')
plt.xlabel('Readmitted')
plt.ylabel('Number of Admissions')
plt.show()

# length of stay distribution
sns.histplot(df_admissions['length_of_stay'],kde=True)
plt.title('Length of Stay Distribution')
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.show()