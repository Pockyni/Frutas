class Frutas:
    def __init__(self):
        self.frutas = {}

    def adicionar_fruta(self, nome, preco, quantidade):
        self.frutas[nome] = {"preco": preco, "quantidade": quantidade}
        print(f"{nome} adicionado com sucesso!")

    def excluir_fruta(self, nome):
        if nome in self.frutas:
            del self.frutas[nome]
            print(f"{nome} removido com sucesso!")
        else:
            print("Fruta não encontrada.")

    def atualizar_fruta(self, nome, preco, quantidade):
        if nome in self.frutas:
            self.frutas[nome]["preco"] = preco
            self.frutas[nome]["quantidade"] = quantidade
            print(f"{nome} atualizado com sucesso!")
        else:
            print("Fruta não encontrada.")

    def calcular_total(self):
        total = sum(self.frutas[nome]["preco"] * self.frutas[nome]["quantidade"] for nome in self.frutas)
        print(f"Total a pagar: R$ {total:.2f}")

    def listar_frutas(self):
        if not self.frutas:
            print("Nenhuma fruta cadastrada.")
        else:
            print("\nLista de Frutas:")
            for nome, info in self.frutas.items():
                print(f"{nome}: Preço R${info['preco']:.2f}, Quantidade: {info['quantidade']}")


if __name__ == "__main__":
    loja = Frutas()
    while True:
        print("\nOpções:")
        print("1 - Adicionar Fruta")
        print("2 - Excluir Fruta")
        print("3 - Atualizar Fruta")
        print("4 - Calcular Total")
        print("5 - Listar Frutas")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da fruta: ")
            preco = float(input("Preço da fruta: "))
            quantidade = int(input("Quantidade: "))
            loja.adicionar_fruta(nome, preco, quantidade)
        elif opcao == "2":
            nome = input("Nome da fruta para remover: ")
            loja.excluir_fruta(nome)
        elif opcao == "3":
            nome = input("Nome da fruta para atualizar: ")
            preco = float(input("Novo preço: "))
            quantidade = int(input("Nova quantidade: "))
            loja.atualizar_fruta(nome, preco, quantidade)
        elif opcao == "4":
            loja.calcular_total()
        elif opcao == "5":
            loja.listar_frutas()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
