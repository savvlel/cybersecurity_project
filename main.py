from tkinter import *
from tkinter import ttk

target_login = 'admin'
target_password = 'admin'
target_mcode = 'mcode'
target_pcode = 'pcode'
 
def click_entrybtn():
    login = entrylog.get()
    password = entrypass.get()
    if target_login == login and target_password == password:
        labellog.grid_remove()
        labelpass.grid_remove()
        entrylog.grid_remove()
        entrypass.grid_remove()
        entrybtn.grid_remove()
        regbtn.grid_remove()
        forgotpass.grid_remove()
        entrymcode.grid(row=2, column=5,columnspan=2)
        labelmcode.grid(row=2, column=2, columnspan=2)
        mcodebtn.grid(row=3, column=3, columnspan=2)
        remcodebtn.grid(row=4, column=3, columnspan=2)
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
        loadbtn.grid(row=3, column = 7, columnspan=2)
    if combobox.get() == 'Зашифровать':
        cypher.grid(row=3, column = 0, columnspan=3)
        cypherbtn.grid(row=5, column = 0, columnspan=2)
        cypher_result.grid(row=7, column = 0, columnspan=2)
        loadbtn.grid(row=3, column = 7, columnspan=2)

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

        
#def click_exitbtn():
#   Tk.destroy
#   root = Tk()     
#   root.title("Шифратор")    
#   root.geometry("300x250")    
#   labellog.grid(row=2, column=2, columnspan=2)
#   entrylog.grid(row=2, column=4, columnspan=3)
#   entrypass.grid(row=4, column=4, columnspan=3)
#   entrybtn.grid(row=5, column=2, columnspan=5)
#   forgotpass.grid(row=6, column=2, columnspan=5)
#   regbtn.grid(row=8, column=2, columnspan=5)  


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
exitbtn = Button(text='Выйти')
gobtn = Button(text='Перейти', command=click_gobtn)
#виджеты "зашифровать"
cypher = Entry()
cypher_result = Label()
cypherbtn = Button(text='Зашифровать', command = click_cypherbtn)
#виджеты "расшифровать"
decypher = Entry()
decypher_result = Label()
decypherbtn = Button(text='Расшифровать', command = click_decypherbtn)
#кнопка "скачать"
loadbtn = Button(text='Скачать')

#размещение виджетов
labellog.grid(row=2, column=2, columnspan=2)
labelpass.grid(row=4, column=2, columnspan=2)
entrylog.grid(row=2, column=4, columnspan=3)
entrypass.grid(row=4, column=4, columnspan=3)
entrybtn.grid(row=5, column=2, columnspan=5)
forgotpass.grid(row=6, column=2, columnspan=5)
regbtn.grid(row=8, column=2, columnspan=5)

root.mainloop()
