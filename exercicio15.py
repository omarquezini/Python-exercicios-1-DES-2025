#Peça a idade do usuário e diga se ele pode se cadastrar em um site:

#Permitido: 13 anos ou mais

idade = int(input("digite sua idade:"))

if idade >= 13:
    print ("pode entrar amigo.")
else:
    print ("caia fora criança!")