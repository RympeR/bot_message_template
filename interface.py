from tkinter import *
from tkinter import ttk
from template_logic import *
from bot_logic import *

class Application(object):
    def __init__(self, master):
        self.master = master
        self.message_template = StringVar()
        self.main_window()

    def main_window(self):
        self.tabs = ttk.Notebook(self.master)
        self.tabs.pack(fill=BOTH, expand=True)
        self.bot_panel = ttk.Frame(self.tabs)
        self.message_panel = ttk.Frame(self.tabs)
        self.tabs.add(self.bot_panel, text="Bot panel")
        self.tabs.add(self.message_panel, text="Message panel")
        self.widgets_message_panel()

    def widgets_bot_panel(self):
        pass

    def widgets_message_panel(self):
        entry_template = Text(self.message_panel, width=60, height=7)
        entry_template.place(x=50, y=60)
        scroll = Scrollbar(self.message_panel, command=entry_template.yview)
        scroll.place(x=540, y=90)
        entry_template.config(yscrollcommand=scroll.set)
        add_message_butn = Button(self.message_panel, text='Добавить шаблон', font='Times 12 bold').place(x=80,y=180)
        self.templates_listbox = Listbox(self.message_panel, height=15, width=60, selectmode=MULTIPLE)
        self.templates_listbox.place(x=400, y=180)
        self.result_template = Text(self.message_panel, width=60, height=7)
        self.result_template.place(x=50, y=60)
        self.lbl_amount_vars = Label(self.message_panel, text='Колличество', font='arial 15 bold')
        self.lbl_amount_vars.place(x=380, y=450)
        self.amount_vars= StringVar(self.master,'10')
        self.variants_amount = Spinbox(self.message_panel, from_=0,to=1000,wrap=True,textvariable=self.amount_vars,width=4)
        self.variants_amount.place(x=500, y=450)


def main():
    root = Tk()
    app = Application(root)
    root.title("Child center")
    root.geometry("800x680")
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
