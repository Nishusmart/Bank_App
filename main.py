from tkinter import *
from tkinter import messagebox
import time
import os.path

if __name__ == '__main__':
    root = Tk()
    root.title("BANK")

    try:
        root.iconbitmap("Data/money_bag.ico")
    except:
        pass

    root.geometry("800x600")
    root.resizable(False, False)

    class Bank:
        def Body(self):
            self.data = []

            self.frame_login = Frame(root, bg="WHITE", bd=2)

            self.button_create_account = Button(self.frame_login, text="CREATE NEW ACCOUNT", width=34, bg="AQUA", font=("times new roman", 15),
                                          relief=FLAT, command=self.create_account)
            self.button_create_account.grid(row=0, column=0, columnspan=6)

            self.label_user_id = Label(self.frame_login, text="User ID:", bg="WHITE", font=("times new roman", 15))
            self.label_user_id.grid(row=1, column=0, columnspan=2)

            self.entry_user_id = Entry(self.frame_login, relief=SOLID, font=("times new roman", 15), justify=CENTER)
            self.entry_user_id.grid(row=1, column=2, columnspan=3)

            self.button_search = Button(self.frame_login, text="FIND", width=6, bg="ORANGE", font=("times new roman", 10),
                                          relief=FLAT, command=self.search)
            self.button_search.grid(row=1, column=5)

            self.label_user_pin = Label(self.frame_login, text="User Pin:", bg="WHITE", font=("times new roman", 15))
            self.label_user_pin.grid(row=2, column=0, columnspan=2)

            self.entry_user_pin = Entry(self.frame_login, relief=SOLID, font=("times new roman", 15), show="*", justify=CENTER, state=DISABLED)
            self.entry_user_pin.grid(row=2, column=2, columnspan=3)

            self.button_clear_pin = Button(self.frame_login, text="\u232B", width=6, bg="ORANGE", font=("times new roman", 10), relief=FLAT,
                                           command=self.login_back_space)
            self.button_clear_pin.grid(row=2, column=5)

            self.button_7 = Button(self.frame_login, text="7", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(7))
            self.button_7.grid(row=3, column=0, columnspan=2)

            self.button_8 = Button(self.frame_login, text="8", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(8))
            self.button_8.grid(row=3, column=2, columnspan=2)

            self.button_9 = Button(self.frame_login, text="9", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(9))
            self.button_9.grid(row=3, column=4, columnspan=2)

            self.button_4 = Button(self.frame_login, text="4", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(4))
            self.button_4.grid(row=4, column=0, columnspan=2)

            self.button_5 = Button(self.frame_login, text="5", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(5))
            self.button_5.grid(row=4, column=2, columnspan=2)

            self.button_6 = Button(self.frame_login, text="6", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(6))
            self.button_6.grid(row=4, column=4, columnspan=2)

            self.button_1 = Button(self.frame_login, text="1", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(1))
            self.button_1.grid(row=5, column=0, columnspan=2)

            self.button_2 = Button(self.frame_login, text="2", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(2))
            self.button_2.grid(row=5, column=2, columnspan=2)

            self.button_3 = Button(self.frame_login, text="3", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(3))
            self.button_3.grid(row=5, column=4, columnspan=2)

            self.button_exit = Button(self.frame_login, text="EXIT", bg="TOMATO", width=11, height=2, font=("times new roman", 15), relief=FLAT, command=root.destroy)
            self.button_exit.grid(row=6, column=0, columnspan=2)

            self.button_0 = Button(self.frame_login, text="0", width=11, height=2, font=("times new roman", 15), relief=FLAT, command= lambda: self.pin_generate(0))
            self.button_0.grid(row=6, column=2, columnspan=2)

            self.button_next = Button(self.frame_login, text="NEXT", bg="GREEN2", width=11, height=2, font=("times new roman", 15), relief=FLAT, command=self.login)
            self.button_next.grid(row=6, column=4, columnspan=2)

            self.frame_login.place(relx=0.25, rely=0.25)

        def create_account(self):
            self.frame_login.destroy()

            self.frame_create_account = Frame(root, bg="WHITE", bd=2)

            self.label_create_account_banner = Label(self.frame_create_account, text="CREATE NEW ACCOUNT", bg="WHITE", font=("times new roman", 15))
            self.label_create_account_banner.grid(row=0, column=0, columnspan=4)


            self.label_username_new = Label(self.frame_create_account, text="User Name: ", bg="WHITE", font=("times new roman", 15))
            self.label_username_new.grid(row=1, column=0)

            self.entry_username_new = Entry(self.frame_create_account, relief=SOLID, font=("times new roman", 15))
            self.entry_username_new.grid(row=1, column=1, columnspan=3)


            self.label_userid_new = Label(self.frame_create_account, text="User ID: ", bg="WHITE", font=("times new roman", 15))
            self.label_userid_new.grid(row=2, column=0)

            self.entry_userid_new = Entry(self.frame_create_account, relief=SOLID, font=("times new roman", 15))
            self.entry_userid_new.grid(row=2, column=1, columnspan=3)


            self.label_userpin_new = Label(self.frame_create_account, text="User PIN: ", bg="WHITE", font=("times new roman", 15))
            self.label_userpin_new.grid(row=3, column=0)

            self.entry_userpin_new = Entry(self.frame_create_account, relief=SOLID, show="*", font=("times new roman", 15))
            self.entry_userpin_new.grid(row=3, column=1, columnspan=3)


            self.label_initial_amount = Label(self.frame_create_account, text="Initial Amount: ", bg="WHITE", font=("times new roman", 15))
            self.label_initial_amount.grid(row=4, column=0)

            self.entry_initial_amount = Entry(self.frame_create_account, relief=SOLID, font=("times new roman", 15))
            self.entry_initial_amount.grid(row=4, column=1, columnspan=3)

            self.button_cancel_create_account = Button(self.frame_create_account, text="CANCEL", bd=1, bg="TOMATO", width=20, height=2, font=("times new roman", 15), relief=SOLID, command=self.cancel_create_account)
            self.button_cancel_create_account.grid(row=5, column=0, columnspan=2)

            self.button_confirm_create_account = Button(self.frame_create_account, text="CONFIRM", bd=1, bg="GREEN2", width=20, height=2, font=("times new roman", 15), relief=SOLID, command= self.confirm_create_account)
            self.button_confirm_create_account.grid(row=5, column=2, columnspan=2)

            self.frame_create_account.place(relx=0.25, rely=0.25)

        def confirm_create_account(self):
            try:
                f = open("Data/"+self.entry_userid_new.get().lower()+".txt", "r")
                f.close()
                messagebox.showwarning("ACCOUNT EXIST", "ACCOUNT ALREADY EXIST, TRY USING OTHER ID.")
            except:
                try:
                    int(self.entry_userpin_new.get())
                    float(self.entry_initial_amount.get())
                    if(len(self.entry_userpin_new.get()) > 4):
                        messagebox.showinfo("INVALID PIN", "Only 4 digit PIN allowed")
                    else:
                        if(os.path.isdir("Data") == False):
                            os.mkdir("Data")
                        f = open("Data/"+self.entry_userid_new.get().lower()+".txt", "w")
                        f.write(self.entry_username_new.get()+"\n")
                        f.write(self.entry_userid_new.get().lower()+"\n")
                        f.write(self.entry_userpin_new.get()+"\n")
                        f.write(self.entry_initial_amount.get()+"\n")
                        f.close()
                        messagebox.showinfo("SUCCESS", "YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED.")
                        self.cancel_create_account()
                except:
                    messagebox.showwarning("INVALID INPUT", "PIN/Amount MUST BE NUMERIC")

        def cancel_create_account(self):
            self.frame_create_account.destroy()
            self.Body()

        def search(self):
            self.frame_login.destroy()

            self.frame_search = Frame(root, bg="WHITE", bd=2)

            self.label_search_banner = Label(self.frame_search, text="SEARCH BY ID/TRANSACTION STATUS", bg="WHITE", font=("times new roman", 15))
            self.label_search_banner.grid(row=0, column=0, columnspan=4)

            self.button_back_search = Button(self.frame_search, text="BACK", bd=1, bg="ORANGE", width=6, font=("times new roman", 10), relief=SOLID, command=self.back_search)
            self.button_back_search.grid(row=1, column=0)

            self.entry_search = Entry(self.frame_search, width=55, relief=SOLID, font=("times new roman", 15))
            self.entry_search.grid(row=1, column=1, columnspan=2)
            self.entry_search.bind('<Return>', self.find)

            self.button_find = Button(self.frame_search, text="FIND", bd=1, bg="GREEN2", width=6, font=("times new roman", 10), relief=SOLID, command=self.find)
            self.button_find.grid(row=1, column=3)

            self.frame_info = Frame(self.frame_search, bg="WHITE", bd=2)

            self.listbox_find = Listbox(self.frame_info, width=80, height=20)
            self.listbox_find.grid(row=0, column=0)

            self.vscrollbar = Scrollbar(self.frame_info, orient=VERTICAL)
            self.vscrollbar.config(command=self.listbox_find.yview)
            self.vscrollbar.grid(row=0, column=1, ipady=100)
            self.listbox_find.config(bd=2, yscrollcommand=self.vscrollbar.set)
            self.listbox_find.config(font=("times new roman", 12))

            self.frame_info.grid(row=2, column=0, columnspan=4)

            self.frame_search.place(relx=0.1, rely=0.1)

        def find(self, event=None):
            if (os.path.isdir("Data") == False):
                os.mkdir("Data")
                os.chdir("Data")
                f = open("transactions.txt", "w")
                f.close()
                os.chdir(os.getcwd()[:-4])

            f = open("Data/transactions.txt", "r")
            self.listbox_find.delete(0, END)
            categories = ["deposit", "withdraw", "transfer"]
            n = self.entry_search.get().lower()
            if (n == "" or n == "all"):
                self.listbox_find.insert(END, "Transaction Time - Transaction Status - Account ID - Account ID - Amount")
                for i in f:
                    temp = list(i.split(","))
                    self.listbox_find.insert(END, temp[0] + " - " + temp[1] + " - " + temp[2] + " - " + temp[3] + " - " + temp[4])
            elif (n in categories):
                if (n == "transfer"):
                    self.listbox_find.insert(END, "Transaction Time - Transaction Status - Deposit From - Credit To - Amount")
                    for i in f:
                        temp = list(i.split(","))
                        if (temp[1] == n):
                            self.listbox_find.insert(END, temp[0]+" - "+temp[1]+" - "+temp[2]+" - "+temp[3]+" - "+temp[4])

                else:
                    self.listbox_find.insert(END, "Transaction Time - Transaction Status - Account ID - Amount")
                    for i in f:
                        temp = list(i.split(","))
                        if (temp[1] == n):
                            self.listbox_find.insert(END, temp[0]+" - "+temp[1]+" - "+temp[2]+" - "+temp[4])
            else:
                self.listbox_find.insert(END, "Transaction Time - Transaction Status - Account ID - Account ID - Amount")
                for i in f:
                    temp = list(i.split(","))
                    if (temp[2] == n or temp[3] == n):
                        self.listbox_find.insert(END, temp[0]+" - "+temp[1]+" - "+temp[2]+" - "+temp[3]+" - "+temp[4])

        def back_search(self):
            self.frame_search.destroy()
            self.Body()

        def login_back_space(self):
            self.entry_user_pin.config(state=NORMAL)
            self.entry_user_pin.delete(self.entry_user_pin.index(INSERT) - 1)
            self.entry_user_pin.config(state=DISABLED)

        def pin_generate(self, event=None):
            if(len(self.entry_user_pin.get()) < 4):
                self.entry_user_pin.config(state=NORMAL)
                self.entry_user_pin.insert(END, str(event))
                self.entry_user_pin.config(state=DISABLED)
            else:
                messagebox.showinfo("INVALID PIN", "Only 4 digit PIN allowed")

        def login(self):
            user_id = self.entry_user_id.get().lower()
            user_pin = self.entry_user_pin.get()
            try:
                f = open("Data/"+user_id+".txt", "r")
                self.data = []
                for i in f:
                    self.data.append(i)
                f.close()

                if (int(user_pin) == int(self.data[2])):
                    self.main_window()
                else:
                    messagebox.showwarning("INCORRECT PIN", "PIN DOES NOT MATCH")
            except:
                messagebox.showwarning("INVALID", "WRONG USER ID")

        def main_window(self):
            self.frame_login.destroy()
            self.frame_main_window = Frame(root, bg="WHITE", bd=2)

            self.label_welcome = Label(self.frame_main_window, text="WELCOME "+self.data[0], bg="WHITE", height=2, width=40, font=("times new roman", 15))
            self.label_welcome.grid(row=0, column=0, columnspan=2)

            self.button_deposit = Button(self.frame_main_window, text="DEPOSIT CASH", bd=1, bg="WHITE", width=20, height=2, font=("times new roman", 15), relief=SOLID, command=self.deposit)
            self.button_deposit.grid(row=1, column=0)

            self.button_withdraw = Button(self.frame_main_window, text="WITHDRAW CASH", bd=1, bg="WHITE", width=20, height=2, font=("times new roman", 15), relief=SOLID, command=self.withdraw)
            self.button_withdraw.grid(row=1, column=1)

            self.button_balance = Button(self.frame_main_window, text="CHECK BALANCE", bd=1, bg="WHITE", width=20, height=2, font=("times new roman", 15), relief=SOLID, command=lambda : messagebox.showinfo("CURRENT BALANCE", "BALANCE: "+self.data[3]))
            self.button_balance.grid(row=2, column=0)

            self.button_transfer = Button(self.frame_main_window, text="TRANSFER MONEY", bd=1, bg="WHITE", width=20, height=2, font=("times new roman", 15), relief=SOLID, command=self.transfer)
            self.button_transfer.grid(row=2, column=1)

            self.button_change_pin = Button(self.frame_main_window, text="CHANGE PIN", bd=1, bg="WHITE", width=20, height=2, font=("times new roman", 15), relief=SOLID, command=self.change_pin)
            self.button_change_pin.grid(row=3, column=0)

            self.button_cancel = Button(self.frame_main_window, text="CANCEL", bd=1, bg="TOMATO", width=20, height=2, font=("times new roman", 15), relief=SOLID, command=self.logout)
            self.button_cancel.grid(row=3, column=1)

            self.frame_main_window.place(relx=0.25, rely=0.25)

        def deposit(self):
            self.frame_main_window.destroy()
            self.frame_deposit = Frame(root, bg="WHITE", bd=2)

            self.label_deposit_banner = Label(self.frame_deposit, text="DEPOSIT MONEY", bg="WHITE",
                                      font=("times new roman", 15))
            self.label_deposit_banner.grid(row=0, column=0, columnspan=4)

            self.label_amount = Label(self.frame_deposit, text="Amount:", bg="WHITE",
                                      font=("times new roman", 15))
            self.label_amount.grid(row=1, column=0)

            self.entry_amount_deposit = Entry(self.frame_deposit, relief=SOLID, font=("times new roman", 15),
                                               justify=CENTER)
            self.entry_amount_deposit.grid(row=1, column=1, columnspan=3)

            self.button_cancel_deposit = Button(self.frame_deposit, text="CANCEL", bg="TOMATO", width=20,
                                                 height=2, font=("times new roman", 15), relief=FLAT,
                                                 command=self.cancel_deposit)
            self.button_cancel_deposit.grid(row=2, column=0, columnspan=2)

            self.button_confirm_deposit = Button(self.frame_deposit, text="DEPOSIT", bg="GREEN2", width=20,
                                                  height=2, font=("times new roman", 15), relief=FLAT,
                                                  command=self.confirm_deposit)
            self.button_confirm_deposit.grid(row=2, column=2, columnspan=2)

            self.frame_deposit.place(relx=0.25, rely=0.25)

        def confirm_deposit(self):
            try:
                temp = float(self.entry_amount_deposit.get())

                self.data[3] = str(float(self.data[3]) + temp) + "\n"
                f = open("Data/"+self.data[1][:-1]+".txt", "w")
                for i in self.data:
                    f.write(i)
                f.close()
                transaction_data = str(time.ctime())+",deposit,"+self.data[1][:-1]+", ,"+str(temp)+"\n"
                f = open("Data/transactions.txt", "a")
                f.write(transaction_data)
                f.close()

                messagebox.showinfo("DEPOSIT SUCCESSFUL", "DEPOSIT : " + str(temp) + "\nCURRENT BALANCE: " + self.data[3])
                self.cancel_deposit()
            except:
                messagebox.showinfo("INVALID", "Amount must be numeric")

        def cancel_deposit(self):
            self.frame_deposit.destroy()
            self.main_window()

        def withdraw(self):
            self.frame_main_window.destroy()
            self.frame_withdraw = Frame(root, bg="WHITE", bd=2)

            self.label_withdraw_banner = Label(self.frame_withdraw, text="WITHDRAW MONEY", bg="WHITE",
                                              font=("times new roman", 15))
            self.label_withdraw_banner.grid(row=0, column=0, columnspan=4)

            self.label_amount = Label(self.frame_withdraw, text="Amount:", bg="WHITE",
                                      font=("times new roman", 15))
            self.label_amount.grid(row=1, column=0)

            self.entry_amount_withdraw = Entry(self.frame_withdraw, relief=SOLID, font=("times new roman", 15),
                                               justify=CENTER)
            self.entry_amount_withdraw.grid(row=1, column=1, columnspan=3)

            self.button_cancel_withdraw = Button(self.frame_withdraw, text="CANCEL", bg="TOMATO", width=20,
                                                 height=2, font=("times new roman", 15), relief=FLAT,
                                                 command=self.cancel_withdraw)
            self.button_cancel_withdraw.grid(row=2, column=0, columnspan=2)

            self.button_confirm_withdraw = Button(self.frame_withdraw, text="WITHDRAW", bg="GREEN2", width=20,
                                                  height=2, font=("times new roman", 15), relief=FLAT,
                                                  command=self.confirm_withdraw)
            self.button_confirm_withdraw.grid(row=2, column=2, columnspan=2)

            self.frame_withdraw.place(relx=0.25, rely=0.25)

        def confirm_withdraw(self):
            try:
                temp = float(self.entry_amount_withdraw.get())
                if(float(self.data[3]) >= temp):
                    self.data[3] = str(float(self.data[3]) - temp) + "\n"
                    f = open("Data/"+self.data[1][:-1]+".txt", "w")
                    for i in self.data:
                        f.write(i)
                    f.close()
                    transaction_data = str(time.ctime())+",withdraw,"+self.data[1][:-1]+", ,"+str(temp)+"\n"
                    f = open("Data/transactions.txt", "a")
                    f.write(transaction_data)
                    f.close()

                    messagebox.showinfo("WITHDRAW SUCCESSFUL", "WITHDRAWN : " + str(temp) + "\nCURRENT BALANCE: " + self.data[3])
                    self.cancel_withdraw()
                else:
                    messagebox.showinfo("LOW BALANCE", "NOT ENOUGH MONEY TO WITHDRAW" + "\nCURRENT BALANCE: " + self.data[3])
            except:
                messagebox.showinfo("INVALID", "Amount must be numeric")

        def cancel_withdraw(self):
            self.frame_withdraw.destroy()
            self.main_window()

        def transfer(self):
            self.frame_main_window.destroy()
            self.frame_transfer_money = Frame(root, bg="WHITE", bd=2)

            self.frame_transfer_banner = Label(self.frame_transfer_money, text="TRANSFER MONEY", bg="WHITE",
                                              font=("times new roman", 15))
            self.frame_transfer_banner.grid(row=0, column=0, columnspan=4)

            self.label_reciever_id = Label(self.frame_transfer_money, text="Receiver ID:", bg="WHITE", font=("times new roman", 15))
            self.label_reciever_id.grid(row=1, column=0)

            self.entry_receiver_id = Entry(self.frame_transfer_money, relief=SOLID, font=("times new roman", 15), justify=CENTER)
            self.entry_receiver_id.grid(row=1, column=1, columnspan=3)

            self.label_amount = Label(self.frame_transfer_money, text="Amount:", bg="WHITE", font=("times new roman", 15))
            self.label_amount.grid(row=2, column=0)

            self.entry_amount_transfer = Entry(self.frame_transfer_money, relief=SOLID, font=("times new roman", 15), justify=CENTER)
            self.entry_amount_transfer.grid(row=2, column=1, columnspan=3)

            self.button_cancel_transfer = Button(self.frame_transfer_money, text="CANCEL", bg="TOMATO", width=20, height=2, font=("times new roman", 15), relief=FLAT, command=self.cancel_transfer)
            self.button_cancel_transfer.grid(row=3, column=0, columnspan=2)

            self.button_confirm_transfer = Button(self.frame_transfer_money, text="TRANSFER", bg="GREEN2", width=20, height=2, font=("times new roman", 15), relief=FLAT, command=self.confirm_transfer)
            self.button_confirm_transfer.grid(row=3, column=2, columnspan=2)

            self.frame_transfer_money.place(relx=0.25, rely=0.25)

        def confirm_transfer(self):
            try:
                temp = float(self.entry_amount_transfer.get())
                try:
                    f = open("Data/"+self.entry_receiver_id.get().lower()+".txt", "r")
                    receiver_data = []
                    for i in f:
                        receiver_data.append(i)
                    f.close()
                    if(float(self.data[3]) >= temp):
                        receiver_data[3] = str(float(receiver_data[3]) + temp) + "\n"
                        self.data[3] = str(float(self.data[3]) - temp) + "\n"
                        f = open("Data/"+self.entry_receiver_id.get().lower()+".txt", "w")
                        for i in receiver_data:
                            f.write(i)
                        f.close()

                        f = open("Data/" + self.data[1][:-1] + ".txt", "w")
                        for i in self.data:
                            f.write(i)
                        f.close()

                        transaction_data = str(time.ctime())+",transfer,"+self.data[1][:-1]+","+self.entry_receiver_id.get().lower()+","+str(temp)+"\n"

                        f = open("Data/transactions.txt", "a")
                        f.write(transaction_data)
                        f.close()

                        messagebox.showinfo("TRANSACTION SUCCESSFUL", "MONEY SENT SUCCESSFULLY" + "\nCURRENT BALANCE: " + self.data[3])
                        self.cancel_transfer()

                    else:
                        messagebox.showinfo("LOW BALANCE", "NOT ENOUGH MONEY TO TRANSFER" + "\nCURRENT BALANCE: " + self.data[3])
                except:
                    messagebox.showwarning("INVALID", "Receiver ID does not exists")
            except:
                messagebox.showwarning("INVALID", "Amount must be numeric")

        def cancel_transfer(self):
            self.frame_transfer_money.destroy()
            self.main_window()

        def change_pin(self):
            self.frame_main_window.destroy()
            self.frame_change_pin = Frame(root, bg="WHITE", bd=2)

            self.label_pin_change_banner = Label(self.frame_change_pin, text="CHANGE YOUR PIN", bg="WHITE", font=("times new roman", 15))
            self.label_pin_change_banner.grid(row=0, column=0, columnspan=4)

            self.label_old_pin = Label(self.frame_change_pin, text="Old Pin:", bg="WHITE", font=("times new roman", 15))
            self.label_old_pin.grid(row=1, column=0)

            self.entry_old_pin = Entry(self.frame_change_pin, relief=SOLID, font=("times new roman", 15), show="*", justify=CENTER)
            self.entry_old_pin.grid(row=1, column=1, columnspan=3)

            self.label_new_pin = Label(self.frame_change_pin, text="New Pin:", bg="WHITE", font=("times new roman", 15))
            self.label_new_pin.grid(row=2, column=0)

            self.entry_new_pin = Entry(self.frame_change_pin, relief=SOLID, font=("times new roman", 15), show="*", justify=CENTER)
            self.entry_new_pin.grid(row=2, column=1, columnspan=3)

            self.button_cancel_pin_change = Button(self.frame_change_pin, text="BACK", bg="ORANGE", width=15, height=2, font=("times new roman", 15), relief=FLAT, command=self.back_pin_change)
            self.button_cancel_pin_change.grid(row=3, column=0, columnspan=2)

            self.button_next = Button(self.frame_change_pin, text="NEXT", bg="GREEN2", width=15, height=2, font=("times new roman", 15), relief=FLAT, command=self.confirm_change_pin)
            self.button_next.grid(row=3, column=2, columnspan=2)

            self.frame_change_pin.place(relx=0.25, rely=0.25)

        def confirm_change_pin(self):
            try:
                int(self.entry_new_pin.get())
                if(len(self.entry_old_pin.get()) > 4 or len(self.entry_new_pin.get()) > 4):
                    messagebox.showinfo("INVALID PIN", "Only 4 digit PIN allowed")
                elif(int(self.entry_old_pin.get()) == int(self.data[2])):
                    self.data[2] = self.entry_new_pin.get()+"\n"
                    f = open("Data/"+self.data[1][:-1]+".txt","w")
                    for i in self.data:
                        f.write(i)
                    f.close()
                    messagebox.showinfo("SUCCESS", "PIN CHANGED SUCCESSFULLY")
                    self.frame_change_pin.destroy()
                    self.main_window()
                else:
                    messagebox.showwarning("INCORRECT PIN", "PIN DOES NOT MATCH")
            except:
                messagebox.showwarning("INVALID INPUT", "PIN MUST BE NUMERIC")

        def back_pin_change(self):
            self.frame_change_pin.destroy()
            self.main_window()

        def logout(self):
            self.frame_main_window.destroy()
            self.Body()

    ob = Bank()
    ob.Body()

    root.mainloop()