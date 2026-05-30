import threading
import sys
import pygame
from inteligence import AtomCore
from interface import desenhar_rosto_atom, LARGURA, ALTURA

if __name__ == "__main__":
    # Inicializa o cérebro do Átom (IA, comandos, microfone e etc.)
    assistente = AtomCore()

    # Inicializa a interface, coisa linda 
    pygame.init()
    pygame.mixer.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Átom - Interface de Sistema")

    # Dispara a lógica de escuta
    thread_assistente = threading.Thread(target=assistente.loop_assistente, daemon=True)
    thread_assistente.start()
 
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
 
        desenhar_rosto_atom(assistente.estado_atual)
        
        clock.tick(60)  