import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
import tkinter as tk
from tkinter import filedialog



def start_recording():
    
    name = name_entry.get()
    duration = int(duration_entry.get())
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    dim = (width,height)
    save_dir = save_dir_entry.get()


    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output = cv2.VideoWriter(save_dir + "/" +name + ".mp4",fourcc,30.0,dim)

    now_start_time = time.time()
    end_time = now_start_time + duration + 3

    while True:
        image = pyautogui.screenshot()
        frame1 = np.array(image)
        frames = cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)

        output.write(frames)
        c_time = time.time()

        if c_time > end_time:
            break

    print("Recording Has Been Saved")
    output.release()

    
    
#UI
win = tk.Tk()
win.title("Recorder")
win.geometry("300x250")

name_label = tk.Label(win,text="Enter New File Name ")
name_label.pack()
name_entry = tk.Entry(win)
name_entry.pack()

duration_label = tk.Label(win,text="Enter The Duration of your Recording")
duration_label.pack()
duration_entry = tk.Entry(win)
duration_entry.pack()

save_dir_label = tk.Label(win,text="Enter The Director Location")
save_dir_label.pack()

save_dir_entry = tk.Entry(win)
save_dir_entry.pack()

def select_save_directory():
    save_dir = filedialog.askdirectory()
    save_dir_entry.delete(0,tk.END)
    save_dir_entry.insert(0,save_dir)

browse_button = tk.Button(win,text="Browse",command= select_save_directory)
browse_button.pack(pady=10)

button_label = tk.Button(win,text="Start Recording",command = start_recording)
button_label.pack(pady=5)

win.mainloop()
