# Menu
VALOR_MAXIMO_SAQUE = 500
QUANTIDADE_MAXIMA_SAQUE = 3

saldo = 1000
saques_realizados = 0
extrato = ""

menu = """
*******************************
*         SIMPLE BANK         *
*******************************
1 - Sacar
2 - Depositar
3 - Ver extrato
0 - Sair
"""

def sacar():
    global saldo, saques_realizados, extrato
    print("Digite o valor que gostaria de sacar: ")
    try:
        valor = float(input())
    except ValueError:
        print("Por favor, insira um valor numérico válido.")
        return
    mensagem = verifica_disponibilidade_saque(valor)
    print(mensagem)

def verifica_disponibilidade_saque(valor_saque):
    global saldo, saques_realizados, extrato
    if valor_saque > saldo:
        return "Saldo insuficiente"
    if valor_saque <= 0:
        return "Valor inválido"
    if saques_realizados >= QUANTIDADE_MAXIMA_SAQUE:
        return f"Limite de {QUANTIDADE_MAXIMA_SAQUE} saques diários atingido. Tente novamente amanhã."
    if valor_saque > VALOR_MAXIMO_SAQUE:
        return f"Cada saque não pode ultrapassar o valor de R${VALOR_MAXIMO_SAQUE:.2f}"
    
    saldo -= valor_saque
    saques_realizados += 1
    extrato += f"Saque: -R${valor_saque:.2f}\n"
    return f"Saque realizado com sucesso! Seu novo saldo é de R${saldo:.2f}"

def depositar():
    global saldo, extrato
    print("Digite o valor que gostaria de depositar: ")
    try:
        valor_deposito = float(input())
    except ValueError:
        print("Por favor, insira um valor numérico válido.")
        return
    saldo += valor_deposito
    extrato += f"Depósito: R${valor_deposito:.2f}\n"
    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso! Seu novo saldo é de R${saldo:.2f}")

def ver_extrato():
    global extrato, saldo
    print("\n********** EXTRATO **********")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo atual: R${saldo:.2f}")
    print("*******************************\n")

# Loop principal
while True:
    opcao = input(menu)
    
    if opcao == "1":
        sacar()
    elif opcao == "2":
        depositar()
    elif opcao == "3":
        ver_extrato()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida, por favor selecione de acordo com as opções exibidas no menu.")
