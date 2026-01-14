"""
Módulo de Gerenciamento de Estoque
Responsável por adicionar, atualizar, excluir e visualizar produtos.
"""

def adicionar_produto(estoque):
    """
    Adiciona um novo produto ao estoque.

    Args:
        estoque (list): A lista de produtos em estoque.
    """
    print("\n>> Adicionar Novo Produto")
    nome = input("Nome do produto: ").strip()  # Remove espaços em branco extras

    # Verifica se o produto já existe no estoque
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print(f"Erro: O produto '{nome}' já existe no estoque.")
            return

    try:
        # Solicita o preço e a quantidade do produto
        preco = float(input("Preço do produto: R$ "))
        quantidade = int(input("Quantidade em estoque: "))

        # Cria um dicionário para o novo produto
        novo_produto = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        # Adiciona o novo produto à lista de estoque
        estoque.append(novo_produto)
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        # Trata o erro caso o preço ou a quantidade não sejam números
        print("Erro: Preço ou quantidade inválidos. Use números.")

def atualizar_produto(estoque):
    """
    Atualiza as informações de um produto existente no estoque.

    Args:
        estoque (list): A lista de produtos em estoque.
    """
    print("\n>> Atualizar Produto")
    nome_busca = input("Digite o nome do produto que deseja atualizar: ").strip()

    # Procura o produto na lista de estoque
    for produto in estoque:
        if produto['nome'].lower() == nome_busca.lower():
            print(f"Produto encontrado: {produto['nome']} | Preço atual: R$ {produto['preco']:.2f} | Qtd: {produto['quantidade']}")
            try:
                # Solicita o novo preço e a nova quantidade
                novo_preco = float(input("Novo preço: R$ "))
                nova_qtd = int(input("Nova quantidade: "))

                # Atualiza as informações do produto
                produto['preco'] = novo_preco
                produto['quantidade'] = nova_qtd
                print("Produto atualizado com sucesso!")
                return
            except ValueError:
                # Trata o erro caso os valores não sejam números
                print("Erro: Valores inválidos.")
                return

    # Informa se o produto não foi encontrado
    print(f"Produto '{nome_busca}' não encontrado.")

def excluir_produto(estoque):
    """
    Exclui um produto do estoque.

    Args:
        estoque (list): A lista de produtos em estoque.
    """
    print("\n>> Excluir Produto")
    nome_busca = input("Digite o nome do produto que deseja excluir: ").strip()

    # Procura o produto na lista de estoque
    for i, produto in enumerate(estoque):
        if produto['nome'].lower() == nome_busca.lower():
            # Pede confirmação para excluir o produto
            confirmacao = input(f"Tem certeza que deseja excluir '{produto['nome']}'? (s/n): ").lower()
            if confirmacao == 's':
                # Remove o produto da lista de estoque
                estoque.pop(i)
                print("Produto excluído com sucesso!")
            else:
                print("Operação cancelada.")
            return

    # Informa se o produto não foi encontrado
    print(f"Produto '{nome_busca}' não encontrado.")

def visualizar_estoque(estoque):
    """
    Exibe todos os produtos em estoque.

    Args:
        estoque (list): A lista de produtos em estoque.
    """
    print("\n>> Estoque Atual")
    # Verifica se o estoque está vazio
    if not estoque:
        print("O estoque está vazio.")
        return

    # Imprime o cabeçalho da tabela de estoque
    print(f"{'Nome':<20} | {'Preço':<10} | {'Quantidade':<10}")
    print("-" * 45)
    # Itera sobre a lista de estoque e imprime as informações de cada produto
    for produto in estoque:
        print(f"{produto['nome']:<20} | R$ {produto['preco']:>7.2f} | {produto['quantidade']:>10}")