############################################################################
# Descobri quantos quadrados da pra se fazer com um qtd de quadrados menores
############################################################################

qtd = input('Digite a qtd de quadrados: ')
x = 0
potencia = 0
contPotencia = 0
conjuntos = 0

while x == 0 :
	potencia = contPotencia**2
	#print ">>> %i**2 = %i" %(contPotencia, potencia)

	if potencia == qtd:
		linhas = qtd**(1.0/2)

		if linhas == 1:
			print ">>> 1 conjunto de 1"
			conjuntos += 1
		else:
			print ">>> 1 conjunto de %i(%ix%i)" %(qtd, linhas, linhas)
			conjuntos += 1
		x = 1

	elif potencia > qtd:
		potenciaAnterior = ((contPotencia-1))**2
		qtd = qtd - potenciaAnterior
		linhas = potenciaAnterior**(1.0/2)
		
		if linhas == 1:
			print ">>> 1 conjunto de 1"
			conjuntos += 1
		else:
			print ">>> 1 conjunto de %i(%ix%i) e %i de sobra" %(potenciaAnterior,linhas, linhas, qtd)

		conjuntos += 1
		contPotencia = 0

	contPotencia += 1

	if qtd == 0:
		x = 1