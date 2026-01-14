"""
Módulo de Gerenciamento de Vendas
Responsável por registrar transações e atualizar o estoque.
"""

def registrar_venda(estoque, vendas):
    """
    Registra uma nova venda e atualiza o estoque.

    Args:
        estoque (list): A lista de produtos em estoque.
        vendas (list): A lista de vendas realizadas.
    """
    print("\n>> Registrar Venda")
    # Verifica se há produtos no estoque
    if not estoque:
        print("Não há produtos no estoque para vender.")
        return

    nome_busca = input("Nome do produto vendido: ").strip()
    # Procura o produto na lista de estoque
    for produto in estoque:
        if produto['nome'].lower() == nome_busca.lower():
            try:
                # Solicita a quantidade a ser vendida
                qtd_venda = int(input(f"Quantidade a vender (Disponível: {produto['quantidade']}): "))

                # Valida a quantidade da venda
                if qtd_venda <= 0:
                    print("Quantidade deve ser maior que zero.")
                    return

                if qtd_venda > produto['quantidade']:
                    print("Erro: Estoque insuficiente.")
                    return

                cliente = input("Nome do cliente: ").strip()

                # Atualiza a quantidade do produto no estoque
                produto['quantidade'] -= qtd_venda

                # Cria um dicionário para a nova venda
                venda = {
                    'produto': produto['nome'],
                    'quantidade': qtd_venda,
                    'preco_unitario': produto['preco'],
                    'total': qtd_venda * produto['preco'],
                    'cliente': cliente
                }
                # Adiciona a nova venda à lista de vendas
                vendas.append(venda)

                print(f"Venda realizada com sucesso! Total: R$ {venda['total']:.2f}")
                return
            except ValueError:
                # Trata o erro caso a quantidade não seja um número
                print("Erro: Quantidade inválida.")
                return

    # Informa se o produto não foi encontrado
    print(f"Produto '{nome_busca}' não encontrado.")