while True:
    op = int(input('''Digite [1] se deseja converter Real para outra moeda, [2] para converter outra moeda para real 
                    ou [3] para finalizar programa: '''))
    while op < 1 or op > 3:
        op = int(input('''Comando invalido, digite [1] se deseja converter Real para outra moeda,
                        [2] para converter outra moeda para real ou [3] para finalizar programa: '''))
    if op == 1:
        m = int(input('''Digite a opção moeda estrangeira 
        [1]- Dólar
        [2]- Euro
        [3]- Peso
        [4]- Libra
        [5]- Iene
        [6]- Yuan:   
         '''))
        while m < 1 or m > 7:
            m = int(input('''Comando invalido, digite a opção moeda estrangeira
        [1]- Dólar
        [2]- Euro
        [3]- Peso
        [4]- Libra
        [5]- Iene
        [6]- Yuan:
         '''))
        vc = 0
        v = float(input('Digite o valor que deseja converter: '))
        if m == 1:
            vc = v * 0.19
            print('O valor R${:.2f} convertido para Dólar é ${:.2f}'.format(v, vc))
        elif m == 2:
            vc = v * 0.16
            print('O valor R${:.2f} convertido para Euro é ${:.2f}'.format(v, vc))
        elif m == 3:
            vc = v * 20
            print('O valor R${:.2f} convertido para Peso é ${:.2f}'.format(v, vc))
        elif m == 4:
            vc = 0.14
            print('O valor R${:.2f} convertido para Libra é ${:.2f}'.format(v, vc))
        elif m == 5:
            vc = v * 20
            print('O valor R${:.2f} convertido para Iene é ${:.2f}'.format(v, vc))
        elif m == 6: 
            vc = v * 1.23  
            print('O valor R${:.2f} convertido para Yuan  é ${:.2f}'.format(v, vc))
    elif op == 2:
        m = int(input('''Digite a opção moeda estrangeira: 
        [1]- Dólar
        [2]- Euro
        [3]- Peso
        [4]- Libra
        [5]- Iene
        [6]- Yuan: 
         '''))
        while m < 1 or m > 7:
            m = int(input('''Comando invalido, digite a opção moeda estrangeira: 
        [1]- Dólar
        [2]- Euro
        [3]- Peso
        [4]- Libra
        [5]- Iene
        [6]- Yuan: 
         '''))
        else:
            vc = 0
            v = float(input('Digite o valor que deseja converter: '))
            if m == 1:
                vc = v * 5.23
                print('O valor ${:.2f} dólares convertido para reais é R${:.2f}'.format(v, vc))
            elif m == 2:
                vc = v * 6.19
                print('O valor ${:.2f} euros convertido para reais é R${:.2f}'.format(v, vc))
            elif m == 3:
                vc = v * 0.05
                print('O valor ${:.2f} pesos convertido para reais é R${:.2f}'.format(v, vc))
            elif m == 4:
                vc = 7.24
                print('O valor ${:.2f} libras convertido para reais é R${:.2f}'.format(v, vc))
            elif m == 5:
                vc = v * 0.05
                print('O valor ${:.2f}  ienes convertido para reais é R${:.2f}'.format(v, vc))
            elif m == 6: 
                vc = v * 0.81
                print('O valor ${:.2f} yuans convertido para reais é R${:.2f}'.format(v, vc)) 
    else:
        break  
print('Conversor finalizado')                    