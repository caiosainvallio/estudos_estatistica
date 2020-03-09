"""Código para achar o arco tangente
"""

import math 

x = float(input("Digite o valor da tangente: "))
n = int(input("Digite a quantidade de termos: "))

inicio = 1
passo = 2
radianos = 0

k = 2

for i in range(inicio, 2 * n, passo):
	coeficiente = ((-1) ** k) / i
	radianos = radianos + coeficiente * x ** i
	k = k + 1

print("O valor da angulo = {:.3f} radianos".format(radianos))
graus = radianos * 180 / math.pi
print("O valor de angulo = {:.3f} graus".format(graus))
