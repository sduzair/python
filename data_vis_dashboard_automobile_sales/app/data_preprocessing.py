import pandas as pd
import pyarrow as pa

url_remote_csv = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
filename_parquet = 'data.parquet'

def load_csv(url):
    return pd.read_csv(
        url,
        parse_dates=['Date'],
        dtype_backend='pyarrow'
    )

def optimize_dtypes(df: pd.DataFrame):
    return df.assign(
        Vehicle_Type=df['Vehicle_Type'].astype('category'),
        City=df['City'].astype('category'),
        Month=df['Month'].astype('category'),
        Year=df['Year'].astype(pd.ArrowDtype(pa.uint16())),
        Competition=df['Competition'].astype(pd.ArrowDtype(pa.uint8())),
        Advertising_Expenditure=df['Advertising_Expenditure'].astype(pd.ArrowDtype(pa.uint16())),
        Recession=df['Recession'].map({1: True, 0: False}).astype(pd.ArrowDtype(pa.bool_())),
        Date=df['Date'].dt.date.astype(pd.ArrowDtype(pa.date32()))
    )

def create_parquet(df: pd.DataFrame, filename_parquet):
    df.to_parquet(filename_parquet)

def load_parquet(filename_parquet):
    # return pq.read_table('data.parquet').to_pandas(types_mapper=pd.ArrowDtype)
    return pd.read_parquet(filename_parquet, dtype_backend='pyarrow')
    
def data_preprocessing(url_remote_csv, filename_parquet):
    df = load_csv(url_remote_csv)
    df_optimized = optimize_dtypes(df)
    create_parquet(df_optimized, filename_parquet)

def main():
    data_preprocessing(url_remote_csv, filename_parquet)

if __name__ == '__main__':
    main()