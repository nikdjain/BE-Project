from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import mysql.connector
##import serial
import time
from mysql.connector import Error
from random import randint
import face_detect

from SMS import send_OTP

def read_next_data():
    global face_id_val
    def show():

        p = password.get() #get password from entry
        p = int(p)
        if(p == OTP):
            print('Password Match')
            top.destroy()
            
            def dummy():
                print('dummy page')

            def banking_details():
                def EXIT():
                    bank_details.destroy()


                colour_d = "#700000"
                colour_f = "#ffefdb"
                colour_w = "#ffffff"
             
                bank_details = Tk()
                bank_details.geometry("1300x600+30+30")
                bank_details.configure(background=colour_f)

                label2 = Label(bank_details, text="COLLEGE  BANK  OF  INDIA")
                label2.configure(background=colour_d)
                label2.configure(foreground=colour_w)
                label2.config(font=("Times New Roman", 40))
                label2.place(x = 0,y=0,height=75, width=1300)

                mySQLconnection = mysql.connector.connect(host='localhost',
                                database='Multi_Bank',
                                user='root',
                                password='king@rO7',auth_plugin='mysql_native_password')

                sql_select_Query = "select * from multi_atm WHERE id = " + str(ID + 1)

                cursor = mySQLconnection .cursor()
                cursor.execute(sql_select_Query)
                recordss = cursor.fetchall()

                label1 = Label(bank_details, text="Bank Balance")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 20))
                label1.place(x = 75,y=90,height=70, width=500)

                label1 = Label(bank_details, text="SBI : ")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 175,y=300,height=70, width=70)

                label1 = Label(bank_details, text="HDFC :")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 175,y=400,height=70, width=70)

                label1 = Label(bank_details, text="ICICI :")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 175,y=500,height=70, width=70)

                label1 = Label(bank_details, text="Account balance")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 320,y=220,height=70, width=200)

                label1 = Label(bank_details, text="Banks")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 105,y=220,height=70, width=200)

                label1 = Label(bank_details, text="-------------------------------------------------")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 80,y=270,height=10, width=500)

                label1 = Label(bank_details, text=recordss[0][2])
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 320,y=300,height=70, width=200)

                label1 = Label(bank_details, text=recordss[0][3])
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 320,y=400,height=70, width=200)

                label1 = Label(bank_details, text=recordss[0][4])
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 320,y=500,height=70, width=200)

                W_Okay = Button(bank_details, text = "EXIT", command = EXIT)
                W_Okay.place(x = 1000,y =350,height=40, width=300)
                W_Okay.config(font=("Times New Roman", 20))
                W_Okay.configure(background=colour_d)
                W_Okay.configure(foreground=colour_w)


            def banking():
                bank_choice.destroy()

                def withdraw():

                    Bank_amount1 = amt1.get()
                    if(len(Bank_amount1) == 0):
                        Bank_amount1 = int(0)
                    else:
                        Bank_amount1 = int(Bank_amount1)

                    Bank_amount2 = amt2.get()
                    if(len(Bank_amount2) == 0):
                        Bank_amount2 = int(0)
                    else:
                        Bank_amount2 = int(Bank_amount2)

                    Bank_amount3 = amt3.get()
                    if(len(Bank_amount3) == 0):
                        Bank_amount3 = int(0)
                    else:
                        Bank_amount3 = int(Bank_amount3)
                        
                    mydb = mysql.connector.connect(host='localhost',
                                database='Multi_Bank',
                                user='root',
                                password='king@rO7',auth_plugin='mysql_native_password')
                    mycursor = mydb.cursor()
                    sql = "UPDATE multi_atm SET B1 = %s WHERE id = %s"
                    val = (str(int(records[0][2]) - Bank_amount1), str(ID+1))
                    mycursor.execute(sql, val)

                    sql = "UPDATE multi_atm SET B2 = %s WHERE id = %s"
                    val = (str(int(records[0][3]) - Bank_amount2), str(ID+1))
                    mycursor.execute(sql, val)

                    sql = "UPDATE multi_atm SET B3 = %s WHERE id = %s"
                    val = (str(int(records[0][4]) - Bank_amount3), str(ID+1))
                    mycursor.execute(sql, val)

                    mydb.commit()
                    bank.destroy()

                    def EXIT():
                        bank_details.destroy()


                    colour_d = "#700000"
                    colour_f = "#ffefdb"
                    colour_w = "#ffffff"
                 
                    bank_details = Tk()
                    bank_details.geometry("1300x600+30+30")
                    bank_details.configure(background=colour_f)

                    label2 = Label(bank_details, text="COLLEGE  BANK  OF  INDIA")
                    label2.configure(background=colour_d)
                    label2.configure(foreground=colour_w)
                    label2.config(font=("Times New Roman", 40))
                    label2.place(x = 0,y=0,height=75, width=1300)

                    mySQLconnection = mysql.connector.connect(host='localhost',
                                database='Multi_Bank',
                                user='root',
                                password='king@rO7',auth_plugin='mysql_native_password')

                    sql_select_Query = "select * from multi_atm WHERE id = " + str(ID + 1)

                    cursor = mySQLconnection .cursor()
                    cursor.execute(sql_select_Query)
                    recordss = cursor.fetchall()

                    label1 = Label(bank_details, text="Bank Balance")
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 20))
                    label1.place(x = 75,y=90,height=70, width=500)

                    label1 = Label(bank_details, text="SBI : ")
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 175,y=300,height=70, width=70)

                    label1 = Label(bank_details, text="HDFC :")
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 175,y=400,height=70, width=70)

                    label1 = Label(bank_details, text="ICICI :")
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 175,y=500,height=70, width=70)

                    label1 = Label(bank_details, text="Account balance")
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 320,y=220,height=70, width=200)

                    label1 = Label(bank_details, text="Banks")
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 105,y=220,height=70, width=200)

                    label1 = Label(bank_details, text="-------------------------------------------------")
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 80,y=270,height=10, width=500)

                    label1 = Label(bank_details, text=recordss[0][2])
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 320,y=300,height=70, width=200)

                    label1 = Label(bank_details, text=recordss[0][3])
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 320,y=400,height=70, width=200)

                    label1 = Label(bank_details, text=recordss[0][4])
                    label1.configure(background=colour_f)
                    label1.configure(foreground=colour_d)
                    label1.config(font=("Bold", 15))
                    label1.place(x = 320,y=500,height=70, width=200)

                    W_Okay = Button(bank_details, text = "EXIT", command = EXIT)
                    W_Okay.place(x = 1000,y =350,height=40, width=300)
                    W_Okay.config(font=("Times New Roman", 20))
                    W_Okay.configure(background=colour_d)
                    W_Okay.configure(foreground=colour_w)
                    ##########################################################

                
    ######
                colour_d = "#700000"
                colour_f = "#ffefdb"
                colour_w = "#ffffff"
             
                bank = Tk()
                bank.geometry("1300x600+30+30")
                bank.configure(background=colour_f)

                label2 = Label(bank, text="COLLEGE  BANK  OF  INDIA")
                label2.configure(background=colour_d)
                label2.configure(foreground=colour_w)
                label2.config(font=("Times New Roman", 40))
                label2.place(x = 0,y=0,height=75, width=1300)


                mySQLconnection = mysql.connector.connect(host='localhost',
                                database='Multi_Bank',
                                user='root',
                                password='king@rO7',auth_plugin='mysql_native_password')

                sql_select_Query = "select * from multi_atm WHERE id = " + str(ID + 1)

                cursor = mySQLconnection .cursor()
                cursor.execute(sql_select_Query)
                records = cursor.fetchall()
                val = records[0]
                time.sleep(2)

                label1 = Label(bank, text="SBI : ")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 75,y=300,height=70, width=70)

                label1 = Label(bank, text="HDFC :")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 75,y=400,height=70, width=70)

                label1 = Label(bank, text="ICICI :")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 75,y=500,height=70, width=70)

                label1 = Label(bank, text="Account balance")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 200,y=200,height=70, width=200)

                label1 = Label(bank, text="Withdrawal amount")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 430,y=200,height=70, width=200)

                label1 = Label(bank, text=records[0][2])
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 220,y=300,height=70, width=200)

                label1 = Label(bank, text=records[0][3])
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 220,y=400,height=70, width=200)

                label1 = Label(bank, text=records[0][4])
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 15))
                label1.place(x = 220,y=500,height=70, width=200)

                amt1 = StringVar()
                bank1Entry = Entry(bank, textvariable=amt1)
                bank1Entry.place(x =500,y=325,height=20, width=60)

                amt2 = StringVar()
                bank2Entry = Entry(bank, textvariable=amt2)
                bank2Entry.place(x =500,y=425,height=20, width=60)

                amt3 = StringVar()
                bank3Entry = Entry(bank, textvariable=amt3)
                bank3Entry.place(x =500,y=525,height=20, width=60)

                W_Okay = Button(bank, text = "CONFIRM", command = withdraw)
                W_Okay.place(x = 1000,y =350,height=40, width=300)
                W_Okay.config(font=("Times New Roman", 20))
                W_Okay.configure(background=colour_d)
                W_Okay.configure(foreground=colour_w)

                colour_d = "#700000"
                colour_f = "#ffefdb"
                colour_w = "#ffffff"

             
                auth = Tk()
                auth.geometry("1300x600+30+30")
                auth.configure(background=colour_f)

                label2 = Label(auth, text="COLLEGE  BANK  OF  INDIA")
                label2 = Label(auth, text="AJAY HERE")
                label2.configure(background=colour_d)
                label2.configure(foreground=colour_w)
                label2.config(font=("Times New Roman", 40))
                label2.place(x = 0,y=0,height=75, width=1300)


                label1 = Label(auth, text="Authentication Success")
                label1.configure(background=colour_f)
                label1.configure(foreground=colour_d)
                label1.config(font=("Bold", 30))
                label1.place(x = 350,y=300,height=70, width=600)
                auth.update()
                time.sleep(2)
                auth.destroy()
                auth.mainloop()

