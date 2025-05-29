# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.

gigabytes = int(input("digite o numero de Gb. "))

if gigabytes > 100:
    print(f"você utrpassou os limites, o que no caso é {gigabytes}. ")
elif  gigabytes <= 100:
    print(f"você ainda está no limite, o que no caso é {gigabytes}")