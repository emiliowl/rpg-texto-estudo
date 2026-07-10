nome_aventureiro = None
classe = None
itens = []
tem_erro = False
missao_inicial = "Olá novamente! Irei lhe passar sua \nprimeira missão, portanto espero que esteja preparado!Sua missão é ir até a \nmontanha de Corcovado, Powerpoint, que é o reino vizinho aonosso. Lá é onde se \nlocalizam os goblins, servos do rei tiranico queatormenta nossa cidade...!Mas \napresse-se, os goblins estão a caminho daqui e chegam em algumas horas!"

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
    global missao_inicial

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
    print(missao_inicial)



main()