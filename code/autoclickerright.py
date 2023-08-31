import pyautogui
import keyboard
import ctypes
import platform

def set_console_title(title):
    if platform.system() == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif platform.system() == "Linux":
        print(f"\033]0;{title}\007", end="", flush=True)

# Set the desired title
new_title = "Orchid V1 / Bridge Assist"

# Call the function to set the console title
set_console_title(new_title)

# Your script code continues here


# Flag to track whether automatic clicks are active
clicks_active = False

print("Press 'J' to start")

# Get desired clicks per second (CPS) from the user
cps = float(input("Enter desired clicks per second: "))

# Calculate the delay between clicks based on CPS
click_delay = 1 / cps

# Toggle automatic clicks when "H" key is pressed
while True:
    if keyboard.is_pressed('J'):
        clicks_active = not clicks_active
        if clicks_active:
            print(f"Automatic clicks started at {cps:.2f} clicks per second.")
        else:
            print("Automatic clicks stopped.")
        while keyboard.is_pressed('J'):  # Wait until "H" key is released
            pass

    if clicks_active:
        pyautogui.rightClick()  # Simulate a right mouse button click
        pyautogui.PAUSE = click_delay
