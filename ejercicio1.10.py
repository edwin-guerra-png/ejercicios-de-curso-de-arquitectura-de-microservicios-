def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

numeros_perfectos = [6, 28, 36, 13]
for numero in numeros_perfectos:
    if numero_perfecto(numero):
        print(f"{numero} es un número perfecto.")
    else:
        print(f"{numero} no es un número perfecto.")