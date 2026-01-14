"""
Módulo de Gerenciamento de Estoque
Responsável por adicionar, atualizar, excluir e visualizar produtos.
"""

def adicionar_produto(estoque):
    print("\n>> Adicionar Novo Produto")
    nome = input("Nome do produto: ").strip()
    
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print(f"Erro: O produto '{nome}' já existe no estoque.")
            return

    try:
        preco = float(input("Preço do produto: R$ "))
        quantidade = int(input("Quantidade em estoque: "))
        
        novo_produto = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        estoque.append(novo_produto)
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("Erro: Preço ou quantidade inválidos. Use números.")

def atualizar_produto(estoque):
    print("\n>> Atualizar Produto")
    nome_busca = input("Digite o nome do produto que deseja atualizar: ").strip()
    
    for produto in estoque:
        if produto['nome'].lower() == nome_busca.lower():
            print(f"Produto encontrado: {produto['nome']} | Preço atual: R$ {produto['preco']:.2f} | Qtd: {produto['quantidade']}")
            try:
                novo_preco = float(input("Novo preço: R$ "))
                nova_qtd = int(input("Nova quantidade: "))
                
                produto['preco'] = novo_preco
                produto['quantidade'] = nova_qtd
                print("Produto atualizado com sucesso!")
                return
            except ValueError:
                print("Erro: Valores inválidos.")
                return
    
    print(f"Produto '{nome_busca}' não encontrado.")

def excluir_produto(estoque):
    print("\n>> Excluir Produto")
    nome_busca = input("Digite o nome do produto que deseja excluir: ").strip()
    
    for i, produto in enumerate(estoque):
        if produto['nome'].lower() == nome_busca.lower():
            confirmacao = input(f"Tem certeza que deseja excluir '{produto['nome']}'? (s/n): ").lower()
            if confirmacao == 's':
                estoque.pop(i)
                print("Produto excluído com sucesso!")
            else:
                print("Operação cancelada.")
            return
            
    print(f"Produto '{nome_busca}' não encontrado.")

def visualizar_estoque(estoque):
    print("\n>> Estoque Atual")
    if not estoque:
        print("O estoque está vazio.")
        return
    
    print(f"{'Nome':<20} | {'Preço':<10} | {'Quantidade':<10}")
    print("-" * 45)
    for produto in estoque:
        print(f"{produto['nome']:<20} | R$ {produto['preco']:>7.2f} | {produto['quantidade']:>10}")
