# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

distancia = int(input("digite o numero da distancia Km. "))

tempo = int(input("digite o numero do tempo h. "))

velocidade = (distancia / tempo)

if velocidade < 5:
    print("você foi lento. ")
elif velocidade == 5 or velocidade == 10:
    print("você foi moderado em sua velocidade. ")
elif velocidade > 10:
    print("você foi rapido")