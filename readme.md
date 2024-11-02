# Menu interativo com funcionalidades POO

O objetivo do projeto é gerenciar produtos através da interação do usuário com o menu, permitindo ações como adicionar, visualizar e atualizar informações sobre os produtos como nome, preço e quantidade.

## Funcionalidades do menu

- **Adicionar Produto**: Adiciona um novo produto.
- **Exibir Produtos**: Exibe todos os produtos cadastrados.
- **Atualizar Preço**: Atualiza o preço de um produto.
- **Atualizar Quantidade**: Atualiza a quantidade em estoque de um produto.
- **Sair**: Encerra o menu.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `produto.py`: Define a classe `Produto`.
- `menu.py` (arquivo principal): Contém a função `menu()` que fornece a interação para gerenciar os produtos.

## Classe `Produto`

### Atributos 

São as características de cada produto.

- `nome`: Implementa o nome do produto.
- `preco`: Indica o valor do produto.
- `quantidade`: Exibe a quantidade daquele produto.

### Métodos:

São os comportamentos dos produtos.

- `__init__(nome, preco, quantidade)`: Inicializa um novo produto com nome, preço e quantidade.
- `exibir_informacoes()`: Exibe as informações do produto, incluindo o nome, o preço e a quantidade em estoque.
- `atualizar_preco(novo_preco)`: Atualiza o preço do produto para um novo valor, se for positivo.
- `atualizar_quantidade(nova_quantidade)`: Atualiza a quantidade do produto, se o novo valor for não negativo.

## Estruturas utilizadas

- **While**: Estrutura de repetição para que o menu seja exibido até que o usuário escolha essa opção.
- **If**: Estrutura de condição para tratamento de erros.
- **For**: Estrutura de repetição para gerenciar os dados dentro da lista produtos.
- **Match Case**: Estrutura de condição para gerenciar a escolha do usuário pelo menu.