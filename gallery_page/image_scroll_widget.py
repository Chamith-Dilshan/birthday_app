
import os
import random
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout,
    QScrollArea,
    QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsTextItem
)
from PySide6.QtGui import (
    QFont, QPixmap, QPainter, QBrush, QPen, QColor, QPainter
)
from PySide6.QtCore import Qt



# ---------- ImageScrollWidget ----------
class ImageScrollWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        container = QWidget()
        layout = QVBoxLayout()

        for i in range(1, 6):
            path = f"assets/img{i}.png"
            if os.path.exists(path):
                # label = QLabel()
                # pixmap = QPixmap(path).scaledToWidth(500, Qt.SmoothTransformation)
                # label.setPixmap(pixmap)
                # label.setAlignment(Qt.AlignCenter)
                # layout.addWidget(label)
                layout.addWidget(self.create_photo_frame(path))


        container.setLayout(layout)
        self.scroll.setWidget(container)

        main_layout = QVBoxLayout()
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