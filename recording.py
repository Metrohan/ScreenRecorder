import pyautogui
import cv2
import numpy as np
import os.path
import time

from PyQt5.QtCore import QTimer
from tray import systemTray


class Recording:
    def __init__(self, main_window):
        self.main_window = main_window
        self.startTimer = 0
        self.timer = QTimer(self.main_window)
        self.timer.timeout.connect(self.updateTimer)
        self.out = None


    def trayInit(self):
        self.onLive = False
        systemTray(self.onLive)

    def createFolder(self):
        record_folder = os.path.expanduser("~\\Documents\\Records")
        if not os.path.exists(record_folder):
            os.mkdir(record_folder)

    def recordLocation(self):
        self.record_folder = os.path.expanduser("~\\Documents\\Records")
        path = os.path.join(self.record_folder)
        os.chdir(path)

    def initVideoWriter(self):
        prefRes = self.main_window.comboBox.currentText()  # preferred resolution
        self.width, self.height = map(int, prefRes.split('x'))
        self.prefName = self.main_window.lineEdit.text()

    def startRecording(self):
        self.startTimer = 0
        self.onLive = True

        self.main_window.pushButton.hide()
        self.main_window.pushButton_2.show()

        resolution = (self.width, self.height)
        codec = cv2.VideoWriter_fourcc(*'mp4v')
        filename = f"{self.prefName}" + '.mp4'

        self.out = cv2.VideoWriter(filename, codec, 30.0, resolution)
        self.timer.start(1000)
        systemTray(self.onLive)
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
        self.startTimer = 0
        self.onLive = False

        self.main_window.label_2.setText("00:00:00")
        self.timer.stop()
        self.out.release()
        cv2.destroyAllWindows()

        self.main_window.pushButton.show()
        self.main_window.pushButton_2.hide()

        systemTray(self.onLive)

    def updateTimer(self):
        if self.onLive:
            self.startTimer += 1
            self.main_window.label_2.setText(time.strftime("%H:%M:%S", time.gmtime(self.startTimer)))
