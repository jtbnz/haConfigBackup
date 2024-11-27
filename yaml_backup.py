import os
import shutil
import asyncio
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BackupHandler(FileSystemEventHandler):
    def __init__(self, backup_folder):
        self.backup_folder = backup_folder
        os.makedirs(backup_folder, exist_ok=True)

    def on_modified(self, event):
        if event.is_directory:
            return
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file = os.path.join(self.backup_folder, f"{os.path.basename(event.src_path)}_{timestamp}")
        shutil.copy(event.src_path, backup_file)

async def start_watching(files_to_watch, backup_folder):
    event_handler = BackupHandler(backup_folder)
    observer = Observer()
    for file in files_to_watch:
        observer.schedule(event_handler, path=os.path.dirname(file), recursive=False)
    observer.start()
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Define the files to watch and the backup folder
files_to_watch = ["/config/configuration.yaml", "/config/automations.yaml"]
backup_folder = "/config/backup"

# Start watching the files
asyncio.run(start_watching(files_to_watch, backup_folder))