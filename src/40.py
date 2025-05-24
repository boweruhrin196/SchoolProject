import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "school_project_code.py":
            print("File has been modified.")
            
def main():
    observer = Observer()
    observer.schedule(MyEventHandler(), path=".", recursive=False)
    observer.start()

if __name__ == "__main__":
    main()
    observer.join()
