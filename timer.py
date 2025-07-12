from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt, QUrl
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtMultimedia import QSoundEffect
import os
import sys
from util import IconButton
from constants import TIMER_DURATION, ZONE_IN, NEARLY_THERE, RECAP, BREAK

def resource_path(relative_path):
    """Get the absolute path to a resource, whether running as a script or bundled with PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lock In Timer")
        self.setGeometry(300, 300, 400, 400)

        font_path = resource_path("resources/Roboto-Thin.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            font_family = font_families[0]
        else:
            raise RuntimeError(f"Failed to load font: {font_path}")
        self.font_family = font_family

        # Styling and layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.setStyleSheet(f"font-family: '{font_family}'; color: black; background-color: #9dc8e3")

        # Timer display
        self.timer_label = QLabel("60:00", self)
        self.set_timer_label_style()
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.timer_label)

        # Comment
        self.text_label = QLabel("You got this!", self)
        self.set_text_label_style()
        self.text_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.text_label)

        self.button_layout = QHBoxLayout()

        # Start, Pause, and Reset buttons
        self.start_button = IconButton(resource_path("resources/play.svg"))
        self.start_button.clicked.connect(self.start_timer)
        self.button_layout.addWidget(self.start_button)

        self.pause_button = IconButton(resource_path("resources/pause.svg"))
        self.pause_button.clicked.connect(self.pause_timer)
        self.button_layout.addWidget(self.pause_button)

        self.reset_button = IconButton(resource_path("resources/reset.svg"))
        self.reset_button.clicked.connect(self.reset_timer)
        self.button_layout.addWidget(self.reset_button)

        self.main_layout.addLayout(self.button_layout)

        # Timer variables
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.remaining_seconds = TIMER_DURATION
        self.running = False

        # Sound effects (zone-in, nearly-there, end)
        self.sounds = {
            'zone_in': 'zone_in.wav',
            'nearly_there': 'nearly_there.wav',
            'end': 'end.wav',
            'breaks_over': 'breaks_over.wav'
        }

        for key, file_name in self.sounds.items():
            sound_effect = QSoundEffect(self)
            sound_effect.setSource(QUrl.fromLocalFile(resource_path(f"resources/{file_name}")))
            self.sounds[key] = sound_effect


    def start_timer(self):
        self.set_text_label_style()
        self.set_timer_label_style()
        self.text_label.setText("Overview and Refresh")
        self.setStyleSheet("background-color: #9de3a4") #green
        if not self.running:
            self.running = True
            self.timer.start(1000)

    def pause_timer(self):
        self.running = False
        self.timer.stop()

    def reset_timer(self):
        self.running = False
        self.timer.stop()
        self.remaining_seconds = TIMER_DURATION
        self.text_label.setText("You got this!")
        self.set_text_label_style()
        self.set_timer_label_style()
        self.setStyleSheet("background-color: #9dc8e3") #blue
        self.update_display()

    def update_timer(self):
        if self.remaining_seconds > 0:
            if self.remaining_seconds == ZONE_IN:
                self.sounds['zone_in'].play()
                self.text_label.setText("Zone in")
                self.set_text_label_style()
                self.set_timer_label_style()
                self.setStyleSheet("background-color: #9dc8e3") #blue
            if self.remaining_seconds == NEARLY_THERE:
                self.sounds['nearly_there'].play()
                self.set_text_label_style()
                self.set_timer_label_style()
                self.text_label.setText("Nearly there")
            if self.remaining_seconds == RECAP:
                self.sounds['end'].play()
                self.set_text_label_style()
                self.set_timer_label_style()
                self.text_label.setText("Recap")
                self.setStyleSheet("background-color: #9de3a4") #green
            if self.remaining_seconds == BREAK:
                self.sounds['end'].play() 
                self.set_text_label_style()
                self.set_timer_label_style()
                self.text_label.setText("Take a walk")
                self.setStyleSheet("background-color: #f291bf") #pink
            self.remaining_seconds -= 1
            self.update_display()
        else:
            self.timer.stop()
            self.running = False
            self.sounds['breaks_over'].play() 
            self.set_text_label_style()
            self.set_timer_label_style()
            self.text_label.setText("Well deserved break")
            self.setStyleSheet("background-color: #9dc8e3") #blue

    def update_display(self):
        minutes, seconds = divmod(self.remaining_seconds, 60)
        self.set_text_label_style()
        self.set_timer_label_style()
        self.timer_label.setText(f"{minutes:02}:{seconds:02}")

    def set_timer_label_style(self):
        self.timer_label.setStyleSheet(
            f"font-family: '{self.font_family}'; letter-spacing: 3px; font-weight: 200; font-size: 110px; padding: 5px; text-align: center;"
        )

    def set_text_label_style(self):
        self.text_label.setStyleSheet(
            f"font-family: '{self.font_family}'; letter-spacing: 3px; font-weight: 110; font-size: 30px; text-align: center;"
        )
