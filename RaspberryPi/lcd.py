"""Simple test for I2C RGB character LCD shield kit. FOR INSTRUCTOR USE ONLY"""
import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

# Set color values
red = [100, 0, 0]
blue = [0, 100, 0]
green = [0, 0, 100]
white = [100, 100, 100]
backlight_off = [0, 0, 0]

# Clear the screen
lcd.clear()

# Set LCD color to red and sleep for 1 second
lcd.color = red
time.sleep(1)

# Print two line message
lcd.message = "Hello\nCircuitPython"
time.sleep(1)

# Set LCD color to blue
lcd.color = blue
time.sleep(1)

# Set LCD color to green
lcd.color = green
time.sleep(1)

# Set LCD color to white
lcd.color = white
time.sleep(1)
lcd.clear()

# Print two line message right to left
lcd.text_direction = lcd.RIGHT_TO_LEFT
lcd.message = "Hello\nCircuitPython"
time.sleep(2)

# Return text direction to left to right
lcd.text_direction = lcd.LEFT_TO_RIGHT

# Display cursor
lcd.clear()
lcd.cursor = True
lcd.message = "Cursor! "
time.sleep(2)

# Display blinking cursor
lcd.clear()
lcd.blink = True
lcd.message = "Blinky Cursor!"
time.sleep(2)

# Move the cursor to the home position
lcd.clear()
lcd.message = "Cursor moved to\nposition (1,1)"
lcd.home()
time.sleep(2)

# Stop blinking and showing cursor
lcd.blink = False
lcd.cursor = False
lcd.clear()

# Create message to scroll
scroll_msg = '<-- Scroll'
lcd.message = scroll_msg
# Scroll to the left
for i in range(len(scroll_msg)):
    time.sleep(0.5)
    lcd.move_left()
lcd.clear()

# Demo turning backlight off and on.
lcd.clear()
lcd.color = white
lcd.message = 'Flash backlight\nin 2 seconds...'
time.sleep(2)

# Turn backlight on and off twice
lcd.color = backlight_off
time.sleep(0.5)
lcd.color = white
time.sleep(0.5)
lcd.color = backlight_off
time.sleep(0.5)
lcd.color = white
time.sleep(1)

# Button demo. Show button state.
lcd.clear()
lcd.message = 'Press buttons...\nSELECT to stop'

# Loop to wait for button presses
while True:
    if lcd.left_button:
        lcd.clear()
        lcd.message = "Left!"
    elif lcd.right_button:
        lcd.clear()
        lcd.message = "Right!"
    elif lcd.up_button:
        lcd.clear()
        lcd.message = "Up!"
    elif lcd.down_button:
        lcd.clear()
        lcd.message = "Down!"
    elif lcd.select_button:
        lcd.clear()
        lcd.message = "Going to sleep\nCya later!"
        time.sleep(2)
        lcd.clear()
        
        # Turn off the display
        lcd.display = False

        # Turn off the backlight
        lcd.color = backlight_off

        # Quit the program
        quit()
        
