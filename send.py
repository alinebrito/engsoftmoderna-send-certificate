import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os.path
import pandas as pd
from time import sleep

subject = "Certificado do Curso de Extensão em Engenharia de Software Moderna"
body = """\
Prezado aluno(a),

Segue em anexo:

* o certificado de aprovação no curso
* uma declaração com as notas obtidas.

Mais uma vez, parabéns pela conclusão e aprovação no nosso curso.

Favor confirmar o recebimento desta mensagem.

Cordialmente,

Prof. Marco Tulio Valente
Coordenador do curso.

P.S. Para quem não fez, gostaríamos de solicitar o preenchimento do formulário de avaliação do curso, disponível em:
https://forms.gle/t49AC1Pa6LDXmkcJA"""

def get_path(code):
  return 'docs/'

def get_certificate(code):
  return 'certificado' + str(code) + '.pdf'

def get_declaration(code):
  return 'declaracao' + str(code) + '.pdf'
  
def add_file(path, file_name):
  with open(path + file_name, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file_name}",
  )
  return part

def send_email(sender_email, password, student_email, student_code):

  path = get_path(student_code)
  filename_certificate = get_certificate(student_code)
  filename_declaration = get_declaration(student_code)

  if (not os.path.isfile(path + filename_certificate)) or (not os.path.isfile(path + filename_declaration)):
    print('\nERRO: File not found, %s, %i' % (student_email, student_code))
    print('%s' % filename_certificate)
    print('%s' % filename_declaration)
    return 

  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = student_email
  message["Subject"] = subject

  message.attach(MIMEText(body, "plain"))
 
  part1 = add_file(path, filename_certificate)
  message.attach(part1)

  part2 = add_file(path, filename_declaration)
  message.attach(part2)

  text = message.as_string()

  print('Sending from %s to %s' % (sender_email, student_email))
  sleep(3)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, [student_email, sender_email], text)##Bcc to sender_email
  return 

def read_csv(file_name):
  print("Reading %s..." % file_name)
  dataset = ""
  if not os.path.isfile(file_name):
    print('ERRO: File not found %s' % file_name)
  else:
    dataset = pd.read_csv(file_name, sep=";", keep_default_na=False)
  return dataset

def run():
  file_name_list_students = input ('CSV de alunos aprovados (ex: aprovados_lote_1.csv): ')
  sender_email = input("Email do curso: ")
  password = input("Senha: ")
  dataset = read_csv(file_name_list_students)
  for index, row in dataset.iterrows():
    student_email = row.get('email')
    student_code = row.get('numero')
    print('\n------\nProcessing %i ...' % student_code)
    send_email(sender_email, password, student_email, student_code)
    print('Waiting 2 seconds...')
    sleep(2)
  print('\nEnd.')
run()