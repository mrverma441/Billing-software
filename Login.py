from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.bg_icon=ImageTk.PhotoImage(file="56vWLQ.jpg")
        self.logo_icon=PhotoImage(file="change-user-male (1).png")
        self.user_icon=PhotoImage(file="change-user-male (2).png")
        self.pass_icon=PhotoImage(file="password.png")


        self.uname=StringVar()
        self.pass_=StringVar()
        
        
        
        
        bg_lbl=Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Login system",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)



        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=400,y=150)
        logolbl=Label(login_frame,image=self.logo_icon,bd=0)
        logolbl.grid(row=0,columnspan=2,pady=20)
        lbluser=Label(login_frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,pady=20,padx=10)
        txtuser=Entry(login_frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,pady=20)

        
        lblpass=Label(login_frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,pady=20,padx=10)
        txtpasss=Entry(login_frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("",15)).grid(row=2,column=1,pady=20)
        btn_log=Button(login_frame,text="Login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
                messagebox.showerror("Error","All fiels are must")
        elif self.uname.get()=="mrverma" and self.pass_.get()=="7534050774":
            messagebox.showinfo("Successful",f"welcome{self.uname.get()}")
            root.destroy()
            import bill
            bill.File_App()
        else:
            messagebox.showinfo("Error","Invalid username or password")
            self.root.destroy()
       
        
       
            
        

            

                                                               

                                                                        
        
                                                                        
                                                                        

                                                                        
root=Tk()
obj=Login_System(root)
root.mainloop()
