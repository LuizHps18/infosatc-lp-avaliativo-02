#Criação das 4 listas
filmes = ['Harry Potter', 'Zumbilandia', 'Invocação do Mal', 'O elo perdido'] 
jogos = ['Valorant', 'Dark Souls', 'Dont Starve Together', 'Cup Head'] 
livros = ['O homem de giz', 'Diario de um banana', 'A guerra dos tronos'] 
esporte = ['xadrez', 'futebol', 'basquete', 'volei'] 

#Adicionar 2 itens em cada lista
filmes.append("Ta dando onda")
filmes.append("O grito")

jogos.append("Minecraft")
jogos.append("Hollow Night")

livros.append("Diario de Anne Frank")
livros.append("Vida de droga")

esporte.append("Tênis")
esporte.append("Corrida")

#Criação de uma lista para as outras 4
listageral = [filmes, jogos, livros, esporte]
print(listageral)


#print de um item da lista livros
print(livros[2])

#Removendo item da lista esportes
del esporte[0]
print(esporte)

print(listageral)

#Adicionando lista na lista geral

disciplinas = ['Matematica', 'Portugues', 'Ciencias', 'Biologia']
print(listageral)

