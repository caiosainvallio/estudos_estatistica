"""*************************************************************
Modelo Simulated Annealing para otimização

@caiosainvallio

Este modelo encontra o mínimo de uma fução de duas variável

*************************************************************"""




# Funções ------------------------------------------------------------
# Fução a ser minimizada
def E(x, y):
	E = x**2 + y**2 - 6*x - 8*y + 26
	return E

# Fução aleatório
# LI = Limite Inferior
# LS = Limite Superior
import numpy as np
def aleatorio(li, ls):
	aleatorio = np.random.random() * (ls - li) + li
	return aleatorio

# Função Probabilidade Natural pn
def pn(de, t):
	try:
		pn = 1 / (np.exp(de/t))
		return pn
	except:
		pn = 0
		return pn

# Variáveis ----------------------------------------------------------
numMaxIter = 1000
tempInicial = 100
a = 0.75
pulo = 25
verbose = 2

x = list(range(0, numMaxIter))
y = list(range(0, numMaxIter))
e = list(range(0, numMaxIter))

maximo = pulo
iterador = 0
t = tempInicial
cont = 0

if verbose == 1:
	print("\n")
	print("Iter" + "\t" + "x", "\t" + "y" + "\t" + "E" + "\t" + "DE" + "\t" + "PN" + "\t" + "PA" + "\t" + "T" + "\t" + "Aceita")
elif verbose == 2:
	print("\n")
	print("Iter" + "\t" + "x", "\t" + "y" + "\t" + "E" + "\t" + "DE" + "\t" + "PN" + "\t" + "PA" + "\t" + "T")

# Código -------------------------------------------------------------
while maximo <= numMaxIter:
	while iterador <= maximo:
		i = 0
		while i <= numMaxIter:
			x[i-1] = aleatorio(0, 5)
			y[i-1] = aleatorio(0, 5)
			e[i-1] = E(x[i-1], y[i-1])
			if i != 0:
				de = e[i-1] - e[i-2]
			else:
				de = e[i-1]
			prob_nat = pn(de, t)
			pa = np.random.rand()
			if de <=0 and prob_nat >= pa:
				aceita = "sim"
			else:
				aceita = "Não"
				x[i-1] = x[i-2]
				y[i-1] = y[i-2]
				e[i-1] = e[i-2]
			if verbose == 1:
				print(" {}	{:.2f}	{:.2f}	{:.2f}	{:.2f}	{:.2f}	{:.2f}	{:.2f}	{}".format(cont, x[i-1], y[i-1], e[i-1], de, prob_nat, pa, t, aceita))
			i += 1	
			cont += 1
		iterador += 1
	if verbose == 2:
		print(" {}	{:.2f}	{:.2f}	{:.2f}	{:.2f}	{:.2f}	{:.2f}	{:.2f}".format(cont, x[-1], y[-1], e[-1], de, prob_nat, pa, t))
	t = a * t
	maximo += pulo

print("\n\n\nResultado final:\n--------------------------------\n")
print("x	y	E(x)")
print("{:.2f}	{:.2f}	{:.2f}\n\n\n".format(x[-1], y[-1], e[-1]))
