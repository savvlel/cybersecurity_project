from tkinter import *
from tkinter import ttk

target_login = 'admin'
target_password = 'admin'
target_mcode = 'mcode'
target_pcode = 'pcode'
current_vidgets = {'Label': {}, 'Entry': {}, 'Button': {}, 'Combobox': {}}

def add_vid_to_grid_and_dict(vidget, location_parameters):
    vidget.grid(row=location_parameters['row'], column=location_parameters['column'], columnspan=location_parameters['columnspan'])
    vidget_type = vidget.winfo_class()
    vidget_name = vidget.winfo_name()
    current_vidgets[vidget_type][vidget_name] = vidget

def remove_vid_from_grid_and_dict(vidget):
    vidget.grid_remove()
    vidget_type = vidget.winfo_class()
    vidget_name = vidget.winfo_name()
    current_vidgets[vidget_type].pop(vidget_name)

def click_entrybtn():
    login = entrylog.get()
    password = entrypass.get()
    if target_login == login and target_password == password:
        vidgets_to_remove = [labellog, labelpass, entrylog, entrypass, entrybtn, regbtn, forgotpass]
        for vidget in vidgets_to_remove:
            remove_vid_from_grid_and_dict(vidget)
        vidgets_to_add = [(entrymcode, {'row': 2, 'column': 5, 'columnspan': 2}),
                          (labelmcode, {'row': 2, 'column': 2, 'columnspan': 2}), 
                          (mcodebtn, {'row': 3, 'column': 3, 'columnspan': 2}),
                          (remcodebtn, {'row': 4, 'column': 3, 'columnspan': 2})]
        for vidget_and_location in vidgets_to_add:
            add_vid_to_grid_and_dict(*vidget_and_location)
    else:
        entrybtn["text"] = "Неверный логин или пароль"
        entrybtn['bg'] = 'red'  

def click_mcodebtn():
    mcode = entrymcode.get()
    if target_mcode == mcode:
        entrymcode.grid_remove()
        labelmcode.grid_remove()
        mcodebtn.grid_remove()
        remcodebtn.grid_remove()
        entrypcode.grid(row=2, column=5,columnspan=2)
        labelpcode.grid(row=2, column=2, columnspan=2)
        pcodebtn.grid(row=3, column=3, columnspan=2)
        repcodebtn.grid(row=4, column=3, columnspan=2)
    else:
        mcodebtn["text"] = "Неверный код"
        mcodebtn['bg'] = 'red'

def click_pcodebtn():
    pcode = entrypcode.get()
    if target_pcode == pcode:
        entrypcode.grid_remove()
        labelpcode.grid_remove()
        pcodebtn.grid_remove()
        repcodebtn.grid_remove()
        combobox.grid(row=0, column=0, columnspan=2)
        gobtn.grid(row=1, column=0, columnspan=2)
        exitbtn.grid(row=0, column=7, columnspan=1)
    else:
        pcodebtn["text"] = "Неверный код"
        pcodebtn['bg'] = 'red'

def click_gobtn():
    print(combobox.get)
    if combobox.get() == 'Расшифровать':
        decypher.grid(row=3, column = 0, columnspan=3)
        decypherbtn.grid(row=5, column = 0, columnspan=2)
        decypher_result.grid(row=7, column = 0, columnspan=2)
        combobox2.grid(row=3, column=7, columnspan=2)
    if combobox.get() == 'Зашифровать':
        cypher.grid(row=3, column = 0, columnspan=3)
        cypherbtn.grid(row=5, column = 0, columnspan=2)
        cypher_result.grid(row=7, column = 0, columnspan=2) 
        combobox2.grid(row=3, column=7, columnspan=2) 

def caesar_encryption(plaintext):
    encryption_str = ''
    plaintext = cypher.get()
    for i in plaintext:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 + 3) % 26) 
            encryption_str = encryption_str + chr(temp)                              
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + 3) % 26)
            encryption_str = encryption_str + chr(temp)
        else:
            encryption_str = encryption_str + i  
    return(encryption_str)
       

