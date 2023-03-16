# QImageWidget
 PyQt widget containing images
 ____
Adding image into pyqt5 ui is very boring, noone likes it, so i made this easy to use class!




# Usage example 

```py
# Imports (including QImageWidget importing)

if __name__ != '__main__':
    sys.exit()
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 500)

        self.imagewid = QImageWidget(self, 'somepicture.png') 
        # Creating a QImageWidget object containing a 'somepicture.png' picture
        
        # You can use absolute path if you want to

        self.imagewid.setScale((100, 50), Qt.IgnoreAspectRatio) 
        # Setting widget a new size with aspectRatioMode parameter
        # You can also use Qt.IgnoreAspectRatio, Qt.KeepAspectRatio and Qt.KeepAspectRatioByExpanding

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit()
```
\
\
This is how it looks like(you need to create your own 'somepicture.png' file in example folder) \
\
![image](https://user-images.githubusercontent.com/74973491/184006901-22b00414-9549-4ac1-83f4-5fec2d79786b.png)
\
\
\
\
Also chatGPT made this example:
```py
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QVBoxLayout, QWidget
from QImageWidget.QImageWidget import QImageWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QImageWidget Example")

        self.image_widget = QImageWidget(self)
        self.setCentralWidget(self.image_widget)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        open_image_action = QAction("Open image", self)
        open_image_action.triggered.connect(self.open_image)
        file_menu.addAction(open_image_action)

        self.setGeometry(100, 100, 640, 480)
        self.show()

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self
```
