menu = ''' 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMTE_SAQUES = 3
lista_depositos = []
lista_saques = []

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
        saldo += qtd_deposito
        lista_depositos.append(qtd_deposito)

    elif opcao == 's':
        print('Saque')
        print('-=' * 20)
        if numero_saques < LIMTE_SAQUES:            
            while True:
                qtd_saque = float(input('Escolha o valor para sacar R$: '))                
                if qtd_saque > 0  and qtd_saque <= 500:
                    break
                else:
                    print('Não são permitidos valores negativos, ou valores acima de R$ 500,00')
            if saldo >= qtd_saque:
                saldo -= qtd_saque
                lista_saques.append(qtd_saque)
                numero_saques += 1
                print(f'O saque de R$ {qtd_saque:.2f} foi realizado')
                print(numero_saques)
            else:
                print(f'O seu saldo atual é de R$ {saldo:.2f}, portanto você não pode sacar a quantia de R$ {qtd_saque:.2f}')
        else:
            print('Você já realizou o limite de 3 saques diários, aguarde o próximo dia.')

    elif opcao == 'e':
        print('Extrato detalhado')
        print('-=' * 20)
        print(f'Você realizou {len(lista_depositos)} depósitos.')
        if len(lista_depositos) > 0:
            print('E eles foram no valor de :  ')
            for valores in lista_depositos:
                print(f'R$ {valores:.2f}')
        print(f'Você realizou {len(lista_saques)} saques. ')
        if len(lista_depositos) > 0:
            print('E eles foram no valor de :  ')
            for saque in lista_saques:
                print(f'R$ {saque:.2f}')
        print(f'O seu salo final é de R$ {saldo:.2f}.')
    
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')


