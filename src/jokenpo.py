def jokenpo(jogada1, jogada2):
	jogada2 = jogada2.upper()
	jogada1 = jogada1.upper()
	if jogada1 == 'PEDRA' and jogada2 == 'PAPEL':
		return('PAPEL')
	elif jogada1 == 'PEDRA' and jogada2 == 'TESOURA':
		return('PEDRA')
	elif jogada1 == 'PEDRA' and jogada2 == 'PEDRA':
		return('EMPATE')
	elif jogada1 == 'PAPEL' and jogada2 == 'PAPEL':
		return('EMPATE')
	elif jogada1 == 'PAPEL' and jogada2 == 'TESOURA':
		return('TESOURA')
	elif jogada1 == 'PAPEL' and jogada2 == 'PEDRA':
		return('PAPEL')
	elif jogada1 == 'TESOURA' and jogada2 == 'PAPEL':
		return('TESOURA')
	elif jogada1 == 'TESOURA' and jogada2 == 'TESOURA':
		return('EMPATE')
	elif jogada1 == 'TESOURA' and jogada2 == 'PEDRA':
		return('PEDRA')	
	else:
		return('PARAMETROS_INCORRETOS')






