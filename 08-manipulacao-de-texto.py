text = '{1} {3} {0} {2} programação'
text2 = 'israel almeida'
text3 = 'israel é um programador'

print(text.format('estudante', 'isRael', 'de', 'é')) #ordena o texto como quiser
print(text2.capitalize()) #converte a primeira letra em maiusculo
print(text2.startswith('alme')) #verifica se o texto começa com a palavra adicionada
print(text2.endswith('ida')) #verifica se o texto termina com a palavra adicionada
print(text3.find('um')) #retorna a posição da string encontrada
print(text2.replace('almeida', 'ALMEIDA')) #Substitui a palavra
print(text3.upper()) #converte todos os caracteres para maiusculo
print(text3.lower()) #converte todos os caracteres para minusculo
print(text2.islower()) #retorna um boolean se o texto é minusculo
print(text2.isupper()) #retorna um boolean se o texto é maiusculo
print(text2.isnumeric()) #retorna um boolean se o texto é numerico