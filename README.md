# ZBrush Batch Decimation Automation

## Overview
This project is a Python-based UI automation system designed to batch-process ZBrush (.ztl) files.
It automates repetitive production tasks such as preparing models, converting them to PolyMesh3D,
running Decimation Master, capturing preview screenshots, saving optimized tools,
and safely closing ZBrush without overwriting original files.

## Key Features
- Batch processing of multiple `.ztl` files
- Automated canvas setup and Edit mode handling
- SubTool panel navigation with scrolling
- PolyMesh3D conversion
- Decimation Master preprocessing and decimation
- Automatic screenshot generation for previews
- Safe “Save As” workflow
- Keep-alive system for long ZBrush operations
- Emergency failsafe support

## Technologies Used
- Python 3
- PyAutoGUI
- ZBrush (UI-driven automation)
- Windows OS

## How It Works
1. Opens each `.ztl` file from the input directory
2. Closes LightBox and places the model on canvas
3. Enters Edit mode and frames the model
4. Handles SubTools and converts the model to PolyMesh3D
5. Runs Decimation Master preprocessing and decimation
6. Captures a preview screenshot
7. Saves the optimized tool to the output directory
8. Closes ZBrush safely without overwriting original files

## Folder Structure
INPUT_DIR/
model_01.ztl
model_02.ztl

OUTPUT_DIR/
model_01.ztl
model_01.png
model_02.ztl
model_02.png

## Safety Notes
- Move the mouse to the **top-left corner** to instantly stop the script
- Screen resolution and UI layout must remain unchanged
- Designed for unattended, long-duration batch processing

## Use Cases
- High-poly asset optimization
- Marketplace asset preparation
- Production pipeline automation
- Overnight batch processing

## Disclaimer
This script relies on fixed screen coordinates.
Any change in UI layout, resolution, or scaling requires coordinate recalibration.
