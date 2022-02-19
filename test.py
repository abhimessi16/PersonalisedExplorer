from pynput import keyboard
import winsound,time

freq,dur=2500,500

combo={keyboard.Key.ctrl_l, keyboard.Key.alt_l}

curr=set()

Start=0
End=0
f=0
c=set()

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

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()