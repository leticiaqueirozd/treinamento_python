numero = int(input('Digite um número inteiro: '))

if numero <= 1:
    print('O número não é primo')
else:
    if numero == 2:
        print('O número é primo')
    elif numero % 2 == 0:
        print('O número não é primo')
    else:
        primo = True
        for i in range(3, numero , 2):
            if numero % i == 0:
                primo = False
                break
        
        if primo:
            print('O numero é primo')
        else:
            print('O numero NÃO é primo')