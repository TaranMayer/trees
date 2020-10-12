from pynput.keyboard import Key, Listener, Controller

def on_press(key):
    print(key)

with Listener(on_press=on_press) as listener:
    listener.join()
