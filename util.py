import os.path
import pandas as pd

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

