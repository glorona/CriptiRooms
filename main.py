from linecache import clearcache
import pygame, sys, time #Importamos pygame y sys
from button import Button
from player import Player
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("RecursosDiscretas/font.ttf", size)



def main_menu():
    pygame.display.set_caption("Menu Principal")

    while True:
        menu_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): #recorriendo eventos
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
    pygame.key.set_repeat()
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


def game_over(nombre, niveles = 0, pistas = 0):
    screen.fill((24,34,76))
    while True:
        gameover_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_continuar.checkForInput(gameover_mouse_pos):
                    user_name() 
                if button_salir.checkForInput(gameover_mouse_pos):
                    sys.exit()

        screen.blit(pergaminofinal, [0,0])

        font = get_font(52)

        texto_nombre = font.render(nombre,True,(0,0,0))
        texto_niveles = font.render(str(niveles),True,(0,0,0))
        texto_pistas = font.render(str(pistas),True,(0,0,0))

        screen.blit(texto_nombre,(800,200))
        screen.blit(texto_niveles,(800,325))
        screen.blit(texto_pistas,(800,445))

        #Botones
        button_continuar = Button(image = None, pos = (750, 565),text_input="INTENTAR DE NUEVO", font = get_font(40), base_color = "#3f8c48", hovering_color="#18224C")
        button_salir = Button(image = None, pos = (450, 565),text_input="SALIR", font = get_font(40), base_color = "#993f3f", hovering_color="#18224C")

        for button in [button_continuar,button_salir]:
            button.changeColor(gameover_mouse_pos)
            button.update(screen)
       
        pygame.display.update()
        clock.tick(60)



