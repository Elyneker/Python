# qtdNos = input("Qual o tamanho da arvore?: ")
qtdNos = 15
linhas = []


def Is_new_line(x):
	x = float(x)
	while x >= 1:
		if x/2 == 1 or x/2 == 0.5:
			return True
		x = x/2
	return False

def monta_nos(nos):
	pos = 0
	for x in range(1, nos + 1):
		if Is_new_line(x):
			linhas.append([])
			linhas[pos].append(x)
			pos += 1
		else:
			linhas[pos-1].append(x)

def espacos(qtdNos):
	x = 1
	while x <= qtdNos:
		x *= 2
	qtdEsp = x-1
	return qtdEsp


monta_nos(qtdNos)
espc = espacos(qtdNos)

for i in range(len(linhas)):
	print 1*" " + (1*" ").join(map(str, linhas[i]))









#####
##### TESTES
#####
def testar_algoritimo(x):
	x = float(x)
	while x >= 1:
		if x/2 == 1 or x/2 == 0.5:
			return True
		x = x/2
	return False

def contador():
	for x in range(1,10000+1):
		result = testar_algoritimo(x)
		if result == True:
			with open("resultado.txt", "a") as f:
				f.write(str(x) + "  -  " + "###" + "\n")


# print testar_algoritimo(tamanho)
# contador()