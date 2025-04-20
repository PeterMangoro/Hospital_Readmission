import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from enriched_admissions import get_enriched_admissions

df = get_enriched_admissions()

# Readmission rate by age group
bins = [0,18,30,45,60,75,90,120]
labels = ['<18', '18-30', '31-45', '46-60', '61-75', '76-90', '90+']
df['age_group'] = pd.cut(df['age'],bins=bins,labels=labels)

plt.figure(figsize=(10, 5))
sns.barplot(data=df, x='age_group', y='readmitted', estimator=lambda x: sum(x)/len(x)*100)
plt.ylabel("Readmission Rate (%)")
plt.title("Readmission Rate by Age Group")
plt.tight_layout()
plt.savefig("eda_readmission_by_age_group.png")
plt.close()

# ------------------------
# B. Readmission Rate by Gender
# ------------------------
plt.figure()
sns.barplot(data=df, x='gender', y='readmitted', estimator=lambda x: sum(x)/len(x)*100)
plt.ylabel("Readmission Rate (%)")
plt.title("Readmission Rate by Gender")
plt.tight_layout()
plt.savefig("eda_readmission_by_gender.png")
plt.close()

# ------------------------
# C. Length of Stay vs Readmission
# ------------------------
plt.figure()
sns.boxplot(data=df, x='readmitted', y='length_of_stay')
plt.xticks([0, 1], ['Not Readmitted', 'Readmitted'])
plt.title("Length of Stay vs Readmission")
plt.tight_layout()
plt.savefig("eda_los_vs_readmission.png")
plt.close()

# ------------------------
# D. Seasonal Admissions Trend
# ------------------------
df['admission_month'] = pd.to_datetime(df['admission_date']).dt.month_name()
month_order = pd.date_range('2023-01-01', periods=12, freq='M').strftime('%B')

plt.figure(figsize=(12, 5))
sns.countplot(data=df, x='admission_month', order=month_order)
plt.title("Admissions by Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("eda_admissions_by_month.png")
plt.close()

# ------------------------
# E. Readmission Rate by Doctor Specialty
# ------------------------
top_specialties = df['specialty'].value_counts().head(5).index
df_top = df[df['specialty'].isin(top_specialties)]

plt.figure(figsize=(10, 6))
sns.barplot(data=df_top, x='specialty', y='readmitted', estimator=lambda x: sum(x)/len(x)*100)
plt.title("Readmission Rate by Doctor Specialty")
plt.ylabel("Readmission Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("eda_readmission_by_specialty.png")
plt.close()

print("✅ EDA complete. Plots saved to current directory.")