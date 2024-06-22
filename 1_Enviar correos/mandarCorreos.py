import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Abrimos el archivo config.json
with open("config.json") as datos:
    json_data = json.load(datos)

# Extraemos los datos del archivo JSON y especificamos el
# otro email que recibira el correo que le enviemos
email = json_data["EMAIL_USER"]
password = json_data["EMAIL_PASSWORD"]
other_email = "NeicerYEANYT18@gmail.com"

# Creamos el objeto mensaje
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = other_email
msg['Subject'] = "Prueba de correo con Python"

body = "Hola, esto es una prueba de correo con Python 🐍"
msg.attach(MIMEText(body, 'plain'))

smtp_server = "smtp.gmail.com"
smtp_port = 587

# Envio del correo
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, other_email, msg.as_string())
    server.quit()
    print("Correo enviado exitosamente!")
except Exception as e:
    print(f"Error al enviar el correo: {e}")

