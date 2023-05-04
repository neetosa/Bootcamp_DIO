from colorama import Fore, Back, Style 

menu = '''
Digite uma das opções abaixo:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

        '''

saldo = 3000
limite = 500
extrato = ''
numero_saques = 0
saque_diario = 0
LIMITE_SAQUES = 3
LIMITE_SAQUE_DIARIO = 1500
lista_deposito = []
lista_saque = []
GREEN = "\033[0;32m"
RED = "\033[1;31m" 
RESET = "\033[0;0m"

while True:

    opcao = str(input(menu))

    if opcao == 'd':
        print()
        deposito = float(input('Informe o valor do depósito: '))
        saldo = saldo + deposito

        if deposito > 0:
            lista_deposito.append(deposito)
            print('Depósito realizado com sucesso!')
            print(f'Seu saldo atual é R$ {saldo:.2f}')

        else:
            print("Valor de depósito inválido! Tente novamente.")

    elif opcao == 's':
        print()
        saque = float(input('Informe o valor do saque: '))

        if (saldo >= saque):
            if numero_saques < 3:
                if (saque >0) and (saque<=500) and (saque_diario <= 1500):
                    saldo -= saque
                    lista_saque.append(saque)
                    saque_diario += saque
                    print('Saque realizado com sucesso!')
                    print(f'Seu saldo atual é de R$ {saldo:.2f}')
                    numero_saques += 1
                else:
                    print('Saque inválido!')
                    print('Você pode ter excidido o número de saques diários, seu limite de saque diário ou saque é maior que R$ 500.00')
            else:
                print('Você excedeu o numéro total de saques diários!')
        else:
            print('Saldo insuficiente!')
       
    elif opcao == 'e':
        print()
        print('Seu extrato diário é:')
        print('\t Depósitos:')
        for i in range(len(lista_deposito)):
            print(Fore.GREEN + f'\t\t R${lista_deposito[i]:.2f}' + Fore.RESET)
        print('\t Saques:')
        for j in range(len(lista_saque)):
            print(Fore.RED + f'\t\t R$ {lista_saque[j]:.2f}' + Fore.RESET)
        print('\t Saldo:')
        print(f'\t\t R$ {saldo:.2f}')

    elif opcao == 'q':
        print()
        print('Obrigado por usar nosso banco!')
        break

    else:
        print("Digite uma das opções válidas.")