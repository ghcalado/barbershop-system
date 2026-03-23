from modules.barbeiros import cadastrar_barbeiro, ver_barbeiros
from modules.clientes import cadastrar_cliente, ver_clientes
from modules.servicos import cadastrar_servico, ver_servicos
from modules.agendamentos import cadastrar_agendamento, ver_agenda, zerar_agenda


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
