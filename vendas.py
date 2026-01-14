"""
Módulo de Gerenciamento de Vendas
Responsável por registrar transações e atualizar o estoque.
"""

def registrar_venda(estoque, vendas):
    print("\n>> Registrar Venda")
    if not estoque:
        print("Não há produtos no estoque para vender.")
        return
        
    nome_busca = input("Nome do produto vendido: ").strip()
    for produto in estoque:
        if produto['nome'].lower() == nome_busca.lower():
            try:
                qtd_venda = int(input(f"Quantidade a vender (Disponível: {produto['quantidade']}): "))
                
                if qtd_venda <= 0:
                    print("Quantidade deve ser maior que zero.")
                    return
                
                if qtd_venda > produto['quantidade']:
                    print("Erro: Estoque insuficiente.")
                    return
                
                cliente = input("Nome do cliente: ").strip()
                
                # Atualizar estoque
                produto['quantidade'] -= qtd_venda
                
                # Registrar venda
                venda = {
                    'produto': produto['nome'],
                    'quantidade': qtd_venda,
                    'preco_unitario': produto['preco'],
                    'total': qtd_venda * produto['preco'],
                    'cliente': cliente
                }
                vendas.append(venda)
                
                print(f"Venda realizada com sucesso! Total: R$ {venda['total']:.2f}")
                return
            except ValueError:
                print("Erro: Quantidade inválida.")
                return
                
    print(f"Produto '{nome_busca}' não encontrado.")
