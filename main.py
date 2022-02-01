import pygame, sys, time #Importamos pygame y sys
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

        bgScale = pygame.transform.scale(bg,(1280,720))
        botoneScale = pygame.transform.scale(botone,(320,160))
        botonsScale = pygame.transform.scale(botons,(320,160))


        screen.blit(bgScale, [0,0]) #set fondo de pantalla
         
        button_e = Button(image = botoneScale, pos = (640, 420),text_input="EMPEZAR", font = get_font(56), base_color = "White", hovering_color="#18224C") #agregar botones
        button_s = Button(image = botonsScale, pos = (640, 620),text_input="SALIR", font = get_font(56), base_color = "White", hovering_color="#18224C") #agregar botones



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

        bgScale = pygame.transform.scale(bg,(1280,720))
        screen.blit(bgScale,[0,0]) #set fondo de pantalla
        font = get_font(40)
        textobienvenida = font.render("Bienvenido, inserta tu nombre!",True,(255,255,255))
        screen.blit(textobienvenida,(380,360))
        
         #BUTTON
        button_enter = Button(image = botons, pos = (640, 600),text_input="VAMOS!", font = get_font(56), base_color = "White", hovering_color="#18224C") #agregar botones

        for button in [button_enter]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
        


       
        #textbox
        text_rect = pygame.Rect(520,440,240,40)
        font = get_font(24)
        texto = font.render(nombre_user,True,(255,255,255))
        pygame.draw.rect(screen,(255,255,255),text_rect,5)
        screen.blit(texto, (text_rect.x + 5.6, text_rect.y + 5.6))

       
        pygame.display.update()
        clock.tick(60)


def tutorial(nombre):
    screen.fill((24,34,76))
    while True:
        tutorial_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_continuar.checkForInput(tutorial_mouse_pos):
                    level_1(nombre) # funcion que da paso al juego principal
                if button_retroceder.checkForInput(tutorial_mouse_pos):
                    main_menu()

        pergaminoScale = pygame.transform.scale(pergaminotuto,(1024,576))
        rect = pergaminoScale.get_rect()
        rect = rect.move((120,80))

        screen.blit(pergaminoScale, rect)

        font = get_font(52)
        texto_nombre = font.render(nombre,True,(0,0,0))
        screen.blit(texto_nombre,(576,172))

        #Reescalado de boton
        
        #Botones
        button_continuar = Button(image = None, pos = (1160, 360),text_input="CONTINUAR", font = get_font(40), base_color = "White", hovering_color="Black")
        button_retroceder = Button(image = None, pos = (120, 360),text_input="RETROCEDER", font = get_font(40), base_color = "White", hovering_color="Black")

        for button in [button_continuar,button_retroceder]:
            button.changeColor(tutorial_mouse_pos)
            button.update(screen)
       
        pygame.display.update()
        clock.tick(60)


def game_over():
    pass

def level_1(nameusr):
    pygame.display.set_caption("Nivel 1")
    timestart =  int(round(time.time(),0))
    minutes = 0
    while True:
        menu_mouse_pos = pygame.mouse.get_pos()
        timegame = int(round(time.time(),0))
        dt = timegame - timestart
        print(dt)
        if minutes < 3:
            for event in pygame.event.get(): #recorriendo eventos
                #print(event)
                if event.type == pygame.QUIT: #if para saber si se salio el juego

                    sys.exit()
            #Cargar gui
            font = get_font(40)
            #bg

            bgl1Scale = pygame.transform.scale(bgl1,(1280,720))
            screen.blit(bgl1Scale,[0,0])
            #texto l1
            textol1 = font.render("Nivel 1",True,(255,255,255))
            screen.blit(textol1,(60,20))
            #timer
            #poner foto
            if dt == 60:
                minutes+=1
                timestart = int(round(time.time(),0))
        
            stringtime = str(minutes) + ":" + str(dt)
            textotimer = font.render(stringtime,True,(255,255,255))
        
            screen.blit (textotimer,(650,20))

            #cargar nivel
            l1Scale = pygame.transform.scale(mapl1,(800,560))

            screen.blit(l1Scale,[250,100])




            


            pygame.display.update()
            clock.tick(60)
        else:
            game_over(nameusr)






pygame.init() #Inicializa pygame

#Definiendo parametros
clock = pygame.time.Clock()

size = (1280,720) #define tamanio de ventana

screen = pygame.display.set_mode(size) #creando nueva ventana



#Recursos del juego

bg = pygame.image.load("ImagesDiscretas/bgmenu.png") #cargar imagen de fondo

bgl1 = pygame.image.load("ImagesDiscretas/fl1.png") #fondo nivel 1

mapl1 = pygame.image.load("ImagesDiscretas/l1.png")

botone = pygame.image.load("ImagesDiscretas/botone.png") #cargar boton empezar ...

botons = pygame.image.load("ImagesDiscretas/botons.png") # cargar boton salida...

pergaminotuto = pygame.image.load("ImagesDiscretas/pergaminotuto.png") #carga pergamino


#Programa

main_menu() #corre menu principal
