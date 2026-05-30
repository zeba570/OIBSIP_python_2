import sqlite3

DATABASE = "../bmi.db"


def create_table():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS bmi_records (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            weight REAL,

            height REAL,

            bmi REAL,

            category TEXT
        )
    """)

    conn.commit()

    conn.close()


create_table()


def insert_record(name, weight, height, bmi, category):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO bmi_records
        (name, weight, height, bmi, category)

        VALUES (?, ?, ?, ?, ?)

    """, (

        name,
        weight,
        height,
        bmi,
        category
    ))

    conn.commit()

    conn.close()


def get_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bmi_records")

    rows = cursor.fetchall()

    conn.close()

    result = []

    for row in rows:

        result.append({

            "name": row[1],
            "weight": row[2],
            "height": row[3],
            "bmi": row[4],
            "category": row[5]
        })

    return result