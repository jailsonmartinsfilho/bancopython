print("CAIXA ELETRONICO")

saldo = 0
listaoperacoes = [ ]

while True:

    tecla = input("PARA VER SEU SALDO TECLE 1, PARA DEPOSITAR DIGITE 2, PARA SACAR DIGITE 3, PARA PAGAR UMA CONTA DIGITE 4, PARA RETIRAR O EXTRATO DIGITE 5: ")
    
    if tecla == '1':
        print(f"Seu saldo é: {saldo} R$")
        listaoperacoes.append(f'CONSULTOU SALDO DE {saldo} R$')
        a = input("PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0: ")
        while (a != '6') and (a != '0'):
            a = input("VALOR INVALIDO. PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0: ")
            if a == '6':
                break
            elif a == '0':
                break

        if a == '6':
            continue
        elif a == '0':
            break
        
    if tecla == '2':
        deposito = int(input("Quanto deseja depositar?: "))
        saldo = saldo + deposito
        print(f"Deposito concluido, seu novo saldo é de {saldo} R$")
        listaoperacoes.append(f'DEPOSITOU {deposito} R$')
        b = input("PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0 ")
        while (b != '6') and (b != '0'):
            b = input("VALOR INVALIDO. PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0: ")
            if b == '6':
                break
            elif b == '0':
                break

        if b == '6':
            continue
        elif b == '0':
            break
    
    if tecla == '3':
        saque = int(input("Quanto deseja sacar?: "))
        saldo = saldo - saque
        print(f"Saque concluido, seu novo saldo é de {saldo} R$")
        listaoperacoes.append(f'SACOU {saque} R$')
        c = input("PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0 ")
        while (c != '6') and (c != '0'):
            c = input("VALOR INVALIDO. PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0: ")
            if c == '6':
                break
            elif c == '0':
                break

        if c == '6':
            continue
        elif c == '0':
            break
            
    if tecla == '4':
        conta = int(input("Qual o valor da conta que deseja pagar?: "))
        saldo = saldo - conta
        print(f"Pagamento da conta concluido, seu novo saldo é de {saldo} R$")
        listaoperacoes.append(f'PAGOU UMA CONTA NO VALOR DE {conta} R$')
        d = input("PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0 ")
        while (d != '6') and (d != '0'):
            d = input("VALOR INVALIDO. PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0: ")
            if d == '6':
                break
            elif d == '0':
                break
        if d == '6':
            continue
        elif d == '0':
            break

    if tecla == '5':
        print(f"Extrato das operaçoes: {listaoperacoes}")
        e = input("PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0 ")
        while (e != '6') and (e != '0'):
            e = input("VALOR INVALIDO. PARA CONTINUAR OPERANDO NO CAIXA DIGITE 6, CASO CONTRARIO DIGITE 0: ")
            if e == '6':
                break

    if tecla != ('1','2','3','4','5'):
        print("VALOR INVALIDO ENTRADO,PRESTE MAIS ATENÇÃO POR FAVOR '-'")
        