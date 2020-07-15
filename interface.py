from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from template_logic import *
from bot_logic import get_profiles
from template_window import *
import json

MESSAGES = {}
PROFILES = []

class Application(object):
    tabs_arr = []

    def __init__(self, master):
        self.master = master
        self.message_template = StringVar()
        self.main_window()

    def main_window(self):
        self.tabs = ttk.Notebook(self.master)
        self.tabs.pack(fill=BOTH, expand=True)
        self.bot_panel = ttk.Frame(self.tabs)

        self.tabs.add(self.bot_panel, text="Bot panel")

        self.widgets_bot_panel()
        self.menu()

    def widgets_bot_panel(self, profile_id=None):
        #рассылка
        self.lbl_message = Label(self.bot_panel, text='Рассылка', font='arial 15 bold')
        self.lbl_message.grid(row=0, column=0, pady=10)
        self.entry_message = Entry(self.bot_panel, width=30, bd=4)
        self.entry_message.grid(row=0, column=1, padx=10, pady=10)

        #анкета
        self.lbl_profile = Label(self.bot_panel, text=f'Текущий профиль {profile_id}',
            font='arial 15 bold')
        self.lbl_profile.grid(row=0, column=2)
        self.profile_combobox=ttk.Combobox(self.bot_panel, font='arial 10',
            justify='center')
        self.profile_items=get_profiles()
        self.profile_combobox['values'] = self.profile_items
        self.profile_combobox['state'] = 'readonly'
        self.profile_combobox.current(0)
        self.profile_combobox.grid(row=0, column=3)
        self.profile_combobox.bind("<<ComboboxSelected>>", self.callback)
        #submit
        submit_button = Button(self.bot_panel, text='Старт', font='Times 14 bold',
            command=lambda x:self.start(self.profile_combobox.get()))
        submit_button.grid(row=1, column=0)

    def callback(self, eventObject):
        print(eventObject)
        self.widgets_bot_panel(self.profile_combobox.get())


    def template_window(self):
        template_form = TemplateForm()

    def menu(self):
        self.menuBar = Menu(self.master)
        self.master.config(menu=self.menuBar)
        self.file = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Template', menu=self.file)
        self.file.add_command(label='template window',
            command=self.template_window)
        self.add_ = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Tabs', menu=self.add_)
        self.add_.add_command(label='Add tab',
            command=self.add_tab)

    def add_tab(self):
        login = simpledialog.askstring(
                "Login", "Input login", parent=self.master)
        password = simpledialog.askstring(
                "Password", "Input password", parent=self.master)
        self.tabs_arr.append(ttk.Frame(self.tabs))

        PROFILES.append({'login' : login,
                        'password': password,
                        'index': len(self.tabs_arr)})

        self.tabs.add(self.tabs_arr[-1],
            text=f"Login {PROFILES[len(self.tabs_arr) - 1]['login']}")
        Label(self.tabs_arr[-1],
            text=f"Login {PROFILES[len(self.tabs_arr) - 1]['login']}\n" + \
            f"Password {PROFILES[len(self.tabs_arr) - 1]['password']}",
             font='Arial 14 bold').grid(row=0, column=0)

def main():
    root = Tk()
    app = Application(root)
    root.title("Template window")
    root.geometry("1100x900")

    root.mainloop()

if __name__ == "__main__":
    main()
