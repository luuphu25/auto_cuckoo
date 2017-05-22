import sys
import glob, os 
import time
import logging
from  watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer
from watchdog.events import FileCreatedEvent

def check_file():
    os.chdir("/vagrant/Code/program")
    i = 0
    file_w = open("/vagrant/Code/program/list.txt", "r+")
    content = file_w.read()
    x = content.split(';')

    flag = 0
    for file in glob.glob("*.*"):
        for s in x :
            if file == s:
                flag = 1
        if flag == 0:
            print file
            file = file +  ";"      
            file_w.write(file)

class Event(FileCreatedEvent):
    path = dir
    def on_moved(self,event):
        return 0
    def on_modified(self,event):
        return 0 
    def on_deleted(self,event):
        return 0
    def on_created(self, event):
       check_file()


if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO,
                        #format='%(asctime)s - %(message)s',
                        #datefmt='%Y-%m-%d %H:%M:%S')
    #x = RegexMatchingEventHandler(ignore_regexes=['.part'], ignore_directories=True)

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Event(FileCreatedEvent)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()