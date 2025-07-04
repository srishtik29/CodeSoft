from tkinter import*

window = Tk()
window.title("Simple Calculator")
window.geometry('400x300')
window.configure(bg='#f0f4f7')

def calculate(z):
    try:
        a = (e1.get())
        b = (e2.get())
        x=int(a)
        y=int(b)
        if z == 1:
            ans = x + y
        elif z == 2:
            ans = x - y
        elif z == 3:
            ans = x * y
        elif z == 4:
            ans = x / y 
        else:
            ans = "Unknown operator"
        answer.delete(0,END)
        answer.insert(0,str(ans))
    except ValueError:
        answer.config(text="Invalid input")

heading = Label(window, text="Simple Calculator", font=('Georgia', 16, 'bold'), fg='#2c3e50', bg='#f0f4f7')
heading.grid(row=0, column=0, columnspan=2, pady=10)

n1=Label(window,text='Number 1: ',font='Georgia 11 bold')
n1.grid(row=1,column=0,padx=15,pady=10)
e1=Entry(window)
e1.grid(row=1,column=1,padx=15,pady=10)

n2=Label(window,text='Number 2: ',font='Georgia 11 bold')
n2.grid(row=2,column=0,padx=15,pady=10)
e2=Entry(window)
e2.grid(row=2,column=1,padx=15,pady=10)

result=Label(window,text='Result: ',font='Georgia 11 bold')
result.grid(row=6,column=0,padx=15,pady=10)
answer=Entry(window)
answer.grid(row=6,column=1,padx=15,pady=10)

button_width=5
style={'width': button_width, 'bg': '#3498db', 'fg': 'white', 'font': ('Georgia', 11)}
add=Button(window,text='  +  ',**style,command=lambda: calculate(1))
add.grid(row=4,column=0,padx=5,pady=10)

sub=Button(window,text='  -  ',**style,command=lambda: calculate(2))
sub.grid(row=4,column=1,padx=5,pady=10)

mul=Button(window,text='  x  ',**style,command=lambda: calculate(3))
mul.grid(row=5,column=0,padx=5,pady=10)

div=Button(window,text='  /  ',**style,command=lambda: calculate(4))
div.grid(row=5,column=1,padx=5,pady=10)

window.mainloop()


