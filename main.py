import pygame
import time

nome_aventureiro = None
classe = None
itens = []
tem_erro = False
missao_inicial = "\nOlá novamente! Irei lhe passar sua \nprimeira missão, portanto espero que esteja preparado!Sua missão é ir até a \nmontanha de Corcovado, Powerpoint, que é o reino vizinho ao nosso. Lá é onde se \nlocalizam os goblins, servos do rei tiranico que atormenta nossa cidade...Mas \napresse-se, os goblins estão a caminho daqui e chegam em algumas horas!"


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
    global fase

    pygame.init()

    pygame.mixer.music.load("musica-abertura.mp3")
    pygame.mixer.music.play()
    
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
        itens.append("espada: 10 de dano")
        itens.append("escudo: -10 no dano causado (propriedade especial: ele pode te curar se o dano causado for menor do que a defesa dele)")
    elif classe == "mago":
        itens.append("cajado: possui a magia bola de fogo: 20 de dano")
        itens.append("capa")

    print("Boa escolha!")
    mostra_itens()
    input("Pressione qualquer enter para prosseguir")

    print(missao_inicial)
    input("Pressione qualquer enter para prosseguir")

    pygame.mixer.music.stop
    
    pygame.mixer.music.load("luta1.mp3")
    pygame.mixer.music.play()
    time.sleep(1.5)

    print("Você se depara com 3 globins enquanto escala a montanha de Corcovado, o que deseja fazer? (Seu HP está em 100)")
    acao_realizada = input("1 - Correr \n2 - Atacar \n3 - defender \n")


main()