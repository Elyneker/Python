qtdNos = input("Qual o tamanho da arvore?(ex: 63): ")
linhas = []
espc_entre_num_base = 2
qtd_carac_num = 2


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


line_space = 2
def firts_espc(last_qtd_espac, qtdNos):
	#define qtd espaco total da ultima linha
	x = 1
	while x <= qtdNos:
		x *= 2
	line = x/2

	#faz os calculos de espaco do comeco da primeira linha em relacao a ultima
	qtd_espc = ((line*qtd_carac_num*espc_entre_num_base)/last_qtd_espac)-qtd_carac_num

	global line_space
	line_space *= 2

	return qtd_espc


string_space = 2
def space_str(last_qtd_espac, qtdNos):
	#define qtd espaco total da ultima linha
	x = 1
	while x <= qtdNos:
		x *= 2

	#faz os calculos de espaco do comeco da primeira linha em relacao a ultima
	qtd_espc = ((x*qtd_carac_num*espc_entre_num_base)/last_qtd_espac)-qtd_carac_num
	global string_space
	string_space *= 2
	return qtd_espc

# Adiciona zeros para manter alinhamento 
def add_zeros(x):
	elem = str(x)
	return (qtd_carac_num - len(elem)) * "0" + elem




#executa funcoes
monta_nos(qtdNos)
#Verifica quantidade de caracteries para definir quantidade de zeros e espacos da base
if len(str(linhas[-1][-1])) != 1:
	qtd_carac_num = len(str(linhas[-1][-1]))
	espc_entre_num_base = len(str(linhas[-1][-1]))

for i in range(len(linhas)):
	space = firts_espc(line_space, qtdNos)
	str_space = space_str(string_space, qtdNos)
	print space*" " + (str_space*" ").join(map(add_zeros, linhas[i]))