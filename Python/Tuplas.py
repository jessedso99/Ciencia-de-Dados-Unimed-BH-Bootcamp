#TUPLAS SAO IMUTAVIES, N SE PODE ALTERAR OS SEUS ITENS
#podemos declara tuplas usando o tuple quando a tupla POSSUIR APENAS 1 ELEMENTO
letras= tuple("python",)
#ou simplesmente passando os itens dentro de parenteses QUANDO POSSUIR VARIOS
frutas= ("laranha", "pera", "uva", 5, "uva", )
#podemos acessar os valores de um tupla assim como fazemos com a lista
print(frutas[1])
#uma boa pratica e coloca , ao final dos itens de uma tupla com apenas 1 elemento
pais= ("brasil",)
# tupla de 1 unico item eh incrementavel. mas eh necessario q tenha sido declarado com tuple()
print(letras[1])
#pais= ("teste") #remover # e ver o print
print(f"{pais} e {type(pais)}")

#tupla aninhadas (tupla de tuplas))
tuplas= (
  (1, "a", 2),
  ("b", 3, 4),
  (6, 5, "c"),
)
#print da tupla de tuplas
print(tuplas[0])
print(tuplas[0][0])
#podemos usar -1 tbm para printar invertido
print(tuplas[0][-1])
print(tuplas[-1][-1])

#Fatiamento (acesso) Start, stop, step
print(tuplas[0:3:2])#acessa cada uma das listas, incianda em 0 e ate 3-1, com passo 2
print(letras[0::2])# acessa as letrtas do elemeno, iniciando em 0, indo ate o fim, com passo 2
print(letras[::-1])#tudo e reverse

print("\n")
#METODOS
print (frutas.count("uva"))
print (len(tuplas))
print (letras.index("y"))

#Podemos armazenar variaveis nas tuplas
#Porem , uma vez criada, mesmos e lateramos o valor da variavel, esse valor na tupla nao sera atualizado
a= 10
tupla2= ("valor", a,)
a= 20
print(f"""Valor de a antes da tupla ser declarada eh 10. 
{tupla2} tipo eh {type(tupla2)}. Porem o valor de a eh {a}""")
