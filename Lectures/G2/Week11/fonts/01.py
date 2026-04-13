import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

running = True

clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 144)

text = font.render("Hello KBTU", True, blue)

x = 400 - text.get_width() // 2
y = 300 - text.get_height() // 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]: 
        x += 1
    if keys[pygame.K_LEFT]: 
        x -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_UP]:
        y -= 1
        
    screen.fill(black)

    screen.blit(text, (x, y))
    
    pygame.display.flip()
    clock.tick(60)