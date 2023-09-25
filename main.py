import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *

import recorderUI
import recording
from tray import systemTray


class RecordingGUI(QMainWindow, recorderUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.setFixedSize(475, 400)

        self.recording = recording.Recording(self)

        self.comboBox.currentIndexChanged.connect(self.recording.initVideoWriter)
        self.lineEdit.textEdited.connect(self.recording.initVideoWriter)

        self.pushButton.setStyleSheet("background-color :#424242; border-radius : 50; border: 5px solid red; ")
        self.pushButton_2.setStyleSheet("background-color :#424242; border-radius : 50; border: 5px solid green; ")
        self.pushButton.pressed.connect(self.recording.startRecording)
        self.pushButton_2.pressed.connect(self.recording.stopRecording)

        self.recording.createFolder()
        self.recording.recordLocation()


def main():
    app = QApplication(sys.argv)
    main_window = RecordingGUI()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
