import sys
import threading
import time
import keyboard
import mouse
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

# Special unlock combination
UNLOCK_COMBO = 'ctrl+alt+u'
unlocked = False

combo_pressed = False
ctrl_held = False
alt_held = False
u_held = False
combo_hold_start = None

def block_all_keys(e):
    global combo_pressed, ctrl_held, alt_held, u_held, combo_hold_start
    # Debug print removed
    # Track Ctrl, Alt, and U state independently
    if e.name == 'ctrl':
        ctrl_held = e.event_type == 'down'
    if e.name == 'alt':
        alt_held = e.event_type == 'down'
    if e.name == 'u':
        u_held = e.event_type == 'down'

    # Require combo to be held for 3 seconds
    if ctrl_held and alt_held and u_held:
        if combo_hold_start is None:
            combo_hold_start = time.time()
        elif not combo_pressed and (time.time() - combo_hold_start >= 3):
            combo_pressed = True
        return True  # Do not suppress unlock combo
    else:
        combo_hold_start = None
    # Suppress all other keys
    return False

def block_mouse_move(e):
    # Always move mouse to (0,0)
    mouse.move(0, 0, absolute=True, duration=0)
    return False

def block_mouse_click():
    return False

class LockScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Keyboard & Mouse Locker')
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setGeometry(0, 0, QApplication.primaryScreen().size().width(), QApplication.primaryScreen().size().height())
        self.setStyleSheet('background-color: #222; color: #fff;')
        layout = QVBoxLayout()
        label = QLabel('Keyboard & Mouse are locked.\nPress Ctrl+Alt+U for 3 seconds to unlock.', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('font-size: 5em;')
        layout.addWidget(label)
        self.setLayout(layout)

    def keyPressEvent(self, event):
        # Override to prevent Alt+F4, etc.
        pass

    def closeEvent(self, event):
        # Prevent window from being closed
        event.ignore()

def block_input():
    # Block all keys (combo detection is handled in block_all_keys)
    keyboard.hook(block_all_keys, suppress=True)
    # Block mouse movement and clicks
    mouse.hook(block_mouse_move)
    mouse.on_button(block_mouse_click, buttons=('left', 'right', 'middle'), types=('down', 'up'))

def unblock_input():
    global unlocked
    unlocked = True
    keyboard.unhook_all()
    mouse.unhook_all()

def listen_for_unlock(app):
    global unlocked, combo_pressed
    # Only unlock via combo
    while not unlocked:
        if combo_pressed:
            unblock_input()
            app.quit()
            break
        time.sleep(0.1)

def main():
    app = QApplication(sys.argv)
    lock_screen = LockScreen()
    lock_screen.showFullScreen()
    
    # Start blocking input
    threading.Thread(target=block_input, daemon=True).start()
    
    # Start listening for unlock (not daemon so it keeps running)
    unlock_thread = threading.Thread(target=listen_for_unlock, args=(app,))
    unlock_thread.start()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
