######################################
# Decomposicao prima de um inteiro > 1 
######################################

num = input('Digite um numero mair que 1: ')
x = 1
lis = []

while x == 1:
	if num % 2 == 0:
		lis.append(2)
		num = num/2
	elif num % 3 == 0:
		lis.append(3)
		num = num/3
	elif num % 5 == 0:
		lis.append(5)
		num = num/5
	elif num % 7 == 0:
		lis.append(7)
		num = num/7
	elif num % 9 == 0:
		lis.append(9)
		num = num/9
	elif num == 1:
		x = 0

print lis