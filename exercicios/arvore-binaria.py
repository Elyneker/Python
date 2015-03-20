qtdNos = input("Qual o tamanho da arvore?: ")
linhas = []


def Is_new_line(x):
	x = float(x)
	while x >= 1:
		if x/2 == 1 or x/2 == 0.5:
			return True
		x = x/2
	return False

def montador(nos):
	pos = 0
	for x in range(1, nos + 1):
		if Is_new_line(x):
			linhas.append([])
			linhas[pos].append(x)
			pos += 1
		else:
			linhas[pos-1].append(x)


def printer(nos):
	for no in range(len(nos)):
		print " ".join(map(str, nos[no]))



montador(qtdNos)
printer(linhas)







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