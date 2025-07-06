from tkinter import*
import random

window=Tk()
window.title("Game")
window.geometry('450x450')
window.config(bg='#FFD66B')
pscore=0
cscore=0

ch=['rock','paper','scissors']

def play(x):
    global pscore
    global cscore
    l=ch[x]
    comp=random.choice(ch)
    c_choice.config(text=f"Computer chose : {comp}")
    if(l==comp):
        c_label.config(text="It's a tie!")
    elif((l=='rock' and comp=='scissors')or (l=='scissors' and comp=='paper') or (l=='paper' and comp=='rock') ):
        c_label.config(text="YOU WON 🤩")
        pscore+=1
        ps_label.config(text=f"Your score={pscore}")
    else:
        c_label.config(text="COMPUTER WON 😥")
        cscore+=1
        cs_label.config(text=f"Computer score={cscore}")
def playagain():
    global pscore
    global cscore
    pscore=0
    cscore=0
    cs_label.config(text=f"Computer score={cscore}")
    ps_label.config(text=f"Your score={pscore}")
    c_label.config(text="")
    c_choice.config(text="")

heading=Label(window,text='ROCK PAPER SCISSORS !',font=("Georgia", 18, "bold"), bg="#4DA8DA", fg="#F5F5F5")
heading.pack(pady=20)

c_choice=Label(window,font=("Georgia", 14, "bold"), bg='#FFD66B', fg="#00809D")
c_choice.pack(pady=20)

c_label=Label(window,font=("Georgia", 14, "bold"), bg='#FFD66B', fg="#06923E")
c_label.pack(pady=20)

cs_label=Label(window,text=f"Computer score={cscore}",font=("Georgia", 14, "bold"), bg='#FFD66B', fg="#EB5B00")
cs_label.pack(pady=10)

ps_label=Label(window,text=f"Your score={pscore}",font=("Georgia", 14, "bold"), bg='#FFD66B', fg="#EB5B00")
ps_label.pack(pady=10)

button= Frame(window, bg='#FFD66B')
button.pack(pady=20)

stone_btn = Button(button, text="Rock 👊", width=12, font=("Georgia", 11), command=lambda: play(0))
stone_btn.grid(row=0, column=0, padx=10)

paper_btn = Button(button, text="Paper ✋", width=12, font=("Georgia", 11), command=lambda: play(1))
paper_btn.grid(row=0, column=1, padx=10)

scissor_btn = Button(button, text="Scissor ✌", width=12, font=("Georgia", 11), command=lambda: play(2))
scissor_btn.grid(row=0, column=2, padx=10)

playagain_btn = Button(button, text="Play Again", width=12, font=("Georgia", 11), command=lambda: playagain())
playagain_btn.grid(row=1, column=1, padx=10,pady=10)

window.mainloop()