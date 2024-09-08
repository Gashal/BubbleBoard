import tkinter as tk


root = tk.Tk()
root.title('BubbleBoard')
root.geometry('800x600+200+20')
root.resizable(False, True)
photo = tk.PhotoImage(file='smile.png')
root.iconphoto(False, photo)
root.config(bg='#dcb480')

for i in range(5):
    for j in range(2):
        tk.Button(root, text=f'Button {i}:{j}').grid(row=i, column=j, stick='we')

# button_1 = tk.Button(root, text='Button 1')
# button_2 = tk.Button(root, text='Button 2 is too long')
# button_3 = tk.Button(root, text='Button 3')
# button_4 = tk.Button(root, text='Button 4')
# button_5 = tk.Button(root, text='Button 5')
# button_6 = tk.Button(root, text='Button 6')
#
# button_1.grid(row=0, column=0, stick='we')
# button_2.grid(row=0, column=1)
# button_3.grid(row=1, column=0,stick='we')
# button_4.grid(row=1, column=1, stick='we')
# button_5.grid(row=2, column=0, columnspan=2, stick='we')
# button_6.grid(row=0, column=2, rowspan=3, stick='ns')

root.grid_columnconfigure(0, minsize=200)
root.grid_columnconfigure(1, minsize=100)

root.mainloop()