tamanho = input("Digite o tamanho do triangulo: ")
triangulo = []

#Faz os calculos dos elementos do triangulo
###########################################
def linhas(l):
	linha = []
	linha = valores(l)
	triangulo.append(linha)

def valores(v):
	lista = []
	for pos in range(v):
		if pos == 0 or pos == v-1:
			lista += [1]
		else:
			lista += [triangulo[v-2][pos-1] + triangulo[v-2][pos]]

	return lista

for i in range(1, tamanho+1):
	linhas(i)


#Acrescenta zeros para manter alinhamento do triangulo
######################################################
def maiornum(lista):
	x = 0
	for listas in lista:
		for elem in listas:
			if len(str(elem)) > x:
				x = len(str(elem))
	global qtd_espacos
	qtd_espacos = x
	verifica_qtd_strings(x, lista)

def verifica_qtd_strings(qtdzero, lista_v):
	for lista in lista_v:
		for elem in range(len(lista)):
			if len(str(lista[elem])) < qtdzero:
				lista[elem] = addzeros(lista[elem], qtdzero)


def addzeros(num, qtdzeros):
	qtdz = qtdzeros - len(str(num))
	numstr = str(num)
	for n in range(1, qtdz+1):
		numstr = '0' + numstr
	return numstr
maiornum(triangulo)

#Imprimi triangulo na tela
##########################
for i in range(len(triangulo)):
	print (len(triangulo) - i)*(qtd_espacos*' ') + (qtd_espacos*' ').join(map(str, triangulo[i]))



#Observacoes para construção
# 1 - Todo primeiro e ultimo elemento x da linha e = 1;
# 2 - O elemento x2 de cada linha e a soma do x1 + x2 dos elementos da linha anterior
# 3 - O elemento x3 de cada linha e a soma do x2 + x3 dos elementos da linha anterior
# 4 - O elemento x4 de cada linha e a soma do x3 + x4 dos elementos da linha anterior
