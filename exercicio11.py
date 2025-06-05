#Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
#Classifique o resultado de acordo com a faixa

#Abaixo do peso (< 18.5)
#Peso normal (18.5 a 24.9)
#Sobrepeso (25 a 29.9)
#Obesidade (>= 30)

Km = int(input("digite seu peso em (Km): "))

M = float(input("digite sua altura em (m): "))

IMC = (Km / (M * M))

if IMC < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= IMC <= 24.9:
    print("Você está com peso normal.")
elif 25 <= IMC <=29.9:
    print("Você está com sobrepeso.")
else:
    print("Você é obeso.")