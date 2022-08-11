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
