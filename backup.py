import os
import shutil
import filecmp
import sys
import zipfile

from datetime import datetime

import tkinter as tk
from tkinter import filedialog

path = filedialog.askdirectory()
def function_start_Everything():
    global path
    current_datetime = datetime.now()
    datetime_string = current_datetime.strftime('%Y%m%d%H%M')
    print(datetime_string)

    # Directory
    directory = datetime_string + "=Production"
    dst_zip = directory + '.zip'
    # Parent Directory path
    parent_dir = "D:\Foldertocopy"

    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    source_folder = r"D:\Foldertocopy\Foldertocopy\\"
    destination_folder = path
    print("pasta: " + path)


    # fetch all files
    for file_name in os.listdir(source_folder):
        print(source_folder)
        print(file_name)
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + '\\' + file_name
        # copy only files
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('copied', file_name)
    print("Caminho antes de Zippar")
    print(path)
    print("Start Zipping")
    shutil.make_archive(path, 'zip', root_dir=source_folder)
    print("Zip done")
    # os.rename(destination_folder, 'D:\Foldertocopy\PastaMudada')
    print("Caminho antes de apagar")
    print(path)
    folder_path = path
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and its contents deleted successfully.")
    except OSError as e:
        print(f"Error deleting folder '{folder_path}': {e.strerror}")



window = tk.Tk()
window.title("My GUI Window")  # Set the window title
window.geometry("800x600")  # Set the window size (width x height)

function_start_Everything()
print("Função Iniciada")
window.mainloop()  # Start the event loop



