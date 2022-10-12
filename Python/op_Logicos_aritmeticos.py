from operator import truediv


print("exponenciação ** e divisao inteira // ")
print("precendenia matematica: (), **, (* e / // % a executa 1º qm esta +a esquerda), (+ e - executa 1º qm esta +a esquerda)")
dir()# lista de nome no escopo
#python e python -1 arquivo.py usar o modo interativo
a= 2**4-10+(1**2//5-3)
print(f"po valor eh: {a}")

b= 20
b +=5 # pega o valor anterior e adiciona 5
print(b)
b -=5 # pega o valor anterior e subtrai 5
print(b)
b *=5 # pega o valor anterior e multiplica por 5
print(b)
b /=5 # pega o valor anterior e divide por 5
print(b)
b //=5 # pega o valor anterior e divide por 5
print(b)
b **=5 # pega o valor anterior e divide por 5
print(b)
b %=5 # pega o valor anterior e divide por 5
print(b)


print("\nteste1")
print(f"valor a= {a} e valor b= {b}") #os todos tem q ser vdd pra TRUE
print(b>= a and a>10)
print(f"valor a= {a} e valor b= {b}")# apenas um tem q ser vdd pra TRUE
print(b>= a or a>10)

print("\nteste2")
# ordenação de comparação eh da esquerda p direita. as prioridades são dos parentes ()
print(True and True)
# O python sempre vai tentar fazer pares de operandos. ((x and y) or (z and w))
print(True and True or False and False)
# Qnd a qnt de operandos for impar ele vai fazer os pares q aperecem primeiro. (((x and y)) or z)
print(True and True or False)
print((((True and True) or False) and False))

print("\nteste3")
teste=[]
print(not a>b)
print(not"a")
print(not"")
print(not teste)