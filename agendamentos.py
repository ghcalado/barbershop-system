import sqlite3
from database import conexao, cursor


def cadastrar_agendamento():
    while True:
        print("\n--- Novo Agendamento ---")

        cursor.execute("SELECT nome FROM barbeiros")
        barbeiros = cursor.fetchall()
        if barbeiros:
            print("Barbeiros cadastrados: " + ", ".join(b[0] for b in barbeiros))

        barbeiro = input("Nome do Barbeiro: ").strip()
        cliente = input("Nome do Cliente: ").strip()
        horario = input("Horário (ex: 14:00): ").strip()
        data = input("Data (ex: 20/06/2025): ").strip()

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
