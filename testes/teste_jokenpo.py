import sys

sys.path.insert(1,'C:\\Documents and Settings\\usuario\\Meus documentos\\Jokenpo\\src')
#sys.path.append('../Jokenpo/src')

import jokenpo

jogada = ['pedra', 'papel', 'tesoura', 'empate', 'paremetros_incorretos']

def partida(retornoFuncao, resultado):
	if retornoFuncao.upper() == resultado.upper():
		print('correto')
	else:
		print('errado')


partida( jokenpo.jokenpo(jogada[0], jogada[1]), jogada[1] )
partida( jokenpo.jokenpo(jogada[0], jogada[2]), jogada[0] )
partida( jokenpo.jokenpo(jogada[0], jogada[0]), jogada[3] )

partida( jokenpo.jokenpo(jogada[1], jogada[1]), jogada[3] )
partida( jokenpo.jokenpo(jogada[1], jogada[2]), jogada[2] )
partida( jokenpo.jokenpo(jogada[1], jogada[0]), jogada[1] )

partida( jokenpo.jokenpo(jogada[2], jogada[1]), jogada[2] )
partida( jokenpo.jokenpo(jogada[2], jogada[2]), jogada[3] )
partida( jokenpo.jokenpo(jogada[2], jogada[0]), jogada[0] )
