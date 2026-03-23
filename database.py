import sqlite3

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
