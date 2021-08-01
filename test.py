import email, smtplib, ssl
import sys

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
 
def test_files(student_name, student_code):
  path = util.get_path(student_code)
  filename_certificate = util.get_certificate(student_code)
  # filename_declaration = util.get_declaration(student_code)
  print('\n-----\nProcessing %d (%s)...' % (student_code, student_name))
  if (util.is_valid_file(path,filename_certificate)):
    print(f"{bcolors.OKBLUE}OK files.{bcolors.ENDC}")
  return 

def test_student_info(student_email, student_code):
  print(f"{bcolors.OKBLUE}OK code.{bcolors.ENDC}" if student_code else f"{bcolors.FAIL}Invalid code.{bcolors.ENDC}")
  print(f"{bcolors.OKBLUE}OK email.{bcolors.ENDC}" if student_email else f"{bcolors.FAIL}Invalid email.{bcolors.ENDC}")
  pass

def run():

  if(len(sys.argv) < 2):
    print("Usage: {} lista_aprovados.csv\n".format(sys.argv[0]))
    return

  file_name_list_students = sys.argv[1]

  dataset = util.read_csv(file_name_list_students)
  for index, row in dataset.iterrows():
    student_name = row.get('nome')
    student_code = row.get('numero')
    student_email = row.get('email')
    test_files(student_name, student_code)
    test_student_info(student_email, student_code)
  print('\n-----\nEnd.')
run()