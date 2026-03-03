import tkinter as tk
import os
import json

#Окно
window = tk.Tk()
window.title(r"Рус/Добро пожаловать)")
#НАстройка

text_Label = tk.Label(window, text='Выберите вашу виндовс для кативации')
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

READY_SIZE = 0
def CreateButton():
    global READY_SIZE
    with open(r'Config.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        for Data2 in data['windows']:
            d1 = data['windows'][Data2]
            print(f'{Data2} - {d1}')

            button = tk.Button(window, text=Data2, command=lambda n=Data2: ActWin(n))
            button.pack(pady=10)

            READY_SIZE += 60
            window.geometry(f'800x{READY_SIZE}')


CreateButton()
window.mainloop()
