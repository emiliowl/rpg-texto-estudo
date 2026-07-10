nome_aventureiro = None
classe = None
itens = []
tem_erro = False

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
    global classe
    global tem_erro
    print("Ola aventureiro! Seja bem vindo!")
    nome_aventureiro = input("Digite seu nome aqui, aventureiro: ")
    imprime_textao(textao_bem_vindo, {"nome_aventureiro": nome_aventureiro})

    print(f"{nome_aventureiro}, voce quer armas de guerreiro ou mago?")
    while classe not in ["guerreiro", "mago"]:
        if tem_erro:
            print("A classe solicitada não está disponível")
            
        classe = input("Digite 'guerreiro' ou 'mago': ")
        tem_erro = classe not in ["guerreiro", "mago"]


    if classe == "guerreiro":
        itens.append("espada")
        itens.append("escudo")
    elif classe == "mago":
        itens.append("cajado")
        itens.append("capa")

    print("Boa escolha!")
    mostra_itens()

main()