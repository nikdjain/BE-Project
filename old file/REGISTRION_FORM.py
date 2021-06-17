from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import mysql.connector

import time
from mysql.connector import Error
from image_store_in_database import take_image

def registraion_from_form():

    global user_name
    global mo_num
    global email_id
    global password

    User_name = user_name.get()
    Mo_num = mo_num.get()

    if(len(User_name) > 0 and len(Mo_num) == 10 and email_id != NULL and password != NULL):

        label2 = Label(top, text=" ")
        label2.configure(background=colour_f)
        label2.configure(foreground="#ee0000")
        label2.config(font=("Times New Roman", 20))
        label2.place(x = 450,y=420,height=30, width=400)

        top.update()
        
        mySQLconnection = mysql.connector.connect(host='localhost',
                                database='Multi_Bank',
                                user='root',
                                password='king@rO7',auth_plugin='mysql_native_password')

        sql_select_Query = "select * from multi_atm"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        name_already_taken = 0
        for record in records:
            if record[1].lower() == User_name.lower():
                name_already_taken = 1
                break

        if name_already_taken == 1:
            label2 = Label(top, text="** User name already taken **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#ee0000")
            label2.config(font=("Times New Roman", 20))
            label2.place(x = 450,y=420,height=30, width=400)

        else:
            sql = "INSERT INTO multi_atm (id, name, B1,B2, B3, phone) VALUES (%s, %s, %s, %s, %s, %s)"
            val = [str(len(records)+1), User_name, '10000', '10000', '10000' , Mo_num]
            cursor.execute(sql, val)
            mySQLconnection.commit()

            label2 = Label(top, text="** Opening Camera **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#00ee00")
            label2.config(font=("Times New Roman", 20))
            label2.place(x = 450,y=420,height=30, width=400)

            top.update()
            time.sleep(2)

            take_image(User_name)
            
            label2 = Label(top, text="** Image Stored Successfully **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#00ee00")
            label2.config(font=("Times New Roman", 20))
            label2.place(x = 450,y=420,height=30, width=400)

            top.update()
            time.sleep(2)

            label2 = Label(top, text="** Registration Completed **")
            label2.configure(background=colour_f)
            label2.configure(foreground="#00ee00")
            label2.config(font=("Times New Roman", 20))
            label2.place(x = 450,y=420,height=30, width=400)

            top.update()
            time.sleep(2)

            label2 = Label(top, text=" ")
            label2.configure(background=colour_f)
            label2.configure(foreground="#00ee00")
            label2.config(font=("Times New Roman", 20))
            label2.place(x = 450,y=420,height=30, width=400)

            user_name = StringVar() 
            passEntry = Entry(top, textvariable=user_name)
            passEntry.place(x = 650,y=250,height=30, width=200)
            passEntry.config(font=("Timesnew roman",14))
            passEntry.configure(background=colour_w)

            mo_num = StringVar() 
            passEntry = Entry(top, textvariable=mo_num)
            passEntry.place(x = 650,y=350,height=30, width=200)
            passEntry.config(font=("Timesnew roman",14))
            passEntry.configure(background=colour_w)


    else:
        label2 = Label(top, text="** Consider all fields **")
        label2.configure(background=colour_f)
        label2.configure(foreground="#ee0000")
        label2.config(font=("Times New Roman", 20))
        label2.place(x = 450,y=420,height=30, width=400)

while True:

    global user_name
    global mo_num

    colour_d = "#700000"
    colour_f = "#ffefdb"
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
    label3.place(x = 350,y=150,height=70, width=600)

    label3 = Label(top, text="User Name")
    label3.configure(background=colour_f)
    label3.configure(foreground=colour_d)
    label3.config(font=("Timesnew roman",14))
    label3.place(x = 350,y=250,height=30, width=300)

    user_name = StringVar() 
    passEntry = Entry(top, textvariable=user_name)
    passEntry.place(x = 650,y=250,height=30, width=200)
    passEntry.config(font=("Timesnew roman",14))
    passEntry.configure(background=colour_w)

    label3 = Label(top, text="Mo. Number")
    label3.configure(background=colour_f)
    label3.configure(foreground=colour_d)
    label3.config(font=("Timesnew roman",14))
    label3.place(x = 350,y=350,height=30, width=300)

    mo_num = StringVar() 
    passEntry = Entry(top, textvariable=mo_num)
    passEntry.place(x = 650,y=350,height=30, width=200)
    passEntry.config(font=("Timesnew roman",14))
    passEntry.configure(background=colour_w)
    
    label3 = Label(top, text="User Name")
    label3.configure(background=colour_f)
    label3.configure(foreground=colour_d)
    label3.config(font=("Timesnew roman",14))
    label3.place(x = 350,y=250,height=30, width=300)


    user_name = StringVar() 
    passEntry = Entry(top, textvariable=user_name)
    passEntry.place(x = 650,y=250,height=30, width=200)
    passEntry.config(font=("Timesnew roman",14))
    passEntry.configure(background=colour_w)


    B1 = Button(top, text = "Capture Image and Register", command = registraion_from_form)
    B1.place(x = 450,y = 480 ,height=40, width=400)
    B1.config(font=("Times New Roman", 20))
    B1.configure(background=colour_d)
    B1.configure(foreground=colour_w)
    
    top.mainloop()

top.mainloop()
