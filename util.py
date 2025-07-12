from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class IconButton(QPushButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon(icon_path))  # Set the icon
        self.setIconSize(QSize(35, 35))  # Adjust the icon size
        self.setStyleSheet("""
        QPushButton {
            background: rgba(255, 255, 255, 45);
            border-radius: 12px;
            border: none;
            padding: 10px;
            margin: 10px;
        }
        QPushButton:hover {
            background: rgba(255, 255, 255, 85);
            border-radius: 12px;
        }
        QPushButton:pressed {
            background-color: #81A1C1;
        }
        """)