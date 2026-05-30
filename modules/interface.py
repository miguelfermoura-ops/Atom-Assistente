import pygame
import math
import random
import threading
import time
import sys
from inteligence import AtomCore  # Importa a classe do núcleo do Átom

pygame.init()
pygame.mixer.init()
 
LARGURA, ALTURA = 600, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Átom - Interface de Sistema")
 
PRETO       = (5, 8, 20)
CIANO       = (0, 220, 210)
CIANO_ESC   = (0, 100, 120)
ROXO        = (80, 0, 160)
ROXO_CLARO  = (140, 60, 220)
BRANCO      = (255, 255, 255)
AZUL_HUD    = (20, 160, 220)
 
def desenhar_rosto_atom(estado):
    tela.fill(PRETO)
    tempo = time.time()
    cx, cy = LARGURA // 2, ALTURA // 2

    # 1. Grade de pontos de fundo
    for x in range(0, LARGURA, 40):
        for y in range(0, ALTURA, 40):
            dist = math.hypot(x - cx, y - cy)
            alpha = max(0, 1 - dist / 350)
            cor_ponto = (0, int(alpha * 50), int(alpha * 70))
            if alpha > 0.05:
                pygame.draw.circle(tela, cor_ponto, (x, y), 1)

    # 2. Silhueta do Rosto
    pontos_rosto = [
        (cx - 100, cy - 160),  # Topo Esquerda
        (cx - 140, cy - 80),   # Têmpora Esquerda
        (cx - 130, cy + 30),   # Bochecha Superior Esquerda
        (cx - 80,  cy + 150),  # Mandíbula Esquerda
        (cx - 40,  cy + 180),  # Queixo Esquerda
        (cx + 40,  cy + 180),  # Queixo Direita
        (cx + 80,  cy + 150),  # Mandíbula Direita
        (cx + 130, cy + 30),   # Bochecha Superior Direita
        (cx + 140, cy - 80),   # Têmpora Direita
        (cx + 100, cy - 160),  # Topo Direita
    ]

    surf_rosto = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
    pygame.draw.polygon(surf_rosto, (5, 25, 40, 180), pontos_rosto)
    tela.blit(surf_rosto, (0, 0))

    # Contorno do Rosto com Brilho
    for espessura, intensidade in [(6, 0.15), (3, 0.4), (1, 1.0)]:
        fator = 0.85 + 0.15 * math.sin(tempo * 2)
        cor = (0, int(200 * fator * intensidade), int(230 * fator * intensidade))
        pygame.draw.polygon(tela, cor, pontos_rosto, espessura)

    # 3. Placas de Armadura
    pygame.draw.lines(tela, CIANO_ESC, False, [(cx - 95, cy - 110), (cx, cy - 135), (cx + 95, cy - 110)], 1)
    pygame.draw.line(tela, CIANO_ESC, (cx - 40, cy + 140), (cx + 40, cy + 140), 1)

    # 4. Malha de Escaneamento Holográfico
    for dx in [-90, -50, 0, 50, 90]:
        pygame.draw.line(tela, (0, 60, 80), (cx + dx, cy - 130), (cx + int(dx * 0.6), cy + 130), 1)

    # 5. Olhos HUD 
    piscar = True
    if estado == "ocioso" and random.random() < 0.015:
        piscar = False

    if piscar:
        pts_olho_esq = [(cx - 90, cy - 30), (cx - 30, cy - 30), (cx - 40, cy - 15), (cx - 85, cy - 15)]
        pts_olho_dir = [(cx + 30, cy - 30), (cx + 90, cy - 30), (cx + 85, cy - 15), (cx + 40, cy - 15)]
        
        pulso_olho = 0.8 + 0.2 * math.sin(tempo * 4)
        cor_olho = (int(0 * pulso_olho), int(220 * pulso_olho), int(210 * pulso_olho))
        
        pygame.draw.polygon(tela, cor_olho, pts_olho_esq)
        pygame.draw.polygon(tela, cor_olho, pts_olho_dir)
        pygame.draw.polygon(tela, BRANCO, pts_olho_esq, 1)
        pygame.draw.polygon(tela, BRANCO, pts_olho_dir, 1)
    else:
        pygame.draw.line(tela, CIANO_ESC, (cx - 90, cy - 22), (cx - 30, cy - 22), 2)
        pygame.draw.line(tela, CIANO_ESC, (cx + 30, cy - 22), (cx + 90, cy - 22), 2)

    # 6. Boca
    boca_y = cy + 70
    if estado == "falando":
        for i, bx in enumerate(range(cx - 70, cx + 75, 7)):
            dist_centro = abs(bx - cx) / 70.0
            fator_forma = max(0.1, 1.0 - dist_centro)
            amp = int((abs(math.sin(tempo * 12 + i * 0.5)) * 35) * fator_forma)
            pygame.draw.line(tela, CIANO, (bx, boca_y - amp // 2), (bx, boca_y + amp // 2), 2)
    elif estado == "ouvindo":
        r_mic = int(12 + 6 * math.sin(tempo * 6))
        pygame.draw.circle(tela, CIANO, (cx, boca_y), r_mic, 1)
        pygame.draw.circle(tela, AZUL_HUD, (cx, boca_y), int(r_mic * 0.6), 0)
    else:
        pygame.draw.line(tela, CIANO_ESC, (cx - 60, boca_y), (cx + 60, boca_y), 1)

    # 7. Elementos de Canto HUD
    try:
        fonte_hud = pygame.font.SysFont("Courier New", 10, bold=True)
    except:
        fonte_hud = pygame.font.Font(None, 16)

    status_txt = "FALANDO" if estado == "falando" else ("OUVINDO" if estado == "ouvindo" else "STANDBY")
    
    tela.blit(fonte_hud.render("DATA INPUT: ACTIVE", True, AZUL_HUD), (25, 30))
    tela.blit(fonte_hud.render(f"LATENCY: {random.randint(12, 45)}ms", True, AZUL_HUD), (LARGURA - 150, 30))
    tela.blit(fonte_hud.render(f"STATUS: {status_txt}", True, CIANO if estado != "ocioso" else AZUL_HUD), (25, ALTURA - 45))
    tela.blit(fonte_hud.render("ATOM SYSTEM v2.0", True, AZUL_HUD), (LARGURA - 150, ALTURA - 45))

    # Molduras angulares
    pygame.draw.lines(tela, CIANO_ESC, False, [(20, 50), (20, 20), (50, 20)], 2)
    pygame.draw.lines(tela, CIANO_ESC, False, [(LARGURA - 20, 50), (LARGURA - 20, 20), (LARGURA - 50, 20)], 2)
    pygame.draw.lines(tela, CIANO_ESC, False, [(20, ALTURA - 50), (20, ALTURA - 20), (50, ALTURA - 20)], 2)
    pygame.draw.lines(tela, CIANO_ESC, False, [(LARGURA - 20, ALTURA - 50), (LARGURA - 20, ALTURA - 20), (LARGURA - 50, ALTURA - 20)], 2)

    pygame.display.flip()

if __name__ == "__main__":
    assistente = AtomCore()

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