import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

running = True

clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 72)

_text_library = dict()

def get_text(font, message, color):
    global _text_library
    text_info = (font, message, color)
    text = _text_library.get(text_info)
    if text is None:
        # os.sep is the path separator for the current OS ('/' on mac/linux, '\' on windows)
        text = font.render(message, True, color)
        _text_library[text_info] = text
    return text

text = get_text(font, "Hello KBTU", blue)

x = WIDTH // 2 - text.get_width() // 2
y = HEIGHT // 2 - text.get_height() // 2

step = 3

stepX = step
stepY = step

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    # cnt = 10000
    # while cnt > 0:
    #     text = get_text(font, "Hello KBTU", blue)
    #     # compare the performance with this:
    #     # text = font.render("Hello KBTU", True, blue)
    #     cnt -= 1

    if keys[pygame.K_RIGHT]: 
        x += 1
    if keys[pygame.K_LEFT]: 
        x -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_UP]:
        y -= 1
        
    x += stepX
    y += stepY

    # checking for collisions with the borders of the window

    # top (y == 0)
    if y <= 0:
        y = 0
        stepY *= -1

    # bottom (y == HEIGHT-1)
    if y + text.get_height() >= HEIGHT-1:
        y = HEIGHT-1 - text.get_height()
        stepY *= -1

    # left (x == 0)
    if x <= 0:
        x = 0
        stepX *= -1

    # right (x == WIDTH-1)
    if x + text.get_width() >= WIDTH-1:
        x = WIDTH-1 - text.get_width()
        stepX *= -1


    screen.fill(black)

    screen.blit(text, (x, y))
    
    pygame.display.flip()
    clock.tick(60)