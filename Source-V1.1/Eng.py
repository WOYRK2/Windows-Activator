import tkinter as tk
import os
import json

#Окно
window = tk.Tk()
window.title(r"Рус/Welcome)")
window.geometry('1920x1080')
#НАстройка

text_Label = tk.Label(window, text='Select ur windows')
text_Label.pack(pady=10)

def ActWin(Win):
    print('-----------------------------')

    with open('Config.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        for D2 in data['windows']:
            if D2 == Win:
                NameWin = D2
                KeyWint = data['windows'][D2]
                print(f'{NameWin} - {KeyWint}')

                os.system(f'slmgr /ipk {KeyWint}')
                os.system('slmgr /skms kms.digiboy.ir')
                os.system('slmgr /ato')

def CreateButton():
    with open(r'Config.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        for Data2 in data['windows']:
            d1 = data['windows'][Data2]
            print(f'{Data2} - {d1}')

            button = tk.Button(window, text=Data2, command=lambda n=Data2: ActWin(n))
            button.pack(pady=10)


CreateButton()
window.mainloop()
