menu = ''' 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''


limite = 500
extrato = {
    'lista_depositos' : [],
    'lista_saques' : [],
    'saldo' : 0
}
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu).lower()

    if opcao == 'd':
        print("Depósito")
        print('-=' * 20)
        while True:            
            qtd_deposito = float(input('Escolha a quantia que quer depositar R$ :  ' ))
            if qtd_deposito >= 0:
                break
            else:
                print('Não é possível depositar valor negativo!')
        extrato['saldo'] += qtd_deposito
        extrato['lista_depositos'].append(qtd_deposito)

    elif opcao == 's':
        print('Saque')
        print('-=' * 20)
        if numero_saques < LIMITE_SAQUES:
            while True:
                qtd_saque = float(input('Escolha o valor para sacar R$: '))                
                if qtd_saque > 0  and qtd_saque <= 500:
                    break
                else:
                    print('Não são permitidos valores negativos, ou valores acima de R$ 500,00')
            if extrato['saldo'] >= qtd_saque:
                extrato['saldo'] -= qtd_saque
                extrato['lista_saques'].append(qtd_saque)
                numero_saques += 1
                print(f'O saque de R$ {qtd_saque:.2f} foi realizado')

            else:
                print(f'O seu saldo atual é de R$ {extrato["saldo"]:.2f}, portanto você não pode sacar a quantia de R$ {qtd_saque:.2f}')
        else:
            print('Você já realizou o limite de 3 saques diários, aguarde o próximo dia.')

    elif opcao == 'e':
        print('Extrato detalhado')
        print('-=' * 20)
        print(f'Você realizou {len(extrato["lista_depositos"])} depósito(s).')
        if len(extrato['lista_depositos']) > 0:
            for deposito in extrato['lista_depositos']:
                print(f'R$ {deposito:.2f}')
        print('-=' * 20)
        print(f'Você realizou {len(extrato["lista_saques"])} saque(s).')
        print('-=' * 20)
        if len(extrato['lista_saques']) > 0:
            for saque in extrato['lista_saques']:
                print(f'R$ {saque:.2f}')
        print('-=' * 20)
        print(f'O seu salo final é de R$ {extrato["saldo"]:.2f}.')
    
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')


