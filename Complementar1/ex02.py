def palindromo(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

if palindromo(palavra):
    print("É um palíndromo")
else:
    print("NÃO é um palíndromo.")
    