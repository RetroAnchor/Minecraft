import pyautogui
import time
import keyboard

# Function to click and hold, moving in a 100-pixel square
def click_and_hold_square(start_x, start_y):
    try:
        print("Press P to start clicking and holding in a 100-pixel square.")
        
        # Wait for the user to press P
        keyboard.wait('p')

        # Set the size of the square
        square_size = 100

        # Move the mouse to the starting position
        pyautogui.moveTo(start_x, start_y, duration=1)

        # Click and hold
        pyautogui.mouseDown()

        print("Clicking and holding in a 100-pixel square. Press Ctrl+C to stop.")

        # Move in a square pattern
        for _ in range(4):
            pyautogui.moveRel(square_size, 0, duration=1)  # Move right
            time.sleep(2)  # Hold for 2 seconds
            pyautogui.moveRel(0, square_size, duration=1)  # Move down
            time.sleep(2)  # Hold for 2 seconds
            pyautogui.moveRel(-square_size, 0, duration=1)  # Move left
            time.sleep(2)  # Hold for 2 seconds
            pyautogui.moveRel(0, -square_size, duration=1)  # Move up
            time.sleep(2)  # Hold for 2 seconds

        # Release the mouse button
        pyautogui.mouseUp()
        print("\nClicking and holding in a 100-pixel square stopped.")

    except KeyboardInterrupt:
        # Release the mouse button if the script is interrupted
        pyautogui.mouseUp()
        print("\nClicking and holding in a 100-pixel square stopped.")

# Define the starting position (adjust these coordinates)
start_x = 100
start_y = 100

# Call the function to click and hold, moving in a 100-pixel square, when P is pressed
click_and_hold_square(start_x, start_y)

