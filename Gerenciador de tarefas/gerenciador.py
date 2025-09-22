import json
import os

# Função para carregar tarefas do arquivo JSON
def carregar_tarefas():
    """
    Carrega as tarefas armazenadas no arquivo JSON 'tarefas.json'.
    Se o arquivo não existir, retorna uma lista vazia.

    Returns:
        list: Lista de tarefas carregadas do arquivo JSON.
    """
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    return []


# Função para salvar as tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    """
    Salva a lista de tarefas no arquivo JSON 'tarefas.json'.
    
    Args:
        tarefas (list): Lista de tarefas a ser salva.
    """
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)


# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, descricao):
    """
    Adiciona uma nova tarefa à lista de tarefas e salva no arquivo JSON.

    Args:
        tarefas (list): Lista de tarefas.
        descricao (str): Descrição da nova tarefa.
    """
    tarefa = {'id': len(tarefas) + 1, 'descricao': descricao}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")


# Função para editar uma tarefa existente
def editar_tarefa(tarefas, id_tarefa, nova_descricao):
    """
    Edita a descrição de uma tarefa existente.

    Args:
        tarefas (list): Lista de tarefas.
        id_tarefa (int): ID da tarefa a ser editada.
        nova_descricao (str): Nova descrição para a tarefa.
    """
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa['descricao'] = nova_descricao
            salvar_tarefas(tarefas)
            print("Tarefa atualizada com sucesso!")
            return
    print("Tarefa não encontrada!")


# Função para excluir uma tarefa
def excluir_tarefa(tarefas, id_tarefa):
    """
    Exclui uma tarefa da lista com base no ID.

    Args:
        tarefas (list): Lista de tarefas.
        id_tarefa (int): ID da tarefa a ser excluída.
    """
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefas.remove(tarefa)
            salvar_tarefas(tarefas)
            print("Tarefa excluída com sucesso!")
            return
    print("Tarefa não encontrada!")


# Função para visualizar todas as tarefas
def visualizar_tarefas(tarefas):
    """
    Exibe todas as tarefas armazenadas na lista.

    Args:
        tarefas (list): Lista de tarefas.
    """
    if not tarefas:
        print("Nenhuma tarefa encontrada!")
        return
    print("\nTarefas:")
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']} - {tarefa['descricao']}")


def menu():
    """
    Função que exibe o menu de opções e executa as ações correspondentes.
    """
    tarefas = carregar_tarefas()

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Editar Tarefa")
        print("3. Excluir Tarefa")
        print("4. Visualizar Tarefas")
        print("5. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
        elif escolha == '2':
            id_tarefa = int(input("Digite o ID da tarefa a ser editada: "))
            nova_descricao = input("Digite a nova descrição da tarefa: ")
            editar_tarefa(tarefas, id_tarefa, nova_descricao)
        elif escolha == '3':
            id_tarefa = int(input("Digite o ID da tarefa a ser excluída: "))
            excluir_tarefa(tarefas, id_tarefa)
        elif escolha == '4':
            visualizar_tarefas(tarefas)
        elif escolha == '5':
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    """
    Função principal para executar o programa de gerenciamento de tarefas.
    """
    menu()
