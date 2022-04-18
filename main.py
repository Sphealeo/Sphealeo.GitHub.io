import firefox
import os
os.system('pip install readchar')
import readchar

firefox.get('firefox').open_new_tab('')
while True:
    key=readchar.readkey()

    print(key)
    print(key)