import pygame, sys #Importamos pygame y sys

pygame.init() #Inicializa pygame


#Parametros de juego

#Definiendo colores
        #R G B
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED =   (255,0,0)
BLUE =  (0,0,255)



size = (1600,900) #define tamanio de ventana

screen = pygame.display.set_mode(size) #creando nueva ventana

while True: #Crear bucle para juego
    for event in pygame.event.get(): #recorriendo eventos
        if event.type == pygame.QUIT: #if para saber si se salio el juego

            sys.exit()

    screen.fill(WHITE) #pintar pantalla de blanco 
    #Zonas de dibujo 
    
    pygame.draw.line(screen, GREEN, [0,100], [1600,100], 5)
    #                escena  color pos inicio pos final grosor
    #                              x,y
    pygame.draw.line(screen, BLUE, [0,300], [1600,600], 10)


    #Fin zona dibujo

    pygame.display.flip() #actualizar pantalla