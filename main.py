from tkinter import *
from spendings_GUI import Spending_GUI


def main():

    root=Tk()
    gui = Spending_GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()