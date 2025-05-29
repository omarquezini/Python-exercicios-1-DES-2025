#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

intregaX = int(input("digite o tempo restante da intragaX. "))
intregaY = int(input("digite o tempo restante da intragaY. "))
intregaZ = int(input("digite o tempo restante da entregaZ. "))

soma = intregaX + intregaY + intregaZ

if intregaX < 0 or intregaY < 0 or intregaZ < 0:
    print("ERRO.")
elif soma >= 0:
    print(f"{soma}")