def level_1(nameusr):
    #pygame.key.set_repeat(15,5)
    pygame.display.set_caption("Nivel 1")
    timestart =  int(round(time.time(),0))
    minutes = 0
    moving_sprites = pygame.sprite.Group()
    player = Player(700,500)
    moving_sprites.add(player)
    steps = 2

    canMove = True
    isCollidingHint1 = False
    isCollidingHint2 = False
    isCollidingHint3 = False
    isCollidingLock = False
    hint1r = False
    hint2r = False
    hint3r = False
    chal1r = False

    hint1_rect = pygame.Rect(380,180,50,25)
    hint2_rect = pygame.Rect(880,567,50,25)
    hint3_rect = pygame.Rect(365,364,50,25)
    lock_rect = pygame.Rect(1015,330,50,25)

    #pared
    wall = pygame.Rect(250,100,800,35)
    wall2 = pygame.Rect(250,100,35,560)
    wall3 = pygame.Rect(250,645,800,35)
    wall4 = pygame.Rect(1025,100,35,560)
    wall5 = pygame.Rect(275,255,300,85)



    #14 rectangulos de obstaculos
    obstacle_r1 = pygame.Rect(337,180,40,32) #cabeza
    obstacle_r2 = pygame.Rect(659,117,36,41) #chimenea
    obstacle_r3 = pygame.Rect(775,165,36,36) #piedra 
    obstacle_r4 = pygame.Rect(870,187,37,34) #pulpo
    obstacle_r5 = pygame.Rect(946,180,38,21) #tronco arriba
    obstacle_r6 = pygame.Rect(980,247,34,50) #pilar sup
    obstacle_r7 = pygame.Rect(980,410,34,50) #pilar inf
    obstacle_r8 = pygame.Rect(318,362,34,50) #pilar latizq
    obstacle_r9 = pygame.Rect(532,362,34,50) #pilar latder
    obstacle_r10 = pygame.Rect(318,500,36,36) #piedra pilar
    obstacle_r11 = pygame.Rect(468,528,38,21) #tronco pilar
    obstacle_r12 = pygame.Rect(965,487,21,38) #tronco derecha arriba
    obstacle_r13 = pygame.Rect(965,585,21,36) #tronco derecha abajo
    obstacle_r14 = pygame.Rect(840,567,36,36) #piedra derecha abajo

    obstacles = [obstacle_r1,obstacle_r2,obstacle_r3,obstacle_r4,obstacle_r5,obstacle_r6
    ,obstacle_r7,obstacle_r8,obstacle_r9,obstacle_r10,obstacle_r11,obstacle_r12,obstacle_r13,obstacle_r14, wall,wall2,wall3,wall4,wall5]

    rect = [hint1_rect]
    points = 0
    ertime = 0
    respu = ""
    respuesta = ""

    # Ventana Ayuda
    ayudaIsVisible = False 

    while True:
        lvl_mouse_pos = pygame.mouse.get_pos()
        timegame = int(round(time.time(),0))
        dt = timegame - timestart
        keyP = pygame.key.get_pressed()
        if minutes < 5:

            if canMove:
                if (keyP[pygame.K_LEFT]) and not player.checkCollision(obstacles,steps, 0):
                    player.update(-steps, 0)
                if (keyP[pygame.K_RIGHT]) and not player.checkCollision(obstacles,-steps, 0):
                    player.update(steps, 0)
                if (keyP[pygame.K_UP]) and not player.checkCollision(obstacles,0, steps):
                    player.update(0, -steps)
                if (keyP[pygame.K_DOWN]) and not player.checkCollision(obstacles,0, -steps):
                    player.update(0, steps)

            for event in pygame.event.get(): #recorriendo eventos
                #print(event)
                if event.type == pygame.QUIT: #if para saber si se salio el juego
                    sys.exit()
                # Ventana de ayuda, Interaccion
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_ayuda.checkForInput(lvl_mouse_pos):
                        if ayudaIsVisible:
                            ayudaIsVisible = False
                        else:
                            ayudaIsVisible = True
                    if button_closeAyuda.checkForInput(lvl_mouse_pos):
                        ayudaIsVisible = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        respu = respu[:-1]
                    elif event.key == pygame.K_RETURN:
                        respu = respu.lower()
                        if respu == respuesta and (isCollidingHint1 or isCollidingHint2 or isCollidingHint3 or isCollidingLock):
                            points+=1
                            if isCollidingHint1:
                                print("Respuesta 1 Correcta")
                                hint1r = True
                                respuesta = ""
                            elif isCollidingHint2:
                                print("Respuesta 2 Correcta")
                                hint2r = True
                                respuesta = ""
                            elif isCollidingHint3:
                                print("Respuesta 3 Correcta")
                                hint3r = True
                                respuesta = ""
                            elif isCollidingLock:
                                print("Nivel Completado")
                                chal1r = True
                                stageclear(nameusr, points)
                        else:
                            if isCollidingHint1 or isCollidingHint2 or isCollidingHint3 or isCollidingLock:
                                ertime = 100
                                timestart-=30
                            


                    elif len(respu) <= 500: #cumple length de la textbox
                        respu += event.unicode

                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        if player.rect.colliderect(hint1_rect):
                            if isCollidingHint1:
                                canMove = True
                                isCollidingHint1 = False
                            else:
                                respuesta = "3"
                                respu = ""
                                canMove = False
                                isCollidingHint1 = True
                        if player.rect.colliderect(hint2_rect):
                            if isCollidingHint2:
                                canMove = True
                                isCollidingHint2 = False
                            else:
                                respu = ""
                                respuesta  = "5"
                                canMove = False
                                isCollidingHint2 = True
                        if player.rect.colliderect(hint3_rect):
                            if isCollidingHint3:
                                canMove = True
                                isCollidingHint3 = False
                            else:
                                respu = ""
                                respuesta = "8"
                                canMove = False
                                isCollidingHint3 = True
                        if player.rect.colliderect(lock_rect):
                            if points >= 3:
                                if isCollidingLock:
                                    canMove = True
                                    isCollidingLock = False
                                else:
                                    respu = ""
                                    respuesta = "matematicas discretas"
                                    canMove = False
                                    isCollidingLock = True

                    

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
            if dt >= 60:
                minutes+=1
                timestart = int(round(time.time(),0)) - (dt-60)
        
            stringtime = str(minutes) + ":" + str(dt)
            textotimer = font.render(stringtime,True,(255,255,255))
        
            screen.blit (textotimer,(650,20))

            #cargar nivel
            l1Scale = pygame.transform.scale(mapl1,(800,560))

            screen.blit(l1Scale,[250,100])

            #cargar jugador
            moving_sprites.draw(screen)
        
            
            


            #textbox
            respu_rect = pygame.Rect(525,525,280,40)
            font = get_font(24)
            texto = font.render(respu,True,(0,0,0))
    


            
            #hints
            hint1 = pygame.transform.scale(minipergamino,(30,30))
            hint2 = hint1
            hint3 = hint1

            #points
            puntosind = pygame.transform.scale(minipergamino,(60,60))
            screen.blit(puntosind,(60,650))
            font = get_font(45)
            textopoints = font.render( "= " + str(points),True,(255,255,255))
            screen.blit(textopoints, (120, 645))

            #chal 
            locks = pygame.transform.scale(lock,(40,40))
            
            screen.blit(hint1,hint1_rect)
            screen.blit(hint2,hint2_rect)
            screen.blit(hint3,hint3_rect)
            screen.blit(locks,lock_rect)


            if isCollidingHint1:
                if not hint1r:
                    screen.blit(minipergamino1,(250,2))  # cambiar las imagenes de los pergaminos aqui, en vez de minipergamino colocar la del hint real
                    pygame.draw.rect(screen,(0,0,0),respu_rect,5)
                    screen.blit(texto, (respu_rect.x + 5.6, respu_rect.y + 5.6))
                else:
                     screen.blit(res1,(250,2))  # muestra respuesta correcta
            if isCollidingHint2:
                if not hint2r:
                    screen.blit(minipergamino2,(250,2))
                    pygame.draw.rect(screen,(0,0,0),respu_rect,5)
                    screen.blit(texto, (respu_rect.x + 5.6, respu_rect.y + 5.6))
                else:
                    screen.blit(res2,(250,2))  # muestra respuesta correcta
                
            if isCollidingHint3:
                if not hint3r:
                    screen.blit(minipergamino3,(250,2))
                    pygame.draw.rect(screen,(0,0,0),respu_rect,5)
                    screen.blit(texto, (respu_rect.x + 5.6, respu_rect.y + 5.6))
                else:
                    screen.blit(res3,(250,2))  # muestra respuesta correcta
            if isCollidingLock: #agregar condicion cantidad pistas
                if not chal1r:
                    screen.blit(chal1,(250,2))
                    pygame.draw.rect(screen,(0,0,0),respu_rect,5)
                    screen.blit(texto, (respu_rect.x + 5.6, respu_rect.y + 5.6))
    
            if ertime > 0:
                screen.blit(error,(500,300))
                ertime-=1


            #Ventana de ayuda, ajuste de posicion de botones
            button_ayuda = Button(image = None, pos = (150, 565),text_input="Acerca de", font = get_font(40), base_color = "White", hovering_color="#18224C")
            button_closeAyuda = Button(image = None, pos = (900, 100),text_input="X", font = get_font(40), base_color = "#993f3f", hovering_color="#18224C")

            if not ayudaIsVisible:
                button_ayuda.changeColor(lvl_mouse_pos)
                button_ayuda.update(screen)
            else:
                screen.blit(minipergamino,(250,2)) # Colocar Pergamino con Teoria aqui
                button_ayuda.changeColor(lvl_mouse_pos)
                button_ayuda.update(screen)
                button_closeAyuda.changeColor(lvl_mouse_pos)
                button_closeAyuda.update(screen)


            pygame.display.update()
            clock.tick(60)
        else:
            game_over(nameusr,1,points)

