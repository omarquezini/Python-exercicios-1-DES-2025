#Loja oferece os seguintes descontos:

#Compras acima de R$ 500,00 têm 10%
#Acima de R$ 300,00 têm 5%
#Menor ou igual a R$ 300,00 não têm desconto

compra = float(input("digite o valor da compra"))

if compra > 300.00 and compra < 500.00:
    print (f"sua compra tem um desconto de 5%, o que no caso é R${compra * 5 / 100} de desconto.")
elif compra < 300.00:
    print (f"obrigado pela compra")
elif compra > 500.00:
    print (f"sua compra tem um desconto de 10%, o que no caso é R${compra * 10 / 100} de desconto.")