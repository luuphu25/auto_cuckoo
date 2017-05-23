from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import glob, os
import requests
import sys
import time

class FileModifiedHandler(FileSystemEventHandler):

    def __init__(self, path, callback):
        #self.file_name = file_name
        self.callback = callback        
        self.observer = Observer()
        self.observer.schedule(self, path, recursive=False)
        self.observer.start()
        self.observer.join()
        

    def waiting_download(self,sample):        
        a = 0;
        b = 0;        
        while a==0:
            statinfo = os.stat(sample)
            a = statinfo.st_size     
       
            time.sleep(2)
            
                               

    def on_created(self, event):
        file_mau = event.src_path + ".part"
        file_mau = event.src_path.split("/")
        file_mau = file_mau[-1]
        
        self.waiting_download(event.src_path)
        REST_URL = "http://localhost:8090/tasks/create/file" 
        self.observer.stop() 
        with open(event.src_path, "rb") as sample:
            files = {"file": (file_mau, sample)}
            r = requests.post(REST_URL, files=files)
        task_id = r.json()["task_id"]
        print "send to sanbox with id: " + str(task_id)

       

            


from sys import argv, exit

if __name__ == '__main__':

    if not len(argv) == 1:
        print("No file specified")
        exit(1)

    def callback():
        print("FILE WAS CREATE")
while True:       
    FileModifiedHandler('.', callback)
