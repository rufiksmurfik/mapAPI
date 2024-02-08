# -*- coding: utf-8 -*-
import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from UI.UI_map import Ui_MainWindow
from PyQt5.QtCore import Qt


lat = 61.665279
lon = 50.813492
zoom = 16
map_type = "map"


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


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        pixmap = QPixmap('map.png')
        self.map_QT.setPixmap(pixmap)

    def keyPressEvent(self, event):
        global zoom
        if event.key() == Qt.Key_PageUp:
            if zoom < 21:
                zoom += 1
            print(zoom)
            params = MapParams(lat, lon, zoom, map_type)
            map_image = params.load_map()
            pixmap = QPixmap(map_image)
            self.map_QT.setPixmap(pixmap)
        if event.key() == Qt.Key_PageDown:
            if zoom > 0:
                zoom -= 1
            print(zoom)
            params = MapParams(lat, lon, zoom, map_type)
            map_image = params.load_map()
            pixmap = QPixmap(map_image)
            self.map_QT.setPixmap(pixmap)


if __name__ == "__main__":
    params = MapParams(lat, lon, zoom, map_type)
    map_image = params.load_map()

    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