def level_2(nameusr, prevPoints):
    #pygame.key.set_repeat(15,5)
    pygame.display.set_caption("Nivel 2")
    timestart =  int(round(time.time(),0))
    minutes = 0
    moving_sprites = pygame.sprite.Group()
    player = Player(700,500)
    moving_sprites.add(player)
    steps = 2

    canMove = True
    isCollidingHint1 = False
    isCollidingHint2 = False
    isCollidingHint3 = False
    isCollidingLock = False
    hint1r = False
    hint2r = False
    hint3r = False
    chal1r = False

    hint1_rect = pygame.Rect(500,170,50,25)
    hint2_rect = pygame.Rect(870,220,50,25)
    hint3_rect = pygame.Rect(550,575,50,25)
    lock_rect = pygame.Rect(880,625,50,25)

    #pared
    wall = pygame.Rect(250,100,800,35)
    wall2 = pygame.Rect(250,100,35,560)
    wall3 = pygame.Rect(250,645,800,35)
    wall4 = pygame.Rect(1025,100,35,560)
    wall5 = pygame.Rect(675,125,45,300)



    #14 rectangulos de obstaculos
    obstacle_r1 = pygame.Rect(337,135,40,40) #chim
    obstacle_r2 = pygame.Rect(317,230,36,48) #cama
    obstacle_r3 = pygame.Rect(563,167,36,36) #cabeza
    obstacle_r4 = pygame.Rect(468,200,40,50) #yunque
    obstacle_r5 = pygame.Rect(345,555,70,50) #mesa
    obstacle_r6 = pygame.Rect(640,280,34,50) #pilar sup
    obstacle_r7 = pygame.Rect(640,380,34,50) #pilar inf
    obstacle_r8 = pygame.Rect(795,250,60,50) #biblio
    obstacle_r9 = pygame.Rect(795,150,60,50) #biblio
    obstacle_r10 = pygame.Rect(680,592,36,36) #vasija
    obstacle_r11 = pygame.Rect(915,150,60,50) #biblio
    obstacle_r12 = pygame.Rect(915,250,60,50) #biblio
    obstacle_r13 = pygame.Rect(735,373,36,36) #craneo2
    obstacle_r14 = pygame.Rect(960,360,48,48) #libros

    obstacles = [obstacle_r1,obstacle_r2,obstacle_r3,obstacle_r4,obstacle_r5,obstacle_r6
    ,obstacle_r7,obstacle_r8,obstacle_r9,obstacle_r10,obstacle_r11,obstacle_r12,obstacle_r13,obstacle_r14, wall,wall2,wall3,wall4,wall5]

    rect = [hint1_rect]
    ertime = 0
    respu = ""
    respuesta = ""
    while True:
        menu_mouse_pos = pygame.mouse.get_pos()
        timegame = int(round(time.time(),0))
        dt = timegame - timestart
        keyP = pygame.key.get_pressed()
        if minutes < 5:

            if canMove:
                if (keyP[pygame.K_LEFT]) and not player.checkCollision(obstacles,steps, 0):
                    player.update(-steps, 0)
                if (keyP[pygame.K_RIGHT]) and not player.checkCollision(obstacles,-steps, 0):
                    player.update(steps, 0)
                if (keyP[pygame.K_UP]) and not player.checkCollision(obstacles,0, steps):
                    player.update(0, -steps)
                if (keyP[pygame.K_DOWN]) and not player.checkCollision(obstacles,0, -steps):
                    player.update(0, steps)

            for event in pygame.event.get(): #recorriendo eventos
                #print(event)
                if event.type == pygame.QUIT: #if para saber si se salio el juego
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        respu = respu[:-1]
                    elif event.key == pygame.K_RETURN:
                        respu = respu.lower()
                        respu.replace(" ", "")
                        if respu == respuesta and (isCollidingHint1 or isCollidingHint2 or isCollidingHint3 or isCollidingLock):
                            prevPoints+=1
                            if isCollidingHint1:
                                print("Respuesta 1 Correcta")
                                hint1r = True
                                respuesta = ""
                            elif isCollidingHint2:
                                print("Respuesta 2 Correcta")
                                hint2r = True
                                respuesta = ""
                            elif isCollidingHint3:
                                print("Respuesta 3 Correcta")
                                hint3r = True
                                respuesta = ""
                            elif isCollidingLock:
                                print("Nivel Completado")
                                chal1r = True
                                game_over(nameusr, 2, prevPoints)
                        else:
                            if isCollidingHint1 or isCollidingHint2 or isCollidingHint3 or isCollidingLock:
                                ertime = 100
                                timestart-=30
                            


                    elif len(respu) <= 500: #cumple length de la textbox
                        respu += event.unicode

                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        if player.rect.colliderect(hint1_rect):
                            if isCollidingHint1:
                                canMove = True
                                isCollidingHint1 = False
                            else:
                                respuesta = "8"
                                respu = ""
                                canMove = False
                                isCollidingHint1 = True
                        if player.rect.colliderect(hint2_rect):
                            if isCollidingHint2:
                                canMove = True
                                isCollidingHint2 = False
                            else:
                                respu = ""
                                respuesta  = "5"
                                canMove = False
                                isCollidingHint2 = True
                        if player.rect.colliderect(hint3_rect):
                            if isCollidingHint3:
                                canMove = True
                                isCollidingHint3 = False
                            else:
                                respu = ""
                                respuesta = "4"
                                canMove = False
                                isCollidingHint3 = True
                        if player.rect.colliderect(lock_rect):
                            if prevPoints >= 6:
                                if isCollidingLock:
                                    canMove = True
                                    isCollidingLock = False
                                else:
                                    respu = ""
                                    respuesta = "11110011010101001011110111001"
                                    canMove = False
                                    isCollidingLock = True

                    

            #Cargar gui
            font = get_font(40)
            #bg
            bgl1Scale = pygame.transform.scale(bgl1,(1280,720))
            screen.blit(bgl1Scale,[0,0])
            #texto l1
            textol2 = font.render("Nivel 2",True,(255,255,255))
            screen.blit(textol2,(60,20))
            #timer
            #poner foto
            if dt >= 60:
                minutes+=1
                timestart = int(round(time.time(),0)) - (dt-60)
        
            stringtime = str(minutes) + ":" + str(dt)
            textotimer = font.render(stringtime,True,(255,255,255))
        
            screen.blit (textotimer,(650,20))

            #cargar nivel
            l2Scale = pygame.transform.scale(mapl2,(800,560))

            screen.blit(l2Scale,[250,100])

            #cargar jugador
            moving_sprites.draw(screen)
        
            


            #textbox
            respu_rect = pygame.Rect(525,525,280,40)
            font = get_font(24)
            texto = font.render(respu,True,(0,0,0))
    


            
            #hints
            hint1 = pygame.transform.scale(minipergamino,(30,30))
            hint2 = hint1
            hint3 = hint1

            #points
            puntosind = pygame.transform.scale(minipergamino,(60,60))
            screen.blit(puntosind,(60,650))
            font = get_font(45)
            textopoints = font.render( "= " + str(prevPoints),True,(255,255,255))
            screen.blit(textopoints, (120, 645))

            #chal 
            locks = pygame.transform.scale(lock,(40,40))
            
            screen.blit(hint1,hint1_rect)
            screen.blit(hint2,hint2_rect)
            screen.blit(hint3,hint3_rect)
            screen.blit(locks,lock_rect)


            if isCollidingHint1:
                if not hint1r:
                    screen.blit(minipergamino4,(250,2))  # cambiar las imagenes de los pergaminos aqui, en vez de minipergamino colocar la del hint real
                    pygame.draw.rect(screen,(0,0,0),respu_rect,5)
                    screen.blit(texto, (respu_rect.x + 5.6, respu_rect.y + 5.6))
                else:
                     screen.blit(res4,(250,2))  # muestra respuesta correcta
            if isCollidingHint2:
                if not hint2r:
                    screen.blit(minipergamino5,(250,2))
                    pygame.draw.rect(screen,(0,0,0),respu_rect,5)
                    screen.blit(texto, (respu_rect.x + 5.6, respu_rect.y + 5.6))
                else:
                    screen.blit(res5,(250,2))  # muestra respuesta correcta
                
            if isCollidingHint3:
                if not hint3r:
                    screen.blit(minipergamino6,(250,2))
                    pygame.draw.rect(screen,(0,0,0),respu_rect,5)
                    screen.blit(texto, (respu_rect.x + 5.6, respu_rect.y + 5.6))
                else:
                    screen.blit(res6,(250,2))  # muestra respuesta correcta
            if isCollidingLock: #agregar condicion cantidad pistas
                if not chal1r:
                    screen.blit(chal2,(250,2))
                    pygame.draw.rect(screen,(0,0,0),respu_rect,5)
                    screen.blit(texto, (respu_rect.x + 5.6, respu_rect.y + 5.6))
    
            if ertime > 0:
                screen.blit(error,(500,300))
                ertime-=1


            pygame.display.update()
            clock.tick(60)
        else:
            game_over(nameusr,1,prevPoints)


