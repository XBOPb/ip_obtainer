import smtplib
import socket
from requests import get

# Enter credentials
email = '##'
password = '##'
destination = '##'
# Mail subject
subject = '##'


def get_network():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    public_ip = get('http://api.ipify.org').text
    return (hostname, local_ip, public_ip)

def send_mail(message):
    # smtp server('smtp.gmail.com')
    server = smtplib.SMTP_SSL('##')
    server.set_debuglevel(1)
    server.ehlo()
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, destination, message)
    server.quit()

if __name__ == '__main__':
    text = get_network()
    message = f'From: {email}\nTo: {destination}\nSubject: {subject}\n\n{text}'
    send_mail(message)
    

    