import json
from bot_logic import get_profiles
from bot_logic import get_user_id
from bot_logic import logout, login, get_offline
from template_logic import *
from template_window import *
from threading import Timer
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from ttkthemes import themed_tk as tk
from multiprocessing.pool import ThreadPool


MESSAGES = {}
PROFILES = []

class Application(object):
    tabs_arr = []
    buttons_arr = []
    begin_work_buttons_arr = []
    labels_arr = []
    begin_work_labels_arr = []
    amount_messages_arr = []
    current_message_arr = []
    entry_string_var_arr = []
    times_arr = []

    def __init__(self, master):
        self.master = master
        self.message_template = StringVar()
        self.main_window()

    def timeout(self, index):
        logout()
        self.begin_work_buttons_arr[index].config(bg='Blue')

    def main_window(self):
        self.tabs = ttk.Notebook(self.master)
        self.tabs.pack(fill=BOTH, expand=True)
        self.bot_panel = ttk.Frame(self.tabs)

        self.tabs.add(self.bot_panel, text="Bot panel")

        self.menu()

    def template_window(self):
        template_form = TemplateForm()

    def menu(self):
        self.menuBar = Menu(self.master)
        self.master.config(menu=self.menuBar)
        self.file = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Template', menu=self.file)
        self.file.add_command(
                                label='template window',
                                command=self.template_window
                    )
        self.add_ = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Tabs', menu=self.add_)
        self.add_.add_command(label='Add tab', command=self.add_tab)


    def start_message(self, login, password, message):
        curr_index = self.tabs.index(self.tabs.select())-1

        self.amount_messages_arr[curr_index] += 1

        self.labels_arr[curr_index].config(text=\
                    f"Current counter {self.amount_messages_arr[curr_index]}\n" + \
                    f"Current message {self.entry_string_var_arr[curr_index].get()}\n",
                    )

        if self.buttons_arr[curr_index]['bg'] == 'red':
            self.buttons_arr[curr_index]['bg'] = 'green'
            return None

        self.buttons_arr[curr_index].config(bg='red')


    def begin_work(self):
        
        curr_index = self.tabs.index(self.tabs.select())-1
        
        authorized = PROFILES[curr_index].get('logined', False)
        if not authorized:
            id_profile, logined = login(
                                PROFILES[curr_index]['login'],
                                PROFILES[curr_index]['password']
                            )
            PROFILES[curr_index]['user_id'] = id_profile
            PROFILES[curr_index]['logined'] = logined
        else:
            get_offline(
                        PROFILES[curr_index]['login'],
                        PROFILES[curr_index]['password']
                )
        print(PROFILES)
        self.begin_work_buttons_arr[curr_index].config(bg='Yellow')
        self.times_arr[curr_index] = Timer(10,
            lambda :self.timeout(curr_index)).start()


    def message_recieved(self, id_user, id_profile):
        mbox = messagebox.askquestion('Сообщение',
                f'ОТ {id_user}\n на анкету\n{id_profile}', icon='notification')
        if mbox == 'yes':
            for profile in PROFILES:
                if id_profile == profile['user_id']:
                    self.tabs.select(profile['index'])


    def add_tab(self):
        """
            Создание новой вкладки
            с виджетами
                отправить рассылку
                вывести в онлайн анкету ( выходит по таймеру)

        """
        login = simpledialog.askstring(
                                        "Login", "Input login",
                                        parent=self.master
                                    )
        password = simpledialog.askstring(
                                        "Password",
                                        "Input password",
                                        parent=self.master
                                    )

        self.tabs_arr.append(ttk.Frame(self.tabs))

        PROFILES.append(
                        {
                            'login' : login,
                            'password': password,
                            'user_id': '',
                            'index': len(self.tabs_arr) - 1
                        }
                    )

        self.amount_messages_arr.append(0)
        self.times_arr.append(0)

        self.tabs.add(self.tabs_arr[-1],
                    text=f"Login {PROFILES[len(self.tabs_arr) - 1]['login']}")

        curr_index = self.tabs.index(self.tabs.select())-1


        self.entry_string_var_arr.append(
                                        Entry(
                                                self.tabs_arr[-1],
                                                width=100
                                                )
                                    )
        self.entry_string_var_arr[-1].grid(row=0, column=1)

        self.buttons_arr.append(
                                Button(
                                    self.tabs_arr[-1],
                                    text='Начать рассылку',
                                    command=lambda :self.start_message(
                                        login=PROFILES[curr_index]['login'],
                                        password=PROFILES[curr_index]['password'],
                                        message=self.entry_string_var_arr[curr_index]
                                    ),
                                    bg='Green')
                            )
        self.buttons_arr[-1].grid(row=1, column=1)

        self.begin_work_buttons_arr.append(
                                        Button(
                                        self.tabs_arr[-1],
                                        text='Анкета оффлайн',
                                        command=self.begin_work,
                                        bg='Blue'
                                        )
                                    )
        self.begin_work_buttons_arr[-1].grid(row=2, column=1)

        self.begin_work_labels_arr.append(
                                        Label(
                                                self.tabs_arr[-1],
                                                text=f"Current time",
                                                font='Arial 14 bold'
                                            )
                                    )
        self.begin_work_labels_arr[-1].grid(row=0, column=0)


        self.labels_arr.append(
                                Label(
                                    self.tabs_arr[-1],
                                    text=f"Login {PROFILES[len(self.tabs_arr) - 1]['login']}\n" + \
                                    f"Password {PROFILES[len(self.tabs_arr) - 1]['password']}\n" + \
                                    f"Current counter {self.amount_messages_arr[curr_index]}\n" ,
                                    font='Arial 14 bold'
                                )
                        )
        self.labels_arr[-1].grid(row=0, column=0)

def main():
    root = Tk()
    app = Application(root)
    root.title("Template window")
    root.geometry("1100x900")

    root.mainloop()

if __name__ == "__main__":
    main()
