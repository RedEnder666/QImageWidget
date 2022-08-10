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

![image](https://user-images.githubusercontent.com/74973491/184006775-2ba66604-f0f8-436e-88b1-6d8179eedc2d.png)
