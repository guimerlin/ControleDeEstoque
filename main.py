"""
Sistema de Controle de Estoque - Arquivo Principal
Coordena a execução do sistema utilizando os módulos específicos.
"""

# Importa as funções necessárias dos outros módulos
from interface import exibir_menu, obter_opcao
from estoque import adicionar_produto, atualizar_produto, excluir_produto, visualizar_estoque
from vendas import registrar_venda

def main():
    """
    Função principal que executa o sistema de controle de estoque.
    """
    # Estruturas de dados centrais para armazenar o estoque e as vendas
    estoque = []
    vendas = []

    # Loop principal que mantém o sistema em execução
    while True:
        exibir_menu()  # Exibe o menu de opções
        opcao = obter_opcao()  # Obtém a opção do usuário

        # Executa a função correspondente à opção escolhida
        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            atualizar_produto(estoque)
        elif opcao == '3':
            excluir_produto(estoque)
        elif opcao == '4':
            visualizar_estoque(estoque)
        elif opcao == '5':
            registrar_venda(estoque, vendas)
        elif opcao == '6':
            # Encerra o programa
            print("Saindo do sistema... Até logo!")
            break
        else:
            # Informa ao usuário que a opção é inválida
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    # Executa a função main se o script for executado diretamente
    main()