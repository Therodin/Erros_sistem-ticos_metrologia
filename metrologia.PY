def processar_erro(err):
    if err == '1':
        I = float(input(f'Qual o valor indicado pelo instrumento de medição?: '))
        vvc = float(input(f'Qual o valor verdadeiro convencional, indicado pela fabrica?: '))
        E = I - vvc
        print(f'Existe uma diferença de {E} do valor convencional')
    elif err == '2':
        medI = float(input('Realize uma série de medições e indique aqui o número que mais apareceu: '))
        valorvc = float(input('Agora insira aqui o valor indicado na embalagem: '))
        tendencia = medI - valorvc
        print(f'A tendencia é {tendencia:.2f}g ')



        


def metrologia():
    print('calculadora de erros')
    wc = input('Essa é a minha calculadora de erros sistemáticos gostaria de começar?, digite sair para fechar: ')
    while wc != 'sair':
        err = input('Gostaria de calcular qual erro? [1] - Diferença entre a medição e o valor dado de fabrica, [2] - Erro Sistemático(Tendencia)')
        processar_erro(err)

if __name__ == '__main__':
    metrologia()   

