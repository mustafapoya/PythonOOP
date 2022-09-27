import sqlite3

from fpdf import FPDF


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user=self, price=seat.get_price(), seat_number=seat_id)
                return "Purchase successful!"
            else:
                return "There was a problem with your card!"
        else:
            return "Seat is taken!"


class Seat:
    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(""" select price from Seat where seat_id = ? """, [self.seat_id])
        price = cursor.fetchall()[0][0]

        return price

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(""" select taken from Seat where seat_id = ? """, [self.seat_id])

        result = cursor.fetchall()[0][0]

        if result == 0:
            return True
        else:
            return False


    def occupy(self):
        if self.is_free():
            connection = sqlite3.connect(self.database)
            connection.execute("""
                UPDATE Seat SET taken=? where seat_id=?
            """, [1, self.seat_id])

            connection.commit()
            connection.close()

class Card:
    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("select balance from Card where number = ? and cvc = ?", [self.number, self.cvc])

        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                    UPDATE Card SET balance = ? WHERE number = ? and cvc = ?
                """, [balance - price , self.number, self.cvc])

                connection.commit()
                connection.close()
                return True



class Ticket:
    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.seat_number = seat_number

    def to_pdf(self):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.set_font(family="times", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1, ln=1, align="C")

        pdf.set_font(family="times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Name: ", border=1)
        pdf.set_font(family="times", style="B", size=12)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1, align="C")
        pdf.cell(w=0, h=5, txt="", border=1, ln=1, align="C")

        pdf.set_font(family="times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Ticket ID", border=1)
        pdf.set_font(family="times", style="B", size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1, align="C")
        pdf.cell(w=0, h=5, txt="", border=1, ln=1)

        pdf.set_font(family="times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family="times", style="B", size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1, align="C")
        pdf.cell(w=0, h=5, txt="", border=1, ln=1)

        pdf.set_font(family="times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Seat Number", border=1)
        pdf.set_font(family="times", style="B", size=12)
        pdf.cell(w=0, h=25, txt=str(self.set_number), border=1, ln=1, align="C")
        pdf.cell(w=0, h=5, txt="", border=1, ln=1)

        pdf.output("sample.pdf", "F")


if __name__ == "__main__":
    name = input("your full name: ")
    seat_id = input("Preferred seat number: ")
    card_type = input("your card type: ")
    card_number = input("your card Number: ")
    card_cvc = input("your card cvc: ")
    card_holder = input("card holder name: ")

    user = User(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

    print(user.buy(seat=seat, card=card))
    