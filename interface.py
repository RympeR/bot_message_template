from tkinter import *
from tkinter import ttk
from template_logic import *
from bot_logic import *
import json

MESSAGES = {}

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
        self.display_templates()
        self.widgets_bot_panel()

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

    def widgets_message_panel(self):
        self.entry_template = Text(self.message_panel,
            font='Times 14', width=60, height=7)
        self.entry_template.grid(row=0, column=0, pady=20)

        scroll = Scrollbar(self.message_panel, command=self.entry_template.yview)
        scroll.grid(row=0, column=1, sticky=W)
        self.entry_template.config(yscrollcommand=scroll.set)

        add_message_butn = Button(self.message_panel, text='Добавить шаблон',
            font='Times 12 bold',
             command=self.add_template).grid(row=0, column=2, pady=(0, 20))

        self.lbl_template = Label(self.message_panel, text='Текущие шаблоны',
            font='arial 15 bold')
        self.lbl_template.grid(row=1, column=0)

        self.templates_listbox = Listbox(self.message_panel,
            height=15, width=60, font='Time 14', selectmode=MULTIPLE)
        self.templates_listbox.grid(row=1, column=2)

        self.lbl_result = Label(self.message_panel,
            text='Готовые рассылки', font='arial 15 bold')
        self.lbl_result.grid(row=2, column=0, pady=(20, 20))

        self.result_template = Text(self.message_panel, width=60, height=10)
        self.result_template.grid(row=2, column=1, columnspan=2, pady=(20, 20))

        self.lbl_amount_vars = Label(self.message_panel, text='Колличество',
            font='arial 15 bold')
        self.lbl_amount_vars.grid(row=3, column=0, pady=(20, 20))

        self.amount_vars= StringVar(self.master,'10')
        self.variants_amount = Spinbox(self.message_panel, from_=0,to=1000,
            wrap=True,textvariable=self.amount_vars,width=4)
        self.variants_amount.grid(row=3, column=1, pady=(20, 20))

        submit_button = Button(self.message_panel,
            text='Создать', command=self.get_messages,
            font='Times 14 bold').grid(row=4, column=0)

    def callback(self, eventObject):
        print(eventObject)
        self.widgets_bot_panel(self.profile_combobox.get())


    def start(self, profile_id):
        print(profile_id)

    def get_messages(self):
        text = [row.replace('\n', '') for row in self.get_templates_selected()]
        print(text)
        amount = int(self.amount_vars.get())
        self.result_template.delete(1.0, END)
        self.result_template.insert(1.0, "\n".join(create_message(amount, text)))


    def clear_templates(self):
        self.templates_listbox.delete(0, END)

    def add_template(self):
        with open('templates.txt', 'a', encoding='utf-8') as f:
            f.write(self.entry_template.get(1.0, END))
        self.display_templates()


    def display_templates(self):
        self.clear_templates()
        with open('templates.txt', 'r', encoding='utf-8') as f:
            text = f.readlines()
            for row in text:
                self.templates_listbox.insert(END, row)


    def get_templates_selected(self):
        UsrFCList = []
        selctd_indices = self.templates_listbox.curselection()
        lst_select = list(selctd_indices)
        for i in lst_select:
            UsrFCList.append(self.templates_listbox.get(i))
        return UsrFCList

def main():
    root = Tk()
    app = Application(root)
    root.title("Child center")
    root.geometry("1100x900")

    root.mainloop()

if __name__ == "__main__":
    main()
