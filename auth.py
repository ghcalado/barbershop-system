from config import SENHA_ADMIN

def fazer_login():
    nome_barbearia = input("Qual o nome da barbearia? ")
    print(f"Bem-Vindo ao sistema, {nome_barbearia}!")

    login = input("Digite seu login: ")
    confirmacao = input("Confirme seu login: ")

    while login != confirmacao:
        print("Os logins não coincidem. Tente novamente!")
        confirmacao = input("Confirme seu login: ")

    print("Login efetuado com sucesso!")
    return nome_barbearia


def verificar_senha():
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        senha = input("Digite a sua senha: ")
        if senha == SENHA_ADMIN:
            print("Acesso liberado. Bem-vindo ao sistema!")
            return True
        else:
            tentativas += 1
            chances_restantes = max_tentativas - tentativas
            if chances_restantes > 0:
                print(f"Senha incorreta. Você ainda tem {chances_restantes} tentativa(s).")
            else:
                print("Acesso negado. Sistema bloqueado!")

    return False
