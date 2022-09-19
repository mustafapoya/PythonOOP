import os.path
import webbrowser

from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    creates a flatmate person who lives in the flat
    and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    creates a pdf file that contains data about
    the flatmates such as their names, their due amounts,
    and the period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(name="android-system-home.png", w=30, h=30)

        #Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)
        # Insert Period Label and Value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and the amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=1, ln=1)

        # Insert name and the amount of the second flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


amount = float(input("Hey user, enter the bill amount"))
period = input("What is the bill period? E.g. December 2020: ")

name1  = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in house during the bill period? "))

name2  = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in house during the bill period? "))


the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{name1} Pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{name2} Pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)