############
############
############



            colour_d = "#700000"
            colour_f = "#ffefdb"
            colour_w = "#ffffff"
         
            bank_choice = Tk()
            bank_choice.geometry("1300x600+30+30")
            bank_choice.configure(background=colour_f)


            label2 = Label(bank_choice, text="COLLEGE  BANK  OF  INDIA")
            label2 = Label(bank_choice, text="choice page")
            label2.configure(background=colour_d)
            label2.configure(foreground=colour_w)
            label2.config(font=("Times New Roman", 40))
            label2.place(x = 0,y=0,height=75, width=1300)


            B1 = Button(bank_choice, text = "Change PIN", command = dummy)
            B1.place(x = 1000,y = 250 ,height=40, width=300)
            B1.config(font=("Times New Roman", 20))
            B1.configure(background=colour_d)
            B1.configure(foreground=colour_w)

            B1 = Button(bank_choice, text = "View Balance", command = banking_details)
            B1.place(x = 1000,y = 350 ,height=40, width=300)
            B1.config(font=("Times New Roman", 20))
            B1.configure(background=colour_d)
            B1.configure(foreground=colour_w)

            B1 = Button(bank_choice, text = "Banking", command = banking)
            B1.place(x = 0,y = 250 ,height=40, width=300)
            B1.config(font=("Times New Roman", 20))
            B1.configure(background=colour_d)
            B1.configure(foreground=colour_w)

            B1 = Button(bank_choice, text = "Change PIN", command = dummy)
            B1.place(x = 0,y = 350 ,height=40, width=300)
            B1.config(font=("Times New Roman", 20))
            B1.configure(background=colour_d)
            B1.configure(foreground=colour_w)

            bank_choice.mainloop()


        else:
            print('Wrong Password')
            top.destroy()

            colour_d = "#700000"
            colour_f = "#ffefdb"
            colour_w = "#ffffff"
         
            auth = Tk()
            auth.geometry("1300x600+30+30")
            auth.configure(background=colour_f)

            label2 = Label(auth, text="COLLEGE  BANK  OF  INDIA")
            label2.configure(background=colour_d)
            label2.configure(foreground=colour_w)
            label2.config(font=("Times New Roman", 40))
            label2.place(x = 0,y=0,height=75, width=1300)


            label1 = Label(auth, text="Access Denied")
            label1.configure(background=colour_f)
            label1.configure(foreground=colour_d)
            label1.config(font=("Bold", 30))
            label1.place(x = 350,y=300,height=70, width=600)

            auth.update()
            time.sleep(2)
            auth.destroy()

            auth.mainloop()

    ##############################

    OTP = randint(1000, 9999)
    print("OTP : ", OTP)

