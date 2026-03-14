# Sistema de Controle de Estoque (Trabalho Acadêmico)

Este projeto é um **trabalho prático de faculdade** desenvolvido para a disciplina de Algoritmos/Lógica de Programação. O objetivo é demonstrar a aplicação de uma **arquitetura modular** em Python para gerenciar o inventário de uma loja de eletrônicos.

## 🚀 Funcionamento

O sistema é executado via terminal e permite o gerenciamento completo de produtos e registros de vendas, utilizando dicionários e listas para o armazenamento em memória.

### Estrutura de Módulos

Para garantir a organização do código, o projeto foi dividido nos seguintes arquivos:

* **`main.py`**: Ponto de entrada que orquestra o loop principal e integra os módulos.
* **`estoque.py`**: Lógica de manipulação de dados (Adicionar, Atualizar, Excluir e Visualizar produtos).
* **`vendas.py`**: Gerenciamento de transações e baixa automática no estoque.
* **`interface.py`**: Funções de exibição de menus e captura de entradas do usuário.

## 🛠️ Funcionalidades Principais

1. **Gestão de Produtos**: Cadastro de itens com verificação de duplicidade, edição de preços/quantidades e remoção.
2. **Registro de Vendas**: Cadastro de vendas por cliente com validação de disponibilidade de estoque.
3. **Relatórios**: Visualização formatada de todos os itens disponíveis no inventário.

## 💻 Como Executar

1. Certifique-se de ter o Python instalado.
2. Navegue até a pasta do projeto:
```bash
cd sistema_estoque

```


3. Execute o arquivo principal:
```bash
python main.py

```



---

> **Nota:** Este software foi desenvolvido exclusivamente para fins didáticos, focando em conceitos de modularização e estruturas de dados simples.
