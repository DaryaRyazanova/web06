import os
import sys

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from api_yandex_map import getImage


SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.response = getImage('37.530887,55.703118', '0.002,0.002', 'map')
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, SCREEN_SIZE[0], SCREEN_SIZE[1] + 120)
        self.setWindowTitle('Отображение карты')

        ## Изображение
        self.label1 = QLabel(self)
        self.label1.move(10, 10)
        self.label1.setText('Широта')
        self.label2 = QLabel(self)
        self.label2.move(10, 50)
        self.label2.setText('Долгота')
        self.label3 = QLabel(self)
        self.label3.move(10, 90)
        self.label3.setText('Маштаб')
        self.line1 = QLineEdit(self)
        self.line1.move(100, 10)
        self.line1.setText('37.530887')
        self.line2 = QLineEdit(self)
        self.line2.move(100, 50)
        self.line2.setText('55.703118')
        self.line3 = QLineEdit(self)
        self.line3.move(100, 90)
        self.line3.setText('0.002')
        self.button = QPushButton(self)
        self.button.move(300, 80)
        self.button.resize(100, 30)
        self.button.clicked.connect(self.ev)
        self.button.setText('Отрисовать')
        self.pixmap = QPixmap.fromImage(QImage.fromData(self.response.content))
        self.image = QLabel(self)
        self.image.move(0, 120)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def ev(self):
        self.response = getImage(','.join([self.line1.text(), self.line2.text()]),
                                 ','.join([self.line3.text(), self.line3.text()]), 'map')
        self.pixmap = QPixmap.fromImage(QImage.fromData(self.response.content))
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageDown:
            self.line3.setText(str(float(self.line3.text()) / 2))
            self.ev()
        elif event.key() == Qt.Key_PageUp:
            if float(self.line3.text()) * 2 <= 1:
                self.line3.setText(str(float(self.line3.text()) * 2))
                self.ev()
        elif event.key() == Qt.Key_Left:
            self.line1.setText(str(float(self.line1.text()) + (float(self.line3.text()) / 2)))
            self.ev()
        elif event.key() == Qt.Key_Right:
            self.line1.setText(str(float(self.line1.text()) - (float(self.line3.text()) / 2)))
            self.ev()
        elif event.key() == Qt.Key_Up:
            self.line2.setText(str(float(self.line2.text()) + (float(self.line3.text()) / 2)))
            self.ev()
        elif event.key() == Qt.Key_Down:
            self.line2.setText(str(float(self.line2.text()) - (float(self.line3.text()) / 2)))
            self.ev()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())