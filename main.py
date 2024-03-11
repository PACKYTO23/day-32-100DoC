# import smtplib

# my_email = "zmssmzx@gmail.com"
# password = "lyqi vxqn qfhq usty"
# the_other_email = "xyz101abc321@yahoo.com"
# email_juan = "juanfcr11@gmail.com"

# connection = smtplib.SMTP("smtp.gmail.com")

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=the_other_email,
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# print(day_of_week)

# date_of_birth = dt.datetime(year=1994, month=7, day=24, hour=21, minute=45)

# print(date_of_birth)

import datetime as dt
import smtplib
import random

my_email = "zmssmzx@gmail.com"
password = "lyqi vxqn qfhq usty"
# the_other_email = "xyz101abc321@yahoo.com"
email_juan = "juanfcr11@gmail.com"

now = dt.datetime.now()
today = now.weekday()

if today == 0:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_juan,
            msg=f"Subject:Mas pruebas, tu tranquilo.\n\nTen una frase para la semana:\n\n{random_quote}"
        )