def stageclear(nombre, points):
    screen.fill((24,34,76))
    while True:
        gameover_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_continuar.checkForInput(gameover_mouse_pos):
                    level_2(nombre, points)
                if button_salir.checkForInput(gameover_mouse_pos):
                    sys.exit()

        screen.blit(nclear, [0,0])

        font = get_font(52)

        #Botones
        button_continuar = Button(image = None, pos = (750, 565),text_input="CONTINUAR", font = get_font(40), base_color = "#3f8c48", hovering_color="#18224C")
        button_salir = Button(image = None, pos = (450, 565),text_input="SALIR", font = get_font(40), base_color = "#993f3f", hovering_color="#18224C")

        for button in [button_continuar,button_salir]:
            button.changeColor(gameover_mouse_pos)
            button.update(screen)
       
        pygame.display.update()
        clock.tick(60)



pygame.init() #Inicializa pygame

#Definiendo parametros
clock = pygame.time.Clock()

size = (1280,720) #define tamanio de ventana

screen = pygame.display.set_mode(size) #creando nueva ventana

#Recursos del juego

bg = pygame.image.load("ImagesDiscretas/bgmenu.png") #cargar imagen de fondo

bgl1 = pygame.image.load("ImagesDiscretas/fl1.png") #fondo nivel 1

