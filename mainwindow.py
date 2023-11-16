# This Python file uses the following encoding: utf-8
# mainwindow.py
import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.PlayButton.setText("Start")

        # Connect button signals to slots
        self.ui.PlayButton.clicked.connect(self.toggleScrolling)
        self.ui.fontComboBox.currentFontChanged.connect(self.changeFont)
        self.ui.fontSize.valueChanged.connect(self.changeFontSize)

        # Initialize scrolling state
        self.isScrolling = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.scrollText)

    def toggleScrolling(self):
        if not self.isScrolling:
            self.startScrolling()
        else:
            self.stopScrolling()

    def startScrolling(self):
        self.isScrolling = True
        self.ui.PlayButton.setText("Stop")
        self.timer.start(50)  # Adjust the scroll speed here (in milliseconds)

    def stopScrolling(self):
        self.isScrolling = False
        self.ui.PlayButton.setText("Start")
        self.timer.stop()

    def scrollText(self):
        # Scroll the text in the text area
        scroll_bar = self.ui.textEdit.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.value() + 1)

    def changeFont(self, font):
        # Change the font of the text in the text area
        self.ui.textEdit.setFont(font)

    def changeFontSize(self, size):
        # Change the font size of the text in the text area
        font = self.ui.textEdit.font()
        font.setPointSize(size)
        self.ui.textEdit.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
