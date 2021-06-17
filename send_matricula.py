import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os.path
import pandas as pd
from time import sleep
import util

subject = "Número de matrícula - Curso de Extensão em Engenharia de Software Moderna (DCC/UFMG)"
body = """\

Prezado(a) aluno(a),

O seu número de matrícula na Turma {} do curso é {}.

--
Curso de Extensão em Engenharia de Software Moderna - DCC/UFMG

"""

def send_email(sender_email, sender_password, student_email, student_email_body):
  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = student_email
  message["Subject"] = subject
  message.attach(MIMEText(student_email_body, "plain"))
  text = message.as_string()
  sleep(5)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, [student_email, sender_email], text)##Bcc to sender_email
  pass 

def run():
  file_name_list_students = input ('CSV (matricula;turma;nome;email): ')
  sender_email = input("Email do curso: ")
  sender_password = input("Senha: ")
  dataset = util.read_csv(file_name_list_students)
  for index, row in dataset.iterrows():
    student_email = row.get('email')
    student_class = row.get('turma')
    student_code = row.get('matricula')
    print('\nSending from %s to %s' % (sender_email, student_email))
    print('Waiting 2 seconds...')
    sleep(2)
    student_email_body = body.format(student_class, student_code)
    send_email(sender_email, sender_password, student_email, student_email_body)

  print('\nEnd.')
run()