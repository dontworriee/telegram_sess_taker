import os
import time
time.sleep(3)
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'client.session')
os.remove(path)
time.sleep(3)
os.system('main.py')