entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

valor= (float(entrada[0])/((float(entrada[2])+float(entrada[1]))))
print(f'{valor:,.2f}')

