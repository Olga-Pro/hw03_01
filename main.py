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
target_width = 80
target_heigth = 80
# скорость перемещения
speed = 3
speed_x = speed
speed_y = speed
list_speed = [3, 2, 1, -1, -2, -3]

# набранные очки
ball = 0
# шрифт
font = pygame.font.Font(None, 36)
black = (0, 0, 0)
white = (255, 255, 255)

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
            # проверка попадания в объект-мишень
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_heigth:
                # если попали - подсчет очков
                ball += 1
                # перемещение объекта в новую точку
                target_x = random.randint(0, SCREEN_WIDTH - target_width - speed)
                target_y = random.randint(0, SCREEN_HEIGHT - target_heigth - speed)
                speed_x = random.choice(list_speed)
                speed_y = random.choice(list_speed)

    target_x += speed_x
    target_y += speed_y

    # контроль соблюдения границ экрана
    # при достижении границы - смена позиции объекта
    if (target_x >= SCREEN_WIDTH - target_width or target_x < 0) or (target_y >= SCREEN_HEIGHT - target_heigth or target_y < 0):
        target_x = random.randint(0, SCREEN_WIDTH - target_width - speed)
        target_y = random.randint(0, SCREEN_HEIGHT - target_heigth - speed)
        speed_x = random.choice(list_speed)
        speed_y = random.choice(list_speed)

    ball_txt = font.render(f"Счет: {ball}", True, white)
    # вывести счет игры на экран
    screen.blit(ball_txt, [10, 10])

    # расместить объект-мишень на экране
    screen.blit(target_image, (target_x, target_y))

    pygame.display.update()
    # ограничиваем частоту кадров (FPS)
    pygame.time.Clock().tick(60)
pygame.quit()
