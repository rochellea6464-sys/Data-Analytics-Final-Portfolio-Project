import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace('[^0-9a-zA-Z]+', '_', regex=True)
        .str.replace('_+', '_', regex=True)
        .str.strip('_')
    )
    return df
