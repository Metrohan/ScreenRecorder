import pyautogui
import cv2
import numpy as np
import sys
import os.path

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import recorderUI


class recordingGUI(QtWidgets.QMainWindow, recorderUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()

        self.initVideoWriter()
        self.createFolder()
        self.recordLocation()

        self.comboBox.currentIndexChanged.connect(self.initVideoWriter)
        self.lineEdit.textEdited.connect(self.initVideoWriter)

        self.pushButton.setStyleSheet("background-color :#424242; border-radius : 50; border: 5px solid green; ")
        self.pushButton_2.setStyleSheet("background-color :#424242; border-radius : 50; border: 5px solid red; ")
        self.pushButton.pressed.connect(self.monitorScreen)
        self.pushButton_2.pressed.connect(self.stopRecording)

        global onLive
        onLive = 0

    def createFolder(self):
        record_folder = os.path.expanduser("~\\Documents\\ScreenRecorder")
        if not os.path.exists(record_folder):
            os.mkdir(record_folder)

    def recordLocation(self):
        self.record_folder = os.path.expanduser("~\\Documents\\ScreenRecorder")
        path = os.path.join(self.record_folder)
        os.chdir(path)

    def initVideoWriter(self):
        prefRes = self.comboBox.currentText()  # preferred resolution
        self.width, self.height = map(int, prefRes.split('x'))
        self.prefName = self.lineEdit.text()

    def monitorScreen(self):
        cv2.namedWindow("Monitor", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Monitor", 480, 270)
        self.recordScreen()

    def recordScreen(self):
        self.onLive = 1
        self.pushButton.hide()
        self.pushButton_2.show()
        resolution = (self.width, self.height)
        codec = cv2.VideoWriter_fourcc(*'mp4v')
        filename = f"{self.prefName}" + '.mp4'
        fps = 30.0

        self.out = cv2.VideoWriter(filename, codec, fps, resolution)
        while self.onLive == 1:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            cv2.imshow('Monitor', frame)
            if cv2.waitKey(1) == ord('p'):
                self.onLive = 0
                self.stopRecording()
                break

    def stopRecording(self):
        self.out.release()
        cv2.destroyAllWindows()
        self.pushButton.show()
        self.pushButton_2.hide()


def main():
    app = QApplication(sys.argv)
    main_widget = recordingGUI()
    main_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
