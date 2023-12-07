import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot


def on_click():
    print('I\'ve been clicked')


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    layout = QVBoxLayout()
    label = QLabel(widget)
    button = QPushButton('Click Me')
    button.clicked.connect(on_click)
    layout.addWidget(button)
    layout.addWidget(label)
    widget.setLayout(layout)
    widget.setWindowTitle('Hello World')
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
