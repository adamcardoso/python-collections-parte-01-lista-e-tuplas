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
