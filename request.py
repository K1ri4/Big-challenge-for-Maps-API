from library import sys, requests


def request(coords='37.617778,55.755833', zoom='20', mode='map'):  # функция запроса карты
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&spn={zoom},{zoom}&l={mode}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
