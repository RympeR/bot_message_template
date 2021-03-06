from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from template_logic import *

class TemplateForm(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Template window")
        self.geometry("1100x1100")

        self.entry_template = Text(self,
            font='Times 14', width=60, height=7)
        self.entry_template.grid(row=0, column=0, pady=20)

        scroll = Scrollbar(self, command=self.entry_template.yview)
        scroll.grid(row=0, column=1, sticky=W)
        self.entry_template.config(yscrollcommand=scroll.set)

        add_message_butn = Button(self, text='Добавить шаблон',
            font='Times 12 bold',
             command=self.add_template).grid(row=0, column=2, pady=(0, 20))

        self.lbl_template = Label(self, text='Текущие шаблоны',
            font='arial 15 bold')
        self.lbl_template.grid(row=1, column=0)

        self.templates_listbox = Listbox(self,
            height=15, width=60, font='Time 14', selectmode=MULTIPLE)
        self.templates_listbox.grid(row=1, column=2)

        self.lbl_result = Label(self,
            text='Готовые рассылки', font='arial 15 bold')
        self.lbl_result.grid(row=2, column=0, pady=(20, 20))

        self.result_template = Text(self, width=60, height=10)
        self.result_template.grid(row=2, column=1, columnspan=2, pady=(20, 20))

        self.lbl_amount_vars = Label(self, text='Колличество',
            font='arial 15 bold')
        self.lbl_amount_vars.grid(row=3, column=0, pady=(20, 20))

        self.amount_vars= StringVar(self,'10')
        self.variants_amount = Spinbox(self, from_=0,to=1000,
            wrap=True,textvariable=self.amount_vars,width=4)
        self.variants_amount.grid(row=3, column=1, pady=(20, 20))

        submit_button = Button(self,
            text='Создать', command=self.get_messages,
            font='Times 14 bold').grid(row=4, column=0)
        self.display_templates()

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
