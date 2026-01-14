"""
Módulo de Interface com o Usuário
Responsável por exibir menus e capturar opções.
"""

def exibir_menu():
    """
    Exibe o menu principal do sistema.
    """
    print("\n--- SISTEMA DE CONTROLE DE ESTOQUE ---")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Excluir Produto")
    print("4. Visualizar Estoque")
    print("5. Registrar Venda")
    print("6. Sair")
    print("--------------------------------------")

def obter_opcao():
    """
    Obtém a opção do usuário a partir do menu.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    return input("Escolha uma opção (1-6): ").strip()