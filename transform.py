import pandas as pd

# los is Length Of Stay
def los_bucket(days):
    if days <=2:
        return 'Short (0-2)'
    
    elif days <=5:
        return 'Medium (3-5)'
    
    else:
        return 'Long (6+)'


def transform_admissions(df):
    # ensure dates are in datetime format
    df['admission_date'] = pd.to_datetime(df['admission_date'])
    df['discharge_date'] = pd.to_datetime(df['discharge_date'])

    # drop null values on critical columns
    df = df.dropna(subset=['admission_date','discharge_date'])

    # ensure that length_of_stay is always positive
    df =df[df['length_of_stay']>=0]

    df['admission_month'] = df['admission_date'].dt.month # add column for month
    df['stay_length_group'] = df['length_of_stay'].apply(los_bucket) #column for los grouping
    df['readmission_label'] = df['readmitted'].map({True:'Yes',False:'No'})

    return df
