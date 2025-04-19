def load_transformed_to_csv(df,path='transformed_admissions.csv'):
    df.to_csv(path,index=False)