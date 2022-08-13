from tictac import *


def main():
    window = Tk()
    window.title('Tic-Tac-Toe')
    window.geometry('500x400')

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
