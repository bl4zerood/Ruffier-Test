from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setObjectName("title")
        self.instructions = QLabel(txt_instruction)
        self.instructions.setObjectName("instructions")
        self.instructions.setWordWrap(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instructions, alignment=Qt.AlignLeft)
        self.layout.addSpacing(12)
        self.layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.layout.setContentsMargins(40, 30, 40, 30)
        self.layout.setSpacing(10)

        # small visual tweaks
        self.hello_text.setFont(QFont("Segoe UI", 20, QFont.Bold))
        self.instructions.setFont(QFont("Segoe UI", 11))
        self.btn_next.setCursor(Qt.PointingHandCursor)
        self.btn_next.setFixedWidth(180)

        self.setLayout(self.layout)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
# global stylesheet for a cleaner modern look
app.setStyleSheet('''
QWidget { background: #f7f9fc; font-family: "Segoe UI", Arial; color: #222; }
QLabel#title { font-size: 20pt; color: #0b3d91; }
QLabel#instructions { font-size: 10pt; color: #333; }
QPushButton { background-color: #2e86de; color: white; border-radius: 6px; padding: 8px 12px; }
QPushButton:hover { background-color: #2874c5; }
''')
mw = MainWin()
app.exec_()