# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.

umidade = int(input("digite o porcentual da umidade. "))

if umidade >= (70 / 100)*100 :
    print("A UMIDADE UTRAPASSOU 70%. ")
else:
    print(f"umidade dentro do padrao:{umidade}%.")