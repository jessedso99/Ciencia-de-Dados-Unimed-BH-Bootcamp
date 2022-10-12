#lista de listas
#lista1=[] é possivel criar lista vazias asssim
#tbm podemos criar listas usando o list()

lista1= ["teste", 12, 1.33, True, ["outra lista", 234, 23.444, ["Mais uma", 45.66, False]]]
lista1[-1]#-1 sempre será o ultim item da lista, seno assim -3 é o antepenultimo iten
print(12 in lista1)
print("teste" not in lista1)
numeros1= list(range(10))

#operadores is e not is verificam se valores ocupam o mesmo espaço da memoria
#são operadores de identidade
#is e not is são operadores de associação

matriz= [
  [1, "a", 2], 
  ["b", 3, 4], 
  [6, 5, "c"]
]
matriz[0]
matriz[1][2]
matriz[0][-1]

#Enumerate: usamos p saber qual o index do item que acessamos qnd percorremos a lista
for indice, item in enumerate(lista1): # a variavel indice se inica em zero, por padrao
  print(f"Lista1, {indice}: {item}")

#------ PARTE 2: METODOS DA CLASSE LIST
lista0= []
  # append adiciona apenas um item no final da lista
lista0.append(1) 
  #clear() limpa a lista, remove todos os elentos
lista0.clear()

lista0.append("Python")
lista0.append("Python")
lista0.append([1, "Gol", 2.4])

  #copy cria uma copia de uma lista
lista2= lista0.copy()
print(lista2)
  #Count conta qnts vezes um dados elementos aparece na lista
lista2.count("Python")
  #extend eh parecido com append, so que ao inves de 1 elemento, pdemos passar uma lista de elementos
lista0.extend([lista2, [1, 2]]) #OBS, podemos passar apenas 1 lista
print(lista0)
  #index devolve a primeira ocorrencia de um elemento
lista0.index("Python")
  #pop remove o ultimo item da lista
lista0.pop()
lista0.pop(2)# tbm pdemos informar qual elemtnos queremos excluir informando seu indice na lista.
  #remove fincionar parecido, mas precisamos infoar o valor do elemento q queremoe exlcuir
lista0.remove("Python") #Obs, Se o elemtno for repetido na lista, o remove remove apenas 1 ocorrencia desses elelmentos.
  #[].sort() ordena a lista
  #sorted([]) é parecido com o sort
  #len([]) devolve o tamanho da lista