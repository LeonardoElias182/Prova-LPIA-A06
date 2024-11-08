print ('Olá, seja bem vindo (a)!')

chances = 3

while True:
    user_login = input('Por favor, cadastre um nome de usuario: ')
    conf_login = input('Por favor, confirme seu nome de usuario: ')
    if (user_login == conf_login):
        break
    else:
        print('Nome de usuário não confere, por favor tente novamente!')

while True:
    user_senha = input(f'Olá {user_login}, por favor cadastre sua senha: ')
    conf_senha = input(f'Olá {user_login}, por favor confirme sua senha: ')
    if (user_senha == conf_senha):
        break
    else:
        print('Senha não confere, tente novamente!')

for i in range(chances):
    chance_senha = input(f'Por favor, {user_login}, insira sua senha a seguir ({chances:02d} chances): ')
    if chance_senha != user_senha:
        chances -= 1
        print(f'Senha incorreta!  Você ainda tem {chances:02d} tentativa(s)!')
        continue
    else:
        print(f'Senha correta, seja bem vindo(a) ao sistema!')
        break
else:
    print('Você tentou 3 vezes. Acesso bloqueado!!!')   
