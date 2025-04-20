from connect_pg import engine

def load_to_csv(df,path='transformed_admissions'):
    df.to_csv(path+'.csv',index=False)
    print(f"Transformed data saved to {path}")

def load_to_db(df,table_name='admission_cleaned'):
    df.to_sql(table_name,engine,if_exists='replace',index=False)
    print(f"Data loaded into table: {table_name}")