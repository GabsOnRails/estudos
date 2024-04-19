# Enviando e-mail com anexo gerado pelo python com as ações do Banco do Brasil



from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = open('senha','r').read()

from_email = "gfelipeoliveira.2000@gmail.com"
to_email = "gfelipeoliveira.2000@gmail.com"
subject = 'Ações Banco do Brasil'
body = open('files/corpo_bb.txt','r',encoding='utf-8').read()

# 1->  Estruturando a mensagem via email
message = EmailMessage()
message ['From'] = from_email
message ['To'] = to_email
message ['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 2 -> Adicionando anexo
anexo = 'files/bb_preco.png'
# print(mimetypes.guess_type(anexo)[0])
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo,'rb') as a:
    message.add_attachment(
        a.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = anexo
    )

# 3 -> Enviando email
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=safe) as smtp:
    smtp.login(from_email,password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
        )