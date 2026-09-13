# ZBrush Batch Decimation Automation

Python + PyAutoGUI automation for batch-processing ZBrush `.ztl` assets.

## Features

- Batch processing of multiple `.ztl` files
- Automated LightBox closing and viewport preparation
- Edit mode and model framing
- SubTools panel preparation and scrolling
- PolyMesh3D conversion
- Decimation Master preprocessing
- Decimate Current
- Automatic full-screen screenshot after PolyMesh3D
- Automated ZTL Save As workflow
- Safe ZBrush closing without saving the original
- Keep-alive click after long waits
- PyAutoGUI emergency failsafe

## Workflow

```text
Find ZTL files
      ↓
Open ZBrush file
      ↓
Close LightBox
      ↓
Prepare model / Edit / F
      ↓
SubTools + Scroll
      ↓
Make PolyMesh3D
      ↓
Wait + Screenshot
      ↓
Decimation Master
      ↓
Process Current
      ↓
Decimate Current
      ↓
Save As optimized ZTL
      ↓
Close ZBrush → No
      ↓
Next ZTL
```

## Technologies

- Python 3
- PyAutoGUI
- Pillow
- ZBrush
- Windows

## Installation

Install Python 3, then run:

```bash
pip install -r requirements.txt
```

## Configuration

Before running, edit these variables in `main.py`:

```python
INPUT_DIR = r"C:\Users\pc\Desktop\asdf"
OUTPUT_DIR = r"C:\Users\pc\Desktop\dfsd"
```

Set them to your actual input and output folders.

## Run

```bash
python main.py
```

The script displays the `.ztl` files it found and starts after a 5-second countdown.

### Emergency stop

PyAutoGUI's failsafe is enabled:

```python
pyautogui.FAILSAFE = True
```

Move the mouse to the top-left corner of the screen to trigger the failsafe.

## Output

For an input file:

```text
head01.ztl
```

the output folder will contain:

```text
head01.ztl
head01.png
```

The PNG is the full-screen screenshot captured after the PolyMesh3D step.

## Important limitation

This project is screen-coordinate-based UI automation. The ZBrush window position, screen resolution, Windows display scaling, and ZBrush UI layout should remain consistent with the coordinates configured in `main.py`.

If the UI changes, recalibrate the coordinates before running a large batch.

## Project Purpose

The project demonstrates practical Python automation for a repetitive 3D production workflow, including GUI automation, batch processing, file handling, long-running task management, and safety controls.
