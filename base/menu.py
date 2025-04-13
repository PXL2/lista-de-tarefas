from crud import adicionar_tarefa, listar_tarefas, atualizar_status, deletar_tarefa

def mostrar_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Marcar como concluída")
    print("4. Deletar tarefa")
    print("0. Sair")

def executar_menu():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            data = input("Data e hora (ex: 2025-04-12 21:00): ")
            adicionar_tarefa(descricao, data)
            print("✅ Tarefa adicionada com sucesso!")

        elif opcao == "2":
            tarefas = listar_tarefas()
            print("\n--- Lista de Tarefas ---")
            for tarefa in tarefas:
                print(f"[{tarefa[0]}] {tarefa[1]} | {tarefa[2]} | Status: {tarefa[3]}")

        elif opcao == "3":
            id = input("ID da tarefa para marcar como concluída: ")
            atualizar_status(int(id), "concluido")
            print("✅ Tarefa marcada como concluída!")

        elif opcao == "4":
            id = input("ID da tarefa para deletar: ")
            deletar_tarefa(int(id))
            print("❌ Tarefa deletada!")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Inicia o menu
executar_menu()
