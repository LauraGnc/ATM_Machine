from backend_ATM import Account, Checking
from tkinter import *

'''This is a simple ATM program.'''

your_account = Account('balance')
your_checking = Checking('checking_balance', 5)

class Interface:

    def __init__(self, interface):
        self.interface = interface

        # Labels
        l1 = Label(interface, text='Main account: ')
        l1.grid(row=0, column=0)

        l2 = Label(interface, text='Checking account: ')
        l2.grid(row=1, column=0)

        l3 = Label(interface, text='Welcome! With this basic program you can manage money')
        l3.grid(row=2, column=0)

        l4 = Label(interface, text='between your accounts. There is a £5 fee if transferring')
        l4.grid(row=3, column=0)

        l4 = Label(interface, text='money to your main account.')
        l4.grid(row=4, column=0)

        # Entries
        main_text = StringVar()
        e1 = Entry(interface, textvariable=main_text)
        e1.grid(row=0, column=1)

        checking_text = StringVar()
        e2 = Entry(interface, textvariable=checking_text)
        e2.grid(row=1, column=1)

        # Buttons
        b4 = Button(interface, text='Quit', width=10, command=interface.destroy)
        b4.grid(row=7, column=3)



interface = Tk()
interface.title('ATM Machine')
interface.geometry('900x500')

Interface(interface)
interface.mainloop()