import pyautogui
import time

# Set the interval (in seconds) for mouse movement
interval = 300  # 5 minutes

try:
    while True:
        # Move the mouse cursor a small distance to prevent sleep
        pyautogui.move(1, 1)
        time.sleep(interval)
except KeyboardInterrupt:
    # Press Ctrl+C to stop the script
    pass