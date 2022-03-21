while True:
    op = int(input('''Enter [1] if you want to convert Real to another currency, [2] to convert another currency to Real
                    or [3] to end program:'''))
    while op < 1 or op > 3:
        op = int(input('''Invalid command, type [1] if you want to convert Real to another currency,
                        [2] to convert another currency to real or [3] to end the program:'''))
    if op == 1:
        m = int(input('''Enter the foreign currency option
        [1]- Dollar
        [2]- Euro
        [3]- Peso
        [4]- Libra
        [5]- Yen
        [6]- Yuan:   
         '''))
        while m < 1 or m > 7:
            m = int(input('''Invalid command, enter foreign currency option
        [1]- Dollar
        [2]- Euro
        [3]- Peso
        [4]- Libra
        [5]- Yen
        [6]- Yuan:
         '''))
        vc = 0
        v = float(input('Enter the value you want to convert:'))
        if m == 1:
            vc = v * 0.19
            print('The value R${:.2f} converted to Dollar is ${:.2f}'.format(v, vc))
        elif m == 2:
            vc = v * 0.16
            print('The value R${:.2f} converted to Euro é ${:.2f}'.format(v, vc))
        elif m == 3:
            vc = v * 20
            print('The value R${:.2f} converted to Peso é ${:.2f}'.format(v, vc))
        elif m == 4:
            vc = 0.14
            print('The value R${:.2f} converted to Libra é ${:.2f}'.format(v, vc))
        elif m == 5:
            vc = v * 20
            print('The value R${:.2f} converted to Yen é ${:.2f}'.format(v, vc))
        elif m == 6: 
            vc = v * 1.23  
            print('The value R${:.2f} converted to Yuan  é ${:.2f}'.format(v, vc))
    elif op == 2:
        m = int(input('''Enter the foreign currency option: 
        [1]- Dollar
        [2]- Euro
        [3]- Peso
        [4]- Libra
        [5]- Yen
        [6]- Yuan: 
         '''))
        while m < 1 or m > 7:
            m = int(input('''Invalid command, enter foreign currency option: 
        [1]- Dollar
        [2]- Euro
        [3]- Peso
        [4]- Libra
        [5]- Yen
        [6]- Yuan: 
         '''))
        else:
            vc = 0
            v = float(input('Enter the value you want to convert: '))
            if m == 1:
                vc = v * 5.23
                print('The value ${:.2f} Dollars converted to reais is R${:.2f}'.format(v, vc))
            elif m == 2:
                vc = v * 6.19
                print('The value ${:.2f} euros converted to reais is R${:.2f}'.format(v, vc))
            elif m == 3:
                vc = v * 0.05
                print('The value ${:.2f} pesos converted to reais is R${:.2f}'.format(v, vc))
            elif m == 4:
                vc = 7.24
                print('The value ${:.2f} libras converted to reais is R${:.2f}'.format(v, vc))
            elif m == 5:
                vc = v * 0.05
                print('The value ${:.2f}  Yens converted to reais is R${:.2f}'.format(v, vc))
            elif m == 6: 
                vc = v * 0.81
                print('The value ${:.2f} yuans converted to reais is R${:.2f}'.format(v, vc)) 
    else:
        break  
print('Finished Converter')                    