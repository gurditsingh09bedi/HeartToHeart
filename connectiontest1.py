# Some important library which help me to connect with mongo DB and create Frame.
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import PIL
from PIL import ImageTk
from PIL import Image
import pymongo
from pymongo import MongoClient
import subprocess

client = MongoClient('mongodb+srv://gurdit:gurdit@cluster0.kndcgcw.mongodb.net/') #connection from mongo DB with username and password
datebase = client['your_database'] #collection name

db_person = datebase['user_data'] #database name


class heartmainframe: #This is my main fream GUI where decision tree and prediction reflected.
    def __init__(self,root): # root is my mainframe name 
        self.root = root
        self.root.title("Heart 2 Heart") # frame title
        self.root.geometry('1166x718') #frame size
        self.root.state('zoomed') #frame state
        #self.root.resizable(0,0) # 0,0 not resizable, not minimize 
       
        #  Open Background image
        # using tkinter library set background image
        self.bg_frame = Image.open('image\\200585.jpg') 
        photo = ImageTk.PhotoImage(self.bg_frame)  
        self.bg_panel = tk.Label(self.root, image=photo) 
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        # Created login frame inside my main frame like container.
        self.login_frame = tk.Frame(self.root, bg='#040405', width='750', height='600')
        self.login_frame.place(x=450, y=150)
        
        # Create label for display content on contaire content is "Welcome to the Heart 2 Heart your presence matter"
        self.txt = 'Welcome to the Heart 2 Heart your presence matter'
        self.heading = tk.Label(self.login_frame, text=self.txt, font=('yu gothic ui',18,'bold'),bg='#040405', fg='white')        
        self.heading.place(x=15,y=5,width=700,height=100)

        # Set heart image in middle frame container.
        self.middle_img = Image.open('240_F_625565623_Ng1XLLWx148uMvMV3i7utD0Wq4vbzl6I.jpg')
        photo = ImageTk.PhotoImage(self.middle_img)
        self.middle_img_label = tk.Label(self.login_frame, image=photo, bg='#040405')
        self.middle_img_label.image = photo
        self.middle_img_label.place(x=10,y=200)
        
        #Set sign in images
        self.sign_in_image = Image.open('lo.jpg')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = tk.Label(self.login_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=500,y=100)
        
        # Set sign in label in middle freame
        self.sign_in_label = tk.Label(self.login_frame, text='Sign In',bg='#040405',fg='white',font=('yu gothic ui',17,'bold'))
        self.sign_in_label.place(x=530,y=250)
        
        # Set both username label and user name entiry
        self.username_label = tk.Label(self.login_frame,text='Email ID',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.username_label.place(x=370,y=300)
        self.username_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.username_entry.place(x=470,y=300,width=200)
        self.username_line = tk.Canvas(self.login_frame,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.username_line.place(x=470,y=330)        
        
        # Set password label and password entity.
        self.password_label = tk.Label(self.login_frame,text='password',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.password_label.place(x=370,y=350)
        self.password_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'),show="*")
        self.password_entry.place(x=470,y=350,width=200)
        self.password_line = tk.Canvas(self.login_frame,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.password_line.place(x=470,y=380)
        
        #login button
        self.loginButton = tk.Button(self.login_frame, text="Login",bg='#040405',fg='#6b6a69',command=self.user_credentials) 
        #self.login = tk.Button(self.logn_button_label)
        self.loginButton.place(x=550,y=400)
        
        #Set label for sign up like "No Account yet ?"
        self.sign_up_label = tk.Label(self.login_frame, text='No Account yet ?', font=('yu gothic ui',13,'bold'),background="#040405",fg='white')
        self.sign_up_label.place(x=400,y=440)
        #sign up
        self.sign_up_button = tk.Button(self.login_frame,text='SignUp',font=('yu gothic ui',13,'bold underline'),fg='white',width=10,bd=0,bg='#040405',activebackground='#040405',cursor='hand2',command=self.sign_up)
        self.sign_up_button.place(x=540,y=440)

    def sign_up(self): # This class is used close the current window frame or pythone script then open for another script my second page File name "htwoh2.py".
        # Close the current window
        root.destroy()
        
        # Run the second Python script using subprocess
        subprocess.Popen(["python", "htwoh2.py"])
        
    def user_credentials(self):
        email_id = self.username_entry.get()  # taking user Email id 
        password = self.password_entry.get()  # using get funtion taking user password from user via GUI
        user = db_person.find_one({'email':email_id,'pass':password}) # find_one is used as query in mongoDB which helps us to find out the user email ID and user Password
        
        if user: # If details found in mongo DB then close the current window frame and open second python file of my project using OOPS concepts.
            messagebox.showerror("Login....","Successfully Login")
            self.decision() # Calling 
        else:
            messagebox.showerror("Login Failed", "Invalid username or password") # if user name and password is incorrected the its reflected error.
            
    
    def decision(self): # this function is to switch main decision window frame if user name and password is corrected.
        # Close the current window
        root.destroy()
        
        # Run the second Python script using subprocess
        subprocess.Popen(["python", "prediction.py"])
        
if __name__ == "__main__":
    root = tk.Tk()
    app = heartmainframe(root)
    root.mainloop()
        
        
        
        