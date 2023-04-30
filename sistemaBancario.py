import datetime
#Definindo variáveis:


menu_inicial = """
[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair
"""
limite_saque = 3
max_saque = 500
saldo = 1500
limite = float(500)
quantidade_saque = 0
extratos_bancarios = {
    "Extrato de Deposito": [],
    "Extrato de Saques": [],
    "Extrato Geral": []
}
data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # DATA atual e hora


#Funções
def sacar(quantidade_saque,limite,saldo):
    #Função que fará o saque
    if quantidade_saque < limite_saque:
        valor_saque = float(input("Valor de saque: R$ "))
        if valor_saque > 0:
            if valor_saque <= limite and valor_saque <= saldo:
                extratos_bancarios["Extrato de Saques"].append(f"Data: {str(data)} - Saque: R$ {valor_saque:.2f}")
                extratos_bancarios["Extrato Geral"].append(f"Data: {str(data)} - Saque: R$ {valor_saque:.2f}")
                print("Saque Realizado com Sucesso!")
                quantidade_saque += 1
                return quantidade_saque, extratos_bancarios
            else:
                print(f"O limite de saque é de {limite:.2f}")
        else:
            print("Você deve informar um valor de saque válido!")
    else:
        print("Você não pode efetuar o saque, você escedeu o limite diário (3 saques)")
    return quantidade_saque, extratos_bancarios

def depositar(saldo):
    #Função que fará o deposito
    valor_deposito = float(input("Valor de deposito: R$ "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extratos_bancarios["Extrato de Deposito"].append(f"Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}")
        extratos_bancarios["Extrato Geral"].append(f"Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}")
        return extratos_bancarios
    else:
        print("Depositar acima de R$ 0")

def extrato(extratos_bancarios):
    #Função que retornará o extrato
    while True:
        opcao_de_estrato = int(input("""
        [ 1 ] Extrato Geral
        [ 2 ] Extrato de Saques
        [ 3 ] Extrato de Depósitos
        [ 4 ] Sair
        """))
        if opcao_de_estrato == 1:
            for extrato_geral in extratos_bancarios["Extrato Geral"]:
                print(extrato_geral)

        if opcao_de_estrato == 2:
            for extrato_saque in extratos_bancarios["Extrato de Saques"]:
                print(extrato_saque)

        if opcao_de_estrato == 3:
            for extrato_deposito in extratos_bancarios["Extrato de Deposito"]:
                print(extrato_deposito)

        if opcao_de_estrato == 4:
            break

#loop da interface
while True:
    print(menu_inicial)
    resposta = input('Qual opção você quer seguir?')
    #Se a resposta for D chamar a função de depositar
    if resposta.upper() == 'D':
        extratos_bancarios = depositar(saldo)
    #Se a resposta for S chamar a função de sacar
    elif resposta.upper() == 'S':
        quantidade_saque, extratos_bancarios = sacar(quantidade_saque, limite, saldo)
    #Se a resposta for E chamar a função de extrato
    elif resposta.upper() == "E":
        extrato(extratos_bancarios)
    #Se a resposta for Q sairá do loop
    elif resposta.upper() == 'Q':
        break
    else:
        print("Operação inválida, por favor digite uma opção válida.")
print("Volte sempre e conte com os nossos serviços!")

    