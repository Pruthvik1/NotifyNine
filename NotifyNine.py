import time
#pip install tk
import tkinter as tk
import os
#pip install pygame
import pygame
from pynput import keyboard, mouse
#pip install Pillow
from PIL import Image, ImageTk

# Set the time limit for inactivity (in seconds)
TIME_LIMIT = 540 # 9 minutes

# Record the time of the last activity
last_activity_time = time.time()

# Define the callback functions for mouse and keyboard events
def on_move(x, y):
    global last_activity_time
    last_activity_time = time.time()

def on_click(x, y, button, pressed):
    global last_activity_time
    last_activity_time = time.time()

def on_scroll(x, y, dx, dy):
    global last_activity_time
    last_activity_time = time.time()

def on_press(key):
    global last_activity_time
    last_activity_time = time.time()

# Set up the listeners for mouse and keyboard events
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press)

# Start the listeners
mouse_listener.start()
keyboard_listener.start()

# Define the function to display the notification
def show_notification():
    root = tk.Tk()
    root.title("NitifyNine Reminds YOU")
    root.geometry("450x250")

    # Load image and resize it to fit in the GUI
    image_path = "icon.png"  
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            width, height = image.size
            max_size = (100, 100)
            if width > max_size[0] or height > max_size[1]:
                image.thumbnail(max_size)
            photo_image = ImageTk.PhotoImage(image)
            image_label = tk.Label(root, image=photo_image)
            image_label.pack(pady=10)
        except Exception as e:
            print("Error loading image: ", e)
    else:
        print("Image not found: ", image_path)

    # Create label for text
    label_text = "Your mouse or keyboard has been inactive for 9 minutes."
    label_font = ("Poppins", 16)
    label = tk.Label(root, text=label_text, font=label_font)
    label.pack(pady=10)

    # Create button to dismiss notification
    button_font = ("Poppins", 12)
    button = tk.Button(root, text="Dismiss", font=button_font, command=root.destroy,
                       bg="white", fg="black", activebackground="#005fa6", activeforeground="#005fa6")
    button.pack(pady=10)

    # Play sound
    sound_path = "sound.wav"  # replace with actual sound file name
    if os.path.exists(sound_path):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
        except pygame.error:
            print("Error playing sound: ", sound_path)
    else:
        print("Sound not found: ", sound_path)

    root.mainloop()

# Loop to check for inactivity
while True:
    # Check if the time since the last activity exceeds the time limit
    if time.time() - last_activity_time > TIME_LIMIT:
        # Display the notification
        show_notification()

    # Wait for 10 second before checking again
    time.sleep(10)
