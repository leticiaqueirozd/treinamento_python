def realizar_senso_academia():
    alturas = []
    pesos = []
    codigos = []

    while True:
        codigo = input("Digite o código do cliente (ou 0 para encerrar): ")
        if codigo == '0':
            break

        altura = float(input("Digite a altura do cliente (em metros): "))
        peso = float(input("Digite o peso do cliente (em kg): "))

        codigos.append(codigo)
        alturas.append(altura)
        pesos.append(peso)

    if not alturas:
        print("Nenhum cliente cadastrado.")
        return

    indice_mais_alto = alturas.index(max(alturas))
    mais_alto = codigos[indice_mais_alto]

    indice_mais_baixo = alturas.index(min(alturas))
    mais_baixo = codigos[indice_mais_baixo]

    indice_mais_gordo = pesos.index(max(pesos))
    mais_gordo = codigos[indice_mais_gordo]

    indice_mais_magro = pesos.index(min(pesos))
    mais_magro = codigos[indice_mais_magro]

    media_alturas = sum(alturas) / len(alturas)
    media_pesos = sum(pesos) / len(pesos)

    print("Cliente mais alto:", mais_alto)
    print("Cliente mais baixo:", mais_baixo)
    print("Cliente mais gordo:", mais_gordo)
    print("Cliente mais magro:", mais_magro)
    print("Média de altura dos clientes:", media_alturas)
    print("Média de peso dos clientes:", media_pesos)

realizar_senso_academia()
