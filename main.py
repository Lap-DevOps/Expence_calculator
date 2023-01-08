# This is example of Python program.
# Small test Python program to work with TKInter as desktop app and SQLite.

import tkinter as tk

# initiate main window and app name
main_window = tk.Tk()
main_window.title("My App")

# make several frames in window and locate them
frame_add_form = tk.Frame(main_window, width=150, height=150, bg="green")
frame_statistic = tk.Frame(main_window, width=150, height=150, bg="yellow")
frame_list = tk.Frame(main_window, width=300, height=150, bg="red")
frame_add_form.grid(row=0, column=0)
frame_statistic.grid(row=0, column=1)
frame_list.grid(row=1, column=0, columnspan=2)

if __name__ == '__main__':
    main_window.mainloop()
