import pygame
import math
from queue import PriorityQueue

WIDTH = 800      #se der erro, colocar 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Algoritmo A Estrela")

VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 255, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROXO = (128, 0, 128)
LARANJA = (255, 165, 0)
CINZA  = (128, 128, 128)
TURQUESA = (64, 224, 208)
MARROM = (82, 68, 60)
class Node:
    def __init__(self, linha, col, width, total_col):
        self.linha - linha
        self.col = col
        self.x = linha * width
        self.y = col * width
        self.color = BRANCO
        self.vizinhos = []
        self.width = width
        self.total_col = total_col
        
        
        def get_pos(self):
            return self.linha, self.col
        
        def fechado(self):
            return self.color == VERMELHO
    
        def aberto(self):
            return self.color == VERDE
        
        def obstaculo(self):
            return self.color == PRETO
        
        def inicio(self):
            return self.color == LARANJA
          
        def final(self):
            return self.color == ROXO
        
        def reset(self):
            self.color == BRANCO
            
        def make_fechado(self):
            self.color = VERMELHO
            
        def make_aberto(self):
            self.color = VERDE
            
        def make_obstaculo(self):
            self.color = PRETO
            
        def make_final(self):
            self.color = ROXO
            
        def make_caminho(self):
            self.color = TURQUESA
            
        def draw(self,win):
            pygame.draw.rect(win, self.color, (self.c, self.y, self.width, self.width))            
            
        def atualiza_vizinhos(self, grid):
            pass
        
        def __lt__(self, other):
            return False
        
def heuristica(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def criarMapa(linhas, width):
    matriz = []
    gap = width // linhas
    for i in range(linhas):
      matriz.append([])
      for j in range(linhas):
            spot = Spot(i, j, gap, linhas)   
            grid[i].append(spot)
    
    return matriz