mapl1 = pygame.image.load("ImagesDiscretas/l1.png")

mapl2 = pygame.image.load("ImagesDiscretas/l2.png")

botone = pygame.image.load("ImagesDiscretas/botone.png") #cargar boton empezar ...

botons = pygame.image.load("ImagesDiscretas/botons.png") # cargar boton salida...

pergaminotuto = pygame.image.load("ImagesDiscretas/pergaminotuto.png") #carga pergamino

pergaminofinal = pygame.image.load("ImagesDiscretas/gameover.png")

minipergamino = pygame.image.load("ImagesDiscretas/hint.png")

minipergamino1 = pygame.image.load("ImagesDiscretas/hint1.png")

minipergamino2 = pygame.image.load("ImagesDiscretas/hint2.png")

minipergamino3 = pygame.image.load("ImagesDiscretas/hint3.png")

minipergamino4 = pygame.image.load("ImagesDiscretas/hint4.png")

minipergamino5 = pygame.image.load("ImagesDiscretas/hint5.png")

minipergamino6 = pygame.image.load("ImagesDiscretas/hint6.png")

chal1 = pygame.image.load("ImagesDiscretas/desafio1.png")

chal2 = pygame.image.load("ImagesDiscretas/desafio2.png")

lock = pygame.image.load("ImagesDiscretas/lock1.png")

res1 = pygame.image.load("ImagesDiscretas/res1.png")

res2 = pygame.image.load("ImagesDiscretas/res2.png")

res3 = pygame.image.load("ImagesDiscretas/res3.png")

res4 = pygame.image.load("ImagesDiscretas/res4.png")

res5 = pygame.image.load("ImagesDiscretas/res5.png")

res6 = pygame.image.load("ImagesDiscretas/res6.png")


error = pygame.image.load("ImagesDiscretas/x.png")

nclear = pygame.image.load("ImagesDiscretas/npas.png")

#Programa
main_menu() #corre menu principal
