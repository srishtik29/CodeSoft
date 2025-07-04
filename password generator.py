from tkinter import*
import random

window = Tk()
window.geometry('500x250')
window.title('Password Generator')
window.configure(bg='#fce4ec')

def copy():
    pswd = e1.get()
    if pswd:
        window.clipboard_clear()
        window.clipboard_append(pswd)
        

def pass_generate():
    s="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={[}]|\:;'<,>.?/"
    str=""
    x=e2.get()
    a=int(x)
    for i in range(a):
        str+=random.choice(s)
    e1.insert(0,str)    

# Heading
heading = Label(window, text='Password Generator', font='Georgia 18 bold', bg='#fce4ec', fg='#880e4f')
heading.grid(row=0, column=0, columnspan=3, pady=10)

# Password Output
l1 = Label(window, text='Password:', font='Georgia 11 bold', bg='#fce4ec')
l1.grid(row=1, column=0, padx=10, pady=10, sticky=E)
e1 = Entry(window, width=35, font=('Courier New', 10))
e1.grid(row=1, column=1, padx=5)
copy_btn = Button(window, text="Copy", command=copy, bg='#ff80ab', fg='white')
copy_btn.grid(row=1, column=2, padx=5)

# Length input
l2 = Label(window, text='Enter Length:', font='Georgia 11 bold', bg='#fce4ec')
l2.grid(row=2, column=0, padx=10, pady=10, sticky=E)
e2 = Entry(window, width=10)
e2.grid(row=2, column=1, sticky=W)

# Generate button
generate = Button(window, text='Generate Password', font='Georgia 11 bold', bg='#ec407a', fg='white', command=pass_generate)
generate.grid(row=3, column=0, columnspan=3, pady=20)

window.mainloop()

