saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input('''
O que você deseja fazer?

1 - Depósito

2 - Saque

3 - Extrato

4 - Sair

Digite o número correspondente: '''
                  

        )

    if opcao == '1':
        
        while True:
            try:
                valor = float(input('Digite o valor: '))
                if valor > 0:
                    saldo = saldo + valor
                    extrato = extrato + f'Depósito - {valor}\n'
                    print('Depósito realizado com sucesso.')
                    break
                else:
                    print('Digite um valor válido')
            except: pass
            
    if opcao == '2':
        try:
            saque = float(input('Digite o valor do saque: '))
            if 0 < saque <= saldo and saque < 500 and numero_saques < LIMITE_SAQUES:
                saldo = saldo - saque
                extrato = extrato + f'Saque - {saque}\n'
                numero_saques = numero_saques + 1
                
            else:
                print('Não foi possível Realizar o saque')
        except: pass
        
    if opcao == '3':
        print(extrato)
        print(f'SALDO -> {saldo}')

    if opcao == '4':
        print('Sessão Finalizada')
        break
