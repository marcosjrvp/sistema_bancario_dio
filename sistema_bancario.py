import textwrap 
    

def menu():
    menu = ''' 

    =============MENU===============

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair

    => '''
    return input(menu)



def depositar(saldo, qtd_deposito, extrato, /):
    try:
        if qtd_deposito < 0:
            raise ValueError('O valor do depósito deve ser positivo.')
        saldo += qtd_deposito
        extrato += f' Depósito: R$ {qtd_deposito:.2f}\n'
        print()
        print(' ==== Depósito realizado com sucesso! ====')
    except ValueError as ve:
        print(f'{ve}')
    except Exception as e:
        print(f'{e}')
    return saldo, extrato

def sacar(*, saldo, qtd_saque, extrato, limite,  numero_saques, limite_saques):
    
    if numero_saques < limite_saques:
            if qtd_saque > 0 and qtd_saque <= limite:
                if saldo > qtd_saque:
                    saldo -= qtd_saque
                    numero_saques += 1
                    extrato += f' Saque: R$ {qtd_saque:.2f}\n'                                       
                    print(f'O saque de R$ {qtd_saque:.2f} foi realizado com sucesso!')
                    
                else:
                    print(f'Você não tem saldo suficiente para sacar a quantia de R${qtd_saque:.2f}. ')
            else:
                print('O valor de saque deve ser R$0,001 até R$500,00.')
    else:
        print('Você já excedeu a quantidade de 3 saques diários.') 

    return saldo, extrato, numero_saques

    
        
    
    pass

def exibir_extrato(saldo, /, *, extrato):
    print('\n==========EXTRATO==========')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('=' * 27)
    pass

def criar_usuario(usuarios):
    cpf = str(input('Informe o CPF(somente números): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nJá existe usuário cadastrado com esse CPF!')
        return

    nome = str(input('Informe o nome completo: '))
    data_nascimento = str(input('Informe a data de nascimento (dd-mm-aaaa): '))
    endereco = str(input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): '))

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('=== Usuário cadastrado com sucesso! ===')


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

    

def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input('Informe o CPF do usuário: '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': usuario
        }
    print('\n Usuário não encontrado, fluxo de criação de conta encerrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}"""
        print('=' * 100)
        print(textwrap.dedent(linha))        
    


def main():

    LIMTE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu() 

        if opcao == 'd':
            qtd_deposito = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, qtd_deposito, extrato)

        elif opcao == 's':
            qtd_saque = float(input(('Informe o valor do saque: ')))

            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                qtd_saque = qtd_saque,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMTE_SAQUES)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

main()