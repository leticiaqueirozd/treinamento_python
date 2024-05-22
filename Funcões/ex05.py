def conversor(horas, minutos):
    if horas == 0:
        horas = 12
        periodo = 'A'
    elif horas < 12:
        periodo = 'A'
    elif horas == 12:
        periodo = 'P'
    else:
        horas -= 12
        periodo = 'P'
    return horas, minutos, periodo

def imprimir_horario(horas, minutos, periodo):
    print(f"A hora convertida é: {horas}:{minutos:02d} {periodo}.")
    print()

def entrada():
    while True:
        horas = int(input("Digite as horas entre 0 e 23: "))
        minutos = int(input("Digite os minutos entre 0 e 59: "))
        if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
            return False
        horas_convertidas, minutos_convertidos, periodo = conversor(horas, minutos)
        imprimir_horario(horas_convertidas, minutos_convertidos, periodo)
        continuar = input("Converter novamente? (s/n): ")
        if continuar.lower() != 's':
            break
entrada()
