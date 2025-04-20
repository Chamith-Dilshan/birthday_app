
import os
from PySide6.QtWidgets import (
     QWidget, QLabel, QVBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


# ---------- CameraWidget ----------
class CameraWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel()
        if os.path.exists("assets/retro_camera.png"):
            pixmap = QPixmap("assets/retro_camera.png").scaledToWidth(400, Qt.SmoothTransformation)
            self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)