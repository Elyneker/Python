#####################################
# Dizer se uma entrada e numero primo
#####################################

num = input('Entre com um numero inteiro: ')

if num == 0 or num == 1:
	print '>>> Nao e primo!'
elif num < 1:
	print '>>> Nao e primo!'
elif num == 2 or num == 3 or num == 5 or num == 7:
	print '>>> %i e Primo!' %(num)
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 9 == 0:
	print '>>> Nao e primo!'
else:
	print '>>> %i e Primo!' %(num)