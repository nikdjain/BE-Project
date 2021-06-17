from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import re
import mysql.connector

import time
from mysql.connector import Error
from image_store_in_database import take_image


def check_email(email):
   regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
   if re.search(regex,email):
   	return True
   else:
   	return False
   
   
def check_name(name):
   regex='^[A-z]{5,15}$'
   if re.search(regex,name):
   	return True
   else:
   	return False
   
def check_no(phone):
   regex='^\d{10}$'
   if re.search(regex,phone):
   	return True
   else:
   	return False
   
def check_pin(pin):
   regex='^\d{4}$'
   if re.search(regex,pin):
   	return True
   else:
   	return False



def registraion_from_form():

    global user_name
    global mo_num
    global pswd1
    global pswd2
    global emailid

    User_name = user_name.get()
    Mo_num = mo_num.get()
    password1 = pswd1.get()
    password2 = pswd2.get()
    email=emailid.get()

    if(len(User_name) > 0 and len(Mo_num) == 10 and len(password1) == 4  and len(password2) == 4 and len(email) != 0):

        label2 = Label(top, text=" ")
        label2.configure(background=colour_f)
        label2.configure(foreground="#ee0000")
        label2.config(font=("Times New Roman", 15))
        label2.place(x = 450,y=450,height=30, width=400)

        top.update()
        
        mySQLconnection = mysql.connector.connect(host='localhost',
                                database='Multi_Bank',
                                user='root',
                                password='king@rO7',auth_plugin='mysql_native_password')

        sql_select_Query = "select * from user_info"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        name_already_taken = 0
        for record in records:
            if record[1].lower() == User_name.lower():
                name_already_taken = 1
                break

        phone_already_taken = 0
        for record in records:
            if record[2] == Mo_num:
                phone_already_taken = 1
                break

        match_pswd = 0
        if password1 == password2:
            match_pswd = 1
            
            
        flag1=check_name(User_name)
        flag2=check_email(email)
        flag3=check_no(Mo_num)
        flag4=check_pin(password1)



        if name_already_taken == 1:
            label2 = Label(top, text="** User name already taken **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#ee0000")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)

        elif phone_already_taken == 1:
            label2 = Label(top, text="** Mobile Number already taken **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#ee0000")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)

        elif match_pswd == 0:
            label2 = Label(top, text="** Password does not matched **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#ee0000")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)
           
        
        elif flag1 == False:
            label2 = Label(top, text="** invalid user_name(only alphabets) **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#ee0000")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)
           
        elif flag2 == False:
            label2 = Label(top, text="** invalid email **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#ee0000")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)
           
        elif flag3 == False:
            label2 = Label(top, text="** invalid phone no **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#ee0000")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)
            
        elif flag4 == False:
            label2 = Label(top, text="** pin must contain only four digits **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#ee0000")
            label2.config(font=("Times New Roman", 20))
            label2.place(x = 450,y=450,height=30, width=400)
            
        

        else:
            label2 = Label(top, text="** Opening Camera **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#00ee00")
            label2.config(font=("Times New Roman", 20))
            label2.place(x = 450,y=450,height=30, width=400)

            top.update()
            time.sleep(2)

            take_image(User_name)
            
            label2 = Label(top, text="** Image Stored Successfully **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#00ee00")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)

            top.update()
            time.sleep(2)

            label2 = Label(top, text="** Registration Completed **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#00ee00")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)

            sql = "INSERT INTO user_info (id, name, phone, emailid, pswd) VALUES (%s, %s, %s, %s, %s)"
            val = [str(len(records)+1), User_name, Mo_num, email, password1]
            cursor.execute(sql, val)
            mySQLconnection.commit()
            
            sql = "INSERT INTO multi_atm (id, name, B1,B2, B3, phone) VALUES (%s, %s, %s, %s, %s, %s)"
            val = [str(len(records)+1), User_name, '10000', '10000', '10000' , Mo_num]
            cursor.execute(sql, val)
            mySQLconnection.commit()

            top.update()
            time.sleep(2)

            label2 = Label(top, text=" ")
            label2.configure(background=colour_f)
            label2.configure(foreground="#00ee00")
            label2.config(font=("Times New Roman", 15))
            label2.place(x = 450,y=450,height=30, width=400)

            user_name = StringVar() 
            passEntry = Entry(top, textvariable=user_name)
            passEntry.place(x = 650,y=200,height=30, width=200)
            passEntry.config(font=("Timesnew roman",14))
            passEntry.configure(background=colour_w)

            mo_num = StringVar() 
            passEntry = Entry(top, textvariable=mo_num)
            passEntry.place(x = 650,y=250,height=30, width=200)
            passEntry.config(font=("Timesnew roman",14))
            passEntry.configure(background=colour_w)
            
            emailid = StringVar() 
            passEntry = Entry(top, textvariable=emailid)
            passEntry.place(x = 650,y=300,height=30, width=200)
            passEntry.config(font=("Timesnew roman",14))
            passEntry.configure(background=colour_w)  

            pswd1 = StringVar() 
            passEntry = Entry(top, textvariable=pswd1, show="*")
            passEntry.place(x = 650,y=350,height=30, width=200)
            passEntry.config(font=("Timesnew roman",14))
            passEntry.configure(background=colour_w)

            pswd2 = StringVar() 
            passEntry = Entry(top, textvariable=pswd2, show="*")
            passEntry.place(x = 650,y=400,height=30, width=200)
            passEntry.config(font=("Timesnew roman",14))
            passEntry.configure(background=colour_w)


    else:
        label2 = Label(top, text="** Consider all fields **")
        label2.configure(background=colour_f)
        label2.configure(foreground="#ee0000")
        label2.config(font=("Times New Roman", 15))
        label2.place(x = 450,y=450,height=30, width=400)

