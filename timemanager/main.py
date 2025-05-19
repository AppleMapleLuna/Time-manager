from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPalette, QColor, QPixmap
import sys
import random
import os

import animatedButton as AB

os.chdir(os.path.dirname(__file__))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Window settings
        self.setWindowTitle("Time Manager Game")
        self.showMaximized()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # temp button
        button = AB.AnimatedButton("Click Me", self)
        button.clicked.connect(self.on_click)

        # Button to start timer
        buttonT = AB.AnimatedButton("Start Timer", self)
        buttonT.clicked.connect(self.start_timer)

        # Create an exit button
        exit_button = AB.AnimatedButton("Exit", self)
        exit_button.clicked.connect(self.close)  # Close the window

        # Image
        self.label = QLabel()
        self.pixmap_active = QPixmap("./img/holy crackers.jpg")  # Active image
        self.pixmap_sleeping = QPixmap("./img/holy crackers eepy.jpg")  # Sleeping image
        self.label.setPixmap(self.pixmap_active)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(exit_button, alignment=Qt.AlignTop | Qt.AlignLeft)  # Exit at top-left
        layout.addWidget(button, alignment=Qt.AlignBottom | Qt.AlignLeft)  # Main button at bottom-left
        layout.addWidget(buttonT, alignment=Qt.AlignBottom | Qt.AlignLeft)  # Timer button next to it
        layout.addWidget(self.label, alignment=Qt.AlignBottom | Qt.AlignRight)  # Character remains in corner

        self.setLayout(layout)

        # Set window palette to allow transparency
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0, 0))  # Transparent background
        self.setPalette(palette)

        # Timer setup
        self.timer = QTimer()
        self.timer.setInterval(5000)  # 5000ms = 5 seconds
        self.timer.timeout.connect(self.change_image)

    def start_timer(self):
        print("Timer started!")
        self.timer.start()
        self.label.setPixmap(self.pixmap_active)

    def change_image(self):
        print("Time's up! Changing image.")
        self.label.setPixmap(self.pixmap_sleeping)
        self.timer.stop()  # Stop timer after changing image

    def on_click(self):
        n = random.randint(0,5)
        if n==0:
            print("Meow.")
        else:
            print("Button clicked!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
