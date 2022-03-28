from cProfile import label
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title('Tic-Tac-Toe')
playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()
player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)
bclick = True
flag = 0


def disableButtons():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def buttonClick(button):
    global bclick, flag, player2_name, player1_name, playerA, playerB
    if button['text'] == ' ' and bclick == True:
        button['text'] = 'X'
        checkForWin()
        bclick = False
        playerB = p2.get()+' wins'
        playerA = p1.get()+' wins'
        flag = flag+1
    elif button['text'] == ' ' and bclick == False:
        button['text'] = 'O'
        checkForWin()
        bclick = True
        flag = flag+1
    else:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'button already clicked')


def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
                disableButtons()
                tkinter.messagebox.showinfo('Tic-Tac-Toe', playerA)
    elif(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or 
         button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
         button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
         button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
         button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
         button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
         button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
         button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
                disableButtons()
                tkinter.messagebox.showinfo('Tic-Tac-Toe', playerB)
    elif(flag==8):
        tkinter.messagebox.showinfo('Tic-Tac-Toe',"It's a tie")


label = Label(tk, text='Player 1: ', font='Times 20 bold',
              bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)
label = Label(tk, text='Player 2: ', font='Times 20 bold',
              bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)
button1 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button1))
button1.grid(row=3, column=0)
button2 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button2))
button2.grid(row=3, column=1)
button3 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button3))
button3.grid(row=3, column=2)
button4 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button4))
button4.grid(row=4, column=0)
button5 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button5))
button5.grid(row=4, column=1)
button6 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button6))
button6.grid(row=4, column=2)
button7 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button7))
button7.grid(row=5, column=0)
button8 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button8))
button8.grid(row=5, column=1)
button9 = Button(tk, text=' ', font='Times 20 bold', bg='grey',
                 fg='white', height=4, width=8, command=lambda: buttonClick(button9))
button9.grid(row=5, column=2)
tk.mainloop()
