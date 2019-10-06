def criba_erastotenes(n):
	numeros_primos = set()
	numeros_tachados = set()
	ultimo_primo = 2

	tope_alcanzado = False

	for i in range(2,n+1):
		if i not in numeros_tachados:
			ultimo_primo = i
			numeros_primos.add(ultimo_primo)
		else:
			continue
		if tope_alcanzado:
			continue

		if ultimo_primo ** 2 > n:
			tope_alcanzado = True

		for i in range(ultimo_primo*2,n+1,ultimo_primo):
			numeros_tachados.add(i)

	return list(numeros_primos)

print(criba_erastotenes(80000))