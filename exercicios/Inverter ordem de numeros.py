num = input('Digite um inteiro: ')
numstr = str(num)
tm = len(numstr)
strfim = ''

for i in range(0, tm):
	tm -= 1
	strfim += numstr[tm]
print strfim