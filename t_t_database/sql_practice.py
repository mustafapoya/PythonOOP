import sqlite3

def create_table():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
        CREATE TABLE "Seat" (
            "seat_id"	TEXT,
            "taken"	INTEGER,
            "price"	REAL
        );
        """)
    connection.commit()
    connection.close()


def insert_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
        INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES ("A1", "0", "90"), ("A3", "1", "100"), ("A3", "0", "80")
    """)
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute(""" SELECT seat_id, price FROM "Seat" where price > 80 """)

    result = cursor.fetchall()
    connection.close()
    return result


def update_value(occupied, seat_id):
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
        update Seat set taken=?  where seat_id=?
    """, [occupied, seat_id])

    connection.commit()
    connection.close()

def delete_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
        delete from Seat where seat_id = "A3"
    """)
    connection.commit()
    connection.close()

# print(select_all())
update_value(occupied=0, seat_id="A2")