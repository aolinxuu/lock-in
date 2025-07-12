# Lock In Timer

A visually appealing, sound-enhanced productivity timer built with PyQt5. Designed to help you focus, track your work session, and take well-timed breaks.

## Features

- **60-minute focus timer** with distinct motivational stages:
  - **Zone In** (last 55 minutes)
  - **Nearly There** (last 20 minutes)
  - **Recap** (last 15 minutes)
  - **Break** (last 10 minutes)
- **Sound notifications** for each stage and when the break is over.
- **Custom UI** with large timer display, motivational messages, and icon-based Start, Pause, and Reset buttons.
- **Custom font** and color themes for a modern, calming look.
- **Packaged as a standalone app** (see below for PyInstaller instructions).

## Installation

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd study-timer
   ```

2. **Install dependencies:**

   - Make sure you have Python 3.7+ installed.
   - Install all required Python packages using:
     ```bash
     pip install -r requirements.txt
     ```
   - (Optional) If you want to build a standalone app, install PyInstaller:
     ```bash
     pip install pyinstaller
     ```

3. **Run the timer:**
   ```bash
   python main.py
   ```

## Packaging as a Standalone App

To build a standalone macOS app using PyInstaller:

```bash
pyinstaller LockIn.spec
```

This will create a `dist/LockIn.app` bundle you can run directly.

## Project Structure

```
study-timer/
  main.py            # Main entry point
  timer.py           # Timer widget and logic
  util.py            # IconButton class for icon-based buttons
  constants.py       # Timer stage durations
  styles.py          # (Optional) Additional style definitions
  resources/         # Icons, sounds, font, and app icon
  LockIn.spec        # PyInstaller build spec
  requirements.txt   # Python dependencies
```

## Requirements

- Python 3.7+
- All Python dependencies listed in `requirements.txt`
