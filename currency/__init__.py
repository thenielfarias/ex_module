def fmt(p):
    return f'${p:.2f}'.replace('.', ',')


def increase(p, perc):
    r = p+(p*(perc/100))
    return r


def decrease(p, perc):
    r = p-(p*(perc/100))
    return r


def double(p):
    r = p*2
    return r


def half(p):
    r = p/2
    return r


def readMoney(msg):
    ok = False
    while not ok:
        userInput = str(input(msg)).replace(',', '.').strip()
        if userInput.isalpha() or userInput == '':
            print(f'\033[0;31mERROR! <{userInput}> is not a valid price.\033[m')
        else:
            ok = True
            return float(userInput)


def report(p, inc, dec):
    print('-'*35)
    print('Price Report'.center(35))
    print('-'*35)
    print(f'Price analyzed: \t{fmt(p)}')
    print(f'Increased by {inc}%: \t{fmt(increase(p, inc))}')
    print(f'Decreased by {dec}%: \t{fmt(decrease(p, dec))}')    
    print(f'Price doubled: \t\t{fmt(double(p))}')
    print(f'Half price: \t\t{fmt(half(p))}')
    print('-'*35)


