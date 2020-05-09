"""
Step1: Import Package smtplib
Step2: Opening Connection (username,Password)
Step3: Sending mail using Sendmail()
Step4:Close the connection
"""

import smtplib

MyCon = smtplib.SMTP('smtp.gmail.com',587)

MyCon.starttls()

MyCon.login("mani.shukla9lt@gmail.com", "********")

Message ="Thank you every one for making this FDP Grand Success, keep learning New things!!!"
MyCon.sendmail("mani.shukla9lt@gmail.com","Ashwini.kanade@gmail.com",Message)
print("Mail Send Successfully !!!!!!!!!!!")
MyCon.quit()