# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)

meta1 = int(input("Digite a nota da primeira meta: "))
meta2 = int(input("Digite a nota da segunda meta: "))
meta3 = int(input("Digite a nota da terceira meta: "))

media = (meta1 + meta2 + meta3) / 3

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Em treinamento")
else:
    print("Reprovado")
