import requests
import sys


class MapParams(object):
    def __init__(self, lat, lon, zoom, map_type):
        self.lat = lat
        self.lon = lon
        self.zoom = zoom
        self.type = map_type

    def ll(self):
        return str(self.lon) + "," + str(self.lat)

    def load_map(self):
        map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=self.ll(), z=self.zoom, type=self.type)
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        map_file = "map.png"
        try:
            with open(map_file, "wb") as file:
                file.write(response.content)
        except IOError as ex:
            print("Ошибка записи временного файла:", ex)
            sys.exit(2)

        return map_file


lat = 61.665279
lon = 50.813492
zoom = 16
map_type = "map"

params = MapParams(lat, lon, zoom, map_type)
map_image = params.load_map()