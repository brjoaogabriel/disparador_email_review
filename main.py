#	Lib responsável por importar as credenciais utilizadas para logar
import credencial

#	Lib responsável por importar a mensagem HTML
import html_mensagem

#	Lib responsável pro encapsular a mensagem do e-mail
import email.message

#	Lib responsável por fazer a conexão com o servidor de disparo de e-mail
import smtplib

#	Setando variáveis de disparo
acesso = credencial.importa_credenciais('acesso.txt')
alvo = "teste@gmail.com"
assunto = "teste"

#	Setando a mensagem
with open('email.txt', 'r') as arq:
	mensagem = html_mensagem.text("USUARIO ZICA")

#	Setando variável responsável por encapsular o e-mail
msg = email.message.Message()
msg['from'] = acesso['user']
msg['to'] = alvo
msg['subject'] = assunto

#	Anexando a mensagem
msg.add_header('Content-Type', 'text/html')
msg.set_payload(mensagem)

#	Iniciando comunicação com o servidor
servidor = smtplib.SMTP('SMTP.office365.com: 587')
servidor.ehlo()
servidor.starttls()
servidor.login(msg['from'],acesso['pass'])

#	Disparando o e-mail
servidor.sendmail(msg['from'], [msg['to']], msg.as_string())