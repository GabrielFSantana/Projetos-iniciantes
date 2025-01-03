tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if tarefas:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa na lista.")

def remover_tarefa(index):
    try:
        tarefa_removida = tarefas.pop(index - 1)
        print(f"Tarefa '{tarefa_removida}' removida!")
    except IndexError:
        print("Índice inválido.")

def main():
    print("Lista de Tarefas")
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(tarefa)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            try:
                index = int(input("Digite o número da tarefa a remover: "))
                remover_tarefa(index)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
