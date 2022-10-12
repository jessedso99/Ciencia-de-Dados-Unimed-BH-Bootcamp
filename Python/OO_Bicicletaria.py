#self representa a instancia do objeto. Eh similar ao This. Na vdd self pode ser trocado por qlqr outro nome
#sempre declar metodos e passar o self, sempre! Tenha esse metodo argumentos ou não.
#construtor. o que é () -> None e pass??
#metodos(comportamentos) são funcoes dentro d classes. Mas temos que passar o self como argumento p essas funcoes
#eh possivel colocar metodo dentro de metodo assim como eh com funcoes

# -------------- Construtores e Destrutores ----------------
# __init__ = contrutor, nele damos o self e instancias da classe
# __del__ = destrutor, nele passamos o self. pode ter argumentos nele. Dps de executado destroi as instancias, 
    # mas sempre no final da execução do metodo
    # Para destruir esse obj em qlqr ponto do codigo: "del {nome do obj}" com um __del__ declarado.

class Bicicleta:
  def __init__(self, cor, modelo, ano, valor):
    print("inicializandoa  classe...")
    self.cor= cor
    self.modelo= modelo
    self.ano= ano
    self.valor= valor
  
  def buzinar(self):
    print("Plim Plimm...")
    #def teste(sem arg?):
      #.....

  def parar(self):
    print("Breck!")

  def correr(self):
    print("Vruummm")

  # def __str__(self): #Ok, mas e se trocarmos o nome de alum atributo ou da classe??? Então...
  #   return f"Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}"

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2012, 300)
Bicicleta.buzinar(b2) #eh o mesmo que b2.buzinar()
print(b2) #aqui consumimos o def __str__(self):. Ele ser mostrar as definicoes de classe
          #se n tivessemos isso o python exibiria algo como o nome class, tipo obj, enderço na memoria 



