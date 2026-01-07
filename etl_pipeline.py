import pandas as pd
import sqlalchemy
import urllib

# ---------------------------------------------------------
# STEP 1: CONFIGURATION
# ---------------------------------------------------------
csv_file_path = r"C:\Users\vasav\OneDrive\Desktop\Project_Data.csv"

server_name = "localhost"
database_name = "SupplyChainDW"

# ---------------------------------------------------------
# STEP 2: RUN THE PIPELINE
# ---------------------------------------------------------
print("--- STARTING PIPELINE ---")

try:
    # 1. Read the CSV
    print(f"1. Reading file from: {csv_file_path}")
    df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")
    print(f"   > SUCCESS! Found {len(df)} rows.")

    # 2. Connect to SQL
    print("2. Connecting to SQL Server...")
    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server_name};"
        f"DATABASE={database_name};"
        f"Trusted_Connection=yes;"
    )
    engine = sqlalchemy.create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

    # 3. Load Data
    print("3. Loading data into SQL (This replaces the old table)...")
    # The 'replace' option fixes your column mismatch issue automatically
    df.to_sql("Raw_Superstore", schema="stage", con=engine, index=False, if_exists="replace")
    
    print("---------------------------------------------------------")
    print("   > PIPELINE SUCCESS! Data is now in SQL Server.")
    print("---------------------------------------------------------")

except Exception as e:
    print("\n!!! ERROR !!!")
    print(e)