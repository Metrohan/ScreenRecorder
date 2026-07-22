> **Project Status: Complete**
>
> This project has reached its intended scope. No major new features are currently planned.

# **ScreenRecorder**
**ScreenRecorder** is a screen recording application for Windows, developed using Python, PyQt5, OpenCV, and QtDesigner. The tool allows users to capture their screen activity with ease, providing options for resolution selection, file naming, and seamless start/stop functionality.

![Screenshot 2023-10-28 202404](https://github.com/Metrohan/ScreenRecorder/assets/54481595/f0be2c52-d11f-4574-9d8a-8d468cdb3d89)

---

## **Download**

Prebuilt Windows binaries are published on the [Releases page](https://github.com/Metrohan/ScreenRecorder/releases) — no Python install required.

---

## **Running from source**

### Prerequisites

- **Python** 3.9+
- The packages listed in `requirements.txt`

### Installation

```bash
git clone https://github.com/Metrohan/ScreenRecorder.git
cd ScreenRecorder
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

### Build a standalone .exe yourself

```bash
pyinstaller --onefile --windowed --icon=recbutton.ico --name ScreenRecorder main.py
```

The built binary will be in `dist/ScreenRecorder.exe`. Releases are also built and attached automatically by CI (`.github/workflows/release.yml`) whenever a `v*` tag is pushed.

---

## **Usage Instructions**

1. **Select a resolution** (optional) — defaults to 1280x720 if left unset.
2. **Enter a recording name** (optional) — defaults to "Recording" if left blank.
3. **Toggle "Show preview window"** if you want a live monitor preview while recording (on by default).
4. **Start Recording** — click **REC**. A 5-second countdown runs before capture starts.
5. **Stop Recording** — click **STOP**.

---

## **Known limitations**

- **Windows only.** File paths and `os.startfile` usage are Windows-specific; there's no macOS/Linux support and none is planned for this release.
- **No audio recording.** Video only — see [issue #11](https://github.com/Metrohan/ScreenRecorder/issues/11) for the reasoning and what a future audio pipeline would require.
- Recording resolution is captured at your screen's native resolution and resized to your selected output resolution; picking a resolution far from your actual screen size will look scaled/stretched rather than cropped.

---

## Fixed in this release (v1.0.0)

- **Crash on Start with empty inputs** ([#10](https://github.com/Metrohan/ScreenRecorder/issues/10)) — sane defaults are now set for resolution/name, and Stop is guarded against being triggered before a recording exists.
- **Stop button unresponsive** ([#8](https://github.com/Metrohan/ScreenRecorder/issues/8)) — screen capture now runs on a `QTimer` tick instead of a blocking loop, so the Qt event loop (and the Stop button) stays responsive. This also fixed a layout bug where Start and Stop shared the same screen position and Stop was drawn on top at launch.
- **Recorded duration didn't match real time** ([#9](https://github.com/Metrohan/ScreenRecorder/issues/9)) — capture is now paced to the same interval declared to the video writer, so a 20-second recording plays back as ~20 seconds.
- **Preview window is now optional** via a checkbox, instead of always opening.

---

# Credits

![Static Badge](https://img.shields.io/badge/Pyinstaller-blue?color=blue&link=https%3A%2F%2Fpyinstaller.org) ![Static Badge](https://img.shields.io/badge/opencv-blue?link=https%3A%2F%2Fopencv.org%2F)
 ![Static Badge](https://img.shields.io/badge/pyqt-brightgreen?link=https%3A%2F%2Fpypi.org%2Fproject%2FPyQt5%2F) ![Static Badge](https://img.shields.io/badge/qtdesigner-green?link=https%3A%2F%2Fwww.qt.io%2Fdownload-open-source)

Special thanks to the Haeydra for his support
