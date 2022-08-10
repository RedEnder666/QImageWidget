from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QSize, Qt


class QImageWidget(QLabel):
    
    def setImage(self, img):
        image = QPixmap(img)
        if img:
            self.pixmap = QPixmap(img)
            self.setPixmap(self.pixmap)
            self.resize(QSize(image.size()))
        self.image = img
        self.pixmap = image
        

    def __init__(self, parent, img):
        super().__init__(parent)
        self.setImage(img)

    def setScale(self, size, aspectRatioMode=Qt.IgnoreAspectRatio):
        # Qt.IgnoreAspectRatio, Qt.KeepAspectRatio, Qt.KeepAspectRatioByExpanding
        self.pixmap = self.pixmap.scaled(*size, aspectRatioMode)
        self.setPixmap(self.pixmap)
        self.resize(QSize(*size))


