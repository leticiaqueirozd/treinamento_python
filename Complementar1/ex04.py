pop_pais_A = 80000
taxa_cresc_A = 0.03

pop_pais_B = 200000
taxa_cresc_B = 0.015

anos = 0

while pop_pais_A < pop_pais_B:
    pop_pais_A += pop_pais_A * taxa_cresc_A
    pop_pais_B += pop_pais_B * taxa_cresc_B
    anos += 1
    
print(f'Serão necessários {anos} anos para o país A atingir ou ultrapassar o país B')