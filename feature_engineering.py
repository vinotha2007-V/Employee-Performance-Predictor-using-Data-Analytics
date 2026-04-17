def feature_engineering(df):
    df['Experience_Level'] = df['YearsAtCompany'].apply(
        lambda x: 'Junior' if x < 3 else 'Mid' if x < 7 else 'Senior'
    )
    return df
