import sqlite3

def initialize_database(db_name):
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Define a table creation SQL statement
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    # Execute the SQL statement
    cursor.execute(create_table_sql)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_name = 'local_database.db'  # Name of the SQLite database file
    initialize_database(db_name)
    print(f"Database '{db_name}' initialized successfully.")
