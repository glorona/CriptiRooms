import pygame, sys #Importamos pygame y sys
from button import Button

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("RecursosDiscretas/font.ttf", size)



def main_menu():
    pygame.display.set_caption("Menu Principal")

    while True:
        menu_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): #recorriendo eventos
            #print(event)
            if event.type == pygame.QUIT: #if para saber si se salio el juego

                sys.exit()
        
        screen.blit(bg,[0,0]) #set fondo de pantalla
        button_e = Button(image = botone, pos = (800, 525),text_input="EMPEZAR", font = get_font(70), base_color = "White", hovering_color="#18224C") #agregar botones
        button_s = Button(image = botons, pos = (800, 775),text_input="SALIR", font = get_font(70), base_color = "White", hovering_color="#18224C") #agregar botones



        for button in [button_e, button_s]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_e.checkForInput(menu_mouse_pos):
                    pass #play() metodo para ingresar juego
                if button_s.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
     


        pygame.display.update() #actualizar la pantalla


pygame.init() #Inicializa pygame

#Definiendo parametros

size = (1600,900) #define tamanio de ventana

screen = pygame.display.set_mode(size) #creando nueva ventana

#Recursos del juego

bg = pygame.image.load("ImagesDiscretas/bgmenu.png") #cargar imagen de fondo

botone = pygame.image.load("ImagesDiscretas/botone.png") #cargar boton empezar ...

botons = pygame.image.load("ImagesDiscretas/botons.png") # cargar boton salida...


#Programa

main_menu() #corre menu principal
