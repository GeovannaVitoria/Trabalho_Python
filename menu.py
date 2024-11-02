from produto import Produto # Importando o arquivo 'produto' com a classe 'Produto'

def menu():
    """
        Exibe um menu interativo para gerenciar produtos, com opções para adicionar, exibir, atualizar preço e atualizar quantidade dos produtos cadastrados de acordo com a opção escolhida pelo usuário.

        Args:
            None

        Returns:
            None
    """
    produtos = [] # Criando uma lista vazia para que ela possa ser preenchida posteriormente com os produtos e seus atributos

    while True: 
        comando = input("Digite a opção que deseja: \n [A] Adicionar produto \n [B] Exibir produtos \n [C] Atualizar preço \n [D] Atualizar quantidade \n [S] Sair \n").upper()

        match comando:
            case 'A':
                print("----- Coletando os dados do produto -----")
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                produto_informacoes = Produto(nome, preco, quantidade)
                produtos.append(produto_informacoes) # Adiciona as informações dos produtos produto_informacoes na lista
                print("Produto cadastrado!")

            case 'B':
                if produtos:
                    print("----- Produtos cadastrados -----")
                    for i, produto in enumerate(produtos, start=1): # Repetição para exibir as informações de CADA produto seguindo o índice da lista produtos
                        print(f"[Produto:  {i}]")
                        produto.exibir_informacoes()
                else:
                    print("Nenhum produto cadastrado")
            
            case 'C':
                print("----- Atualizando o preço -----")
                if produtos:
                    for i, produto in enumerate(produtos, start=1):
                        print(f"[{i}] {produto.nome}")
                    escolha = int(input("Escolha o produto pelo número: ")) - 1 # -1 Pois em programação tudo começa com 0, então devemos decrementar para ficar o mais próximo do mundo real
                    if 0 <= escolha < len(produtos): # 'escolha' deve ser maior que 0 para tratar erros e estar dentro do limite do tamanho da lista.
                        novo_preco = float(input("Digite o novo preço: R$"))
                        produtos[escolha].atualizar_preco(novo_preco)
                        print("Preço atualizado!")
                    else:
                        print("Produto inválido")
                else:
                    print("Nenhum produto cadastrado")

            case 'D':
                print("----- Atualizando a quantidade -----")
                if produtos:
                    for i, produto in enumerate(produtos, start=1): 
                        print(f"[{i}] {produto.nome}")
                    escolha = int(input("Escolha o produto pelo número: ")) - 1 
                    if 0 <= escolha < len(produtos):
                        nova_quantidade = int(input("Digite a nova quantidade: "))
                        produtos[escolha].atualizar_quantidade(nova_quantidade)
                        print("Quantidade atualizada!")
                    else:
                        print("Produto inválido")
                else:
                    print("Nenhum produto cadastrado")
            case 'S':
                break

            case _:
                print("----- Código inválido -----")

if __name__ == "__main__": # Função 'main' chamando a função 'menu'
    menu()
