import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import PIL
from PIL import ImageTk
from PIL import Image
import pymongo
from pymongo import MongoClient
import subprocess

client = MongoClient('mongodb+srv://gurdit:gurdit@cluster0.kndcgcw.mongodb.net/') #This is my third main fream GUI where decision tree and prediction reflected.
db = client["your_database"] # #collection name 
user_data_collection = db["user_data"] # database name


class heartmainframe:
    def __init__(self,root): # root is my mainframe name 
        self.root = root # intialize attribute or object
        self.root.title("Heart 2 Heart") # frame title
        self.root.geometry('1166x718') #frame geometry
        self.root.state('zoomed')
        #self.root.resizable(0,0) # 0,0 not resizable, not minimize 
        # Open Background image
        # using tkinter library set background image
        self.bg_frame = Image.open('image\\200585.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = tk.Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # Set login frame
        self.login_frame = tk.Frame(self.root, bg='#040405', width='750', height='600')
        self.login_frame.place(x=450, y=150)
        # Create label for display content on contaire content is "Heart 2 Heart"     
        self.txt = 'Heart 2 Heart'
        self.heading = tk.Label(self.login_frame, text=self.txt, font=('yu gothic ui',18,'bold'),bg='#040405', fg='white')        
        self.heading.place(x=15,y=5,width=700,height=100)
        
        #Set sign in images
        self.sign_in_image = Image.open('signup.jpg')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = tk.Label(self.login_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=80,y=250)
        
        #set Sign UP label.
        self.sign_in_label = tk.Label(self.login_frame, text='Sign Up',bg='#040405',fg='white',font=('yu gothic ui',17,'bold'))
        self.sign_in_label.place(x=320,y=100)
        
        #Set username label and Entity
        self.username_label = tk.Label(self.login_frame,text='First Name',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.username_label.place(x=280,y=200)
        self.username_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.username_entry.place(x=380,y=200,width=200)
        self.username_line = tk.Canvas(self.login_frame,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.username_line.place(x=380,y=225)        
        
        # Set password label and Entity
        self.last_name_label = tk.Label(self.login_frame,text='Last Name',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.last_name_label.place(x=280,y=250)
        self.last_name_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.last_name_entry.place(x=380,y=250,width=200)
        self.last_name_line = tk.Canvas(self.login_frame,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.last_name_line.place(x=380,y=275)
        
        #Set Email ID label and Entity.
        self.email_id_label = tk.Label(self.login_frame,text='Email Id',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.email_id_label.place(x=280,y=300)
        self.email_id_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.email_id_entry.place(x=380,y=300,width=200)
        self.email_id_line = tk.Canvas(self.login_frame,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.email_id_line.place(x=380,y=325)
        
        #Set password Label and Entity
        self.password_label = tk.Label(self.login_frame,text='Password',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.password_label.place(x=280,y=350)
        self.password_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.password_entry.place(x=380,y=350,width=200)
        self.password_line = tk.Canvas(self.login_frame,width=200,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.password_line.place(x=380,y=375)
        
        #Set login button label and entity
        self.loginButton = tk.Button(self.login_frame, text='Create',bg='#040405',fg='#6b6a69',command=self.save_user_input)
        #self.login = tk.Button(self.logn_button_label)
        self.loginButton.place(x=450,y=400)
        
        #back to front page
        self.loginButton = tk.Button(self.login_frame, text='Back to login',bg='#040405',fg='#6b6a69',command=self.decision)
        #self.login = tk.Button(self.logn_button_label)
        self.loginButton.place(x=450,y=480)
        
        #this is used to diplay the tect after succesfull register
        self.message_label = tk.Label(self.login_frame, text="") 
        self.message_label.place(x=400,y=440)
        
        self.root.mainloop()
        
    
    def save_user_input(self):
        # taking values from function GUI user input
        name = self.username_entry.get()
        last = self.last_name_entry.get()
        email = self.email_id_entry.get()
        password = self.password_entry.get()
        user_data = {
            "firstname": name,
            "lastemail": last,
            "email": email,
            "pass": password
        }
 
        # Insert user input data into MongoDB
        user_data_collection.insert_one(user_data)
 
        self.clear_fields() # this fuction Clear the field after successfull upload the vales in mongo DB
        self.message_label.config(text="Successfully account created")
 
    def clear_fields(self):
        self.username_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.email_id_entry.delete(0, 'end')
    
    def decision(self): #After successfully register then it will move to login page where we can use register email id and password
        # Close the current window
        root.destroy()
        
        # Run the second Python script using subprocess
        subprocess.Popen(["python", "connectiontest1.py"])
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = heartmainframe(root)
    root.mainloop()
        
        
        
        