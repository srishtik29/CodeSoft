from tkinter import*
import random

window=Tk()
window.title("Game")
window.geometry('450x400')
window.config(bg='#FFD66B')

ch=['rock','paper','scissors']

def play(x):
    l=ch[x]
    comp=random.choice(ch)
    c_choice.config(text=f"Computer chose : {comp}")
    if(l==comp):
        c_label.config(text="It's a tie!")
    elif((l=='rock' and comp=='scissors')or (l=='scissors' and comp=='paper') or (l=='paper' and comp=='rock') ):
        c_label.config(text="YOU WON 🤩")
    else:
        c_label.config(text="COMPUTER WON 😥")

heading=Label(window,text='ROCK PAPER SCISSORS !',font=("Georgia", 18, "bold"), bg="#4DA8DA", fg="#F5F5F5")
heading.pack(pady=20)

c_choice=Label(window,font=("Georgia", 14, "bold"), bg='#FFD66B', fg="#00809D")
c_choice.pack(pady=20)

c_label=Label(window,font=("Georgia", 14, "bold"), bg='#FFD66B', fg="#06923E")
c_label.pack(pady=20)

butoon= Frame(window, bg='#FFD66B')
butoon.pack(pady=20)

stone_btn = Button(butoon, text="Rock 👊", width=12, font=("Georgia", 11), command=lambda: play(0))
stone_btn.grid(row=0, column=0, padx=10)

paper_btn = Button(butoon, text="Paper ✋", width=12, font=("Georgia", 11), command=lambda: play(1))
paper_btn.grid(row=0, column=1, padx=10)

scissor_btn = Button(butoon, text="Scissor ✌", width=12, font=("Georgia", 11), command=lambda: play(2))
scissor_btn.grid(row=0, column=2, padx=10)
window.mainloop()