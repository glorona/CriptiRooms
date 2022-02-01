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
                    user_name()#play() metodo para ingresar juego
                if button_s.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
     

        pygame.display.update() #actualizar la pantalla
        clock.tick(60)

def user_name():
    pygame.display.set_caption("Menu Principal")
    nombre_user = ""
    while True:
        menu_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): #recorriendo eventos
            if event.type == pygame.QUIT: #if para saber si se salio el juego
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre_user = nombre_user[:-1]
                elif event.key == pygame.K_RETURN:
                    tutorial(nombre_user)
                elif len(nombre_user) <= 15: #cumple length de la textbox
                    nombre_user += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_enter.checkForInput(menu_mouse_pos):
                    tutorial(nombre_user)#play() metodo para ingresar juego
        screen.blit(bg,[0,0]) #set fondo de pantalla
        font = get_font(50)
        textobienvenida = font.render("Bienvenido, inserta tu nombre!",True,(255,255,255))
        screen.blit(textobienvenida,(475,450))
        
         #BUTTON
        button_enter = Button(image = botons, pos = (800, 750),text_input="VAMOS!", font = get_font(70), base_color = "White", hovering_color="#18224C") #agregar botones

        for button in [button_enter]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
        


       
        #textbox
        text_rect = pygame.Rect(650,550,300,50)
        font = get_font(30)
        texto = font.render(nombre_user,True,(255,255,255))
        pygame.draw.rect(screen,(255,255,255),text_rect,5)
        screen.blit(texto, (text_rect.x + 7, text_rect.y + 7))

       
        pygame.display.update()
        clock.tick(60)


def tutorial(nombre):
    pass




pygame.init() #Inicializa pygame

#Definiendo parametros
clock = pygame.time.Clock()

size = (1600,900) #define tamanio de ventana

screen = pygame.display.set_mode(size) #creando nueva ventana



#Recursos del juego

bg = pygame.image.load("ImagesDiscretas/bgmenu.png") #cargar imagen de fondo

botone = pygame.image.load("ImagesDiscretas/botone.png") #cargar boton empezar ...

botons = pygame.image.load("ImagesDiscretas/botons.png") # cargar boton salida...

pergaminotuto = pygame.image.load("ImagesDiscretas/pergaminotuto.png") #carga pergamino


#Programa

main_menu() #corre menu principal
