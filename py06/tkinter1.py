import tkinter
from functools import partial

root = tkinter.Tk()
lb = tkinter.Label(root, text='hello world!', font='Arial 20')
b1 = tkinter.Button(root, bg='blue', fg='while', text='Button 1')
MyButton = partial(tkinter.Button, root, bg='blue', fg='while')
b2 = MyButton(text='123')
b3 = MyButton(text='124')
b4 = MyButton(text='125')

for i in [lb, b1, b2, b3, b4]:
    i.pack()
root.mainloop()