###############################
# Dividir numeros por soma #
################################

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero ')
resultado = 0
resultado2 = 0

def divisor(num, den):
	global resultado2
	while num != 0:
		num -= den
		resultado2 = resultado2 + 1

while num1 != 0:
	num1 -= num2
	resultado = resultado + 1

	if num1-num2 < 0 and num1 != 0:
		num3 = 10 - num1
		num1 = num1 + num3
		divisor(num1, num2)*

print str(resultado) + ',' + str(resultado2)