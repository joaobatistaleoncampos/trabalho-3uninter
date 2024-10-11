# Exigência de código 1 de 

print( " \n Bem Vindo a Madereira do Lenhador joão batista leon campos")

# Exigência de código 2 de 7
def escolha_tipo():
    while True:
        tipo = input(" \n Entre com o Tipo de madeira desejado  \n PIN -Tora de Pinho \n PER - Tora de Peroba \n MOG - Tora de Mogno \n IPE - Tora de Ipê \n IMB - Tora de Imbuia ").upper()
        if tipo == "PIN":
            return 150.40
        elif tipo == "PER":
            return 170.20
        elif tipo == "MOG":
            return 190.90
        elif tipo == "IPE":
            return 210.10
        elif tipo == "IMB":
            return 220.70
        else:
            print("Escolha inválida , entre com o modelo novamente.")

# Exigência de código 3 de 7
def qtd_toras():
    while True:
        try:
            quantidade = float(input(" \nInforme a quantidade de toras (em m³): "))
            if quantidade <= 0:
                print("Por favor , entre com a quantidade novamente.")
            elif quantidade > 2000:
                print("não aceitamos pedidos com essa quantidades de toras .")
                print("Por favor , entre com a quantidade novamente. ")
            else:
                if quantidade < 100:
                    desconto = 0
                elif 100 <= quantidade < 500:
                    desconto = 4 / 100
                elif 500 <= quantidade < 1000:
                    desconto = 9 / 100
                elif 1000 <= quantidade <= 2000:
                    desconto = 16 / 100
                return quantidade, desconto
        except ValueError:
            print("Valor não numérico. Tente novamente.")

# Exigência de código 4 de 7
def transporte():
    while True:
        tipo_transporte = input("\n Escolha o Tipo de Transporte:  \n 1-Rodoviário,\n 2-Ferroviário,\n 3-Hidroviário): ")
        if tipo_transporte == "1":
            return 1000
        elif tipo_transporte == "2":
            return 2000
        elif tipo_transporte == "3":
            return 2500
        else:
            print("Tipo de transporte inválido. Tente novamente.")

# Exigência de código 5 de 7
# Código principal
tipo_madeira = escolha_tipo()
qtd, desconto = qtd_toras()
transporte_valor = transporte()

total = ((tipo_madeira * qtd) * (1 - desconto)) + transporte_valor
print(f'\n R$ total á Pagar = {total}')
