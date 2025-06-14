from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QPushButton
from PySide2.QtGui import QPixmap, QImage, QMovie
from PySide2.QtCore import QSize, Qt


class QImageWidget(QLabel):

    def __init__(self, parent, img=''):
        super().__init__(parent)
        self.img = img
        self.setImage(img)

    def setImage(self, img):
        self.img = img
        image = QPixmap(img)
        if img:
            if img.endswith('.gif'):
                self.movie = QMovie(img)
                self.setMovie(self.movie)
                self.movie.start()
                self.resize(QSize(image.size()))
            else:
                self.pixmap = QPixmap(img)
                self.setPixmap(self.pixmap)
                self.resize(QSize(image.size()))
        self.image = img

    def setScale(self, size, aspectRatioMode=Qt.IgnoreAspectRatio):
        # Qt.IgnoreAspectRatio, Qt.KeepAspectRatio, Qt.KeepAspectRatioByExpanding
        self.setImage(self.img)
        if self.img.endswith('.gif'):
            self.movie.setScaledSize(QSize(*size))
            self.resize(QSize(*size))
        else:
            self.pixmap = self.pixmap.scaled(*size, aspectRatioMode)
            self.setPixmap(self.pixmap)
            self.resize(QSize(*size))
