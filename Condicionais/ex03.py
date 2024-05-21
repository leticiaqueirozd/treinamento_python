while True: 
    pop_pais_A = int(input('Digite a quantidade de habitantes no país A: '))
    taxa_cresc_A = float(input('Digite o percentual da taxa de crescimento no país A: '))


    pop_pais_B = int(input('Digite a quantidade de habitantes no país B: '))
    taxa_cresc_B = float(input('Digite o percentual da taxa de crescimento no país B: '))

    anos = 0

    while pop_pais_A < pop_pais_B:
        pop_pais_A += pop_pais_A * taxa_cresc_A
        pop_pais_B += pop_pais_B * taxa_cresc_B
        anos += 1
    
    print(f'Serão necessários {anos} anos para o país A atingir ou ultrapassar o país B')