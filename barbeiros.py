import sqlite3
from database import conexao, cursor


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
