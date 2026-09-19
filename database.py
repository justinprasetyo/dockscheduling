import sqlite3

dock_dict = [
    {   
        "name": "North Pier West - 410'",
        "dock_number": 1,
        "width": 20,
        "length": 100
    },
    {   
        "name": "North Pier Face - 75'",
        "dock_number": 2,
        "width": 30,
        "length": 150
    },
    {   
        "name": "North Pier East - 240'",
        "dock_number": 3,
        "width": 40,
        "length": 200
    },
    {   
        "name": "Inner Channel - 55'",
        "dock_number": 4,
        "width": 20,
        "length": 100
    },
    {   
        "name": "South Float West - 90'",
        "dock_number": 5,
        "width": 30,
        "length": 150
    },
    {   "name": "South Float East - 90'",
        "dock_number": 6,
        "width": 40,
        "length": 200
    }
]

connection = sqlite3.connect("database.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS docks (
        id INTEGER PRIMARY KEY,
        dock_number INTEGER,
        width REAL,
        length REAL
    )
""")

for dock in dock_dict:
    connection.execute("""
        INSERT INTO docks (dock_number, width, length)
        VALUES (?, ?, ?)
    """, (
        dock["dock_number"],
        dock["width"],
        dock["length"]
    ))

connection.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY,
        dock_number INTEGER,
        start_date TEXT,
        end_date TEXT,
        reason TEXT
    )
""")

connection.commit()
connection.close()

def get_db():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection

def get_allrows():
    connection = get_db()

    rows = connection.execute(
        "SELECT * FROM docks"
    ).fetchall()

    connection.close()
    return rows

def make_reservation(dock_num, start, end, reason):
    connection = get_db()

    connection.execute("""
        INSERT INTO reservations (dock_number, start_date, end_date, reason)
        VALUES (?, ?, ?, ?)
    """, (
        dock_num,
        start,
        end,
        reason
    ))

    connection.commit()
    connection.close()
    return '', 204

def delete_reservation(dock_num, start, end):
    connection = get_db()

    connection.execute("""
        DELETE FROM reservations
        WHERE dock_number = ?
        AND start_date = ?
        AND end_date = ?;
    """, (
        dock_num,
        start,
        end
    ))

    connection.commit()
    connection.close()
    return '', 204

