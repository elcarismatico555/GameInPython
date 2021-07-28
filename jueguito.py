import pygame,sys
from constantes import BLACK,BLUE, WHITE,YELLOW
pygame.init()

#  Titulo ventana
pygame.display.set_caption("B-Darlux")


size = (800,478)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

#  carga imagen y escalado
background = pygame.image.load("galaxy.jpg").convert()
ship = pygame.image.load("ship.png")
ship = pygame.transform.scale(ship,(50,50))

#  coordenadas y speed nave
ship_cordX = 400
ship_cordY = 300
ship_speedX = 0
ship_speedY = 0

#  disparo coordenadas y speed
shoot_cordX = 0
shoot_cordY = 0
shoot_speedY = 0

#  activar disparo y reiniciarlo
shoot = 0

contador_fps = 0
fps = 90

#  Fuentes
fuente1 = pygame.font.SysFont("Bauhaus 93",30)
fuente2 = pygame.font.SysFont("Arial",14)

#  objeto texto
Nombre = fuente1.render("B-Darlux",True,WHITE)

#  Escenas
menu_inicio = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.WINDOWFOCUSGAINED:
            foco = True
        if event.type == pygame.WINDOWFOCUSLOST:
            foco = False
        if pygame.key.get_focused() == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    fps -= 1
                if event.key == pygame.K_2:
                    fps += 1
                if event.key == pygame.K_w:
                    ship_speedY += -0.3
                if event.key == pygame.K_s:
                    ship_speedY += 0.3
                if event.key == pygame.K_a:
                    ship_speedX += -0.3
                if event.key == pygame.K_d:
                    ship_speedX += 0.3
                if event.key == pygame.K_m:
                    shoot = 1
                    shoot_speedY = -0.4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    ship_speedY = 0
                if event.key == pygame.K_s:
                    ship_speedY = 0
                if event.key == pygame.K_a:
                    ship_speedX = 0
                if event.key == pygame.K_d:
                    ship_speedX = 0

    #  mostrar tiempo
    cronometro = pygame.time.get_ticks()
    cronometro /= 1000
    show_cronometro = fuente2.render("cronometro"+str(cronometro),True,WHITE)

    #  tiempo entre frames
    deltaTime = clock.tick_busy_loop(fps)
    show_deltaTime = fuente2.render("deltaTime "+str(deltaTime),True,WHITE)

    #  mostrar FPS
    contador_fps = int(clock.get_fps())
    mostrar_fps = fuente2.render("FPS "+str(contador_fps),True,WHITE)

    #  dibujar ventana y fondo
    screen.fill(BLACK)
    screen.blit(background, (0,0))

    #  dibujar texto
    screen.blit(Nombre,(10,10))

    #  dibujar contador fps
    screen.blit(mostrar_fps,(710,20))

    #  dibujar deltatime
    screen.blit(show_deltaTime,(710,35))
    #  dibujar cronometro
    screen.blit(show_cronometro,(710,50))

    #  Movimiento nave
    ship_cordX += ship_speedX*deltaTime
    ship_cordY += ship_speedY*deltaTime

    #  Control de disparo
    if shoot == 1:
        shoot_cordX = shoot_cordX
        if shoot_cordY > -5:
            shoot_cordY += shoot_speedY*deltaTime
            pygame.draw.circle(screen,YELLOW,(shoot_cordX,shoot_cordY),5,0)
        if shoot_cordY <= 0:
            shoot = 0
    else:
        #  movimiento shoot
        shoot_cordY = ship_cordY
        shoot_cordX = ship_cordX + 25

    #  dibujar nave
    screen.blit(ship,(ship_cordX,ship_cordY))

    pygame.display.flip()
