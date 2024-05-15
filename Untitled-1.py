def adicionar_item(carrinho, precos):
    print("BEM VINDO AO CONTROLE DE ESTOQUE!")
    while True:
        item = input("Qual produto você deseja adicionar ao estoque? (ou digite 'sair' para fechar): ").lower()
        if item == 'sair':
            break
        quantidade = int(input("Quantos produtos?: "))
        if quantidade in carrinho:
            carrinho[item] += quantidade
        else:
            carrinho[item] = quantidade
        print(f"Foi adicionado {quantidade} unidade(s) de {item}")
        valor = float(input("Qual é o valor do produto?: "))
        precos[item] = valor

def resultado(carrinho, precos):
    print("\n================================= \n      SEUS ITENS NO CARRINHO! \n=================================")
    for item, quantidade in carrinho.items():
        print(f"{item}: {quantidade} unidade(s)!")
    print("=================================")

def somar_itens(carrinho, precos):
    total = sum(precos[item] * quantidade for item, quantidade in carrinho.items())
    return total

def main():
    carrinho = {}
    precos = {}
    adicionar_item(carrinho, precos)
    total = somar_itens(carrinho, precos)
    resultado(carrinho, precos)
    print(f"Valor total do estoque: R${total:.2f}")
        
if __name__ == "__main__":
    main()