import sqlite3

dock_dict = [
    {   
        "name": "North Pier West - 410'",
        "dock_number": 1,
        "width": 100,
        "length": 410
    },
    {   
        "name": "North Pier Face - 75'",
        "dock_number": 2,
        "width": 40,
        "length": 75
    },
    {   
        "name": "North Pier East - 240'",
        "dock_number": 3,
        "width": 40,
        "length": 240
    },
    {   
        "name": "Inner Channel - 55'",
        "dock_number": 4,
        "width": 30,
        "length": 55
    },
    {   
        "name": "South Float West - 90'",
        "dock_number": 5,
        "width": 50,
        "length": 90
    },
    {   "name": "South Float East - 90'",
        "dock_number": 6,
        "width": 50,
        "length": 90
    }
]

connection = sqlite3.connect("database.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS docks (
        id INTEGER PRIMARY KEY,
        dock_number INTEGER UNIQUE,
        width REAL,
        length REAL
    )
""")

for dock in dock_dict:
    connection.execute("""
        INSERT OR IGNORE INTO docks (dock_number, width, length)
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

def get_alldocks():
    connection = get_db()

    rows = connection.execute(
        "SELECT * FROM docks"
    ).fetchall()

    for row in rows:
        print(dict(row))

    connection.close()
    return '', 204

def allreservations():
    connection = get_db()

    rows = connection.execute("""
        SELECT * FROM reservations
    """).fetchall()

    for row in rows:
        print(dict(row))

    connection.close()
    return '', 204

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
    print("reservation successfully made!")
    connection.commit()
    connection.close()
    return '', 204

def delete_reservation(res_id):
    connection = get_db()

    connection.execute("""
        DELETE FROM reservations
        WHERE id = ?
    """, (
        res_id,
    ))

    connection.commit()
    connection.close()
    return '', 204

def check_dockreservations(dock_num, new_end, new_start):
    connection = get_db()

    arr = []
    rows = connection.execute("""
       SELECT id, start_date, end_date, reason FROM reservations
       WHERE dock_number = ? 
       AND start_date <= ? 
       AND end_date >= ?
   """, (
       dock_num, 
       new_end, 
       new_start
    )).fetchall()
    for row in rows:
        arr.append(dict(row))
    connection.close()
    return arr

def get_allreservations():
    connection = get_db()

    arr = []
    rows = connection.execute("""
        SELECT id, dock_number, start_date, end_date, reason
        FROM reservations
        ORDER BY start_date 
   """, 
   ).fetchall()
    for row in rows:
        arr.append(dict(row))
    connection.close()
    return arr

def get_filteredreservations(filtertype, filterinput):
    allowed = {"dock_number", "start_date", "end_date", "reason", "id"}
    if filtertype not in allowed:
        return []
    
    connection = get_db()

    arr = []
    rows = connection.execute(f"""
        SELECT id, dock_number, start_date, end_date, reason
        FROM reservations
        WHERE {filtertype} LIKE '%{filterinput}%'
        ORDER BY start_date 
   """, 
   ).fetchall()
    for row in rows:
        arr.append(dict(row))
    connection.close()
    return arr

def seed_reservations():
    connection = get_db()
    count = connection.execute("SELECT COUNT(*) FROM reservations").fetchone()[0]
    if count == 0:
        sample = [
            (1, "2026-10-01", "2026-10-05", "ROV-X 7:15 AM example"),
            (2, "2026-10-03", "2026-10-04", "Community sail day"),
            (3, "2026-10-10", "2026-10-20", "R/V2 8:30 AM example"),
        ]
        connection.executemany(
            "INSERT INTO reservations (dock_number, start_date, end_date, reason) VALUES (?, ?, ?, ?)",
            sample,
        )
        connection.commit()
    connection.close()

seed_reservations()
