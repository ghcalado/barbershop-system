import sqlite3
from database import conexao, cursor


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
