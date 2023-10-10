import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/arung/Downloads"
to_dir = "C:/Users/arung/Desktop/ByjuS/C103/PRO-C103-Student-Boilerplate-main/DownloadedFiles"


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self,event):
        print(f"Oops, someone deleted " {event.src_path})
        
    def on_modified(self,event):
        print(f"Oops, someone has modified" {event.src_path})
    
    def on_moved(self,event):
        print(f"Hey, {event.src_path} has been moved!")



event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()
try:
    while True:
        time.sleep(5)
        print('running')
except KeyboardInterrupt:
    print('stop')
    observer.stop()

while True:
    time.sleep(2)
    print("running...")


try:
    while True:
        time.sleep(2)
        print("running....")
except KeyboardInterrupt:
    print("stopped!")
    obsever.stop()