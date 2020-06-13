import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os.path
import pandas as pd
from time import sleep
import util

class bcolors:
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
 
def is_valid_file(path, file_name):
  is_valid = os.path.isfile(os.path.join(path, file_name))
  if (not is_valid):
    print(f"{bcolors.FAIL}ERROR: File not found %s{bcolors.ENDC}" % (file_name))
  return is_valid

def test_files(student_name, student_code):
  path = util.get_path(student_code)
  filename_certificate = util.get_certificate(student_code)
  filename_declaration = util.get_declaration(student_code)
  print('\n-----\nProcessing %d (%s)...' % (student_code, student_name))
  if (is_valid_file(path,filename_certificate) and is_valid_file(path, filename_declaration)):
    print(f"{bcolors.OKBLUE}OK files.{bcolors.ENDC}")
  return 

def test_student_info(student_email, student_code):
  print(f"{bcolors.OKBLUE}OK code.{bcolors.ENDC}" if student_code else f"{bcolors.FAIL}Invalid code.{bcolors.ENDC}")
  print(f"{bcolors.OKBLUE}OK email.{bcolors.ENDC}" if student_email else f"{bcolors.FAIL}Invalid email.{bcolors.ENDC}")
  pass

def run():
  file_name_list_students = input ('CSV de alunos aprovados (ex: alunos_aprovados_exemplo.csv): ')
  dataset = util.read_csv(file_name_list_students)
  for index, row in dataset.iterrows():
    student_name = row.get('nome')
    student_code = row.get('numero')
    student_email = row.get('email')
    test_files(student_name, student_code)
    test_student_info(student_email, student_code)
  print('\n-----\nEnd.')
run()