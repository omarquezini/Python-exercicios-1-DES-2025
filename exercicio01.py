# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.

curso02 = int(input("digite a quantidadede de avaliaçoes desse curso02. "))

curso01 = int(input("digite a quantidade de avaliaçoes desse curso01. "))

if curso01 == curso02:
    print("empate, A É.")
elif curso02 > curso01:
    print("cursso02 teve mais avaliaçoes.")
else:
    print("o curso01 teve mais avaliaçoes.")