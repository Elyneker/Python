#####################################
# Descobrir se um numero e triangular
#####################################

num = input("Digite um numero diferente de 0: ")
while num == 0:
	num = input("Digite um numero diferente de 0: ")
a = 1
x = 0
while x < num:
	x = a*(a+1)*(a+2)
	if x == num:
		print "Seu numero e triangular!"
	elif x > num:
		print "Seu numero nao e triangular"
	a += 1