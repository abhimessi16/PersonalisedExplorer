from pynput import keyboard
import winsound,time

# the frequency and duration of the beep when activation is done
freq,dur=2500,500

# the combo keys that will activate the program
# i selected them so that they don't coincide with system hotkeys
combo={keyboard.Key.ctrl_l, keyboard.Key.alt_l}

# this will store all the keys that have been pressed
curr=set()

# to store the time at the start and end of key events
# to be able to check the duration of the key press
Start=0
End=0

# a flag to check if the activation-hotkey was pressed f=1
# or if the activation-hotkey was released f=0
f=0

# c will store the keys that are pressed at any given instant of time
c=set()

# the code for the on_press event
def on_press(key):
    global Start,End,f,work
    if key in combo:
        curr.add(key)
        c.add(key)
    if all(k in curr for k in combo):
        if not f:
            Start=time.time()
            f=1
    if key==keyboard.Key.esc:
        listener.stop()

# the code for the on_release event
def on_release(key):
    global Start,End,f,c,work
    try:
        curr.remove(key)
        if key in combo:
            c.add(key)
        if f and c==combo:
            End=time.time()
            if End-Start>=0.75:
                winsound.Beep(freq,dur)
            c=set()
            f=0
        work=None
    except KeyError:
        pass

# context manager for the keyboard listener
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
