def zodiaco(ano):
    signos = ['Dragão', 'Cobra', 'Cavalo', 'Ovelha', 'Macaco', 'Galo', 'Cachorro', 'Porco', 'Rato', 'Boi', 'Tigre', 'Lebre']
    
    calculo = ano % 12
    return signos[calculo]

ano_nasc = int(input('Digite o ano em que nasceu: '))

signo = zodiaco(ano_nasc)

print(f'O seu signo no Zodíaco Chinês é {signo}')