##    send_OTP(OTP)
    ID = face_id_val

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
        if int(record[0]) == ID+1:
            phone_numberr = record[5]
            break

    print("phone_numberr : ",phone_numberr )

    send_OTP(OTP,phone_numberr)

    if(face_id_val == ID):


        print('Authenticated')

        mySQLconnection = mysql.connector.connect(host='localhost',
                                database='Multi_Bank',
                                user='root',
                                password='king@rO7',auth_plugin='mysql_native_password')



        sql_select_Query = "select * from multi_atm WHERE id = " + str(ID + 1)

        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
##        print(records[0][ID-1])
        val = records[0]
        time.sleep(2)

        label3 = Label(top, text="Welcome  " + records[0][1])
        label3.configure(background=colour_f)
        label3.config(font=("Courier",25))
        label3.place(x = 350,y=150,height=70, width=600)

        label3 = Label(top, text="OTP is send to your registered Mobile Number")
        label3.configure(background=colour_f)
        label3.configure(foreground=colour_d)
        label3.config(font=("Courier",15))
        label3.place(x = 350,y=250,height=70, width=600)

        password = StringVar() #Password variable
        passEntry = Entry(top, textvariable=password, show='*')
        passEntry.place(x = 550,y=350,height=30, width=200)
        passEntry.configure(background=colour_w)

        submit = Button(top, text='ENTER',command=show)
        submit.place(x = 575,y = 420 ,height=30, width=150)
        submit.config(font=("Times New Roman", 20))
        submit.configure(background=colour_d)
        submit.configure(foreground=colour_w)
    else:
        top.destroy()


def camera_on():

    global face_id_val
    face_id_val = face_detect.face_id()
    print("face ID",face_id_val)
    read_next_data()

    label3 = Label(top, text= "  ")
    label3.configure(background=colour_f)
    label3.config(font=("Courier",25))
    label3.place(x = 1000,y=200,height=40, width=300)


while True:
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

    B1 = Button(top, text = "CAMERA ON", command = camera_on)
    B1.place(x = 1000,y = 200 ,height=40, width=300)
    B1.config(font=("Times New Roman", 20))
    B1.configure(background=colour_d)
    B1.configure(foreground=colour_w)
    
    top.mainloop()

#######################################################
      
########################################################

top.mainloop()
