# En este programa vamos a realizar el juego clasico de la bola rebotando en una pantalla y rebotando en un bate, usando la tematica del juego Metal Slug.

# Importamos e iniciamos pygame.
import pygame
pygame.init()

# Definimos el tamaño del background.

ventana = pygame.display.set_mode((640,480))
bg = pygame.image.load("cascadas.png")
bg = pygame.transform.scale(bg,(640,480))

#Ponemos titulo al background
pygame.display.set_caption("Metal Slug Minigame")


# Creamos la bola y la tratamos como un cuadrado
bola = pygame.image.load("lasergun.png")
bolacuadrada = bola.get_rect()


# Asignamos velocidad y posicion inicial a la bola
speed = [4,4]
bolacuadrada.move_ip(0,0)


# Creamos el bate y lo tratamos como un simple rectángulo
bate = pygame.image.load("platform.png")
baterectangular = bate.get_rect()


# Asignamos la posicion inicial del bate
baterectangular.move_ip(240,420)


# Establecemos el juego por frames, y definimos las interacciones entre la bola y el bate. Asignamos teclas de movimiento horizontal al bate.

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterectangular = baterectangular.move(-5,0)
    if keys[pygame.K_RIGHT]:
        baterectangular = baterectangular.move(5,0)
    # Compruebo si hay colisión
    if baterectangular.colliderect(bolacuadrada):
        speed[1] = -speed[1]
    bolacuadrada = bolacuadrada.move(speed)
    if bolacuadrada.left < 0 or bolacuadrada.right > ventana.get_width():
        speed[0] = -speed[0]
    if bolacuadrada.top < 0 or bolacuadrada.bottom > ventana.get_height():
        speed[1] = -speed[1]
    ventana.fill((200, 203, 230))
    ventana.blit(bg,(0,0))
    ventana.blit(bola, bolacuadrada)
    # Dibujo el bate
    ventana.blit(bate, baterectangular)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