while True:

    global user_name
    global mo_num
    global pswd1
    global pswd2
    global emailid

    colour_d = "#04009a"
    colour_f = "#b6c9f0"
    colour_w = "#ffffff"
      
    top = Tk()
    top.geometry("1300x600+30+30")
    top.configure(background=colour_f)

    label2 = Label(top, text="COLLEGE  BANK  OF  INDIA")
    label2.configure(background=colour_d)
    label2.configure(foreground=colour_w)
    label2.config(font=("Times New Roman", 40))
    label2.place(x = 0,y=0,height=75, width=1300)

    label3 = Label(top, text="Registration Page")
    label3.configure(background=colour_f)
    label3.config(font=("Courier",25))
    label3.place(x = 350,y=120,height=70, width=600)
##
    label3 = Label(top, text="User Name")
    label3.configure(background=colour_f)
    label3.configure(foreground=colour_d)
    label3.config(font=("Timesnew roman",14))
    label3.place(x = 350,y=200,height=30, width=300)

    user_name = StringVar() 
    passEntry = Entry(top, textvariable=user_name)
    passEntry.place(x = 650,y=200,height=30, width=200)
    passEntry.config(font=("Timesnew roman",14))
    passEntry.configure(background=colour_w)
##
    label3 = Label(top, text="Mo. Number")
    label3.configure(background=colour_f)
    label3.configure(foreground=colour_d)
    label3.config(font=("Timesnew roman",14))
    label3.place(x = 350,y=250,height=30, width=300)

    mo_num = StringVar() 
    passEntry = Entry(top, textvariable=mo_num)
    passEntry.place(x = 650,y=250,height=30, width=200)
    passEntry.config(font=("Timesnew roman",14))
    passEntry.configure(background=colour_w)
##
    label3 = Label(top, text="Email ID")
    label3.configure(background=colour_f)
    label3.configure(foreground=colour_d)
    label3.config(font=("Timesnew roman",14))
    label3.place(x = 350,y=300,height=30, width=300)

    emailid = StringVar() 
    passEntry = Entry(top, textvariable=emailid)
    passEntry.place(x = 650,y=300,height=30, width=200)
    passEntry.config(font=("Timesnew roman",14))
    passEntry.configure(background=colour_w)    
    
##
    label3 = Label(top, text="Password")
    label3.configure(background=colour_f)
    label3.configure(foreground=colour_d)
    label3.config(font=("Timesnew roman",14))
    label3.place(x = 350,y=350,height=30, width=300)

    pswd1 = StringVar() 
    passEntry = Entry(top, textvariable=pswd1, show="*")
    passEntry.place(x = 650,y=350,height=30, width=200)
    passEntry.config(font=("Timesnew roman",14))
    passEntry.configure(background=colour_w)

##
    label3 = Label(top, text="Confirm Password")
    label3.configure(background=colour_f)
    label3.configure(foreground=colour_d)
    label3.config(font=("Timesnew roman",14))
    label3.place(x = 350,y=400,height=30, width=300)

    pswd2 = StringVar() 
    passEntry = Entry(top, textvariable=pswd2, show="*")
    passEntry.place(x = 650,y=400,height=30, width=200)
    passEntry.config(font=("Timesnew roman",14))
    passEntry.configure(background=colour_w)

    B1 = Button(top, text = "Capture Image and Register", command = registraion_from_form)
    B1.place(x = 450,y = 500 ,height=40, width=400)
    B1.config(font=("Times New Roman", 15))
    B1.configure(background=colour_d)
    B1.configure(foreground=colour_w)
    
    top.mainloop()

top.mainloop()
