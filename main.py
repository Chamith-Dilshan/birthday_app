import sys
import os
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QScrollArea, QGraphicsOpacityEffect, QSpacerItem, QSizePolicy, QHBoxLayout,
    QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsTextItem
)
from PySide6.QtGui import (
    QIcon, QFont, QPixmap, QTransform, QPainter, QBrush, QPen, QColor, QPainter
)
from PySide6.QtCore import Qt, QTimer, QPoint, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Julien.exe")
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setStyleSheet("background-color: black;")
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(BirthdayLogin(self))

    def show_scroll_view(self):
        self.setCentralWidget(ScrollPageWidget(self))

    def show_final_message(self):
        self.setCentralWidget(FinalMessagePage(self))


class BirthdayLogin(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet("background-color: black;")
        self.init_ui()

    def init_ui(self):
        font = QFont("Courier New", 12)
        font.setBold(True)

        self.title = QLabel("Access To Julien.exe")
        self.title.setStyleSheet("color: #00FF90;")
        self.title.setFont(QFont("Courier New", 16))
        self.title.setAlignment(Qt.AlignCenter)

        self.username_label = QLabel("Agent:")
        self.username_label.setStyleSheet("color: #00590B;")
        self.username_label.setFont(font)

        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("color: white; background-color: #003300; border: 1px solid #00590B;")

        self.password_label = QLabel("Secret Code:")
        self.password_label.setStyleSheet("color: #00590B;")
        self.password_label.setFont(font)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("color: white; background-color: #003300; border: 1px solid #00590B;")

        self.login_button = QPushButton("ENGAGE")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #00590B;
                color: white;
                padding: 8px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #00FF90;
                color: black;
            }
        """)
        self.login_button.clicked.connect(self.verify_login)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def verify_login(self):
        if self.username_input.text() and self.password_input.text() == "0099":
            self.main_window.show_scroll_view()


class ScrollPageWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet("background-color: #121212;")
        self.init_ui()

    def init_ui(self):
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        container = QWidget()
        container.setStyleSheet("background-color: #121212;")
        container_layout = QVBoxLayout()
        container_layout.setContentsMargins(20, 20, 20, 40)
        container_layout.setSpacing(40)

        # Add retro camera header
        if os.path.exists("assets/retro_camera.png"):
            camera_label = QLabel()
            camera_pixmap = QPixmap("assets/retro_camera.png")
            camera_label.setPixmap(camera_pixmap.scaledToWidth(250, Qt.SmoothTransformation))
            camera_label.setAlignment(Qt.AlignCenter)
            container_layout.addWidget(camera_label)

        # Add photo frames
        self.image_paths = [f"assets/img{i}.png" for i in range(1, 6) if os.path.exists(f"assets/img{i}.png")]
        for path in self.image_paths:
            frame = self.create_photo_frame(path)
            container_layout.addWidget(frame)

        # Add celebration button
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
        self.button.clicked.connect(self.start_celebration)
        container_layout.addWidget(self.button, alignment=Qt.AlignCenter)

        container.setLayout(container_layout)
        self.scroll.setWidget(container)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll)
        self.setLayout(main_layout)

    def create_photo_frame(self, image_path):
        # Create a container widget
        container = QWidget()
        container.setStyleSheet("background: transparent;")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(50, 20, 50, 20)
    
        # Create graphics view
        graphics_view = QGraphicsView()
        graphics_view.setStyleSheet("background: transparent; border: none;")
        graphics_view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
        # Create scene
        scene = QGraphicsScene()
        graphics_view.setScene(scene)
    
        # Create frame item
        frame_item = QGraphicsRectItem(0, 0, 700, 500)
        frame_item.setBrush(QBrush(QColor("#f0f0f0")))
        frame_item.setPen(QPen(QColor("#d8d8d8"), 15))
        scene.addItem(frame_item)
    
        # Create photo item
        pixmap = QPixmap(image_path).scaled(650, 450, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        photo_item = QGraphicsPixmapItem(pixmap)
        photo_item.setPos(25, 25)
        scene.addItem(photo_item)
    
        # Apply rotation
        angle = random.uniform(-1.5, 1.5)
        frame_item.setRotation(angle)
        photo_item.setRotation(angle)
    
        # Add footer text
        footer_text = QGraphicsTextItem("■ 1999-07-20   ✦ ★ ✦")
        footer_text.setDefaultTextColor(QColor("#505050"))
        footer_text.setFont(QFont("Courier New", 12))
        footer_text.setPos(30, 480)
        scene.addItem(footer_text)
    
        # Set scene rect
        scene.setSceneRect(scene.itemsBoundingRect())
    
        layout.addWidget(graphics_view)
        return container

    def start_celebration(self):
        self.spawn_count = 0
        self.popup_total = 40
        self.popup_windows = []
        self.spawn_timer = QTimer()
        self.spawn_timer.timeout.connect(self.spawn_one_popup)
        self.spawn_timer.start(100)

    # Rest of the celebration popup methods remain the same...

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
        label.setGeometry(QRect(0, 30, 200, 50))

    def closeEvent(self, event):
        self.controller.close_all_popups()


class FinalMessagePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: black;")
        layout = QVBoxLayout()
        self.label = QLabel("Julien, the world’s been hacked with joy because of you.")
        self.label.setStyleSheet("color: #00FF90; font-size: 24px;")
        self.label.setFont(QFont("Courier New", 16))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())