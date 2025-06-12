
#Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
#Fórmula: F = C × 1.8 + 32

celsius = int(input("digite o numero de celsius: "))

fahrenheit = celsius * 1.8 + 32

if celsius > 0:
    print(f"{fahrenheit}")