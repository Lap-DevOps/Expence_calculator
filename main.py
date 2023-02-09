# This is example of Python program.
# Small expense calculator

import tkinter as tk
from tkinter import messagebox as mbox
from tkinter import ttk

from tkcalendar import DateEntry

import expenses_helper as eh


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My App')
        self.lang = 'ru'
        self.schema = eh.get_lang_schema(self.lang)
        self.style = ttk.Style()
        self.style.configure('ErrLbl.TLabel', foreground='red', padding=(10, 10, 60, 10))
        self.style.configure('Smpllbl.TLabel', padding=(10, 10, 60, 10))
        self.style.configure('BldLbl.TLabel', font=('Helvetica', 13, 'bold'),
                             padding=(0, 10, 0, 10))
        self['background'] = '#EBEBEB'
        self.put_frames()
        self.put_menu()
        self.popup = Popup(self)

    def put_menu(self):
        self.config(menu=MainMenu(self))

    def put_frames(self):
        self.add_form_frame = AddForm(self).grid(row=0, column=0, sticky='nswe')
        self.stat_frame = StatFrame(self).grid(row=0, column=1, sticky='nswe')
        self.table_frame = TableFrame(self).grid(row=1, column=0, columnspan=2, sticky='nswe')

    def refresh(self):
        all_names = [f for f in self.children]
        for f_name in all_names:
            self.nametowidget(f_name).destroy()
        self.put_frames()
        self.put_menu()

    def switch_lang(self, language):
        self.lang = language
        self.schema = eh.get_lang_schema(language)
        self.refresh()


class AddForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.items = eh.get_all_expenses_items()
        self.put_widgets()

    def put_widgets(self):
        self.l_choose = ttk.Label(self, text=self.master.schema['l_choose'], style='Smpllbl.TLabel')
        self.f_choose = ttk.Combobox(self, values=self.items['names'])
        self.l_amount = ttk.Label(self, text=self.master.schema['l_amount'], style='Smpllbl.TLabel')
        self.f_amount = ttk.Entry(self, justify=tk.RIGHT,
                                  validate='key', validatecommand=(self.register(self.validate_amount), '%P'))
        self.l_date = ttk.Label(self, text=self.master.schema['l_date'], style='Smpllbl.TLabel')
        self.f_date = DateEntry(self, foreground='black', normalforeground='black',
                                selectforeground='red', background='white',
                                date_pattern='dd-mm-YYYY')
        self.btn_submit = ttk.Button(self, text=self.master.schema['btn_submit'], command=self.form_submit)
        self.l_choose.grid(row=0, column=0, sticky='w', )
        self.f_choose.grid(row=0, column=1, sticky='e', )
        self.l_amount.grid(row=1, column=0, sticky='w', )
        self.f_amount.grid(row=1, column=1, sticky='e', )
        self.l_date.grid(row=2, column=0, sticky='w', )
        self.f_date.grid(row=2, column=1, sticky='e', )
        self.btn_submit.grid(row=3, column=0, columnspan=2, sticky='n', )
        self.f_date._top_cal.overrideredirect(False)

    def validate_amount(self, input):
        try:
            x = float(input)
            return True
        except ValueError:
            self.bell()
            return False

    def form_submit(self):
        flag = True

        payment_date = eh.get_timestamp_from_str(self.f_date.get())

        try:
            expanse_id = self.items['accordance'][self.f_choose.get()]
            amount = float(self.f_amount.get())
            self.l_choose['style'] = "Smpllbl.TLabel"
            self.l_amount['style'] = "Smpllbl.TLabel"
        except KeyError:
            if self.f_choose.get() != '':
                pass
            else:
                flag = False
                self.l_choose['style'] = "ErrLbl.TLabel"
                self.bell()
        except ValueError:
            flag = False
            self.l_amount['style'] = "ErrLbl.TLabel"
            self.bell()

        if flag:
            insert_payments = (amount, payment_date, expanse_id)
            if eh.insert_payments(insert_payments):
                self.master.refresh()


class StatFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        l_most_common_text = ttk.Label(self, text=self.master.schema['l_most_common'], style='Smpllbl.TLabel')
        l_most_common_value = ttk.Label(self, text=eh.get_most_common_item(), style='BldLbl.TLabel')
        l_exp_item_text = ttk.Label(self, text=self.master.schema['l_exp_item'], style='Smpllbl.TLabel')
        l_exp_item_value = ttk.Label(self, text=eh.get_most_expansive_item(), style='BldLbl.TLabel')
        l_exp_day_text = ttk.Label(self, text=self.master.schema['l_exp_day'], style='Smpllbl.TLabel')
        l_exp_day_value = ttk.Label(self, text=eh.get_most_expansive_day(self.master.lang), style='BldLbl.TLabel')
        l_exp_month_text = ttk.Label(self, text=self.master.schema['l_exp_month'], style='Smpllbl.TLabel')
        l_exp_month_value = ttk.Label(self, text=eh.get_most_expansive_month((self.master.lang)), style='BldLbl.TLabel')

        l_most_common_text.grid(row='0', column='0', sticky='w', )
        l_most_common_value.grid(row='0', column='1', sticky='e', )
        l_exp_item_text.grid(row='1', column='0', sticky='w', )
        l_exp_item_value.grid(row='1', column='1', sticky='e', )
        l_exp_day_text.grid(row='2', column='0', sticky='w', )
        l_exp_day_value.grid(row='2', column='1', sticky='e', )
        l_exp_month_text.grid(row='3', column='0', sticky='w', )
        l_exp_month_value.grid(row='3', column='1', sticky='e', )


class TableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        table = ttk.Treeview(self, show='headings', )
        l = self.master.schema
        heads = [
            l['l_head_id'],
            l['l_head_name'],
            l['l_head_amount'],
            l['l_head_date']
        ]
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')

        for row in eh.get_table_data():
            table.insert('', tk.END, values=row, )
        scroll_pane = ttk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


class MainMenu(tk.Menu):
    def __init__(self, mainwindow):
        super().__init__(mainwindow)

        file_menu = tk.Menu(self)
        option_menu = tk.Menu(self)
        help_menu = tk.Menu(self)

        file_menu.add_command(label="Refresh", command=mainwindow.refresh)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=lambda: mainwindow.popup.show('quit'))

        lang_menu = tk.Menu(option_menu)
        self.s_var = tk.StringVar()
        self.s_var.set(self.master.lang)
        lang_menu.add_radiobutton(label="Русский", variable=self.s_var, value='ru',
                                  command=lambda: mainwindow.switch_lang(self.s_var.get()))
        lang_menu.add_radiobutton(label='English', variable=self.s_var, value='en',
                                  command=lambda: mainwindow.switch_lang(self.s_var.get()))
        option_menu.add_cascade(label='Switch language', menu=lang_menu)
        option_menu.add_separator()
        option_menu.add_command(label='Switch theme')
        help_menu.add_command(label='About Us', command=lambda: mainwindow.popup.show('faq'))
        help_menu.add_separator()
        help_menu.add_command(label='FAQ', command=lambda: mainwindow.popup.show('faq'))

        self.add_cascade(label='File', menu=file_menu)
        self.add_cascade(label='Options', menu=option_menu)
        self.add_cascade(label='Help', menu=help_menu)


class Popup:
    def __init__(self, master):
        self.master = master

    def quit(self):
        answer = mbox.askquestion('Quit', 'A You sure?')
        if answer == "yes":
            self.master.destroy()
        else:
            pass

    def faq(self):
        self.master.bell()
        mbox.showinfo('FAQ', 'This functionality not reade yet')

    def show(self, window_type):
        getattr(self, window_type)()


if __name__ == '__main__':
    app = App()
    app.mainloop()
