import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

mouse = Controller()

# Set a key to toggle clicking on/off
TOGGLE_KEY = KeyCode(char='z')  # Press 'Z' to start/stop

clicking = False

def click_mouse():
    global clicking
    while True:
        if clicking:
            mouse.click(Button.left)
        time.sleep(0.001)  # Adjust this for speed (lower = faster)

def on_press(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
        print(f"Clicking {'ON' if clicking else 'OFF'}")

# Start the clicking thread
click_thread = threading.Thread(target=click_mouse, daemon=True)
click_thread.start()

# Start listening for the toggle key
with Listener(on_press=on_press) as listener:
    listener.join()
