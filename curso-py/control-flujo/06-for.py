buscar = 10

for numero in range(5):
    print (numero)
    if numero == buscar:
        print ("Encontrado", buscar)
        break # Termina el ciclo
else:
    print ("No encontrado el número buscado")

for char in "Ultimate Python":
    print (char)