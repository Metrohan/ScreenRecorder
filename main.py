import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import filePath
import recorderUI
import recording


class RecordingGUI(QMainWindow, recorderUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.setFixedSize(520, 350)

        self.recording = recording.Recording(self)

        self.comboBox.currentIndexChanged.connect(self.recording.initVideoWriter)
        self.nameEdit.textEdited.connect(self.recording.initVideoWriter)

        self.startButton.setStyleSheet("background-color :#424242; border-radius : 50; border: 5px solid red; ")
        self.stopButton.setStyleSheet("background-color :#424242; border-radius : 50; border: 5px solid green; ")
        self.startButton.pressed.connect(self.recording.countdown)
        self.stopButton.pressed.connect(self.recording.stopRecording)
        self.chooseLoc.pressed.connect(self.recording.choose_file_location)

        self.recording.createFolder()
        self.recording.recordLocation()


def main():
    app = QApplication(sys.argv)
    main_window = RecordingGUI()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
