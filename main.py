idades = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
print(type(idades))
print('Essa é a lista de idades: ', idades)
print('Essa é a idade do primeiro elemento da lista: ', idades[0])

idades.append(51)
print('Essa é a lista de idades: ', idades)

idades.remove(39)
print('Essa é a lista de idades: ', idades)

idades.clear()
print('Essa é a lista de idades: ', idades, ' e ela está vazia')

idades = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
print('Essa é a lista de idades: ', idades)

if 39 in idades:
    print('A idade 39 está na lista de idades')
else:
    print('A idade 39 não está na lista de idades')

if 55 not in idades:
    idades.append(55)
    print('A idade 55 foi adicionada na lista de idades')
    print(idades)
else:
    print('A idade 55 já está na lista de idades')

idades.extend([56, 57, 58, 59, 60])
print('Essa é a lista de idades: ', idades)

idades_no_ano_que_vem = []

for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)
print('Essa é a lista de idades no ano que vem: ', idades_no_ano_que_vem)

