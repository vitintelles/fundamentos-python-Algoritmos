# Lista para adicionar tarefas(Cada tarefa será um dicionário)
Tarefas = []
print("=== Bem vindo ao Gerenciador de Tarefas ===")
while True:
    # 1. Exibe o menu de opções
    print("\n--- Menu ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefa")
    print("3. Concluir Tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")
    
    #Opção 1 adicionar tarefa
    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        categoria = input("Digite a categoria (ex: Python, Estudos, Trabalho): ")

        # Criando um dicionário com os dados das tarefas
        nova_tarefa = {
            "nome": nome,
            "categoria": categoria,
            "status": "Pendente"
        }

        # Adiciona o dicionário na lista de tarefas
        Tarefas.append (nova_tarefa)
        print(f"Tarefa '{nome}' adicionada com sucesso!")
    # Opção 2 Listar tarefas
    elif opcao == "2":
        if len(Tarefas) == 0:
            print("Nenhuma tarefa cadastrada até o momento.")
        else:
            print("\n--- Suas Tarefas---")
            # Aqui vou usar o enumerate pois ele da o índice nas tarefas
            for indice, tarefa in enumerate(Tarefas, start=1):
                print(f"{indice}. [{tarefa['status']}] {tarefa['nome']} - Categoria: {tarefa['categoria']}")

    # Opção 3 Concluir Tarefa
    elif opcao == "3":
        if len(Tarefas) == 0:
            print("Não há tarefas para concluir.")
        else:
            try:
                num = int(input("Digite o número da tarefa que deseja concluir: "))
                # Ajusta o número digitado para o índice que começa em 0
                posicao = num - 1

                if 0 <= posicao < len(Tarefas):
                    Tarefas[posicao]["status"] = "Concluída"
                    print(f"Tarefa '{Tarefas[posicao]['nome']}' marcada como concluída!")
                else:
                    print("Número de tarefa inválido.")
            except ValueError:
                print("Por favor, digite apenas números inteiros.")
    # Opção 4 Sair
    elif opcao == "4":
        print("\nSaindo do Gerenciamento de Tarefas.")
        print("Até mais!")
        break
    else:
        print("Opção inválida. Digite um número de 1 a 4.")