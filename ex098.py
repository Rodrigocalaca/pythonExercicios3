def contador(i, f, p):
	if i < f:
		while i <= f:
			print(f'{i}', end=' ')
			i += p
	elif f < i:
		while f <= i:
			print(f'{i}', end=' ')
			i -= p


contador(1, 10, 2)
print('')
print('-' * 20)
contador(10, 1, 2)