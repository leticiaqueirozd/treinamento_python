def ler_strings(str1, str2):
    posicao = str1.find(str2)
    
    if posicao != -1:
        print(f'{str2} na posição {posicao} e {str1}')
    else:
        print(f'{str2} não encontrado em {str1}')

str1 = input('Digite a primeira string: ')
str2 = input('Digite a segunda string: ')

ler_strings(str1, str2)