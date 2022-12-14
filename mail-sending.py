import smtplib
import ssl
import getpass

from 

port = 465
password = getpass.getpass()

context = ssl.create_default_context()

email_remitente = 'javierrojas14.jr@gmail.com'
email_receptor = 'pruebadevelopmentjavier@gmail.com'

mensaje = '''
Subject: Hola, soy yo


Este es un wapo mensaje enviado desde Python, te digo hola :).

'''

with smtplib.SMTP_SSL('smtp.gmail.com', port=port, context=context) as server:
    server.login('javierrojas14.jr@gmail.com', password)
    server.sendmail(email_remitente, email_receptor, mensaje)
