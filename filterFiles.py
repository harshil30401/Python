import time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder_to_track = " " 
folder_dest = " "

class Handler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track+ "/" +filename
            new_dest = folder_dest+ "/"+filename  
            s = str(filename)
            if(s.endswith(".jpg") or s.endswith(".jpeg")):
                os.rename(src, new_dest)
                print(filename+" has been moved to "+folder_dest)
                

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

