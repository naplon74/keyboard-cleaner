# ⌨️ Keyboard cleaner

<div align="center">
   
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white)](#)
[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
 
A minimal, modern Python app to temporarily lock your keyboard and mouse for cleaning or other purposes. Unlock with a secure key combination.
</div>

> [!NOTE]
> Linux port comming soon.

## Features
- Locks all keyboard and mouse input
- Minimal fullscreen GUI (PyQt5)
- Unlock by holding **Ctrl + Alt + U** for 3 seconds (in any order)
- Prevents accidental unlocks
- Cross-platform

## Usage (Or install V1.0.0)

> [!TIP]
> Ignore if you don't understand.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install PyQt5 keyboard mouse
   ```
2. Run the app:
   ```bash
   python main.py
   ```
3. To unlock, hold **Ctrl + Alt + U** for 3 seconds.

## Why?
- Clean your keyboard and mouse without accidental input
- Lock input for focus or security

## Requirements (Only if you wanna run the Python script. Ignore if you don't understand.)
- Python 3.8+
- PyQt5
- keyboard
- mouse
