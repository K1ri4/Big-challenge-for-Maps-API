from library import os
from settings import *
from request import request


zoom = float(input('Введите масштаб карты: '))  # запрос масштаба
while zoom > 90:  # верхняя граница 90
    zoom = float(input('Введите масштаб карты: '))
request(zoom=zoom)

while True:  # основной цикл программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.remove(name_map)  # удаление файла после завершения работы
            pygame.quit()
            break
    screen.blit(pygame.image.load(name_map), (0, 0))  # отображение карты
    pygame.display.flip()
    clock.tick(fps)
