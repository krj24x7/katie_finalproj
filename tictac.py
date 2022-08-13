from tkinter import *
from tkinter import messagebox


click = True
count = 0
winner = False


class GUI:
    def __init__(self, window):
        self.window = window

        self.space1 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space1))
        self.space2 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space2))
        self.space3 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space3))
        self.space4 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space4))
        self.space5 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space5))

        self.space6 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space6))
        self.space7 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space7))
        self.space8 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space8))
        self.space9 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                             command=lambda: self.space_click(self.space9))
        self.space10 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space10))

        self.space11 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space11))
        self.space12 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space12))
        self.space13 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space13))
        self.space14 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space14))
        self.space15 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space15))

        self.space16 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space16))
        self.space17 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space17))
        self.space18 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space18))
        self.space19 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space19))
        self.space20 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space20))

        self.space21 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space21))
        self.space22 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space22))
        self.space23 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space23))
        self.space24 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space24))
        self.space25 = Button(window, text='', font=('Arial', 20), height=3, width=6, bg='white',
                              command=lambda: self.space_click(self.space25))

        self.space1.grid(row=0, column=0)
        self.space2.grid(row=0, column=1)
        self.space3.grid(row=0, column=2)
        self.space4.grid(row=0, column=3)
        self.space5.grid(row=0, column=4)

        self.space6.grid(row=1, column=0)
        self.space7.grid(row=1, column=1)
        self.space8.grid(row=1, column=2)
        self.space9.grid(row=1, column=3)
        self.space10.grid(row=1, column=4)

        self.space11.grid(row=2, column=0)
        self.space12.grid(row=2, column=1)
        self.space13.grid(row=2, column=2)
        self.space14.grid(row=2, column=3)
        self.space15.grid(row=2, column=4)

        self.space16.grid(row=3, column=0)
        self.space17.grid(row=3, column=1)
        self.space18.grid(row=3, column=2)
        self.space19.grid(row=3, column=3)
        self.space20.grid(row=3, column=4)

        self.space21.grid(row=4, column=0)
        self.space22.grid(row=4, column=1)
        self.space23.grid(row=4, column=2)
        self.space24.grid(row=4, column=3)
        self.space25.grid(row=4, column=4)

    def space_click(self, b):
        global click
        global count

        if b['text'] == '' and click == True:
            b['text'] = 'X'
            click = False
            count += 1
            self.who_won()
        elif b['text'] == '' and click == False:
            b['text'] = 'O'
            click = True
            count += 1
            self.who_won()
        else:
            messagebox.showerror('Tic-Tac-Toe', 'This space has already been selected. Pick a different box!')

    def who_won(self):
        global winner
        if self.space1['text'] == 'X' and self.space2['text'] == 'X' and self.space3['text'] == 'X' and self.space4['text'] == 'X' and self.space5['text'] == 'X':
            self.space1.config(bg='blue')
            self.space2.config(bg='blue')
            self.space3.config(bg='blue')
            self.space4.config(bg='blue')
            self.space5.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space6['text'] == 'X' and self.space7['text'] == 'X' and self.space8['text'] == 'X' and self.space9['text'] == 'X' and self.space10['text'] == 'X':
            self.space6.config(bg='blue')
            self.space7.config(bg='blue')
            self.space8.config(bg='blue')
            self.space9.config(bg='blue')
            self.space10.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space11['text'] == 'X' and self.space12['text'] == 'X' and self.space13['text'] == 'X' and self.space14['text'] == 'X' and self.space15['text'] == 'X':
            self.space11.config(bg='blue')
            self.space12.config(bg='blue')
            self.space13.config(bg='blue')
            self.space14.config(bg='blue')
            self.space15.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space16['text'] == 'X' and self.space17['text'] == 'X' and self.space18['text'] == 'X' and self.space19['text'] == 'X' and self.space20['text'] == 'X':
            self.space16.config(bg='blue')
            self.space17.config(bg='blue')
            self.space18.config(bg='blue')
            self.space19.config(bg='blue')
            self.space20.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space21['text'] == 'X' and self.space22['text'] == 'X' and self.space23['text'] == 'X' and self.space24['text'] == 'X' and self.space25['text'] == 'X':
            self.space21.config(bg='blue')
            self.space22.config(bg='blue')
            self.space23.config(bg='blue')
            self.space24.config(bg='blue')
            self.space25.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()

        elif self.space1['text'] == 'X' and self.space6['text'] == 'X' and self.space11['text'] == 'X' and self.space16['text'] == 'X' and self.space21['text'] == 'X':
            self.space1.config(bg='blue')
            self.space6.config(bg='blue')
            self.space11.config(bg='blue')
            self.space16.config(bg='blue')
            self.space21.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space2['text'] == 'X' and self.space7['text'] == 'X' and self.space12['text'] == 'X' and self.space17['text'] == 'X' and self.space22['text'] == 'X':
            self.space2.config(bg='blue')
            self.space7.config(bg='blue')
            self.space12.config(bg='blue')
            self.space17.config(bg='blue')
            self.space22.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space3['text'] == 'X' and self.space8['text'] == 'X' and self.space13['text'] == 'X' and self.space18['text'] == 'X' and self.space23['text'] == 'X':
            self.space3.config(bg='blue')
            self.space8.config(bg='blue')
            self.space13.config(bg='blue')
            self.space18.config(bg='blue')
            self.space23.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space4['text'] == 'X' and self.space9['text'] == 'X' and self.space14['text'] == 'X' and self.space19['text'] == 'X' and self.space24['text'] == 'X':
            self.space4.config(bg='blue')
            self.space9.config(bg='blue')
            self.space14.config(bg='blue')
            self.space19.config(bg='blue')
            self.space24.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space5['text'] == 'X' and self.space10['text'] == 'X' and self.space15['text'] == 'X' and self.space20['text'] == 'X' and self.space25['text'] == 'X':
            self.space5.config(bg='blue')
            self.space10.config(bg='blue')
            self.space15.config(bg='blue')
            self.space20.config(bg='blue')
            self.space25.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()

        elif self.space1['text'] == 'X' and self.space7['text'] == 'X' and self.space13['text'] == 'X' and self.space19['text'] == 'X' and self.space25['text'] == 'X':
            self.space1.config(bg='blue')
            self.space7.config(bg='blue')
            self.space13.config(bg='blue')
            self.space19.config(bg='blue')
            self.space25.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()
        elif self.space5['text'] == 'X' and self.space9['text'] == 'X' and self.space13['text'] == 'X' and self.space17['text'] == 'X' and self.space21['text'] == 'X':
            self.space5.config(bg='blue')
            self.space9.config(bg='blue')
            self.space13.config(bg='blue')
            self.space17.config(bg='blue')
            self.space21.config(bg='blue')
            winner = True
            messagebox.showinfo('Tic-Tac-Toe', 'Player X is the winner!')
            self.game_over()

        if self.space1['text'] == 'O' and self.space2['text'] == 'O' and self.space3['text'] == 'O' and self.space4['text'] == 'O' and self.space5['text'] == 'O':
            self.space1.config(bg='red')
            self.space2.config(bg='red')
            self.space3.config(bg='red')
            self.space4.config(bg='red')
            self.space5.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space6['text'] == 'O' and self.space7['text'] == 'O' and self.space8['text'] == 'O' and self.space9['text'] == 'O' and self.space10['text'] == 'O':
            self.space6.config(bg='red')
            self.space7.config(bg='red')
            self.space8.config(bg='red')
            self.space9.config(bg='red')
            self.space10.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space11['text'] == 'O' and self.space12['text'] == 'O' and self.space13['text'] == 'O' and self.space14['text'] == 'O' and self.space15['text'] == 'O':
            self.space11.config(bg='red')
            self.space12.config(bg='red')
            self.space13.config(bg='red')
            self.space14.config(bg='red')
            self.space15.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space16['text'] == 'O' and self.space17['text'] == 'O' and self.space18['text'] == 'O' and self.space19['text'] == 'O' and self.space20['text'] == 'O':
            self.space16.config(bg='red')
            self.space17.config(bg='red')
            self.space18.config(bg='red')
            self.space19.config(bg='red')
            self.space20.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space21['text'] == 'O' and self.space22['text'] == 'O' and self.space23['text'] == 'O' and self.space24['text'] == 'O' and self.space25['text'] == 'O':
            self.space21.config(bg='red')
            self.space22.config(bg='red')
            self.space23.config(bg='red')
            self.space24.config(bg='red')
            self.space25.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()

        elif self.space1['text'] == 'O' and self.space6['text'] == 'O' and self.space11['text'] == 'O' and self.space16['text'] == 'O' and self.space21['text'] == 'O':
            self.space1.config(bg='red')
            self.space6.config(bg='red')
            self.space11.config(bg='red')
            self.space16.config(bg='red')
            self.space21.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space2['text'] == 'X' and self.space7['text'] == 'O' and self.space12['text'] == 'O' and self.space17['text'] == 'O' and self.space22['text'] == 'O':
            self.space2.config(bg='red')
            self.space7.config(bg='red')
            self.space12.config(bg='red')
            self.space17.config(bg='red')
            self.space22.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space3['text'] == 'O' and self.space8['text'] == 'O' and self.space13['text'] == 'O' and self.space18['text'] == 'O' and self.space23['text'] == 'O':
            self.space3.config(bg='red')
            self.space8.config(bg='red')
            self.space13.config(bg='red')
            self.space18.config(bg='red')
            self.space23.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space4['text'] == 'O' and self.space9['text'] == 'O' and self.space14['text'] == 'O' and self.space19['text'] == 'O' and self.space24['text'] == 'O':
            self.space4.config(bg='red')
            self.space9.config(bg='red')
            self.space14.config(bg='red')
            self.space19.config(bg='red')
            self.space24.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space5['text'] == 'O' and self.space10['text'] == 'O' and self.space15['text'] == 'O' and self.space20['text'] == 'O' and self.space25['text'] == 'O':
            self.space5.config(bg='red')
            self.space10.config(bg='red')
            self.space15.config(bg='red')
            self.space20.config(bg='red')
            self.space25.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()

        elif self.space1['text'] == 'O' and self.space7['text'] == 'O' and self.space13['text'] == 'O' and self.space19['text'] == 'O' and self.space25['text'] == 'O':
            self.space1.config(bg='red')
            self.space7.config(bg='red')
            self.space13.config(bg='red')
            self.space19.config(bg='red')
            self.space25.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()
        elif self.space5['text'] == 'O' and self.space9['text'] == 'O' and self.space13['text'] == 'O' and self.space17['text'] == 'O' and self.space21['text'] == 'O':
            self.space5.config(bg='red')
            self.space9.config(bg='red')
            self.space13.config(bg='red')
            self.space17.config(bg='red')
            self.space21.config(bg='red')
            winner = False
            messagebox.showinfo('Tic-Tac-Toe', 'Player O is the winner!')
            self.game_over()

    def game_over(self):
        self.space1.config(state=DISABLED)
        self.space2.config(state=DISABLED)
        self.space3.config(state=DISABLED)
        self.space4.config(state=DISABLED)
        self.space5.config(state=DISABLED)
        self.space6.config(state=DISABLED)
        self.space7.config(state=DISABLED)
        self.space8.config(state=DISABLED)
        self.space9.config(state=DISABLED)
        self.space10.config(state=DISABLED)
        self.space11.config(state=DISABLED)
        self.space12.config(state=DISABLED)
        self.space13.config(state=DISABLED)
        self.space14.config(state=DISABLED)
        self.space15.config(state=DISABLED)
        self.space16.config(state=DISABLED)
        self.space17.config(state=DISABLED)
        self.space18.config(state=DISABLED)
        self.space19.config(state=DISABLED)
        self.space20.config(state=DISABLED)
        self.space21.config(state=DISABLED)
        self.space22.config(state=DISABLED)
        self.space23.config(state=DISABLED)
        self.space24.config(state=DISABLED)
        self.space25.config(state=DISABLED)
        messagebox.showinfo('Tic-Tac-Toe', 'Game Over!\n')
