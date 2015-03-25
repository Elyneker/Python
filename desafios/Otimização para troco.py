#########################################################
# Devolver ao cliente o menor numero de notas de um troco
#########################################################

valor = input("valor da conta: ")
pago = input("valor pago: ")

while pago < valor:
	pago = input("Valor pago (Digite um valor igual ou superior ao da conta): ")

troco = pago - valor
trococ = 0

print
print ">>> O troco e %i" %(troco)
print

notas = 0

if troco == 0 or troco < 1:
	print ">>> 0 de troco"
while troco >= 50:
	troco -= 50
	notas += 1
if notas >= 1:
	print ">>> Notas de 50: " + str(notas)
notas = 0

while troco >= 20:
	troco -= 20
	notas += 1
if notas >= 1:
	print ">>> Notas de 20: " + str(notas)
notas = 0

while troco >= 5:
	troco -= 5
	notas += 1
if notas >= 1:
	print ">>> Notas de 5: " + str(notas)
notas = 0

while troco >= 2:
	troco -= 2
	notas += 1
if notas >= 1:
	print ">>> Notas de 2: " + str(notas)
notas = 0

while troco >= 1:
	troco -= 1
	notas += 1
if notas >= 1:
	print ">>> Notas de 1: " + str(notas)
notas = 0

print
