nome_aventureiro = None
classe = None
itens = []

textao_bem_vindo = """
Bem vindo, {nome_aventureiro}! 
Precisamos de sua ajuda para derrotar o rei tiranico que maltrata o 
reino de Powertronic, nosso reino.
"""

def imprime_textao(textao, parametros):
    print(textao.format(**parametros))

def mostra_itens():
    print("Voce possui os seguintes itens:")
    for item in itens:
        print(f"- {item}")

def main():
    print("Ola aventureiro! Seja bem vindo!")
    nome_aventureiro = input("Digite seu nome aqui, aventureiro: ")
    imprime_textao(textao_bem_vindo, {"nome_aventureiro": nome_aventureiro})

    print(f"{nome_aventureiro}, voce quer armas de guerreiro ou mago?")
    classe = input("Digite 'guerreiro' ou 'mago': ")
    if classe == "guerreiro":
        itens.append("espada")
        itens.append("escudo")
    elif classe == "mago":
        itens.append("cajado")
        itens.append("capa")

    print("Boa escolha!")
    mostra_itens()

main()