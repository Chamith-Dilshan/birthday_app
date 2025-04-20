import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,QLabel
)
from PySide6.QtGui import (
     QFont
)
from PySide6.QtCore import Qt, QTimer, QPoint

# ---------- ButtonWidget ----------
class ButtonWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        wrapper = QWidget()  # Wrapper is not needed, you can add the layout directly to the ButtonWidget
        
        layout = QVBoxLayout()
        self.button = QPushButton("UNLEASH CELEBRATION")
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #FF00FF;
                color: white;
                font-size: 18px;
                padding: 12px 24px;
                border-radius: 8px;
                font-family: 'Courier New';
                border: 2px solid #00FF90;
            }
            QPushButton:hover {
                background-color: #00FF90;
                color: black;
            }
        """)
        self.button.setFont(QFont("Courier New", 12))
        self.button.clicked.connect(self.start_celebration)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(layout)  # Set the layout of ButtonWidget directly
        
        # Timer for closing popups
        self.close_timer = QTimer(self)
        self.close_timer.timeout.connect(self.close_one_popup)
        
    def start_celebration(self):
        self.spawn_count = 0
        self.popup_total = 40
        self.popup_windows = []
        self.spawn_timer = QTimer(self)
        self.spawn_timer.timeout.connect(self.spawn_one_popup)
        self.spawn_timer.start(100)

    def spawn_one_popup(self):
        if self.spawn_count >= self.popup_total:
            self.spawn_timer.stop()
            return

        screen = QApplication.primaryScreen()
        geo = screen.availableGeometry()

        popup = PopupWindow(self.main_window, self)
        x = random.randint(geo.left(), geo.right() - 200)
        y = random.randint(geo.top(), geo.bottom() - 100)
        popup.move(QPoint(x, y))
        popup.show()
        self.popup_windows.append(popup)
        self.spawn_count += 1

    def close_all_popups(self):
        self.close_timer.start(100)

    def close_one_popup(self):
        if not self.popup_windows:
            self.close_timer.stop()
            self.main_window.show_final_message()
            return
        popup = self.popup_windows.pop()
        popup.close()


class PopupWindow(QWidget):
    def __init__(self, main_window, controller):
        super().__init__()
        self.main_window = main_window
        self.controller = controller
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFixedSize(200, 100)
        self.setStyleSheet("background-color: #000; border: 2px solid #00FF90;")

        label = QLabel("\ud83c\udf89 HAPPY BIRTHDAY JULIEN!", self)
        label.setStyleSheet("color: #FFFF33;")
        label.setFont(QFont("Courier New", 10))
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 30, 200, 50)

    def closeEvent(self, event):
        self.controller.close_all_popups()
        event.accept()  # Ensure the event is properly accepted when closing
