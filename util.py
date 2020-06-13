import os.path
import pandas as pd

class bcolors:
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
def get_path(code):
  return 'docs'

def get_certificate(code):
  return 'certificado' + str(code) + '.pdf'

def get_declaration(code):
  return 'declaracao' + str(code) + '.pdf'

def read_csv(file_name):
  print("Reading %s..." % file_name)
  dataset = ""
  if not os.path.isfile(file_name):
    print('ERRO: File not found %s' % file_name)
  else:
    dataset = pd.read_csv(file_name, sep=";", keep_default_na=False)
  return dataset

def is_valid_file(path, file_name):
  is_valid = os.path.isfile(os.path.join(path, file_name))
  if (not is_valid):
    print(f"{bcolors.FAIL}ERROR: File not found %s{bcolors.ENDC}" % (file_name))
  return is_valid

