from tkinter import *
from tkinter import ttk
import pyotp 
import qrcode 
from PIL import Image

target_login = 'admin'
target_password = 'admin'
target_mcode = 'mcode'
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
        vidgets_to_add = [(labelmail, {'row': 1, 'column': 2, 'columnspan': 2}),
                          (entrymail, {'row': 1, 'column': 4, 'columnspan': 4}),
                          (sendmcodebtn, {'row': 2, 'column': 3, 'columnspan': 2}),
                          (entrymcode, {'row': 5, 'column': 5, 'columnspan': 2}),
                          (labelmcode, {'row': 5, 'column': 2, 'columnspan': 2}), 
                          (mcodebtn, {'row': 6, 'column': 3, 'columnspan': 2}),
                          (remcodebtn, {'row': 7, 'column': 3, 'columnspan': 2})]
        for vidget_and_location in vidgets_to_add:
            add_vid_to_grid_and_dict(*vidget_and_location)
    else:
        entrybtn["text"] = "Неверный логин или пароль"
        entrybtn['bg'] = 'red'  

def click_mcodebtn():
    mcode = entrymcode.get()
    if target_mcode == mcode:
        vidgets_to_remove = [labelmail, entrymail, sendmcodebtn, entrymcode, labelmcode, mcodebtn, remcodebtn]
        for vidget in vidgets_to_remove:
            remove_vid_from_grid_and_dict(vidget)
        vidgets_to_add = [(generateqrcodebtn, {'row': 1, 'column': 3, 'columnspan': 2}),
                          (labelqrcode, {'row': 2, 'column': 1, 'columnspan': 2}), 
                          (entryqrcode, {'row': 2, 'column': 3, 'columnspan': 2}),
                          (qrcodebtn, {'row': 3, 'column': 3, 'columnspan': 2})]
        for vidget_and_location in vidgets_to_add:
            add_vid_to_grid_and_dict(*vidget_and_location)
    else:
        mcodebtn["text"] = "Неверный код"
        mcodebtn['bg'] = 'red'

def click_generateqrcodebtn():
    key = 'GeeksforGeeksIsBestForEverything'
    uri = pyotp.totp.TOTP(key).provisioning_uri(name='dimas', issuer_name='pivas') 
    qrcode.make(uri).save("qr.png") 
    Image.open("qr.png").show()
    totp = pyotp.TOTP(key)
    return totp.verify(entryqrcode.get())

def click_qrcodebtn():
    if click_generateqrcodebtn() == True:
        vidgets_to_remove = [generateqrcodebtn, entryqrcode, labelqrcode, qrcodebtn]
        for vidget in vidgets_to_remove:
            remove_vid_from_grid_and_dict(vidget)
        vidgets_to_add = [(combobox, {'row': 0, 'column': 0, 'columnspan': 2}),
                          (gobtn, {'row': 1, 'column': 0, 'columnspan': 2}),
                          (exitbtn, {'row': 0, 'column': 7, 'columnspan': 1})]
        for vidget_and_location in vidgets_to_add:
            add_vid_to_grid_and_dict(*vidget_and_location)
    else:
        qrcodebtn["text"] = "Неверный код"
        qrcodebtn['bg'] = 'red'

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
    vidgets = [(labellog, {'row': 2, 'column': 2, 'columnspan': 2}),
               (labelpass, {'row': 4, 'column': 2, 'columnspan': 2}),
               (entrylog, {'row': 2, 'column': 4, 'columnspan': 3}),
               (entrypass, {'row': 4, 'column': 4, 'columnspan': 3}),
               (entrybtn, {'row': 5, 'column': 2, 'columnspan': 5}),
               (forgotpass, {'row': 6, 'column': 2, 'columnspan': 5}),
               (regbtn, {'row': 8, 'column': 2, 'columnspan': 5}),]
    for vidget_and_location in vidgets:
            add_vid_to_grid_and_dict(*vidget_and_location)
 

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
labelmail = Label(text='Введите почту')
entrymail = Entry()
sendmcodebtn = Button(text='Отправить')
entrymcode = Entry()
labelmcode = Label(text='Код подтверждения с почты')
mcodebtn = Button(text='Подтвердить', command=click_mcodebtn)
remcodebtn = Button(text='Отправить ещё раз')
#виджеты подтверждения через QR код
generateqrcodebtn = Button(text='Сгенерировать QR-код', command=click_generateqrcodebtn)
entryqrcode = Entry()
labelqrcode = Label(text='Введите код')
qrcodebtn = Button(text='Подтвердить', command=click_qrcodebtn)
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
