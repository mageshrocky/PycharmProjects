import smtplib

email = smtplib.SMTP("smtp.gmail.com", 587)
email.starttls()
email.login("magesh1699@gmail.com", "Mechon16")
message = "testing mail"
email.sendmail("magesh1699@gmail.com", "maaahi003@gmail.com", message)
email.quit()