pessoa= {"nome": "Jess", "idade":22}#jeito 1
pessoa= dict(nome= "Jess", idade=22)#jeito 2
pessoa= {"nome": "Jose", "idade":20}#se craimos uma nova igualdade seja do jeito 1 ou 2, sobrescrevemos o dicionario
print(pessoa)
  #os valores das chaves devem ser imultaveis, pode ser uma chave string, ou uma tupla, numeros, etc

  #acessando valors de dicio
print(pessoa["nome"])
  #adicionamos um novo cahve:valor ao dicionario
pessoa["telefone"]= "3333-1234" 
print(pessoa)
  #Dicios aninhados sao possiveis
contatos= {
    "teste@gmail.com": {"nome":"teste", "idade":20}, 
    "jesse@gmail.com": {"nome":"jesse", "idade":22}, 
    "tombraider@gmail.com": {"nome":"tombraider", "idade":10, "extra":"teste"}#aqui n vai dar problema
}
print(contatos["jesse@gmail.com"]["idade"])
extrateste= contatos["tombraider@gmail.com"]["extra"] #[qual  dicio][qual a chave do valor q qro acessar]
print(extrateste)

  #podemos acessar seus valores usando o for
for chave in contatos: #a var chave incia-se em 0, e vai se iterando, percorrendo o dicio
  print(chave, contatos[chave])

print("\nchave valor com for") #mesmo result
for chave, valor in contatos.items(): #a var chave incia-se em 0, e vai se iterando, percorrendo o dicio
  print(chave, valor)

# ------- ETAPA 2: METODOS DA CLASSE DICT
#{}.clear() limpa todos os chave:valor do dicio
#{}.copy() tira uma copia do dicio. podemos armazenar em um otro dicio. EX: dicio2= dicio1.copy()

#{}.fromkeys -> cria chave e da o valor none p elas ou um defalt
novoDicio= {}
novoDicio.fromkeys(["nome", "telefone"])# da o valor none p essas chaves
novoDicio.fromkeys(["idade", "cidade"], "desconhecidos") #passa o valor padrao "desconhecido"
print(f"\n{novoDicio}")

  #get(chave) e retorna se a chave existe no dicio ou nao
  #contatos["maria@gmail.com"]# gera um erro, e para a execução pq a chave n existe
print(contatos.get("maria@gmail.com"))# no caso n existe
print(contatos.get("jesse@gmail.com"))#esse existe

  #items() retorna um tupla
  #{}.keys() rtorna so as chaves
dicio_teste= {"a": 100, 1:"teste", "b":"python"}
print(dicio_teste.keys())

  #{}.pop() remove itens do dicio
dicio_teste.pop("a")#exclui a chave a
print(dicio_teste.pop("a", "n existe"))# caso a chave n exista, retorne um valor padrao p eu saber

  #setdefault() adiciona cahve caso ela n exista

  #{}.update altera o valor de uma chave ja existente no dicio
contatos.update({"jesse@gmail.com": {"nome": "jose"}})#atualizamos e agr tem um unico "item", que eh nome
contatos.update({"joao@gmail.com": {"nome": "Joao", "idade":12}}) #A chave n existe, entao ele criou
print(contatos)

  #{}.values() retona apenas os vsalores das chaves

  #in eh usado p fazer algumas verificacoes como
print("idade" in contatos["jesse@gmail.com"])
print("jesse@gmail.com" in contatos)

  #del() deleta uam dada chave:valor
del contatos["joao@gmail.com"]["nome"]
print(contatos["joao@gmail.com"])#excuimo o nome de joao
del contatos["jesse@gmail.com"]
print(contatos.get("jesse@gmail.com"))#verificando se deletou mesmo
