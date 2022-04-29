import  smtplib

gmail = "smnrsendmsg@gmail.com"
password = "py.123456789"
 
server = smtplib.SMTP("smtp.gmail.com",5870)
server.starttls()

server.login(gmail,password)

msg ="Hi ,there !!"
receiver = gmail # own

template = """Subject: {}

{}

{}

"""

subject ="About the project"
msg="That project is a only template"
name= "Semanur"

mail = template.format(subject,msg,name)
receiver= input("To :")
'''receiver=gmail #own '''

server.sendmail(gmail,receiver,mail.encode("utf_8"))
print("Send message")

with smtplib.SMTP("smtp.gmail.com",5870) as server :
     server.starttls()
     server.loging(gmail,password)
     server.send(gmail,receiver,mail.encode("utf_8"))