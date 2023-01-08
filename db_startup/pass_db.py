import sqlite3


def convert(k):
    return ''.join(k).split()


def create_table():
    conn = sqlite3.connect("passenger.db")

    c = conn.cursor()

    c.execute("""
    CREATE TABLE passengers(
    bus_name text,
    number_pass int)
    """)
    print("Table created")

    conn.commit()
    conn.close()


def add_one():
    conn = sqlite3.connect("passenger.db")
    c = conn.cursor()

    bus_name = input("State the bus you want to add: ")

    c.execute("INSERT INTO passengers VALUES (?,?)", (bus_name, 0))
    print("Element added successfully")

    conn.commit()
    conn.close()


def add_many():
    conn = sqlite3.connect("passenger.db")
    c = conn.cursor()

    bus_name = input("State the buses you want to add: ")
    k = convert(bus_name)

    for item in k:
        c.execute("INSERT INTO passengers VALUES (?,?)", (item, 0))
    print("Elements added successfully")

    conn.commit()
    conn.close()


def show_all():
    conn = sqlite3.connect("passenger.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM passengers")

    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()


def delete_one():
    conn = sqlite3.connect("passenger.db")
    c = conn.cursor()

    deleted = input("Enter which data you want to delete: ")
    j = convert(deleted)

    c.execute("DELETE from passengers WHERE bus_name = ?", j)
    print("Element deleted successfully")

    conn.commit()
    conn.close()


def delete_table():
    conn = sqlite3.connect("passenger.db")
    c = conn.cursor()

    c.execute("DROP TABLE passengers")
    print("Table dropped")

    conn.commit()
    conn.close()
