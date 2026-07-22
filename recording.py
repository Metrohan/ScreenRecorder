import pyautogui
import cv2
import numpy as np
import os.path
import time

from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import QTimer

TARGET_FPS = 20.0
FRAME_INTERVAL_MS = int(1000 / TARGET_FPS)


class Recording:
    def __init__(self, main_window):
        self.main_window = main_window
        self.startTimer = 0
        self.timer = QTimer(self.main_window)
        self.timer.timeout.connect(self.updateTimer)
        self.captureTimer = QTimer(self.main_window)
        self.captureTimer.timeout.connect(self.captureFrame)
        self.out = None
        self.onLive = False
        self.filename = ""
        # Sane defaults so recording can start even if the user never
        # touches the resolution combobox or name field first.
        self.width = 1280
        self.height = 720
        self.prefName = "Recording"
        self.folder_path = ""

    def createFolder(self):
        record_folder = os.path.expanduser("~\\Documents\\Records")
        if not os.path.exists(record_folder):
            os.makedirs(record_folder, exist_ok=True)

    def set_file_location(self):
        self.folder_path = self.main_window.locLineEdit.text()

    def save_file_location(self):
        self.folder_path = self.main_window.locLineEdit.text()

    def choose_file_location(self):
        folder = QFileDialog.getExistingDirectory()
        if folder:
            self.main_window.locLineEdit.setText(folder)
            self.folder_path = folder

    def recordLocation(self):
        self.record_folder = os.path.expanduser("~\\Documents\\Records")
        os.chdir(self.record_folder)

    def initVideoWriter(self):
        prefRes = self.main_window.comboBox.currentText()
        try:
            width, height = map(int, prefRes.split('x'))
        except ValueError:
            # Placeholder combobox text ("Choose a resolution...") or any
            # other unparseable value - keep the previous/default resolution.
            width = height = None
        if width and height:
            self.width, self.height = width, height
        self.prefName = self.main_window.nameEdit.text() or self.prefName

    def startRecording(self):
        if self.onLive:
            return
        self.startTimer = 0
        self.onLive = True

        self.main_window.startButton.hide()
        self.main_window.stopButton.show()

        resolution = (self.width, self.height)
        codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        name = self.main_window.nameEdit.text() or self.prefName or "Recording"
        filename = f"{name}.avi"

        self.out = cv2.VideoWriter(filename, codec, TARGET_FPS, resolution)
        self.timer.start(1000)
        # Capture on a fixed-interval QTimer tick instead of a blocking
        # while-loop: this keeps the Qt event loop free so button clicks
        # (Stop) are handled immediately, and it paces frame writes to
        # match the fps declared to VideoWriter, so recorded duration
        # tracks real elapsed time.
        self.captureTimer.start(FRAME_INTERVAL_MS)

    def captureFrame(self):
        if not self.onLive or self.out is None:
            return
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if frame.shape[1] != self.width or frame.shape[0] != self.height:
            frame = cv2.resize(frame, (self.width, self.height))
        self.out.write(frame)
        if getattr(self.main_window, "previewCheckBox", None) is not None \
                and self.main_window.previewCheckBox.isChecked():
            cv2.imshow('Monitor', frame)
            cv2.waitKey(1)

    def stopRecording(self):
        if not self.onLive:
            return
        self.startTimer = 0
        self.onLive = False

        self.main_window.timer.setText("00:00:00")
        self.timer.stop()
        self.captureTimer.stop()
        if self.out is not None:
            self.out.release()
            self.out = None
        cv2.destroyAllWindows()

        self.main_window.startButton.show()
        self.main_window.stopButton.hide()

    def updateTimer(self):
        if self.onLive:
            self.startTimer += 1
            self.main_window.timer.setText(time.strftime("%H:%M:%S", time.gmtime(self.startTimer)))

    def countdown(self):
        if self.onLive:
            return
        t = 5
        while t != -1:
            self.main_window.countdown.setText(str(t))
            QApplication.processEvents()
            time.sleep(1)
            t -= 1
        self.startRecording()
