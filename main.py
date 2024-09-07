import tkinter as tk

root = tk.Tk()
root.title('BubbleBoard')
root.geometry('800x600+200+20')
root.resizable(False, True)
photo = tk.PhotoImage(file='smile.png')
root.iconphoto(False, photo)
root.config(bg='#dcb480')
label_1 = tk.Label(root, text='Start the Game\n Buddy!',
                   bg='#dcb480',
                   fg='white',
                   font=('Liberation', 20, 'bold'),
                   padx=40,
                   pady=40,
                   width=20,
                   anchor='w',
                   relief=tk.RAISED,
                   bd=20,
                   justify=tk.RIGHT
                   )
label_1.pack()

root.mainloop()
