import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

tools = ('rectangle', 'rhombus')

selected_tool = tools[0]

currX = 0
currY = 0

prevX = 0
prevY = 0

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_rhombus(x1, y1, x2, y2):
    width  = abs(x1 - x2)
    height = abs(y1 - y2)
    left_x = min(x1, x2)
    top_y  = min(y1, y2)

    top_point    = (left_x + width // 2, top_y)
    rigth_point  = (left_x + width, top_y + height // 2)
    bottom_point = (left_x + width // 2, top_y + height)
    left_point   = (left_x, top_y + height // 2)

    return (top_point, rigth_point, bottom_point, left_point)

def draw_figure(surface, color, points):
    prevX, prevY, currX, currY = points # points is a tuple
    if selected_tool == 'rectangle':
        pygame.draw.rect(screen, colorRED, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
    elif selected_tool == 'rhombus':
        pygame.draw.polygon(screen, colorRED, calculate_rhombus(prevX, prevY, currX, currY), THICKNESS)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            screen.blit(base_layer, (0, 0))
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                draw_figure(screen, colorRED, (prevX, prevY, currX, currY))

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            draw_figure(screen, colorRED, (prevX, prevY, currX, currY))
            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
            if event.key == pygame.K_r and event.mod and pygame.KMOD_LSHIFT:
                selected_tool = 'rectangle'
            if event.key == pygame.K_r and event.mod and pygame.KMOD_LCTRL:
                selected_tool = 'rhombus'

    pygame.display.flip()
    clock.tick(60)