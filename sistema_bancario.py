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

while True:
    
    menu = input("""
Selecione uma operação

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

>>>""") 
    
    # DEPÓSITO
    
    if menu == "d":
        print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
        try:
            deposito = float(input("Digite o valor de depósito: "))
        except ValueError:
            print("Digite um número válido!\n")
            continue
        #deposito = float(input("Digite o valor de depósito: "))
        saldo += deposito
        print(f"Você depositou R$ {deposito:.2f} Reais\n")
        print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
        extrato += f"- Depósito de R$ {deposito:.2f} Reais\n"
                
        
    # SAQUE    
    
    elif menu == "s":
        if qtde_saque >= limite_saques:
            print("Limite diário de saque excedido!")
            
        
        else:
            print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
            try:
                saque = float(input("Digite o valor do saque: "))
            except ValueError:
                print("Digite um número válido!")
                continue
            
            if saque > limite_dinheiro:
                print("Valor de saque não pode ser maior que R$ 500.00 Reais\n")
                

            elif saque <= limite_dinheiro and saque > 0:
                qtde_saque += 1
                saldo -= saque
                print(f"Você sacou R$ {saque:.2f} Reais\n")
                print(f"Seu saldo atual é: R$ {saldo:.2f} Reais\n")
                extrato += f"- Saque de R$ {saque:.2f} Reais\n"
                
            
            else:
                print("Algo deu errado :(")
                
    # EXTRATO
            
    elif menu == "e":
        if extrato == "":
            print(f"Não há nada no extrato.\nSeu saldo atual é R$ {saldo:.2f} Reais")
        print(extrato)
                
    # SAIR
        
    elif menu == "q":
        menu = input("Você realmente deseja sair? ").lower().replace("ã", "a")
        if menu == "sim":
            break
        elif menu == "nao":
            menu = input("""
Selecione uma operação

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

>>>""") 
        else:
            print("Comando não reconhecido!")
            
    
    else:
        print("Operação inválida.\n")
        