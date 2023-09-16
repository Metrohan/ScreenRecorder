import pyautogui
import cv2
import numpy as np
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import recorderUI


class recording(QtWidgets.QMainWindow, recorderUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()

        self.initVideoWriter()

        self.initSettings()

        self.comboBox.currentIndexChanged.connect(self.updateSettings)
        self.comboBox_2.currentIndexChanged.connect(self.updateSettings)
        self.comboBox_3.currentIndexChanged.connect(self.updateSettings)
        self.comboBox_4.currentIndexChanged.connect(self.updateSettings)
        self.lineEdit.textChanged.connect(self.updateSettings)

        self.pushButton.pressed.connect(self.monitorScreen)

    def initSettings(self):

        self.comboBox.setCurrentIndex(13)
        self.comboBox_2.setCurrentIndex(6)
        self.comboBox_3.setCurrentIndex(1)
        self.comboBox_4.setCurrentIndex(1)

    def initVideoWriter(self):
        prefRes = self.comboBox.currentText()  # preferred resolution
        width, height = map(int, prefRes.split('x'))
        prefCodec = self.comboBox_2.currentText()  # preferred codec
        prefFormat = self.comboBox_4.currentText()  # preferred file format
        prefName = self.lineEdit.text()

        resolution = (width, height)
        codec = cv2.VideoWriter_fourcc(*prefCodec)
        filename = f"{prefName}" + prefFormat
        fps = 30.0

        self.out = cv2.VideoWriter(filename, codec, fps, resolution)

    def monitorScreen(self):
        cv2.namedWindow("Monitor", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Monitor", 480, 270)
        self.recordScreen()

    def recordScreen(self):
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            cv2.imshow('Monitor', frame)
            if cv2.waitKey(1) == ord('p'):
                self.stopRecording()
                break

    def stopRecording(self):
        self.out.release()
        cv2.destroyAllWindows()

    def updateSettings(self):
        new_name = self.lineEdit.text()
        if new_name != self.prefName:
            self.stopRecording()
            self.initVideoWriter()
            self.prefName = new_name


def main():
    app = QApplication(sys.argv)
    main_widget = recording()
    main_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
