import pyodbc
import pandas as pd

# Connection details
server = 'SERVERHERE'
database = 'DATABASE HERE'
driver = '{SQL Server}'  # Use the appropriate SQL Server driver

# Define your SQL queries and filenames
queries = [
    {"query": "SELECT * FROM [TABLE1]", "filename": "Table1export.csv"},
    {"query": "SELECT * FROM [TABLE2]", "filename": "Table2export.csv"},
    {"query": "SELECT * FROM [TABLE3]", "filename": "Table3export.csv"}
]

try:
    # Establish database connection using Trusted Connection
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
    cursor = conn.cursor()

    # Loop through each query
    for item in queries:
        query, filename = item["query"], item["filename"]

        print(f"Running query: {query}")
        df = pd.read_sql(query, conn)  # Execute query and store results in a DataFrame

        # Save results to CSV
        df.to_csv(filename, index=False)
        print(f"Saved results to {filename}")

    # Close connection
    cursor.close()
    conn.close()
    print("All queries executed successfully.")

except Exception as e:
    print(f"Error: {e}")
