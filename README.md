# **ScreenRecorder**
**ScreenRecorder** is a screen recording application for Windows, developed using Python, PyQt5, OpenCV, and QtDesigner. The tool allows users to capture their screen activity with ease, providing options for resolution selection, file naming, and seamless start/stop functionality.

![Screenshot 2023-10-28 202404](https://github.com/Metrohan/ScreenRecorder/assets/54481595/f0be2c52-d11f-4574-9d8a-8d468cdb3d89)

---

## **Installation**

### Prerequisites:

To run **ScreenRecorder**, you will need the following dependencies:

- **Python** (version 3.x or higher)
- **PyQt5**: A set of Python bindings for Qt5, used for creating the GUI.
- **OpenCV**: A library for computer vision tasks, including screen capture.

### Installation Steps:

1. Clone the repository or download the source code.
2. Install the necessary dependencies:

   ```bash
   pip install pyqt5 opencv-python
   ```
 ### Run the application from terminal or exe file:
   ```bash
   python screenrecorder.py
   ```
---

## **Usage Instructions**

1. **Select Resolution:**
   Choose the desired screen resolution for your recording from the dropdown menu.

2. **Enter a Recording Name:**
   Provide a name for your recording file. This is mandatory to proceed, and the application will crash if left empty.

3. **Start Recording:**
   - Click the **'REC'** button to begin recording.
   - A 5-second countdown will occur before the recording starts.
   - A monitor preview window will appear during the recording process.

4. **Stop Recording:**
   - Click the **'Stop'** button to end the recording.
   - Alternatively, you can press **'P'** on the monitor window to stop the recording.

---

**Important:** You must choose a resolution and pick a name for your recording. If either is left unselected, the recorder will crash!

---

## **Todo**

- Optimize the program for better performance.
- Add support for voice recording during screen capture.
- Remove the monitor preview window during recording.
- Improve the user interface for a more polished experience.

---

## **Bugs**

- Occasionally, the recorded video may play faster than expected. For example, a 20-second recording might be saved as 15 or 17 seconds.
- If a resolution or recording name is not selected, the program will crash.
- Sometimes the **'Stop'** button doesn't work properly. In that case, you can press **'P'** on the monitor to stop the recording.


# Credits

![Static Badge](https://img.shields.io/badge/Pyinstaller-blue?color=blue&link=https%3A%2F%2Fpyinstaller.org) ![Static Badge](https://img.shields.io/badge/opencv-blue?link=https%3A%2F%2Fopencv.org%2F)
 ![Static Badge](https://img.shields.io/badge/pyqt-brightgreen?link=https%3A%2F%2Fpypi.org%2Fproject%2FPyQt5%2F) ![Static Badge](https://img.shields.io/badge/qtdesigner-green?link=https%3A%2F%2Fwww.qt.io%2Fdownload-open-source)

 Special thanks to the Haeydra for his support










