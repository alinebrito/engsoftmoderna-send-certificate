# engsoftmoderna-send-certificate
Script para enviar os certificados das turmas do [Curso de Extensão em Engenharia de Software Moderna (DCC/UFMG)](http://www.engsoftmoderna.dcc.ufmg.br/)

## Instruções:

0) Habilitar login via apps no Gmail do curso: [lesssecureapps](https://myaccount.google.com/lesssecureapps)

1) Criar um arquivo  CSV separado por ";" com os dados dos alunos.  Exemplo: [alunos_aprovados_exemplo.csv](https://github.com/alinebrito/engsoftmoderna-send-certificate/blob/master/alunos_aprovados_exemplo.csv)

2) Armazenar no diretório `docs` o certificado e declaracao do aluno conforme o seu número. Por exemplo, para o aluno de código 41:

>docs/declaracao41.pdf\
>docs/certificado41.pdf

3) Verificar se os arquivos estão corretos. Para tanto, execute o script de teste e informe o nome do arquivo CSV:

> python3 test.py

4) Envie os certificados e declarações. Os emails são enviados em Bcc para o email do curso (informado ao executar o script).

> python3 send.py

## Instalar dependências

> pip3 install -r requirements.txt




