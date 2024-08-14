import sqlite3

def verify_tables():
    # Connect to the database
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Check if tables exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(table[0])

    conn.close()

if __name__ == "__main__":
    verify_tables()
