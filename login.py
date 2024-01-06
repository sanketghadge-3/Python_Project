from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System ")
        self.root.geometry("1600x800+0+0")
        #=========Image================================
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=90)
        self.root.config(bg="#fafafa")

        #==========login Frame================================
        self.employee_id=StringVar()
        self.password=StringVar()
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=120,width=350,height=480)

        titlr=Label(login_frame,text="Login System",font=("elephant",30,"bold"),bg="white").place(x=0,y=30,relwidt=1)

        lbl_user=Label(login_frame,text="UserName",font=("Andlus",15,),bg="white",fg="#767171").place(x=50,y=100)
        txt_username=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15,),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_password=Label(login_frame,text="Password",font=("Andlus",15,),bg="white",fg="#767171").place(x=50,y=200)
        txt_password=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15,),bg="#ECECEC").place(x=50,y=230,width=250)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)

        btn_forget_pass=Button(login_frame,text="Forget Password?",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="blue",cursor="hand2").place(x=100,y=390)

        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=620,width=350,height=60)

        lbl_reg=Label(register_frame,text="Don't have an account",font=("times new roman",13),bg="white").place(x=40,y=20)
        btn_signup=Button(register_frame,text="Sign up",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="blue",cursor="hand2").place(x=200,y=18)

        #========animation =====
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=193,width=240,height=428)

        self.animation()

    def animation(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animation)



    def login(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="" :
                 messagebox.showerror("Error","All Fileds are required",parent=self.root)
            else:
               cur.execute('select utype  from emp13 where eid=? AND pass=?',(self.employee_id.get(),self.password.get()))
               user=cur.fetchone()
               if user==None:
                   messagebox.showerror("Error","Invalid USERNAME/PASSWORD",parent=self.root) 
               else:
                #    print(user)
                   if user[0]=="Admin":    
                     self.root.quit()
                     os.system("python dashbord.py")
                   else:
                       self.root.quit()
                       os.system("python billing.py")
                       
               
        except Exception as ex:
                print("Error",f"Error due to :{str(ex)}")
 


root=Tk()
obj=Login_System(root)
root.mainloop()