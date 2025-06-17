
#Peça três números e exiba-os em ordem crescente.

numero1 = int(input("digite o #1 numero"))

numero2 = int(input("digite o #2 numero"))

numero3 = int(input("digite o #3 numero"))

if numero1 > numero2 and numero2 > numero3:
    print(f"{numero1} {numero2} {numero3}")
elif numero2 > numero1 and numero1 > numero3:
    print(f"{numero2} {numero1} {numero3}")
elif numero3 > numero2 and numero2 > numero1:
    print(f"{numero3} {numero2} {numero1}")
elif numero1 > numero3 and numero3 > numero2:
    print(f"{numero1} {numero3} {numero2}")
elif numero2 > numero3 and numero3 > numero1:
    print(f"{numero2} {numero3} {numero1}")
elif numero3 > numero1 and numero1 > numero2:
    print(f"{numero3} {numero1} {numero2}")