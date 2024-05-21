def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True

primos = []
number = 2

while len(primos) < 100:
    if is_primo(number):
        primos.append(number)
    number += 1

for primo in primos:
    print(primos)
    