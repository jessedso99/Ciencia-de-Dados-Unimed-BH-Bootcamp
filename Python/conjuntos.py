#SET é uma coleção que não possui objetos repetidos.
#Podemos usá-los para representar conjuntos matemáticos ou para eliminar itens deuplicados de uma iterável
#podem ser declarados usan o SET() ou usando {}
set1= {"palio", 2, "palio", 3, 3, 2} #set craido com {}
print(set1)
lista1= ["palio", 2, "palio", 3, 3, 2]
set2= set(lista1) # set criado com set() baseado na lista1

print("Essa eh nossa lista ", lista1)
print("Esse eh nosso SET baseado na lista", set2)# mesmo result do set1
#outro exemplo... N considerar a ordem do set
print(set("abacaxi")) #string iteravel
#funfa com tuplas tbm
tupla1= ("palio", "palio", "Celta", "gol", "Gol")
print(set(tupla1)) #letras em Maisc. ou minusc. diferenciam palavras iguais

    #ALGUMAS PROPRIEDADES
print("\n\tACESSAR VALORES DO SET so eh possivel transfm em listas")  #ACESSANDO VALORES DO SET. N podemos acessar os valores do set
numeros1= {1, "Celta", 2, "Celta", 2}
#print(numeros1[0]) #TypeError: 'set' object is not subscriptable
#Se quiser consumir os valores tem que tranformar o SET  em uma LISTA
numerosList= list(numeros1)
print(numerosList[1])

  #PODEMOS PERCORRER UM SET COM FOR()
for iten in numeros1: #Observe que os itens repetidos n foram iterados, enquanto numa lista isso n ocorreria
  print(f"iten de numeros1: {iten}")

print("\n\tENUMERATE")  #ENUMERATE
for indice, iten in enumerate(numeros1):
  print(f"{indice}: {iten}") #numeros1= {1, "Celta", 2, "Celta", 2}

#ETAPA2
print("\n\tEtapa 2: Union, intersection, difference, symmetric_differnte, issubset, issuperset, isdisjoint")
conjunto_a= {1, 2, 2, 3}
conjunto_b= {3, 4, 2, 5}

print(conjunto_a.union(conjunto_b))#Union: os repetidos sao apresentados 1 vez
print(conjunto_a.intersection(conjunto_b))#intersection: So os elementos comuns entre os 2 sets
print(conjunto_a.difference(conjunto_b))#compelmente de A em B. O A e dif pq tem o 1
print(conjunto_b.difference(conjunto_a))#compelmente de B em A. O B e dif pq tem 4, 5
print(conjunto_a.symmetric_difference(conjunto_b))# todos os elementos dos 2 sets q n estão na interseccao

conjunto_c= {1, 2, 2, 3} 
conjunto_d= {1, 3, 4, 2, 5}
print(conjunto_c.issubset(conjunto_d)) #IsSubSet verifica se um conjunto esta contido em outro
print(conjunto_d.issubset(conjunto_c)) #todos os elemtnso de C estao em D? Todos de D estao em C
#Existe tbm o issuperset() q faz uma operação similar so q com pensameto "inverso"
# isdisjoint verifica se há qlqr similaridade entre os sets. se não então true

  #ETAPA3
print("\n\tEtapa 3: Manipulação -> add(), copy(), discard(), remove(), pop(), len(), operador in")
conjunto_e= {1, "Batata", 1, 2, "Batata", "Uva", 2}
conjunto_e.add("Bola") #add ao fim do set
conjunto_e.add(1) #se o iten ja existe ele n adiciona
print(conjunto_e)
  #copy cria uma copia do set
copiaE = conjunto_e.copy()
print(copiaE)
  # discard descarta um item do set
copiaE.discard("Batata")
copiaE.discard("Batatao2")#esse valor n existe o discard n vai reclamar disso. Ja o remove()...
  #remove() eh similar ao discard mas mostrara um erro se o elemento q qr remover n exisitr no set
#copiaE.discard("Batatao2") #exibira um erro
print(copiaE)
  #pop remove sempre o primeiro item do set
copiaE.pop()# {2, 'Bola', 'Uva'}
copiaE.pop()# {'Bola', 'Uva'}
print(copiaE)
  #len mostra o tamanho do set
print(len(copiaE))
  #operador in retornar true ou false
print("Bola" in copiaE)#true
print("Batata" in copiaE)#false