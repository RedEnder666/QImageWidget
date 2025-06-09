# QImageWidget Documentation
QImageWidget is a Python library that provides a widget for displaying images in a PyQt5 GUI. The library allows you to easily load images and scale them to fit the widget.

<br />
<br />


# Installation
You can install QImageWidget by cloning the GitHub repository:
```bash
git clone https://github.com/RedEnder666/QImageWidget
```
<br />

# Methods
|Method|Arguments|Description|
|---|---|---|
|__init__(self, parent, img='')|parent: QWidget, img: str|Initializes a new QImageWidget object with an optional image.|
|setImage(self, img)|img: str|Sets the image for the QImageWidget.|
|setScale(self, size, aspectRatioMode=Qt.IgnoreAspectRatio)|size: tuple, aspectRatioMode: Qt.AspectRatioMode|Scales the image to the specified size with the specified aspect ratio mode.|

<br />
# Usage
Here is an example of how to use QImageWidget:

```py
import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from QImageWidget.QImageWidget import QImageWidget

class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QImageWidget object
        self.imageWidget = QImageWidget(self)

        # Set the image
        self.imageWidget.setImage('example.jpg')

        # Set the scaling
        self.imageWidget.setScale((400, 400), Qt.KeepAspectRatio)

        # Create a button to update the image
        self.btnUpdate = QPushButton('Update', self)
        self.btnUpdate.clicked.connect(self.updateImage)

        # Create a vertical layout and add the widgets to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.imageWidget)
        layout.addWidget(self.btnUpdate)

    def updateImage(self):
        # Update the image
        self.imageWidget.setImage('example2.jpg')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create an ImageWidget object
    widget = ImageWidget()
    widget.show()

    sys.exit(app.exec_())
```
This example creates a QImageWidget object, sets an image, sets scaling, and adds the widget to a vertical layout along with a button to update the image. When the button is clicked, the updateImage method is called, which changes the image to a different one. The code also creates a QApplication object and displays the widget on the screen.
