from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from validate_email import validate_email
from os import environ


def CambiarPassword(destinatario):
    existeEmail = validate_email(destinatario)

    if not existeEmail:
        print('El correo no existe')
        return

    texto = '''Hola
    Parece que has cambiado tu contraseña, si no fuiste tu comuicate con nosotros, caso contrario, has caso omiso a este mensaje'''
    emailEmisor = environ.get('CORREO_EMISOR')#'isaias.guizado@gmail.com'
    passwordEmisor = environ.get('PASSWORD_CORREO_EMISOR')#'mhoypavrsfsoyqgn'

    cuerpo = MIMEText(texto, 'plain')

    correo = MIMEMultipart()
    correo['Subject'] = 'Cambiaste tu contraseña'
    correo['To'] = destinatario
    correo.attach(cuerpo)

    emisor = SMTP('smtp.gmail.com', 587)

    emisor.starttls()

    emisor.login(emailEmisor, passwordEmisor)
    emisor.sendmail(from_addr=emailEmisor, to_addrs=destinatario, msg=correo.as_string())

    emisor.quit()

    print('Correo enviado exitosamente')