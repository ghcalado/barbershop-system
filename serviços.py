import sqlite3
from database import conexao, cursor


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
