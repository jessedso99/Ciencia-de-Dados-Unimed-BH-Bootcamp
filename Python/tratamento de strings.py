curso= "   pyTHon . "
print(curso.upper())
print(curso.lower())
print(curso.title())

#remover espaços: todos, da esq p dir, e da dir p esq
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

print(curso.center(10))
print(curso.center(10, '#'))
print("-".join(curso))

numero = 3.14159
print(f"\ninterpolando com fstring {numero}")
#formatando com fstring
print(f"o valor c 2 casa dec. eh: {numero:.2f}")
print(f"o valor c 2 casa dec. eh: {numero:10.2f}")

#eh possivel usar o format com dicionario. os valores dentro de {} na strig devem ser as chaves do dicionario
dados= {"nome": "jess", "idade": 23}
print("\nmeu nome eh {nome} e tenho {idade}".format(**dados))

#FATIAMENTO DE STRING

nome= "Jesse da Silva Oliveira"
print(nome[0])
print(nome[:5])
print(nome[9:14])
print(nome[9:22:2])
print(nome[:])
print(nome[::-2])

#STRING DE MULTIPLAS LINHAS OU STRING TRIPLAS
  #Preserva os espaços e quebras de linha
nome2= "Jesse2"
print(f'''    === MENU ===
1- OPÇAO 1
        2- OPÇAO 2
 . 3- SAIR\n''')

 #como saber qnts vezes a palavra se repete na string
string11= "ola mundo, mundo hello"
print(string11.count("mundo"))
#replace
print(string11.replace("hello","HELLOOWW"))