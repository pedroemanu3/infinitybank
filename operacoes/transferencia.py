from banco import obterConta, banco

def tranferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print('Transferencia realizada com sucesso!')
        else:
            print('saldo insuficiente!')
    else:
        print('uma ou mais contas nao existem!')

if __name__ == "__main__":
    tranferir(1,2,159.99)
    print(banco)
