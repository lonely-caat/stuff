import smtplib
import csv
import email
from email.message import EmailMessage
import unicodedata
from unidecode import unidecode
from email.mime.text import MIMEText


def receipt_data():
    with open('', mode='r', ) as data:
        #expected format:
        #me myself,mbilichenko@llnw.com,1360
        reader = data.read()

        #normalize ASCII
        n = unicodedata.normalize('NFKD', reader)
        #remove abundant new lines and make it a list of strings
        r = n.replace('\n', ',')[:-1].split(',')
        #make a list of tuple of every 3 items
        l = list(zip(*[iter(r)] * 3))
        #make a dict with 2 values
        d = {a: (b, c) for a, b, c in l}

        return d

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("", "")
    buyers_dict = receipt_data()
    for buyer in buyers_dict:

        msg = 'Hi {0}, here is your amount due: {1}grn'.format(unidecode(buyer), buyers_dict[buyer][1])
        message = 'Subject: {0}\n\n{1}'.format('Nuts receipt', msg)

        server.sendmail(from_addr="bigfreshnuts@gmail.com", to_addrs=buyers_dict[buyer][0], msg=message)

        # server.sendmail("bigfreshnuts@gmail.com", buyer, '''\
        # Subject: test
        #
        #  {0} , your amount due is: {1}
        #  '''.format(buyers_dict[buyer][0], buyers_dict[buyer][1]))


send_email()

