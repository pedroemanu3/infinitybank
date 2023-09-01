from banco import obterConta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f'saldo: {cliente["saldo"]}')
    else:
        print('Conta nao existe!')

if __name__ == "__main__":
    consultarSaldo(1)
    print(banco)
