import sys
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.dr = False
        self.signal = -1
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

    def mousePressEvent(self, event):
        self.x, self.y = event.x(), event.y()
        if event.button() == Qt.LeftButton:
            self.signal = 0
        elif event.button() == Qt.RightButton:
            self.signal = 1
        self.dr = True
        self.repaint()
        self.dr = False

    def mouseMoveEvent(self, event):
        self.x, self.y = event.x(), event.y()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.signal = 2
            self.dr = True
            self.repaint()
        self.dr = False

    def paintEvent(self, event):
        if not self.dr:
            return
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        size = randint(10, 50)
        qp.drawEllipse(self.x - size // 2, self.y - size // 2, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
