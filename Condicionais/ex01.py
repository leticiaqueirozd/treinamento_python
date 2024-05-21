while True:
    
    usuario = input('Insira seu usuário: ')
    senha = input ('Insira sua senha: ')

    if usuario == senha:
        print('A senha e usuário precisam ser diferentes, tente novamente')
    else:
        print('Login efetuado com sucesso!')
        break