from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl, Slot


@Slot()
def say_hello():
    print("Button clicked, Hello!")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create a button, connect it and show it
    button = QPushButton("Click me")
    button.clicked.connect(say_hello)
    button.show()
    # Run the main Qt loop
    app.exec_()
