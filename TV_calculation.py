from tkinter import Tk, Label, Button, messagebox
from tkinter import *
from PIL import ImageTk, Image


class Login_Page:

    def __init__(self, login=Tk()):
        """
        :type login: object
        """
        self.login = login
        login.protocol("WM_DELETE_WINDOW",self.event_X)
        login.title("Login - EIS Hospital")
        login.geometry("450x230+450+170")

        self.username = Label(login, text="Username:")
        self.username.place(relx=0.285, rely=0.298, height=20, width=65)

        self.password = Label(login, text=" Password:")
        self.password.place(relx=0.285, rely=0.468, height=20, width=65)

        # Creating Buttons

        self.login_button = Button(login, text="Login")
        self.login_button.place(relx=0.440, rely=0.638, height=30, width=60)
        self.login_button.configure(command=self.login_user)

        self.login_completed = IntVar()

        self.exit_button = Button(login, text="Exit")  # , command=master.quit)
        self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)
        self.exit_button.configure(command=self.exit_login)

        # Creating entry boxes

        self.username_box = Entry(login)
        self.username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)

        self.password_box = Entry(login)
        self.password_box.place(relx=0.440, rely=0.468, height=20, relwidth=0.35)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")

        # Creating checkbox

        self.var = IntVar()
        self.show_password = Checkbutton(login)
        self.show_password.place(relx=0.285, rely=0.650, relheight=0.100, relwidth=0.125)
        self.show_password.configure(justify='left')
        self.show_password.configure(text='''Show''')
        self.show_password.configure(variable=self.var, command=self.cb)

    def event_X(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            exit()

    def cb(self, ):
        if self.var.get() == True:
            self.password_box.configure(show="")
        else:
            self.password_box.configure(show="*")

# Giving function to login process

    def login_user(self):
        name = self.username_box.get()
        password = self.password_box.get()
        login_completed = self.login_completed.get()

        if name == "user" and password == "1234":
            self.login.destroy()
            self.login_completed == 1

        else:
            messagebox.showwarning("Login Failed - Acess Denied", "Username or Password incorrect!")

    def exit_login(self):
        msg = messagebox.askyesno("Exit login page", "Do you really want to exit?")
        if (msg):
            exit()

    def mainloop_window(self):
        self.login.mainloop()


login_page = Login_Page()
login_page.mainloop_window()


class Main_Win:

    def __init__(self, main_win=Tk()):

        def Tidal_volume():
            res = int(e2.get()) * int(e3.get())
            myText.set(res)

        self.main_win = main_win
        main_win.title('Tidal Volume Calculation')
        myText = StringVar();
        main_win.geometry("450x230+450+170")

        Label(main_win, text="Patient ID").grid(row=0, sticky=W)
        Label(main_win, text="Body Wight (kg)").grid(row=1, sticky=W)
        Label(main_win, text="Tidal Volume (6-8 mL/kg)").grid(row=2, sticky=W)
        Label(main_win, text="Tidal Volume (mL):").grid(row=3, sticky=W)
        result = Label(main_win, text="", textvariable=myText).grid(row=3, column=1, sticky=W)

        e1 = Entry(main_win)
        e2 = Entry(main_win)
        e3 = Entry(main_win)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)

        b = Button(main_win, text="Calculate", command=Tidal_volume)
        b.grid(row=3, column=3, columnspan=4, rowspan=4, sticky=W, padx=5, pady=5)


    def mainloop_window(self):
        self.main_win.mainloop()


main_win = Main_Win()
main_win.mainloop_window()