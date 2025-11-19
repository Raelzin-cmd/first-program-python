numeros = [34, 5, 120, 8,  654]
nomes = ['Israel', 'Pedro']
booleanos = [True, False]
lista = [[1, 3, 5], [2, 4, 6]]

# Manipulação
print(numeros[2]) #retorma o elemento pela posição mencionada
print(numeros[1:3]) #retorna elemento de um ponto a outro pela posição
print(lista[0][1]) #retorna o elemento de uma lista dentro de uma lista

# Metodos
nomes.append('Maria') #Adiciona um elemento na lista
nomes.append('Joao')
print(nomes)
numeros.insert(1, 54) #insere um elemento na lista de acordo com a posição
numeros.insert(len(numeros), 1000) #insere um elemento na lista na ultima posição
print(numeros)
nomes.remove('Pedro') #remove o elemento pelo valor
print(nomes)
nomes.pop(1) #remove o elemento pela posição
print(nomes)
nomes.clear() #limpa toda a lista
print(nomes)

numeros.sort() #ordena a lista
print(numeros)
print(numeros[0])  #retorna o menor numero (ordem crescente)
numeros.reverse() #reverte a ordem
print(numeros)
print(numeros[0]) #retorna o maior numero (ordem decrescente)
