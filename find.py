from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import glob, os
import requests
import sys
import time
import subprocess

class FileModifiedHandler(FileSystemEventHandler):

    def __init__(self, path, callback):
        #self.file_name = file_name
        self.host = host        
        self.observer = Observer()
        self.observer.schedule(self, path, recursive=False)
        self.observer.start()
        self.observer.join()
        

   

    def on_created(self, event):
        command = "python send_sample.py "+ str(self.host) +" "+ str(event.src_path)
        
        os.system(command)       
        

        #self.check_file('.')

           


from sys import argv, exit

if __name__ == '__main__':

    if sys.argv[1:]:
        host = str(sys.argv[1])
    else:
        host = "localhost"
while True:       
    FileModifiedHandler('.', host)