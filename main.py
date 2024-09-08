import tkinter as tk
import random as rd


root = tk.Tk()
root.title('BubbleBoard')
root.geometry('800x600+200+20')
root.resizable(False, True)
photo = tk.PhotoImage(file='smile.png')
root.iconphoto(False, photo)
root.config(bg='#dcb480')

# Виджет Label, основные параметры.

label_1 = tk.Label(root, text='Start the Game\n Buddy!',
                   bg='#dcb480',
                   fg='white',
                   font=('Liberation', 20, 'bold'),
                   padx=40,
                   pady=40,
                   width=20,
                   #anchor='w',
                   relief=tk.RAISED,
                   bd=20,
                   justify=tk.CENTER
                   )
label_1.pack()

# Виджет Button, основные параметры

def add_new_label():
    new_label = tk.Label(root, text='It is new me')
    new_label.pack()

count = 0

def counter():
    '''

    Функция для подсчета количества нажатий на кнопку button_3.
    Также блокирует нажатие кнопки button_1 если счетчик нечетный и button_2 если четный.

    '''
    global count
    count += 1
    button_3['text'] = f'Счетчик нажатий: {count}'
    if count % 2 == 0:
        button_2['state'] = tk.DISABLED
        button_1['state'] = tk.NORMAL
    else:
        button_1['state'] = tk.DISABLED
        button_2['state'] = tk.NORMAL

def chage_bg():
    '''

    Randomly change bg color in root.config.

    '''
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)

    root.config(bg=f'#{r:02x}{g:02x}{b:02x}')
    print(f'#{r:x}{g:x}{b:x}', r, g, b)


button_1 = tk.Button(root, text="Let's go", command=chage_bg)
button_2 = tk.Button(root, text="Other button", command=lambda: tk.Label(root, text='Lambda button').pack())
button_3 = tk.Button(root, text=f'Счетчик нажатий: {count}', command=counter, bg='blue', activebackground='red')
button_1.pack()
button_2.pack()
button_3.pack()




root.mainloop()
