from database import criar_tabelas, conexao
from auth import fazer_login, verificar_senha
from menu import menu

if __name__ == "__main__":
    criar_tabelas()
    nome_barbearia = fazer_login()

    if verificar_senha():
        menu(nome_barbearia)

    conexao.close()
