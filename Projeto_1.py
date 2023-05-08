from colorama import Fore, Back, Style 
import textwrap
from datetime import date

def funcao_saque(*, saldo, saque, extrato, limite, numero_saque, limite_saques):

    if (saldo < saque):
        print('Saldo insuficiente!')
    
    elif (saque > limite):
        print('Você excedeu o limite de R$ 500.00 por saque!')

    elif (numero_saque >= 3): 
        print('Você excedeu o limite de saques diarios disponíveis!')

    elif (saldo >= saque) and (saque > 0):
        saldo -= saque
        numero_saque += 1
        extrato += 'Saque: \t\t' + Fore.RED + f'R$ {saque:.2f}' + Fore.RESET + '\n'
        print(f'Saque realizado com sucesso! Seu saldo atual é de R$ {saldo:.2f}')

    else:
        print('Saque inválido!')

    return saldo, extrato, numero_saque

def funcao_deposito(saldo, deposito, extrato, /):
    if (deposito > 0):
        saldo = saldo + deposito
        print(f'Depósito realizado com sucesso! Seu saldo atual é R$ {saldo:.2f}') 
        extrato += 'Depósito: \t' + Fore.GREEN + f'R$ {deposito:.2f}' + Fore.RESET + '\n'
    else:
        print('Valor de depósito inválido! Tente novamente.')
    
    return saldo, extrato

def funcao_extrato(saldo, /, *, extrato):
    print()
    print('============Extrato============')
    print('Ainda não houve nenhuma movimentação na sua conta' if not extrato else extrato)
    print(f'Saldo: \t\t' + f'R$ {saldo:.2f}')
    print('===============================')

    return ' '

def menu():
    menu = '''
    =============Menu=============
    Digite uma das opções abaixo:

        [d] \tDepositar
        [s] \tSacar
        [e] \tExtrato
        [nu]\tNovo Usuário
        [cc]\tCriar Conta
        [q] \tSair

    => '''
    return input(textwrap.dedent(menu))

def novo_usuario(lista_usuario):
    CPF = str(input('Digite o CPF que deseja cadastrar no formato xxxxxxxxxxx: '))

    if CPF in lista_usuario.keys():
        print('Usuário já está cadastrado na base da dados!')
        
    else:
        nome = str(input('Digite o nome do usuário: '))
        data_componentes = input('Digite a data de nascimento no formato DD-MM-AAAA: ').split('-')
        dia, mes, ano = [int(item) for item in data_componentes]
        data = date(ano, mes, dia)
        endereco = str(input('Digite o endereço no formato logradorou - nro - bairro - cidade/sigla do estado: '))
        lista_usuario.update({CPF : {'nome' : nome, 'Data de nascimento': data, 'Endereço': endereco}})

    return lista_usuario

def criar_conta(lista_contas, lista_usuario):
    CPF = str(input('Digite o número da CPF que deseja vincular a conta: '))

    if CPF in lista_usuario.keys():
        lista_contas.update({f'{len(lista_contas.keys())}' : {'Agência' : '0001', 'CPF': CPF}})
        print('Conta criada com sucesso!')
        print(f'O número da sua conta é {len(lista_contas.keys())} e agência 0001!')
    else:
        print('Esse CPF não está cadastrado na nossa base de dados!')

    return lista_contas


def main():

    saldo = 3000
    LIMITE = 500
    extrato = ''
    numero_saque = 0
    LIMITE_SAQUES = 3
    lista_usuarios = dict()
    lista_contas = dict()

    while True:

        opcao = menu()

        if opcao == 'd':
            print()
            deposito = float(input('Informe o valor do depósito: '))
            saldo, extrato = funcao_deposito(saldo, deposito, extrato)

        elif opcao == 's':
            print()
            saque = float(input('Informe o valor do saque: '))
            saldo, extrato, numero_saque = funcao_saque(saldo = saldo, saque = saque, extrato = extrato, limite = LIMITE, numero_saque = numero_saque, limite_saques = LIMITE_SAQUES)
    
        elif opcao == 'e':
            print()
            print(funcao_extrato(saldo, extrato = extrato))

        elif opcao == 'q':
            print()
            print('Obrigado por usar nosso banco!')
            break
        
        elif opcao == 'nu':
            print()
            lista_usuarios = novo_usuario(lista_usuario = lista_usuarios)

        elif opcao == 'cc':
            print()
            lista_contas = criar_conta(lista_contas = lista_contas, lista_usuario = lista_usuarios)

        else:
            print("Digite uma das opções válidas.")

main()
