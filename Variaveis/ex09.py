def altura (v0, t, g):
    H = (v0 * t) + 0.5 * g * (t**2)
    return H

v0 = 0.75
t = 7.5
g = 9.8

altura_final = altura (v0, t, g)
print(f'A altura após {t} segundos é de {altura_final} metros')