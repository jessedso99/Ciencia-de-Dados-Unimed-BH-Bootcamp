a, b = (False, "teste")
print(type(b))
print(type(a))
a = 10
b = int(a)
print(f'hello {b}')

nome= input("insira seu nome: ")
sobrenome= input("insira seu nome: ")
# dentro do print temos os atributos sep, end, file e flush
print(nome, sobrenome)
print(nome, sobrenome, end= "...\n")
print(nome, sobrenome, sep= "#")