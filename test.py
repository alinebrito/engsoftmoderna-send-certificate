import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os.path
import pandas as pd
from time import sleep

def get_path(code):
  return 'docs/'

def get_certificate(code):
  return 'certificado' + str(code) + '.pdf'

def get_declaration(code):
  return 'declaracao' + str(code) + '.pdf'
  
def test_files(student_name, student_code):
  path = get_path(student_code)
  filename_certificate = get_certificate(student_code)
  filename_declaration = get_declaration(student_code)

  print('\n-----\nProcessing %d (%s)...' % (student_code, student_name))
  if (not os.path.isfile(path + filename_certificate)) or (not os.path.isfile(path + filename_declaration)):
    print('\nERRO: File not found, %s, %i' % (student_email, student_code))
    print('%s' % filename_certificate)
    print('%s' % filename_declaration)
  else:
    print('OK.') 
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
  dataset = read_csv(file_name_list_students)
  for index, row in dataset.iterrows():
    student_name = row.get('nome')
    student_code = row.get('numero')
    test_files(student_name, student_code)
  print('\nEnd.')
run()