# Depósito
# Saque
# Extrato
# Limite de saques = 3
# Limite dinheiro por saque = 500

saldo = 1800
deposito = None
saque = None
extrato = ""
limite_saques = 3
limite_dinheiro = 500
qtde_saque = 0

menu = input("""
Selecione uma operação

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

>>>""") 

while True:
    
    # DEPÓSITO
    
    if menu == "d":
        print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
        deposito = int(input("Digite o valor de depósito: "))
        saldo += deposito
        print(f"Você depositou R$ {deposito:.2f} Reais\n")
        print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
        extrato += f"- Depósito de R$ {deposito:.2f} Reais\n"
        menu = input("Selecione uma operação\n\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\n\n>>> ")
        
        
    # SAQUE    
    
    elif menu == "s":
        if qtde_saque >= limite_saques:
            print("Limite diário de saque excedido!")
            menu = input("Selecione uma operação\n\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\n\n>>> ")
        
        else:
            print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
            saque = int(input("Digite o valor do saque: "))
            
            if saque > limite_dinheiro:
                print("Valor de saque não pode ser maior que R$ 500.00 Reais\n")
                menu = input("Selecione uma operação\n\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\n\n>>> ")

            elif saque <= limite_dinheiro and saque > 0:
                qtde_saque += 1
                saldo -= saque
                print(f"Você sacou R$ {saque:.2f} Reais\n")
                print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
                extrato += f"- Saque de R$ {saque:.2f} Reais\n"
                menu = input("Selecione uma operação\n\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\n\n>>> ")
            
            else:
                print("Algo deu errado :(")
                
    # EXTRATO
            
    elif menu == "e":
        if extrato == "":
            print(f"Não há nada no extrato.\nSeu saldo atual é R$ {saldo:.2f} Reais")
        print(extrato)
        menu = input("Selecione uma operação\n\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\n\n>>> ")
                
    # SAIR
        
    elif menu == "q":
        menu = input("Você realmente deseja sair? ").lower().replace("ã", "a")
        if menu == "sim":
            break
        elif menu == "nao":
            menu = input("Selecione uma operação\n\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\n\n>>> ")
        else:
            print("Comando não reconhecido!")
            menu = input("Selecione uma operação\n\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\n\n>>> ")
    
    else:
        print("Operação inválida.\n")
        menu = input("Selecione uma operação\n\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\n\n>>> ")