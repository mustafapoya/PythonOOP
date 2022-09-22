import time

import yagmail
import pandas
from news import NewsFeed
import datetime


def send_email():
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today, language="en")
    email = yagmail.SMTP(user="the_email", password="the_password")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi, {row['name']}\n See what's on about {row['interest']} today. {news_feed.get()}\nMustafa",
               attachments="news.py")


while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 47:
        df = pandas.read_excel('people.xlxs')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)
