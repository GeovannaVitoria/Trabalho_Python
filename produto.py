class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None: 
        """
            Inicializa um novo objeto Produto com nome, preço e quantidade.

            Args:
                nome (str): O nome do produto
                preco (float): O preço do produto
                quantidade (int): A quantidade em estoque do produto

            Returns:
                None
        """
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def exibir_informacoes(self) -> None:
        """
            Exibe as informações do produto, incluindo nome, preço e quantidade em estoque.

            Args:
                None

            Returns:
                None
        """
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        
    def atualizar_preco(self, novo_preco: float) -> None:
        """
            Atualiza o preço do produto, se o novo preço for um valor positivo.

            Args:
                novo_preco (float): O novo valor do preço do produto

            Returns:
                None
        """
        if novo_preco > 0:
            self.preco = novo_preco
            print(f"Preço atualizado: {novo_preco:.2f}")
        else:
            print("O preço deve ser um valor positivo.")
        
    def atualizar_quantidade(self, nova_quantidade: int) -> None:
        """
            Atualiza a quantidade do produto, se a nova quantidade for zero ou um valor positivo.

            Args:
                nova_quantidade (int): A nova quantidade em estoque do produto

            Returns:
                None
        """
        if nova_quantidade >= 0:
            self.quantidade = nova_quantidade
            print(f"Quantidade atualizada: {nova_quantidade}")
        else:
            print("A quantidade precisa ser positiva.")