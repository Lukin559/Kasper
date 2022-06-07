with open('Лукин_Илья_Спринт1.txt', 'rb') as a:
    if a.read(2) == 'MZ':
        print('0x4D 0x5A, MZ - executable, OS Windows')
    else:
        a.seek(0, 0)
        symbols = a.read(2)
        print(f'{hex(ord(symbols[0]))} {hex(ord(symbols[1]))}  {symbols} - non-executable')

