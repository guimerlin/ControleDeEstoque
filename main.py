"""
Sistema de Controle de Estoque - Arquivo Principal
Coordena a execução do sistema utilizando os módulos específicos.
"""

from interface import exibir_menu, obter_opcao
from estoque import adicionar_produto, atualizar_produto, excluir_produto, visualizar_estoque
from vendas import registrar_venda

def main():
    # Estruturas de dados centrais
    estoque = []
    vendas = []
    
    while True:
        exibir_menu()
        opcao = obter_opcao()
        
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
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
