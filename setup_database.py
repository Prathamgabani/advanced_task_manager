import sqlite3

def setup_database():
    # Connect to the SQLite database
    # If the database does not exist, it will be created
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Create the categories table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    # Create the tasks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        category_id INTEGER,
        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

# Run the setup
if __name__ == "__main__":
    setup_database()
