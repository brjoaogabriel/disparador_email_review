def importa_credenciais(diretorio):
	with open('acesso.txt', 'r') as arq:
		__creds = (arq.read().split(","))

	return {'user': __creds[0], 'pass':__creds[1]}