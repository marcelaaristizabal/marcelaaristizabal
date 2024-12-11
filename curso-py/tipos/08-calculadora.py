n1 = input("Digite el primer número: ") 
n2 = input("Digite el segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
la suma es {suma},
la resta es {resta},
la multiplicación es {multiplicacion},
la división es {division}
"""
print(mensaje)