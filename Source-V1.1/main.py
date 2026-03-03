import glob
import json
import tkinter
import os
import sys
from pickle import GLOBAL

LANG_USER = None

with open('Config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    if data['Lang'] is None:

        #Настройка
        window = tkinter.Tk()
        window.title('Select ur language')
        window.geometry('500x300')

        def selectLang(getLang):
            global LANG_USER

            data['Lang'] = getLang
            LANG_USER = data['Lang']

            print(LANG_USER)

            json.dump(data, open('Config.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
            window.destroy()

        Text = tkinter.Label(window, text='Pls select ur language')
        Text.pack(pady=10)

        ButtonRus = tkinter.Button(window, text='Russ', command=lambda: selectLang('Rus'), width=10, height=5)
        ButtonRus.pack(pady=10)

        ButtonEng = tkinter.Button(window, text='English', command=lambda: selectLang('Eng'), width=10, height=5)
        ButtonEng.pack(pady=10)

        #Заруск окан
        window.mainloop()

    else:
        LANG_USER = data['Lang']
        print(LANG_USER)


if LANG_USER == 'Rus':
    #Папки
    Folders = glob.glob('**/*.exe', recursive=True)
    print(Folders)

    flag = False
    for path in Folders:
        print(path)
        if path == r'Rus.exe':
            os.startfile(r'Rus.exe')
            flag = True
            print(flag)
            break

    if not flag:
        from tkinter import messagebox

        messagebox.showwarning('Ошибка','Не был найден exe файл с навзанием Rus.exe. Посмотрите в корневой папке программы есть ли такой файл и запустите его самостоятельно.')

else:
    # Папки
    Folders = glob.glob('**/*.exe', recursive=True)
    print(Folders)

    flag = False
    for path in Folders:
        print(path)
        if path == r'Eng.exe':
            os.startfile(r'Eng.exe')
            flag = True
            print(flag)
            break

    if not flag:
        from tkinter import messagebox

        messagebox.showwarning('Error','No Eng.exe file was found. Check the programs root folder for the file and run it yourself.')