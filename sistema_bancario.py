# Variáveis

saldo = 1000
extrato = "EXTRATO".center(21, "-")
limite_saques = 3
limite_dinheiro = 500
qtde_saque = 0

# Funções

def depositar(saldo, extrato, valor):
    if valor <= 0:
        print("Insira um número válido!")
        return saldo, extrato
    else:
        saldo += valor
        print(f"Você depositou R$ {valor:.2f} Reais\n")
        print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
        extrato += f"- Depósito de R$ {valor:.2f} Reais\n"
        return saldo, extrato
    
    
def sacar(saldo, extrato, qtde_saque, valor):
    if valor > limite_dinheiro:
        print("Valor de saque não pode ser maior que R$ 500.00 Reais\n")
        return saldo, extrato, qtde_saque
    elif valor > saldo:
        print("Você não pode saquar mais dinheiro do que tem!") 
        return saldo, extrato, qtde_saque
    elif valor <= 0:
        print("Insira um número válido!")
        return saldo, extrato, qtde_saque
    else:
        qtde_saque += 1
        saldo -= valor
        print(f"Você sacou R$ {valor:.2f} Reais\n")
        print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
        extrato += f"- Saque de R$ {valor:.2f} Reais\n"
        return saldo, extrato, qtde_saque
    
# Código

while True:
    
    menu = input("""
Selecione uma operação

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

>>>""").lower() 
    
    # DEPÓSITO
    
    if menu == "d":
        print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
        try:
            saldo, extrato = depositar(saldo, extrato, float(input("Digite valor de depósito: ")))
        except ValueError:
            print("Digite um número válido!\n")
            continue
                
    # SAQUE    
    
    elif menu == "s":
        if qtde_saque >= limite_saques:
            print("Limite diário de saque excedido!")
        
        else:
            print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
            try:
                saldo, extrato, qtde_saque = sacar(saldo, extrato, qtde_saque, float(input("Digite o valor do saque: ")))
            except ValueError:
                print("Digite um número válido!")
                continue
            
            #else:
            #    print("Algo deu errado :(")
                
    # EXTRATO
            
    elif menu == "e":
        if extrato == "":
            print(f"Não há nada no extrato.\nSeu saldo atual é R$ {saldo:.2f} Reais")
        else:
            print(extrato)
            print(f"Seu saldo atual é R$ {saldo:.2f} Reais")
                
    # SAIR
        
    elif menu == "q":
        menu = input("Você realmente deseja sair? ").lower().replace("ã", "a")
        if menu == "sim":
            break
        elif menu == "nao":
            continue
        else:
            print("Comando não reconhecido!")
            
    
    else:
        print("Operação inválida.\n")
        