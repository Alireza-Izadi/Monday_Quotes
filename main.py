import datetime as dt
import smtplib
import random

#You should use gmail for diffrent kind of  email please enter that email smtp
SEND_FROM = ""
YOUR_PASSWORD = ""
SEND_TO = ""

#---------------------------READING DATA FROM QUOTES-------------------------------#
with open("./quotes.txt", "r") as file:
    quotes = [quote.strip() for quote in file.readlines()]
    
#---------------------------------------Time-----------------------------------------------------#
current_time = dt.datetime.now()
current_weekday = current_time.weekday()

#------------------------------------SENDING EMAILS---------------------------------------#
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=SEND_FROM, password=YOUR_PASSWORD)
    if current_weekday == 0:
        connection.sendmail(
            from_addr=SEND_FROM,
            to_addrs=SEND_TO,
            msg=f"Subject:Quote of the day\n\n{random.choice(quotes)}"
            )
#===========================================================#