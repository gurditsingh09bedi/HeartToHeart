import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import pymongo
from pymongo import MongoClient
import subprocess
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import tree
from io import BytesIO

class heartmainframe: #This is my third main fream GUI where decision tree and prediction reflected.
    def __init__(self,root): # root is my mainframe name 
        
        self.root = root # intialize attribute or object
        self.root.title("Heart 2 Heart") # frame title
        self.root.geometry('1166x718') #frame state
        self.root.state('zoomed')
        
        self.setup_gui()
        self.load_data()
        self.train_model()
        
        
    def setup_gui(self): # This function i have created to understand easily about GUI creation 
        
        # Open Background image
        # using tkinter library set background image
        self.bg_frame = Image.open('image\\200585.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = tk.Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
       
        #login frame
        # Created login frame inside my main frame like container.
        self.login_frame = tk.Frame(self.root, bg='black', width='750', height='600')
        self.login_frame.place(x=450, y=150)
        # Create label for display content on contaire content is "Hope your Heart will be healty, stay safe"        
        self.txt = 'Hope your Heart will be healty, stay safe'
        self.heading = tk.Label(self.login_frame, text=self.txt, font=('yu gothic ui',18,'bold'),bg='#040405', fg='white')        
        self.heading.place(x=15,y=5,width=700,height=100)        
        
        # Set user age label and entity
        self.userage_label = tk.Label(self.login_frame,text='Age',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.userage_label.place(x=15,y=210)
        self.userage_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.userage_entry.place(x=300,y=210,width=200)
        
        #Set user gender label and user gender entity.
        self.gender = tk.Label(self.login_frame,text='Gender (0 - Female, 1 - Male):',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.gender.place(x=15,y=235)
        self.gender_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.gender_entry.place(x=300,y=235,width=200)
        
        #Set Chestpain label and entity.
        self.chestpain = tk.Label(self.login_frame,text='ChestPain (0-ASY ,1-ATA, 2-NAP):',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.chestpain.place(x=15,y=260)
        self.chestpain_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.chestpain_entry.place(x=300,y=260,width=200)
        
        #Set Bloodpresure label and entity
        self.bp = tk.Label(self.login_frame,text='Blood Presure',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.bp.place(x=15,y=280)
        self.bp_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.bp_entry.place(x=300,y=280,width=200)
        
        #Set Cholesterol label and entity
        self.cholestrol = tk.Label(self.login_frame,text='Cholestrol',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.cholestrol.place(x=15,y=310)
        self.cholestrol_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.cholestrol_entry.place(x=300,y=310,width=200)
        
        #Set FastingBS Label and entity
        self.fastingbs = tk.Label(self.login_frame,text='FastingBS',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.fastingbs.place(x=15,y=350)
        self.fastingbs_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.fastingbs_entry.place(x=300,y=350,width=200)
        
        #Set maxhr Label and entity.
        self.hr = tk.Label(self.login_frame,text='MaxHR',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.hr.place(x=15,y=380)
        self.hr_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.hr_entry.place(x=300,y=380,width=200)
        
        #Set RatingECG Label and entity.
        self.ratingecg = tk.Label(self.login_frame,text='RatingECG (0-Normal, 1-ST)',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.ratingecg.place(x=15,y=410)
        self.ratingecg_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.ratingecg_entry.place(x=300,y=410,width=200)
        
        #Set ExeriseAngina Label and Entity.
        self.exercise = tk.Label(self.login_frame,text='ExeriseAngina (0-NO, 1- Yes)',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.exercise.place(x=15,y=450)
        self.exercise_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.exercise_entry.place(x=300,y=450,width=200)
        
        #Set oldpeak label and Entity.
        self.oldpeak = tk.Label(self.login_frame,text='OldPeak',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.oldpeak.place(x=15,y=480)
        self.oldpeak_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.oldpeak_entry.place(x=300,y=480,width=200)
        
        #Set stslop label and Entity.
        self.st = tk.Label(self.login_frame,text='ST SLOP (0-Flat, 1-UP)',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.st.place(x=15,y=510)
        self.st_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.st_entry.place(x=300,y=510,width=200)
        
        #Set heartdisease label and Enitiy
        self.heartdisease = tk.Label(self.login_frame,text='HeartDisease (0-No, 1-Yes)',bg='#040405',font=('yu gothic ui',13,'bold'),fg='#4f4e4d')
        self.heartdisease.place(x=15,y=540)
        self.heartdisease_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',12,'bold'))
        self.heartdisease_entry.place(x=300,y=540,width=200)
        
        # Set Predict button 
        self.predict_button = tk.Button(self.login_frame, text="Predict", command=self.predict_heart_attack)
        self.predict_button.place(x=580,y=300)

        # Decision Tree Graph button
        self.graph_button = tk.Button(self.login_frame, text="Show Decision Tree Graph", command=self.show_decision_tree_graph)
        self.graph_button.place(x=580,y=400)
        
        
        
    def load_data(self): # Connect to MongoDB and fetch the dataset
        client = MongoClient("mongodb+srv://gurdit:gurdit@cluster0.kndcgcw.mongodb.net/")
        db = client["your_database"] # This is mongo DB client connection 
        collection = db["decisiontree"] # This is CSV file Uploaded.
        data = list(collection.find()) # Converted CSV data collection in list.
        self.df = pd.DataFrame(data)  # Assuming data is stored as a DataFrame
        categorical_columns = self.df.select_dtypes(include=['object']).columns

        # Apply Label Encoding or One-Hot Encoding to each categorical column
        for column in categorical_columns: #conveted catagorical values in  numeric values RestingECG, Sex, ChestPainType, ExerciseAngina, ST_Slope
            # Option 1: Label Encoding
            self.df[column] = self.df[column].astype('category')
            self.df[column] = self.df[column].cat.codes

    def train_model(self):
        # Split the dataset into features (X) and the target (y)
        self.X = self.df.drop("HeartDisease", axis=1)
        print(self.X) # printing spliting data to check the spliting values
        
        self.y = self.df["HeartDisease"] # Printing y train  
        print(self.y)
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Create and train the decision tree classifier
        self.clf = DecisionTreeClassifier()
        self.clf.fit(X_train, y_train)

    def predict_heart_attack(self): # Create predition funtion for the decesion tree 
        # taking values from function GUI user input and all inputs values in converted in INT  format
        age = int(self.userage_entry.get()) 
        gender = int(self.gender_entry.get())
        chest_pain_type = int(self.chestpain_entry.get())
        resting_bp = int(self.bp_entry.get())
        cholesterol = int(self.cholestrol_entry.get())
        fasting_bs = int(self.fastingbs_entry.get())
        resting_ecg = int(self.ratingecg_entry.get())
        max_hr = int(self.hr_entry.get())
        exercise_angina = int(self.exercise_entry.get())
        oldpeak = float(self.oldpeak_entry.get())
        st_slope = int(self.st_entry.get())
        heartd = int(self.heartdisease_entry.get())
        
        user_input = {'Age': age, 
                       'Sex': gender,
                       'ChestPainType': chest_pain_type, 
                       'RestingBP': resting_bp, 
                       'Cholesterol': cholesterol, 
                       'FastingBS': fasting_bs, 
                       'RestingECG': resting_ecg, 
                       'MaxHR': max_hr, 
                       'ExerciseAngina': exercise_angina, 
                       'Oldpeak': oldpeak, 
                       'ST_Slope': st_slope,
                       'HeartDisease': heartd
                      }
    
        # Convert the dictionary into a NumPy array
        user_input_array = np.array([list(user_input.values())])

        # Make a prediction using the model
        prediction = self.clf.predict(user_input_array)
        
        if prediction[0] == 1:
            messagebox.showerror("Alert", "The model predicts a High risk of a heart attack.")
        else:
            messagebox.showerror("The model predicts a low risk of a heart attack.")
            
    def show_decision_tree_graph(self): # This function is used to display the decision tree of CSV file which is linked with monmgo DB
        plt.figure(figsize=(14, 10)) #fig size
        tree.plot_tree(self.clf, filled=True, feature_names=self.X.columns.tolist(), class_names=["No Heart Attack", "Heart Attack"])
        plt.title("Decision Tree Graph") # plot title
        img_data = BytesIO() 
        plt.savefig(img_data, format="png")
        img_data.seek(0)

        # Create a new window to display the graph
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Decision Tree Graph")
        img = tk.PhotoImage(data=img_data.read())
        img_label = tk.Label(graph_window, image=img)
        img_label.image = img
        img_label.pack()
        img_data.close()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = heartmainframe(root)
    root.mainloop()
        