def caesar_decryption(ciphertext):
    decryption_str = ''
    ciphertext = decypher.get()
    for i in ciphertext:
        if i.isupper():
            if ((ord(i) - 65 - 3) < 0):
                temp = 65 + ((ord(i) - 65 - 3 + 26) % 26) 
            else:
                temp = 65 + ((ord(i) - 65 - 3) % 26) 
            decryption_str = decryption_str + chr(temp)                              
        elif i.islower():
            if ((ord(i) - 97 - 3) < 0):
                temp = 97 + ((ord(i) - 97 - 3 + 26) % 26) 
            else:
                temp = 97 + ((ord(i) - 97 - 3) % 26) 
            decryption_str = decryption_str + chr(temp)
        else:
            decryption_str = decryption_str + i  
    return(decryption_str)

def click_cypherbtn():
   cypher_result['text'] = caesar_encryption(cypher.get())

def click_decypherbtn():
   decypher_result['text'] = caesar_decryption(decypher.get())

def click_exitbtn():
    for vidget_class_name in current_vidgets:
        for vidget in current_vidgets[vidget_class_name]:
            vidget.grid_remove()
        current_vidgets[vidget_class_name].clear()
    draw_entry_window_vidgets()

def draw_entry_window_vidgets():
    vidgets = [labellog, labelpass, entrylog, entrypass, entrybtn, forgotpass, regbtn]
    labellog.grid(row=2, column=2, columnspan=2)
    labelpass.grid(row=4, column=2, columnspan=2)
    entrylog.grid(row=2, column=4, columnspan=3)
    entrypass.grid(row=4, column=4, columnspan=3)
    entrybtn.grid(row=5, column=2, columnspan=5)
    forgotpass.grid(row=6, column=2, columnspan=5)
    regbtn.grid(row=8, column=2, columnspan=5)




#окно
root = Tk()     # создаем корневой объект - окно
root.title("Шифратор")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размеры окна
 
#сетка
for c in range(9): root.columnconfigure(index=c, weight=1)
for r in range(9): root.rowconfigure(index=r, weight=1)

#виджеты окна входа
labellog = Label(text='Логин')
labelpass = Label(text='Пароль')
entrylog = Entry()
entrypass = Entry()
entrybtn = Button(text='Войти', command=click_entrybtn)
forgotpass = Button(text='Забыли пароль?')
regbtn = Button(text='Зарегистрироваться')
#виджеты подтверждения через код с почты
entrymcode = Entry()
labelmcode = Label(text='Код подтверждения с почты')
mcodebtn = Button(text='Подтвердить', command=click_mcodebtn)
remcodebtn = Button(text='Отправить ещё раз')
#виджеты подтверждения через код с телефона
entrypcode = Entry()
labelpcode = Label(text='Код подтверждения с телефона')
pcodebtn = Button(text='Подтвердить', command=click_pcodebtn)
repcodebtn = Button(text='Отправить ещё раз')
#виджеты залогиненного пользователя
options = ["Зашифровать", "Расшифровать", "Мои шифры", "Скачать"]
combobox = ttk.Combobox(values=options)
exitbtn = Button(text='Выйти', command=click_exitbtn)
gobtn = Button(text='Перейти', command=click_gobtn)
#виджеты "зашифровать"
cypher = Entry()
cypher_result = Label()
cypherbtn = Button(text='Зашифровать', command = click_cypherbtn)
options2 = ['RSA', 'Кузнечик']
combobox2 = ttk.Combobox(values=options2)
#виджеты "расшифровать"
decypher = Entry()
decypher_result = Label()
decypherbtn = Button(text='Расшифровать', command = click_decypherbtn)

#размещение виджетов
draw_entry_window_vidgets()

root.mainloop()
