def exibir_msg():
  print("Ola mundo!")

def exibir_msg2(nome, idade):
  print(f"bem vindo {nome}! Sua idade eh: {idade}")

def exibir_msg3(nome= "Antonio"):
  print(f"bem vindo {nome}!")

exibir_msg()
exibir_msg2("Jessie", 16)
exibir_msg3()
print(exibir_msg3("Jesseh"))#quando damos um print, ele exibe tbm o return da funcao, q nesse caso é none(padrao)

#RETURN eh usado para retornar determinaod valor. Por padrao, as funcoes em python retornam NONE qnd n especificado
#Python pode retornar mais de uma valor, diferentemente de outras ling. de prog.
# os valores do return são retornados em um TUPLA
def soma1(a, b):
  valor= (int(a)+int(b))
  c= "teste"
  return valor, c

print(soma1(a=5,b=7))

#DIFERENTES MANDEIRAS DE SE PASAR VALORES PRA FUNCOES
def salvar_carro(marca, modelo, ano, placa):
  print(f"Carro inserido! {marca}/{modelo}/{ano}/{placa}")

#Passando na ordem em que foram declarados
salvar_carro("Fiat", "Uno", "2010", "ABC-1234")
#Passando FORA DA ORDEM
salvar_carro(placa= "ABC-1234", marca= "Fiat", ano= 2010, modelo= "Uno")
#Passando Com DICIONARIOS
salvar_carro(**{"placa":"ABC-1234", "marca":"Fiat", "ano":2010, "modelo":"Uno"})
#dicio1= {"placa":"DEF-5678", "marca":"Ford", "ano":2015, "modelo":"Fiesta", "Cor":"Azul"}

#args kwargs
#(a, b, c, d) -> deve-se passar valroes pode posição(na ordem em q foram declarados)
#(a, b, /, c, d) -> deve-se passar os valores de a e b orbigatoriamente por posição e os outros fica a criterio passar ou n por posição
#(a, b, /, *, c, d) -> deve-se passar os valores de a e b orbigatoriamente por posição e os outros passar orbigatoriamente por nome (1, 2, c=3, d=4)

#--------------------------------
#OBJETOS DE PRIMEIRA CLASSE
#Em python tudo eh objeto, dessa forma funções também o são. Iso as tornam objetos de primeira classe
#Sendo assim, podemos atribuir essas funcoes como
#valor p variavies, inclui-las em listas, tuplas, dics, passa-las como paramentros p funcoes
def somar(a, b):
  return a+ b

def exibir_result(a1, b1, funcSomar):
  result= funcSomar(a1, b1)
  print(f"O resul da operação {a1}+{b1}= {result}.")

exibir_result(5, 7, somar)

#aqui fizemos parecido so que...
def exibir_result_2(a2, b2, funcSomar2):
  result2= funcSomar2 #estamas atribuindo aqui à variavel result2 as tarefas da funcao funSomar2...
  print(f"O resul da operação {a2}+{b2}= {result2(a2, b2)}.") #e aqui, passamos os paramentros pra essa "variavel/funcao"
exibir_result_2(5, 7, somar)

#-------------
# VARIAVEIS TÊM ESCOPO LOCAL DENTRO DAS FUNCOES
# N posso usar em uma funcao X uma variavel que foi declarada fora dessa funcao. A nao ser que...
#eu use o argumetno Global, informando que quero usar uma variavel global dentro da funcao
salario= 1000
def aumento(bonus):
  global salario
  salario+= bonus
  print(f"O novo salario eh {salario}")
aumento(200)
print(f"salario global eh {salario}") # a funcao alterou o valor global da var salario
#-------------