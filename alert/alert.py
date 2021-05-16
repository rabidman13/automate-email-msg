import smtplib
from email.message import EmailMessage
import imghdr

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    files = ['123.jpg', '456.jpg']
    for file in files:
        with open(file, 'rb') as m:
            file_data = m.read()
            file_type = imghdr.what(m.name)
            file_name = m.name

        msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

    file2 = '123.pdf'
    with open(file2, 'rb') as m2:
        file_data = m2.read()
        file_name = m2.name
        msg.add_attachment(file_data, maintype = 'application', subtype = 'pdf', filename = file_name)
    

    contacts = ['mrbluebird1213@gmail.com', 'ylananlance@yahoo.com']
    msg['subject'] = subject
    msg['to'] = ','.join(contacts)
    
    

    user = "mrbluebird1213@gmail.com"
    msg['from'] = user
    password = "kkqwxqvcvjrhhrrb"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert("hey", "hello world", '')

