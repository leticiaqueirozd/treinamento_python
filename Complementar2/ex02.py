def ler_strings(str1, str2):
    conj1 = set(str1)
    conj2 = set(str2)
    
    em_comum = conj1.intersection(conj2)
    
    strings = ' '.join(em_comum)
    return strings

str1 = input('Digite a primeira string: ')
str2 = input('Digite a segunda string: ')

resultado = ler_strings(str1, str2)

print(f'Os caracteres comuns dentre as strings lidas são: {resultado}')
