"""Cógigo gerador de fracoes de Farey
"""

num_iter = int(input('Digite o valor do número máximo para a sequência de Farey: '))

f = []

"""
for i in range(1, num_iter + 1, 1):
    for j in range(i, num_iter + 1, 1):
        f.append(round((i / j), 2))
f = set(f)
f = sorted(f) # classificar o set
"""

i = 1
while i <= num_iter:
    j = i
    while j <= num_iter:
        f.append(round(i / j, 2))
        j = j + 1
    i = i + 1
f = set(f)
f = sorted(f)
print(f)
