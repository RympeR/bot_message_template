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
        entry_template.place(x=50, y=20)
        scroll = Scrollbar(command=entry_template.yview)
        scroll.place(x=540, y=50)
        entry_template.config(yscrollcommand=scroll.set)
        add_message_butn = Button(self.message_panel, text='Добавить шаблон', font='Times 12 bold').place(x=80,y=140)
        self.templates_listbox = Listbox(self.message_panel, height=15, width=60, selectmode=MULTIPLE)
        self.templates_listbox.place(x=400, y=140)



def main():
    root = Tk()
    app = Application(root)
    root.title("Child center")
    root.geometry("800x680")
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
