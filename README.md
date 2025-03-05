# SQL Exporter with PyODBC and Pandas

## Overview
This Python script connects to an **SQL Server** database using `pyodbc`, executes multiple queries, and exports the results to CSV files. It provides an easy way to extract data from SQL tables and store them as structured CSV files for further analysis.

## Requirements
Ensure you have the following installed before running the script:

- Python 3.x
- Required Python libraries:
  - `pyodbc`
  - `pandas`

You can install the necessary dependencies using:
```sh
pip install pyodbc pandas
```

## How to Use
1. Modify the connection details in RunListofSQLQueries.py:

- Update server with your SQL Server hostname.
- Update database with your database name.
- Ensure your driver ({SQL Server}) is correct.

2. Define the SQL queries.
   
```sh
queries = [
    {"query": "SELECT * FROM [TABLE1]", "filename": "Table1export.csv"},
    {"query": "SELECT * FROM [TABLE2]", "filename": "Table2export.csv"},
    {"query": "SELECT * FROM [TABLE3]", "filename": "Table3export.csv"}
]
```
3. Run the script (RunListofSQLQueries.py)
4. Check the generated CSV files in the same directory.

## Example Output

```sh
Running query: SELECT * FROM [TABLE1]
Saved results to Table1export.csv
Running query: SELECT * FROM [TABLE2]
Saved results to Table2export.csv
Running query: SELECT * FROM [TABLE3]
Saved results to Table3export.csv
All queries executed successfully.
```

## Troubleshooting

If you encounter a driver error, check your installed SQL Server ODBC drivers using:

```sh
odbcinst -q -d
```

## License

This project is licensed under the MIT License.


