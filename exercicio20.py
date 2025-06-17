
#Simule um login com nome de usuário "admin" e senha "1234".
#Caso os dados estejam corretos, exiba "Acesso concedido", senão "Acesso negado".

osuario = input("digite se nome de osuário: ")

senha = int(input("digite sua senha: "))

if senha == 1234 or osuario == ("admin"):
    print("Acesso concedido.")
else:
    print("acesso negado.")