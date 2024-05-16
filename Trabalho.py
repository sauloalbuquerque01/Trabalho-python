def adicionar_item(carrinho, precos):
    print("BEM VINDO AO CONTROLE DE ESTOQUE!")
    while True:
        item = input("Qual produto você deseja adicionar ao estoque? (ou digite 'sair' para fechar): ").capitalize()
        if item == 'Sair':
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
    print("\n================================= \n      SEUS ITENS NO ESTOQUE! \n=================================")
    for item, quantidade in carrinho.items():
        print(f"{item}: {quantidade} unidade(s)!")
    print("=================================")
    
def resultado2(carrinho, precos):
    print("\n================================= \n     SEUS ITENS NO ESTOQUE! \n=================================")
    for item, quantidade in carrinho.items():
        print(f"{item}: {quantidade} unidade(s)!")
    print("=================================")

def somar_itens(carrinho, precos):
    total = sum(precos[item] * quantidade for item, quantidade in carrinho.items())
    return total

def remover_item(carrinho):
    while True:
        menu = input("---------------------- \nO que deseja fazer?: \nREMOVER ITEM \nSAIR \nDigite: ").upper()
        print("----------------------")
        if menu == "SAIR":
            break
        elif menu == "REMOVER ITEM":
            item = input("Digite o nome do item que você deseja remover do estoque: ").capitalize()
            if item in carrinho:
                quantidade = int(input(f"Quantas unidades de {item} você deseja remover? "))
                if quantidade <= carrinho[item]:
                    carrinho[item] -= quantidade
                    print(f"{quantidade} unidades de {item} foram removidas do estoque.")
                else:
                    print(f"Não há {quantidade} unidades de {item} disponíveis no estoque.")
            else:
                print(f"{item} não está no estoque.")

def main():
    carrinho = {}
    precos = {}
    adicionar_item(carrinho, precos)
    resultado(carrinho, precos)
    remover_item(carrinho)
    total = somar_itens(carrinho, precos)
    resultado2(carrinho, precos)
    print(f"Valor do seu estoque é {total:.2f}")
        
if __name__ == "__main__":
    main()