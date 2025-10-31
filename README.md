# KeyboardCleaner

A minimal, modern Python app to temporarily lock your keyboard and mouse for cleaning or other purposes. Unlock with a secure key combination.

## Features
- Locks all keyboard and mouse input
- Minimal fullscreen GUI (PyQt5)
- Unlock by holding **Ctrl + Alt + U** for 3 seconds (in any order)
- Prevents accidental unlocks
- Cross-platform (Windows recommended)

## Usage
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

## Requirements
- Python 3.8+
- PyQt5
- keyboard
- mouse

## Notes
- On Windows, you may need to run as administrator for full keyboard/mouse blocking.
- Use at your own risk! Always test the unlock combo before cleaning.

## License
MIT
