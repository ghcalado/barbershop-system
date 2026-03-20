import sqlite3
import os

# ================== CONFIGURAÇÃO ==================
SENHA_ADMIN = os.environ.get("SENHA_BARBEARIA", "1234")  # Configure via variável de ambiente

# ================== BANCO DE DADOS ==================
conexao = sqlite3.connect('barbearia.db')
cursor = conexao.cursor()

def criar_tabelas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS barbeiros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barbeiro TEXT,
            cliente TEXT,
            horario TEXT,
            data TEXT,
            servicos TEXT
        )
    ''')
    conexao.commit()

# ================== LOGIN ==================
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

# ================== SENHA ==================
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

# ================== CADASTRO DE BARBEIRO ==================
def cadastrar_barbeiro():
    while True:
        nome = input("\nNome do barbeiro: ").strip()
        if not nome:
            print("[ERRO] O nome não pode ser vazio.")
            continue
        telefone = input("Telefone do barbeiro: ").strip()
        try:
            cursor.execute("INSERT INTO barbeiros (nome, telefone) VALUES (?, ?)", (nome, telefone))
            conexao.commit()
            print(f"Barbeiro '{nome}' cadastrado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar barbeiro: {e}")

        if input("Deseja cadastrar outro? (s/n): ").lower() != "s":
            break

# ================== CADASTRO DE CLIENTE ==================
def cadastrar_cliente():
    while True:
        nome = input("\nNome do cliente: ").strip()
        if not nome:
            print("[ERRO] O nome não pode ser vazio.")
            continue
        telefone = input("Telefone do cliente: ").strip()
        try:
            cursor.execute("INSERT INTO clientes (nome, telefone) VALUES (?, ?)", (nome, telefone))
            conexao.commit()
            print(f"Cliente '{nome}' cadastrado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar cliente: {e}")

        if input("Deseja cadastrar outro? (s/n): ").lower() != "s":
            break

# ================== CADASTRO DE SERVIÇOS ==================
def cadastrar_servico():
    while True:
        nome = input("\nNome do serviço: ").strip()
        if not nome:
            print("[ERRO] O nome não pode ser vazio.")
            continue
        try:
            valor = float(input("Valor do serviço (ex: 35.50): ").replace(",", "."))
            if valor < 0:
                print("[ERRO] O valor não pode ser negativo.")
                continue
            cursor.execute("INSERT INTO servicos (nome, valor) VALUES (?, ?)", (nome, valor))
            conexao.commit()
            print(f"Serviço '{nome}' (R$ {valor:.2f}) cadastrado com sucesso!")
        except ValueError:
            print("[ERRO] Valor inválido. Use ponto ou vírgula como separador decimal.")
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar serviço: {e}")

        if input("Deseja cadastrar outro? (s/n): ").lower() != "s":
            break

# ================== CADASTRO DE AGENDAMENTO ==================
def cadastrar_agendamento():
    while True:
        print("\n--- Novo Agendamento ---")

        # Lista barbeiros disponíveis
        cursor.execute("SELECT nome FROM barbeiros")
        barbeiros = cursor.fetchall()
        if barbeiros:
            print("Barbeiros cadastrados: " + ", ".join(b[0] for b in barbeiros))

        barbeiro = input("Nome do Barbeiro: ").strip()
        cliente = input("Nome do Cliente: ").strip()
        horario = input("Horário (ex: 14:00): ").strip()
        data = input("Data (ex: 20/06/2025): ").strip()

        # Lista serviços disponíveis
        cursor.execute("SELECT nome, valor FROM servicos")
        servicos_db = cursor.fetchall()
        if servicos_db:
            print("Serviços disponíveis:")
            for s in servicos_db:
                print(f"  - {s[0]}: R$ {s[1]:.2f}")

        servicos = input("Serviços (separe por vírgula): ").strip()

        if not barbeiro or not cliente or not horario or not data:
            print("[ERRO] Preencha todos os campos obrigatórios.")
            continue

        try:
            cursor.execute('''
                INSERT INTO agendamentos (barbeiro, cliente, horario, data, servicos)
                VALUES (?, ?, ?, ?, ?)
            ''', (barbeiro, cliente, horario, data, servicos))
            conexao.commit()
            print(f"Agendamento de '{cliente}' salvo com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao salvar agendamento: {e}")

        if input("Deseja cadastrar outro agendamento? (s/n): ").lower() != "s":
            break

# ================== VER AGENDA ==================
def ver_agenda():
    print("\n" + "="*20 + " AGENDA " + "="*20)
    cursor.execute("SELECT barbeiro, cliente, horario, data, servicos FROM agendamentos ORDER BY data, horario")
    registros = cursor.fetchall()

    if not registros:
        print("A agenda está vazia no momento.")
    else:
        for item in registros:
            print(f"Data: {item[3]} | Hora: {item[2]}")
            print(f"Cliente: {item[1]} | Barbeiro: {item[0]}")
            print(f"Serviços: {item[4]}")
            print("-" * 40)

# ================== ZERAR AGENDA ==================
def zerar_agenda():
    confirmar = input("Tem certeza que deseja apagar TODA a agenda? (s/n): ").lower()
    if confirmar == "s":
        try:
            cursor.execute("DELETE FROM agendamentos")
            conexao.commit()
            print("Agenda zerada com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao zerar agenda: {e}")
    else:
        print("Operação cancelada.")

# ================== VER BARBEIROS ==================
def ver_barbeiros():
    print("\n" + "="*20 + " BARBEIROS " + "="*20)
    cursor.execute("SELECT id, nome, telefone FROM barbeiros ORDER BY nome")
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum barbeiro cadastrado.")
    else:
        for item in registros:
            print(f"ID: {item[0]} | Nome: {item[1]} | Telefone: {item[2]}")
            print("-" * 40)

# ================== VER CLIENTES ==================
def ver_clientes():
    print("\n" + "="*20 + " CLIENTES " + "="*20)
    cursor.execute("SELECT id, nome, telefone FROM clientes ORDER BY nome")
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum cliente cadastrado.")
    else:
        for item in registros:
            print(f"ID: {item[0]} | Nome: {item[1]} | Telefone: {item[2]}")
            print("-" * 40)

# ================== VER SERVIÇOS ==================
def ver_servicos():
    print("\n" + "="*20 + " SERVIÇOS " + "="*20)
    cursor.execute("SELECT id, nome, valor FROM servicos ORDER BY nome")
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum serviço cadastrado.")
    else:
        for item in registros:
            print(f"ID: {item[0]} | Serviço: {item[1]} | Valor: R$ {item[2]:.2f}")
            print("-" * 40)

# ================== MENU PRINCIPAL ==================
def menu(nome_barbearia):
    opcoes = {
        1: ("Cadastrar Barbeiro", cadastrar_barbeiro),
        2: ("Cadastrar Cliente", cadastrar_cliente),
        3: ("Cadastrar Serviços", cadastrar_servico),
        4: ("Cadastrar Agendamentos", cadastrar_agendamento),
        5: ("Ver agenda", ver_agenda),
        6: ("Zerar agenda", zerar_agenda),
        7: ("Ver barbeiros cadastrados", ver_barbeiros),
        8: ("Ver clientes cadastrados", ver_clientes),
        9: ("Ver serviços cadastrados", ver_servicos),
    }

    while True:
        print(f"\n{'='*10} MENU: {nome_barbearia} {'='*10}")
        for num, (descricao, _) in opcoes.items():
            print(f"{num}- {descricao}")
        print("0- Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("[ERRO] Digite apenas o número da opção.")
            continue

        if opcao == 0:
            print("Saindo do sistema... Até logo!")
            break
        elif opcao in opcoes:
            opcoes[opcao][1]()
        else:
            print(f"Opção inválida! Tente um número de 0 a {max(opcoes)}.")

# ================== EXECUÇÃO ==================
if __name__ == "__main__":
    criar_tabelas()
    nome_barbearia = fazer_login()

    if verificar_senha():
        menu(nome_barbearia)

    conexao.close()
