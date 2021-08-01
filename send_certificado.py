import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os.path
import pandas as pd
from time import sleep
import util

subject = "Certificado do Curso de Extensão em Teste de Software (DCC/UFMG)"
body = """\
Prezado(a) aluno(a),

Segue em anexo o certificado de aprovação.

Mais uma vez, parabéns pela conclusão e aprovação no nosso curso.

Favor confirmar o recebimento desta mensagem.

Cordialmente,

Prof. André Hora
Coordenador do curso.

P.S. Para quem não fez, gostaríamos de solicitar o preenchimento do formulário de avaliação do curso, disponível em:
https://docs.google.com/forms/d/e/1FAIpQLSfzuSNT9Q_xmVvJFk9R3nvPyBHNUK940BbyhL7FPXd7MaNUUg/viewform?usp=sf_link"""

def add_file(path, file_name):
  with open(os.path.join(path, file_name), "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
      "Content-Disposition",
      f"attachment; filename= {file_name}",
    )
  return part

def send_email(sender_email, password, student_email, student_code):

  path = util.get_path(student_code)
  filename_certificate = util.get_certificate(student_code)
  # filename_declaration = util.get_declaration(student_code)

  if(util.is_valid_file(path, filename_certificate)):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = student_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    part1 = add_file(path, filename_certificate)
    message.attach(part1)
    # part2 = add_file(path, filename_declaration)
    # message.attach(part2)

    text = message.as_string()
    print('Sending from %s to %s' % (sender_email, student_email))
    sleep(5)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, [student_email, sender_email], text)##Bcc to sender_email

  return 

def run():
  file_name_list_students = input ('CSV de alunos aprovados (ex: alunos_aprovados_exemplo.csv): ')
  sender_email = input("Email do curso: ")
  password = input("Senha: ")
  dataset = util.read_csv(file_name_list_students)
  for index, row in dataset.iterrows():
    student_email = row.get('email')
    student_code = row.get('numero')
    student_name = row.get('nome')
    print('\n------\nProcessing %i: %s ...' % (student_code, student_name))
    send_email(sender_email, password, student_email, student_code)
    print('Waiting 2 seconds...')
    sleep(2)
  print('\nEnd.')
run()