import tkinter as tk
from tkinter import font as tkFont
from gpiozero import LED

# GPIO pin numbers for the LEDs
led_pins = [14, 15, 18]
colour = ["Red", "Blue", "Green"]

# Create LED objects
leds = [LED(pin) for pin in led_pins]

# GUI DEFINITIONS
win = tk.Tk()
win.title("LED Controller")

# Use a custom font
myFont = tkFont.Font(family='Helvetica', size=18, weight="bold")

# Set the window size
win.geometry('400x300')

# Function to handle radio button selection
def select_led(led_index):
    for i, led in enumerate(leds):
        if i == led_index:
            led.on()
        else:
            led.off()

# Function to exit the GUI and turn off all LEDs
def close():
    for led in leds:
        led.off()
    win.destroy()

# Create radio buttons
radio_buttons = []
for i, color in enumerate(colour):
    radio_button = tk.Radiobutton(win, text=f"LED {color}", font=myFont, value=i, command=lambda i=i: select_led(i))
    radio_button.pack(pady=10, anchor='w')
    radio_buttons.append(radio_button)

# Exit button
exitButton = tk.Button(win, text='Exit', font=myFont, command=close, bg='red', height=2, width=10)
exitButton.pack(pady=20)

# Configure the window to handle closing
win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
