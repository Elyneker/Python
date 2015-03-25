############################
# Dividir numeros por soma #
############################

num1 = input('Digite o numerador: ')
num2 = input('Digite o denominador ')
resultado = 0
resultado2 = 0

def mult_por_10(valor):
	t = 0
	for x in range(1, 11):
		t += valor
	return t

while num1 != 0:
	if num1 - num2 < 0:
		num3 = mult_por_10(num1)
		while num3 > 0:
			if num3 - num2 < 0:
				break
			num3 -= num2
			resultado2 += 1
		break
	num1 -= num2
	resultado += 1

print str(resultado) + ',' + str(resultado2)

# Esta com apenas 1 numero depois da virgula. Preguica ter deminar. Se eu fosse fazer para varios mumeros depois
# da vírgula usaria a mesma logica, mas criaria uma funcao para ir retornando os valores depois da virgula.