from operacoes import consulta, saque, deposito, transferencia
from banco import *

def menu():
    while true:
        print("------ bem vindo ao menu ------")
        print("1 - Adicionar conta")
        print("2 - Editar Nome")
        print("3 - Excluir conta")
        print("4 - Consultar conta")
        print("5 - Listar todas as contas")
        print("6 - Consultar saldo")
        print("7- Fazer deposito")
        print("8- Fazer saque")
        print("9 - transferencia")
        print("10 - sair")
        opcao = int(input('selecione uma opçao:'))
        if opcao ==1:
            nome = input('Digite o nome do cliente:')
            saldo = float(input('Digite o saldo:'))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o numero da conta:'))
            novoNome = input("Digite seu novo nome:")
            editarNome(novoNome, conta)
        elif opcao == 3:
            conta = int(input('digite o numero da conta:'))
            deletarConta(conta)
        elif opcao == 4:
            conta = int (input('Digite o numero da conta:'))
            consultarCliente(conta)
        elif opcao == 5:
            listarTodasContas()
        elif opcao == 6:
            conta = int(input('Digite o numero da conta:'))
            consulta.consultarSaldo(conta)
        elif opcao == 7:
            conta = int(input('Digite o numero da conta:'))
            valor = float(input('Digite o valor do deposito:'))
            deposito.depositar(conta, valor)
        elif opcao == 8:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de saque: '))
            saque.sacar(conta, valor)
        elif opcao == 9:
            contaOrigem = int(input('Digite o número da conta: '))
            contaDestino = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de transferencia: '))
            transferencia.transferir(contaOrigem, contaDestino, valor)
            elif opcao == 10:
            print('---- VOCÊ SAIU DO PROGRAMA ----')
            break
    menu()



