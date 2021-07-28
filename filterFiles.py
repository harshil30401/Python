import time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path_source = " " 
path_destination = " "

class Handler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for filename in os.listdir(path_source):
            src = path_source+ "/" +filename
            new_dest = path_destination+ "/"+filename  
            s = str(filename)
            if(s.endswith(".jpg") or s.endswith(".jpeg")):
                os.rename(src, new_dest)
                print(filename+" has been moved to "+path_destination)
                

observer = Observer()
eventHandler = Handler()

observer.schedule(event_handler=eventHandler, path=folder_to_track, recursive=True)
observer.start()

try:
    while(1):
        time.sleep(10)
except KeyboardInterrupt:
        observer.stop()

observer.join()

