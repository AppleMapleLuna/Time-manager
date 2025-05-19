from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPropertyAnimation, QRect

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                font-family: 'Segoe UI';
                background-color: white;
                font-size: 20px;
                padding: 10px;
                border: 2px double black;
                border-radius: 5px;
            }
            
            QPushButton:hover {
                background-color: black;
                color: white;
                border: 2px double white;
            }
        """)

    def enterEvent(self, event):
        """Triggers when the mouse enters the button"""
        self.animate_size(expand=True)
        super().enterEvent(event)

    def leaveEvent(self, event):
        """Triggers when the mouse leaves the button"""
        self.animate_size(expand=False)
        super().leaveEvent(event)

    def animate_size(self, expand):
        """Animates button size change"""
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(500)  # 500ms transition

        if expand:
            new_rect = self.geometry().adjusted(-5, -5, 5, 5)  # Expand slightly
        else:
            new_rect = self.geometry().adjusted(5, 5, -5, -5)  # Shrink back

        animation.setStartValue(self.geometry())
        animation.setEndValue(new_rect)
        animation.start()
