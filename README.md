# ⌨️ Keyboard cleaner

<div align="center">
   
![Version](https://img.shields.io/badge/version-1.1-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
 
A minimal, modern Python app to temporarily lock your keyboard and mouse for cleaning or other purposes. Unlock with a secure key combination. (Windows Only)
</div>

## New
- Custom background
- Background blur effect
- Debug mode (Good if you plan to touch the code I guess)

## Features
- Locks all keyboard and mouse input
- Minimal fullscreen GUI (PyQt5)
- Unlock by holding **Ctrl + Alt + U** for 3 seconds (in any order)
- Prevents accidental unlocks

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python main.py
   ```
3. To unlock, hold **Ctrl + Alt + U** for 3 seconds.

## Why?
- Clean your keyboard and mouse without accidental input
- Lock input for focus or security

## Requirements

- Python 3.8+
- PyQt5
- keyboard
- mouse
- Pillow
- PyYaml
- Pyinstaller