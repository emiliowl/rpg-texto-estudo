nome_aventureiro = None
itens = []

textao_bem_vindo = """
Bem vindo, {nome_aventureiro}! 
Precisamos de sua ajuda para derrotar o rei tiranico que maltrata o 
reino de Powertronic, nosso reino.
"""

def imprime_textao(textao, parametros):
    print(textao.format(**parametros))

def main():
    print("Ola aventureiro! Seja bem vindo!")
    nome_aventureiro = input("Digite seu nome aqui, aventureiro: ")
    imprime_textao(textao_bem_vindo, {"nome_aventureiro": nome_aventureiro})

main()