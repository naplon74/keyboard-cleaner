# ⌨️ Keyboard Cleaner

<div align="center">
   
![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![VirusTotal Detection](https://img.shields.io/badge/VirusTotal-4%2F70%20detected-yellow)

A minimal, modern Python app to temporarily lock your keyboard and mouse for cleaning or other purposes. Unlock with a secure key combination. (Windows Only)
</div>

## Full VirusTotal Report
[![VirusTotal](https://a11ybadges.com/badge?logo=virustotal)](https://www.virustotal.com/gui/file/3ba944bbb49ab4e8191dd075d589a1bb315286613e1cea560f79e668beac1798)

## Features
- Locks all keyboard and mouse input
- Minimal fullscreen GUI (PyQt5)
- Unlock by holding **Ctrl + Alt + U** for 3 seconds (in any order)
- Prevents accidental unlocks
- Cross-platform

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
