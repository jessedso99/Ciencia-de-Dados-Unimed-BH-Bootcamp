print("\t\t\tJogo da velha\n\n")
namePlayer1 = input("nome do jogador 1")
namePlayer2 = input("nome do jogador 2")
rodada = True
validarJogada = False
coordenada = ""
jogadas = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
dictCoord = {"A1":"0", "A2":"1", "A3":"2", "B1":"3", "B2":"4", "B3":"5", "C1":"6", "C2":"7", "C3":"8"}
gameOver = False
cabecalho = "  1|2|3"
linha1 = "A "+jogadas[0]+"|"+jogadas[1]+"|"+jogadas[2]
linha2 = "B "+jogadas[3]+"|"+jogadas[4]+"|"+jogadas[5]
linha3 = "C "+jogadas[6]+"|"+jogadas[7]+"|"+jogadas[8]
tabuleiro = cabecalho+"\n"+linha1+"\n"+linha2+"\n"+linha3+"\n"

print(tabuleiro)

while gameOver == False:
  if rodada == True:
    print("\tvez de " + namePlayer1 + "(X)")
  if rodada == False:
    print("\tvez de " + namePlayer2 + "(O)")
  while validarJogada == False:
    coordenada = input("\tinforme a coordenada: ")
    if coordenada.upper() not in dictCoord:
      print("Jogada invalida, tente dnv")
    elif jogadas[int(dictCoord[coordenada.upper()])] != " ":
      print("Jogada invalida, tente dnv")
    else:
      validarJogada = True
  if rodada == True:
    jogadas[int(dictCoord[coordenada.upper()])] = "X"
  if rodada == False:
    jogadas[int(dictCoord[coordenada.upper()])] = "O"
  cabecalho = "  1|2|3"
  linha1 = "A "+jogadas[0]+"|"+jogadas[1]+"|"+jogadas[2]
  linha2 = "B "+jogadas[3]+"|"+jogadas[4]+"|"+jogadas[5]
  linha3 = "C "+jogadas[6]+"|"+jogadas[7]+"|"+jogadas[8]
  tabuleiro = cabecalho+"\n"+linha1+"\n"+linha2+"\n"+linha3+"\n"
  print(tabuleiro)
  rodada = not rodada
  validarJogada = not validarJogada

  if jogadas[0] != " " and jogadas[0] == jogadas[1] and jogadas[0] == jogadas[2]:
    gameOver = True
  elif jogadas[3] != " " and jogadas[3] == jogadas[4] and jogadas[3] == jogadas[5]:
    gameOver = True
  elif jogadas[6] != " " and jogadas[6] == jogadas[7] and jogadas[6] == jogadas[8]:
    gameOver = True
  elif jogadas[0] != " " and jogadas[0] == jogadas[3] and jogadas[0] == jogadas[6]:
    gameOver = True
  elif jogadas[1] != " " and jogadas[1] == jogadas[4] and jogadas[1] == jogadas[7]:
    gameOver = True
  elif jogadas[2] != " " and jogadas[2] == jogadas[5] and jogadas[2] == jogadas[8]:
    gameOver = True
  elif jogadas[0] != " " and jogadas[0] == jogadas[4] and jogadas[0] == jogadas[8]:
    gameOver = True
  elif jogadas[2] != " " and jogadas[2] == jogadas[4] and jogadas[2] == jogadas[6]:
    gameOver = True

if rodada == True:
  print("\n\n\t\t\tO ganahdor foi " + namePlayer1)
else:
  print("\n\n\t\t\tO ganahdor foi " + namePlayer2)