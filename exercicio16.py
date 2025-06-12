
#Crie um programa que calcule o reajuste de salário:

#Salários até R$ 2000,00: +15%
#De R$ 2000,01 a R$ 5000,00: +10%
#Acima de R$ 5000,00: +5%

salario = float(input("digite o quanto você ganha: "))

if salario <= 2000.00:
    print(f"seu salario é {salario + salario * 15 / 100}")
elif 2000.01 <= salario <= 5000.00:
    print(f"seu salario é {salario + salario * 10 / 100}")
else:
    print(f"seu salario é {salario + salario * 5 / 100}")