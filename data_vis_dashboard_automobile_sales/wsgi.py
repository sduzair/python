# wsgi.py
# NOTE - Does not run on Windows
from app import create_app
from app.data_preprocessing import data_preprocessing, load_parquet, url_remote_csv, filename_parquet


data_preprocessing(url_remote_csv, filename_parquet)
df = load_parquet(filename_parquet)
app = create_app(df)
server = app.server

if __name__ == "__main__":
    app.run_server(debug=False)
