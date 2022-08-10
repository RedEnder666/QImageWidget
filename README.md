# QImageWidget
 PyQt widget containing images

____

# Usage example

```py
# usage example

if __name__ != '__main__':
    sys.exit()
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 500)
        self.btn = QPushButton(self)
        self.imag = QImageWidget(self, 'madeby.png')
        self.imag.setScale((1600*10, 1000*10))
        self.btn.clicked.connect(self.imag.show)
        self.imag.move(50, 25)
        self.imag.setScale((200, 200), Qt.KeepAspectRatio)
        self.imag.hide()
        self.imag2 = QImageWidget(self, 'with.png')
        self.imag2.move(100, 200)
        self.imag3 = QImageWidget(self, 'me.png')
        self.imag3.move(200, 100)
        self.imag3.setScale((100, 50), Qt.IgnoreAspectRatio)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit()
```