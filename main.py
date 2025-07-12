import sys
from PyQt5.QtWidgets import QApplication
from timer import Timer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Timer()
    window.show()
    sys.exit(app.exec_())