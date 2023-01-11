# This is example of Python program.
# Small test Python program to work with TKInter as desktop app and SQLite.
# This is small home expense calculator.


import tkinter as tk


import expenses_helper as eh

# initiate main window and app name
main_window = tk.Tk()
main_window.title("My App")


# make several frames in window and locate them
frame_add_form = tk.Frame(main_window, bg="green")
frame_statistic = tk.Frame(main_window, bg="yellow")
frame_list = tk.Frame(main_window, bg="red")

frame_add_form.grid(row=0, column=0, sticky='ns')
frame_statistic.grid(row=0, column=1)
frame_list.grid(row=1, column=0, columnspan=2, sticky='we')

# labels in statistic
l_most_common_text = tk.Label(frame_statistic, text="Most common item")
l_most_common_value = tk.Label(frame_statistic, text=eh.get_most_common_item(), font="Helvetica 14 bold")
l_exp_item_text = tk.Label(frame_statistic, text="Most expensive  item")
l_ext_item_value = tk.Label(frame_statistic, text=eh.get_most_exp_item(), font="Helvetica 14 bold")
l_exp_day_text = tk.Label(frame_statistic, text="Most expansive day")
l_exp_day_value = tk.Label(frame_statistic, text=eh.get_most_exp_day(), font="Helvetica 14 bold")
l_exp_month_text = tk.Label(frame_statistic, text="Most expansive month")
l_exp_month_value = tk.Label(frame_statistic, text=eh.get_most_exp_month(), font="Helvetica 14 bold")

l_most_common_text.grid(row=0, column=0, sticky='w', padx=10, pady=10)
l_most_common_value.grid(row=0, column=1, sticky='e', padx=10, pady=10)
l_exp_item_text.grid(row=1, column=0, sticky='w', padx=10, pady=10)
l_ext_item_value.grid(row=1, column=1, sticky='e', padx=10, pady=10)
l_exp_day_text.grid(row=2, column=0, sticky='w', padx=10, pady=10)
l_exp_day_value.grid(row=2, column=1, sticky='e', padx=10, pady=10)
l_exp_month_text.grid(row=3, column=0, sticky='w', padx=10, pady=10)
l_exp_month_value.grid(row=3, column=1, sticky='e', padx=10, pady=10)

# labels for forms
l_temp_frame_add_form = tk.Label(frame_add_form, text="Add frame form")
l_temp_frame_list = tk.Label(frame_list, text="Statistic")
l_temp_frame_add_form.pack(expand=True, padx=20, pady=20)
l_temp_frame_list.pack(expand=True, padx=20, pady=20)

if __name__ == '__main__':
    main_window.mainloop()
