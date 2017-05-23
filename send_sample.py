import os
from sys import argv, exit
import sys
import time
import requests

def waiting_download(sample):        
        a = 0;
        b = 0;
        print "sending to sandbox..", 
        while a==0:
            statinfo = os.stat(sample)
            a = statinfo.st_size
            
            print ".",
            time.sleep(2)
            statinfo = os.stat(sample)
            b = statinfo.st_size


if __name__ == '__main__':
	host = sys.argv[1]
	path = sys.argv[2]
	filename, file_extension = os.path.splitext(path)
	if file_extension == '.part':
		sys.exit() 
	file_mau = path.split("/")
	file_mau = file_mau[-1]      
	REST_URL = "http://" + str(host) +":8090/tasks/create/file"
	waiting_download(path)   
	with open(path, "rb") as sample:
	    files = {"file": (file_mau, sample)}
	    r = requests.post(REST_URL, files=files)
	task_id = r.json()["task_id"]