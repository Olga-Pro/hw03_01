import pygame
import random

# инициализация pygame
pygame.init()

# размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# название экрана
pygame.display.set_caption("Игра ТИР")

# иконка
icon = pygame.image.load("image/logo.png")
pygame.display.set_icon(icon)

# цель - куда стрелять будем
target_image =  pygame.image.load("image/alarm_clock_fotor.png")
# размер изображения
target_width = 50
target_heigth = 50

# случайные координаты для изображения
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_heigth)

# случайный цвет для заливки экрана
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) )

running = True
while running:
    # заливка фона цветом (очистка экрана)
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # координаты клика мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # проврка попадания в объект-мишень
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_heigth:
                # если попали - перемещение объекта
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_heigth)

    # расместить объект на экране
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()
pygame.quit()
