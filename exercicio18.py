
#Receba duas notas e seus respectivos pesos. Calcule a média ponderada.
#Fórmula: (nota1 × peso1 + nota2 × peso2) / (peso1 + peso2)

nota = int(input("digite o numero da #1 nota"))

nota2 = int(input("digite o numero da #2 nota"))

peso = int(input("digite o numero da #1 peso"))

peso2 = int(input("digite o numero da #2 peso"))

formula = (nota * peso + nota2 * peso2) / (peso + peso2)

print(f"formula:{formula}")
