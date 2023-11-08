import os
import time
import platform
import tkinter as tk
from tkinter import ttk
from threading import Thread

def lock_computer():
    os.system('rundll32.exe user32.dll, LockWorkStation')

def timer_thread(entry, label, start_button, root):
    entry.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)
    start_button.grid_remove()
    minutes = int(entry.get())
    for remaining_minutes in range(minutes, 0, -1):
        if remaining_minutes == 1:
            root.configure(bg='#ff6e40')
            main_frame.configure(bg='#ff6e40')
            minutes_label.configure(bg='#ff6e40')
            time_left_label.configure(bg='#ff6e40')
            for i in range(60, 0, -1):
                label.config(text=f'{i} second(s) left.')
                time.sleep(1)
            break
        elif remaining_minutes <= 5:
            root.configure(bg='#ffc13b')
            main_frame.configure(bg='#ffc13b')
            minutes_label.configure(bg='#ffc13b')
            time_left_label.configure(bg='#ffc13b')
        label.config(text=f'{remaining_minutes} minute(s) left.')
        time.sleep(60)

    label.config(text='Time is up! Locking the computer...')
    lock_computer()
    root.destroy()

def start_timer(entry, label, start_button, root):
    t = Thread(target=timer_thread, args=(entry, label, start_button, root))
    t.start()

def main():
    root = tk.Tk()
    root.title('Child Timer')
    root.configure(bg='#a2d5c6')

    # Remove the window's system menu and disable Alt+F4
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    root.attributes('-toolwindow', True)

    # Make the window always on top
    root.attributes('-topmost', True)

    global main_frame, minutes_label, time_left_label
    main_frame = tk.Frame(root, bg='#a2d5c6', padx=10, pady=10)
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    minutes_label = tk.Label(main_frame, text='Timer:', bg='#a2d5c6', font=('Verdana', 10))
    minutes_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

    minutes_entry = ttk.Entry(main_frame)
    minutes_entry.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

    start_button = ttk.Button(main_frame, text='Start', command=lambda: start_timer(minutes_entry, time_left_label, start_button, root))
    start_button.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

    time_left_label = tk.Label(main_frame, text='', bg='#a2d5c6', font=('Verdana', 10))
    time_left_label.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
