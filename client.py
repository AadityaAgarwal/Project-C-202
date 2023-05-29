import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

class GUI:

    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()

        self.login_window=Toplevel()
        self.login_window.title("Login ")
        self.login_window.resizable(width=False,height=False)
        self.login_window.configure(width=400,height=400,bg='black')

        self.nickname_req=Label(self.login_window,text="Enter nickname please: ",justify=CENTER,font='Helvetica 15 bold')
        self.nickname_req.place(relheight=0.1,relx=0.2,rely=0.05)

        self.nickname_label=Label(self.login_window,text="Name",font='Calibri 12')
        self.nickname_label.place(relheight=0.1,relx=0.1,rely=0.2)

        self.nickname_input=Entry(self.login_window,font='Calibri 12',fg="white")  
        self.nickname_input.place(relwidth=0.4,relheight=0.1,relx=0.4,rely=0.2)
        self.nickname_input.focus()

        self.enter_button=Button(self.login_window,text="Login", command=lambda:self.login(self.nickname_input.get()),font="Calibri 18",fg="red",borderwidth=2,bg="red")
        self.enter_button.place(relx=0.4,rely=0.5)

        self.Window.mainloop()
    
    def login(self,nickname):
        self.login_window.destroy()
        self.name=nickname

        rcv=Thread(target=self.receive)
        rcv.start()

    
    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                client.close()
                break




print("Connected with the server...")
g=GUI()
