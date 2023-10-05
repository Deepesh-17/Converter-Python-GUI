import tkinter as tk
from tkinter import ttk
import datetime

def page1():
    notebook.select(tab1)

def page2():
    notebook.select(tab2)
    
def page3():
    notebook.select(tab3)
    
def page4():
    notebook.select(tab4)

def update_datetime():
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    datetime_label.config(text=current_datetime)
    tab1.after(1000, update_datetime)



app = tk.Tk()
app.title("Convetion")
app.geometry("525x400+490+150")


# Create a notebook widget (tabbed interface)
notebook = ttk.Notebook(app)


# =========================Create Page 1===========================
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Home")

##setting the background color
canvas1 = tk.Canvas(tab1, background="#0072BB")
canvas1.pack(fill="both", expand=True)

#Creating a label to display date and time
datetime_label = tk.Label(canvas1, font=("CourierNew", 16))
datetime_label.place(x= 150,y= 0)


#Label for introdution
label1 = tk.Label(tab1, text="Welcome to Unit Converter")
label1.place(x=100,y=50)
update_datetime()


## =========================Create Page 2===========================
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Page 1")

coloor = tk.Canvas(tab2, background="#FFF700")
coloor.pack(fill="both", expand=True)

c_tab2= tk.Label(coloor, text="")



title_label=tk.Label(tab2, text="--This Page helps you in Convertion of Length--")
title_label.place(x=130, y=0)

lscale=['Meters','Inches','Foot','Centimeter']
_from = tk.StringVar()

from_label=tk.Label(tab2, text="Select Unit: ")
from_label.place(x=80, y=60)

from_menu=tk.OptionMenu(tab2,_from, *lscale)
from_menu.place(x= 180,y= 55)

labl=tk.Label(tab2,text="Convert to: ")
labl.place(x= 300,y= 60)

to_=tk.StringVar()
to_menu=tk.OptionMenu(tab2, to_ , *lscale)
to_menu.place(x= 380,y= 55) 

enter=tk.Label(tab2,text="Enter the Length: ")
enter.place(x= 80,y= 105)

#Input box widget to get number
val=tk.Entry(tab2)
val.place(x= 230,y= 105)

def conv():

    frem=_from.get()
    to  = to_.get()
    try:
        
        num_val=val.get()
        num=float(num_val)
        result_text = ""

        #Meter to *
        if frem == 'Meters' and to == 'Inches':
            con_num = num*39.37
        elif frem == 'Meters' and to == 'Foot':
            con_num = num*3.28
        elif frem == 'Meters' and to == 'Centimeter':
            con_num = num*100

        #Inches to *
        elif frem == 'Inches' and to == 'Foot':
            con_num = num*0.08
        elif frem == 'Inches' and to == 'Centimeter':
            con_num = num*2.54
        elif frem == 'Inches' and to == 'Meters':
            con_num = num*0.02

        #Foot to *
        elif frem == 'Foot' and to == 'Inches':
            con_num = num*12
        elif frem == 'Foot' and to == 'Meters':
            con_num = num*30.48
        elif frem == 'Foot' and to == 'Centimeter':
            con_num = num*2.54

        #Centimeter to *
        elif frem == 'Centimeter' and to == 'Meters':
            con_num = num*0.01
        elif frem == 'Centimeter' and to == 'Foot':
            con_num = num*0.03
        elif frem == 'Centimeter' and to == 'Inches':
            con_num = num*0.39

        else:
            con_num = num

    except ValueError:
        result_label.config(text="Enter a valid number")

    result_text = f"{num} {frem} is equal to {con_num:.2f} {to}."
    result_label.config(text=result_text)

result_label = tk.Label(tab2, text="", fg="green")
result_label.place(x=180, y=180)


#Convertion Button
convbut=tk.Button(tab2,text='Convert' ,command=conv)
convbut.place(x = 180,y = 150)

#===========================Create Page 3===========================
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Page 2")

##Background Color
coloor = tk.Canvas(tab3, background="#FFF700")
coloor.pack(fill="both", expand=True)
c_tab3= tk.Label(coloor, text="")




title_label=tk.Label(tab3, text="--This Page helps you in Convertion of Temperature--")
title_label.place(x=130, y=0)

Tscale=['° Celsius','Kelvin','Fahrenheit']


from_label1=tk.Label(tab3, text="Select Unit1: ")
from_label1.place(x=80, y=60)

_tfrom = tk.StringVar()
Tfrom_menu=tk.OptionMenu(tab3,_tfrom, *Tscale)
Tfrom_menu.place(x= 180,y= 55)

Tlabl=tk.Label(tab3,text="Convert to Unit2: ")
Tlabl.place(x= 280,y= 60)

Tto_=tk.StringVar()
Tto_menu=tk.OptionMenu(tab3, Tto_ , *Tscale)
Tto_menu.place(x= 380,y= 55) 

Tenter=tk.Label(tab3,text="Enter the Temperature: ")
Tenter.place(x= 80,y= 105)

#Input box widget to get number
T_val=tk.Entry(tab3)
T_val.place(x= 230,y= 105)

def conv():

    T_frem=_tfrom.get()
    T_to  = Tto_.get()
    try:
        
        num_valu=T_val.get()
        temp_val=float(num_valu)
        resul_text = ""

        #Celsius to *
        if T_frem == '° Celsius' and T_to == 'Kelvin':
            temp = temp_val + 273.15 ##0°C + 273.15 
        elif T_frem == '° Celsius' and T_to == 'Fahrenheit':
            temp = (temp_val* (1.8)) + 32 ##(0°C × 9/5) + 32

        #Kelvin to *
        elif T_frem == 'Kelvin' and T_to == 'Fahrenheit':
            temp = ((temp_val - 273.15) * (1.8) + 32 ) ##(0K − 273.15) × 9/5 + 32 
        elif T_frem == 'Kelvin' and T_to == '° Celsius':
            temp = temp_val - 273.15  ##0K − 273.15 

        #Fahrenheit to *
        elif T_frem == 'Fahrenheit' and T_to == '° Celsius':
            temp = ((temp_val - 32) * (0.56))  ##(0°F − 32) × 5/9
        elif T_frem == 'Fahrenheit' and T_to == 'Kelvin':
            temp = ((temp_val - 32) * (0.56) + 273.15)    ##(0°F − 32) × 5/9 + 273.15

        else:
            temp = temp_val

    except ValueError:
        result_label.config(text="Enter a valid number")

    resul = f"{temp_val} {T_frem} is equal to {temp:.2f} {T_to}."
    resul_label.config(text=resul)

resul_label = tk.Label(tab3, text="", fg="green")
resul_label.place(x=150, y=200)


#Convertion Button
convbut=tk.Button(tab3,text='Convert' ,command=conv)
convbut.place(x = 200,y = 150)

#============================Create Page 4==========================
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Page 3")

##Set Background Color
page_color=tk.Canvas(tab4,background="#FF2700")
page_color.pack(fill="both",expand=True)
tab_color=tk.Label(page_color,text="")

##Page Title
label4 = tk.Label(tab4, text="--This Page helps you in Convertion of Currency--")
label4.place(x=130,y=0)

##List of Currncy
c_list=['₹ INR','$ USD Dollor','¥ Yen','€ Euro','₩ Won']


##First Label for dropbox
f1_label=tk.Label(tab4,text="Select Currency:")
f1_label.place(x=80,y=60)

##First Dropbox,
currenc1=tk.StringVar()
drop_box1=tk.OptionMenu(tab4,currency1, *c_list)
drop_box1.place(x=180,y=55)

##Second Label for dropbox
f2_label=tk.Label(tab4,text="Convert into:")
f2_label.place(x=280,y=60)

##Second Dropbox,
currenc2=tk.StringVar()
drop_box21=tk.OptionMenu(tab4,currency2, *c_list)
drop_box2.place(x=180,y=55)

##Label for input box
curr_labl=tk.Label(tab4,text="Enter the Value:")
cutt_labl.place(x=80,y=105)

##Input box to get value
cur_val=tk.Entry(tab4)
cur_val.place(x=80,y=105)

def currecy():
    in_curr=currency1.get()
    out_curr=currency2.get()
    try:
        inpt1=cur_val.get()
        curny=float(inpt1)
        result_value = ""




        



notebook.pack(fill="both", expand=True)
page1()  # Start on Page 1
app.mainloop()

import tkinter as tk
from tkinter import ttk
import datetime

def page1():
    notebook.select(tab1)

def page2():
    notebook.select(tab2)
    
def page3():
    notebook.select(tab3)
    
def page4():
    notebook.select(tab4)

def update_datetime():
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    datetime_label.config(text=current_datetime)
    tab1.after(1000, update_datetime)



app = tk.Tk()
app.title("Convetion")
app.geometry("525x400+490+150")


# Create a notebook widget (tabbed interface)
notebook = ttk.Notebook(app)


# =========================Create Page 1===========================
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Home")

##setting the background color
canvas1 = tk.Canvas(tab1, background="#0072BB")
canvas1.pack(fill="both", expand=True)

#Creating a label to display date and time
datetime_label = tk.Label(canvas1, font=("CourierNew", 16))
datetime_label.place(x= 150,y= 0)


#Label for introdution
label1 = tk.Label(tab1, text="Welcome to Unit Converter")
label1.place(x=100,y=50)
update_datetime()


## =========================Create Page 2===========================
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Page 1")

coloor = tk.Canvas(tab2, background="#FFF700")
coloor.pack(fill="both", expand=True)

c_tab2= tk.Label(coloor, text="")



title_label=tk.Label(tab2, text="--This Page helps you in Convertion of Length--")
title_label.place(x=130, y=0)

lscale=['Meters','Inches','Foot','Centimeter']
_from = tk.StringVar()

from_label=tk.Label(tab2, text="Select Unit: ")
from_label.place(x=80, y=60)

from_menu=tk.OptionMenu(tab2,_from, *lscale)
from_menu.place(x= 180,y= 55)

labl=tk.Label(tab2,text="Convert to: ")
labl.place(x= 300,y= 60)

to_=tk.StringVar()
to_menu=tk.OptionMenu(tab2, to_ , *lscale)
to_menu.place(x= 380,y= 55) 

enter=tk.Label(tab2,text="Enter the Length: ")
enter.place(x= 80,y= 105)

#Input box widget to get number
val=tk.Entry(tab2)
val.place(x= 230,y= 105)

def conv():

    frem=_from.get()
    to  = to_.get()
    try:
        
        num_val=val.get()
        num=float(num_val)
        result_text = ""

        #Meter to *
        if frem == 'Meters' and to == 'Inches':
            con_num = num*39.37
        elif frem == 'Meters' and to == 'Foot':
            con_num = num*3.28
        elif frem == 'Meters' and to == 'Centimeter':
            con_num = num*100

        #Inches to *
        elif frem == 'Inches' and to == 'Foot':
            con_num = num*0.08
        elif frem == 'Inches' and to == 'Centimeter':
            con_num = num*2.54
        elif frem == 'Inches' and to == 'Meters':
            con_num = num*0.02

        #Foot to *
        elif frem == 'Foot' and to == 'Inches':
            con_num = num*12
        elif frem == 'Foot' and to == 'Meters':
            con_num = num*30.48
        elif frem == 'Foot' and to == 'Centimeter':
            con_num = num*2.54

        #Centimeter to *
        elif frem == 'Centimeter' and to == 'Meters':
            con_num = num*0.01
        elif frem == 'Centimeter' and to == 'Foot':
            con_num = num*0.03
        elif frem == 'Centimeter' and to == 'Inches':
            con_num = num*0.39

        else:
            con_num = num

    except ValueError:
        result_label.config(text="Enter a valid number")

    result_text = f"{num} {frem} is equal to {con_num:.2f} {to}."
    result_label.config(text=result_text)

result_label = tk.Label(tab2, text="", fg="green")
result_label.place(x=180, y=180)


#Convertion Button
convbut=tk.Button(tab2,text='Convert' ,command=conv)
convbut.place(x = 180,y = 150)

#===========================Create Page 3===========================
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Page 2")

##Background Color
coloor = tk.Canvas(tab3, background="#FFF700")
coloor.pack(fill="both", expand=True)
c_tab3= tk.Label(coloor, text="")




title_label=tk.Label(tab3, text="--This Page helps you in Convertion of Temperature--")
title_label.place(x=130, y=0)

Tscale=['° Celsius','Kelvin','Fahrenheit']


from_label1=tk.Label(tab3, text="Select Unit1: ")
from_label1.place(x=80, y=60)

_tfrom = tk.StringVar()
Tfrom_menu=tk.OptionMenu(tab3,_tfrom, *Tscale)
Tfrom_menu.place(x= 180,y= 55)

Tlabl=tk.Label(tab3,text="Convert to Unit2: ")
Tlabl.place(x= 280,y= 60)

Tto_=tk.StringVar()
Tto_menu=tk.OptionMenu(tab3, Tto_ , *Tscale)
Tto_menu.place(x= 380,y= 55) 

Tenter=tk.Label(tab3,text="Enter the Temperature: ")
Tenter.place(x= 80,y= 105)

#Input box widget to get number
T_val=tk.Entry(tab3)
T_val.place(x= 230,y= 105)

def conv():

    T_frem=_tfrom.get()
    T_to  = Tto_.get()
    try:
        
        num_valu=T_val.get()
        temp_val=float(num_valu)
        resul_text = ""

        #Celsius to *
        if T_frem == '° Celsius' and T_to == 'Kelvin':
            temp = temp_val + 273.15 ##0°C + 273.15 
        elif T_frem == '° Celsius' and T_to == 'Fahrenheit':
            temp = (temp_val* (1.8)) + 32 ##(0°C × 9/5) + 32

        #Kelvin to *
        elif T_frem == 'Kelvin' and T_to == 'Fahrenheit':
            temp = ((temp_val - 273.15) * (1.8) + 32 ) ##(0K − 273.15) × 9/5 + 32 
        elif T_frem == 'Kelvin' and T_to == '° Celsius':
            temp = temp_val - 273.15  ##0K − 273.15 

        #Fahrenheit to *
        elif T_frem == 'Fahrenheit' and T_to == '° Celsius':
            temp = ((temp_val - 32) * (0.56))  ##(0°F − 32) × 5/9
        elif T_frem == 'Fahrenheit' and T_to == 'Kelvin':
            temp = ((temp_val - 32) * (0.56) + 273.15)    ##(0°F − 32) × 5/9 + 273.15

        else:
            temp = temp_val

    except ValueError:
        result_label.config(text="Enter a valid number")

    resul = f"{temp_val} {T_frem} is equal to {temp:.2f} {T_to}."
    resul_label.config(text=resul)

resul_label = tk.Label(tab3, text="", fg="green")
resul_label.place(x=150, y=200)


#Convertion Button
convbut=tk.Button(tab3,text='Convert' ,command=conv)
convbut.place(x = 200,y = 150)

#============================Create Page 4==========================
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Page 3")

##Set Background Color
page_color=tk.Canvas(tab4,background="#FF2700")
page_color.pack(fill="both",expand=True)
tab_color=tk.Label(page_color,text="")

##Page Title
label4 = tk.Label(tab4, text="--This Page helps you in Convertion of Currency--")
label4.place(x=130,y=0)

##List of Currncy
c_list=['₹ INR','$ USD Dollor','¥ Yen','€ Euro','₩ Won']


##First Label for dropbox
f1_label=tk.Label(tab4,text="Select Currency:")
f1_label.place(x=80,y=60)

##First Dropbox,
currenc1=tk.StringVar()
drop_box1=tk.OptionMenu(tab4,currenc1, *c_list)
drop_box1.place(x=180,y=55)

##Second Label for dropbox
f2_label=tk.Label(tab4,text="Convert into:")
f2_label.place(x=280,y=60)

##Second Dropbox,
currenc2=tk.StringVar()
drop_box2=tk.OptionMenu(tab4,currenc2, *c_list)
drop_box2.place(x=180,y=55)

##Label for input box
curr_labl=tk.Label(tab4,text="Enter the Value:")
curr_labl.place(x=80,y=105)

##Input box to get value
cur_val=tk.Entry(tab4)
cur_val.place(x=80,y=105)

def currecy():
    in_curr=currenc1.get()
    out_curr=currenc2.get()
    try:
        inpt1=cur_val.get()
        curny=float(inpt1)
        r_value = ""
        
        ##INR -> *
        if in_curr=='₹ INR' and out_curr=='$ USD Dollor':
            conv_curr = inpt1 * 0.012 ## 1 -> 0.012
        elif in_curr=='₹ INR' and out_curr=='¥ Yen':
            conv_curr = inpt1 * 1.79 ## 1 -> 1.79
        elif in_curr=='₹ INR' and out_curr=='€ Euro':
            conv_curr = inpt1 * 0.011 ## 1 -> 0.011
        elif in_curr=='₹ INR' and out_curr=='₩ Won':
            conv_curr = inpt1 * 16.07 ## 1 -> 16.07           
        
        ##USD Dollor --> *
        elif in_curr=='$ USD Dollor' and out_curr=='₹ INR':
            conv_curr = inpt1 * 83.10 ## 1 -> 83.10           
        elif in_curr=='$ USD Dollor' and out_curr=='¥ Yen':
            conv_curr = inpt1 * 148.28 ## 1 -> 148.28           
        elif in_curr=='$ USD Dollor' and out_curr=='€ Euro':
            conv_curr = inpt1 * 0.94 ## 1 -> 0.94           
        elif in_curr=='$ USD Dollor' and out_curr=='₩ Won':
            conv_curr = inpt1 * 1335.65 ## 1 -> 1335.65         

        ##Yen ---> *
        elif in_curr=='¥ Yen' and out_curr=='₹ INR':
            conv_curr = inpt1 * 0.56 ## 1 -> 0.56           
        elif in_curr=='¥ Yen' and out_curr=='$ USD Dollor':
            conv_curr = inpt1 * 0.0067 ## 1 -> 0.0067           
        elif in_curr=='¥ Yen' and out_curr=='€ Euro':
            conv_curr = inpt1 * 0.0063 ## 1 -> 0.0063           
        elif in_curr=='¥ Yen' and out_curr=='₩ Won':
            conv_curr = inpt1 * 9.01 ## 1 -> 9.01
            
        ##Euro ----> *
        elif in_curr=='€ Euro' and out_curr=='₹ INR':
            conv_curr = inpt1 * 88.69 ## 1 -> 88.69           
        elif in_curr=='€ Euro' and out_curr=='¥ Yen':
            conv_curr = inpt1 * 158.27 ## 1 -> 158.27           
        elif in_curr=='€ Euro' and out_curr=='$ USD Dollor':
            conv_curr = inpt1 * 1.07 ## 1 -> 1.07           
        elif in_curr=='€ Euro' and out_curr=='₩ Won':
            conv_curr = inpt1 * 1,425.48 ## 1 -> 1,425.48
            
        ##Won -----> *
        elif in_curr=='₩ Won' and out_curr=='₹ INR':
            conv_curr = inpt1 * 0.062 ## 1 -> 0.062           
        elif in_curr=='₩ Won' and out_curr=='¥ Yen':
            conv_curr = inpt1 * 0.11 ## 1 -> 0.11           
        elif in_curr=='₩ Won' and out_curr=='€ Euro':
            conv_curr = inpt1 * 0.00070 ## 1 -> 0.00070           
        elif in_curr=='₩ Won' and out_curr=='$ USD Dollor':
            conv_curr = inpt1 * 0.00075 ## 1 -> 0.00075
            
    except ValueError:
        rs_label.config(text="Enter a valid number")

    reslt=f"{inpt1} {in_curr} is equal to {conv_curr:.4f} {out_curr}."
    rs_label.config(text=reslt)
    
rs_label = tk.Label(tab4,text="", fg="green")
rs_label.place(x=180,y=200)


notebook.pack(fill="both", expand=True)
page1()  # Start on Page 1
app.mainloop

##_______________________________________________________________________
##import tkinter as tk
##from tkinter import ttk
##win = tk.Tk()
##def convert():
##    try:
##        meters = float(entry.get())
##        feet = meters * 3.28084
##        result_label.config(text=f"{meters} meters = {feet:.2f} feet")
##    except ValueError:
##        result_label.config(text="Please enter a valid number")
##
### Create the main window
##
##win.geometry('400x350+200+100')
##win.title("Length Converter")
##
### Create and configure widgets
##label = tk.Label(win, text="Select Length")
##
##
### Start the GUI main loop
##win.mainloop()

#_______________________________________________________________________
##import tkinter as tk
##
##def convert_length():
##    try:
##        value = float(entry_value.get())
##        from_unit = from_var.get()
##        to_unit = to_var.get()
##
##        # Define conversion factors
##        conversion_factors = {
##            "Meters to Feet": 3.28084,
##            "Meters to Inches": 39.3701,
##            "Feet to Meters": 0.3048,
##            "Feet to Inches": 12,
##            "Inches to Meters": 0.0254,
##            "Inches to Feet": 0.0833333,
##        }
##
##        result = value * conversion_factors[f"{from_unit} to {to_unit}"]
##        result_label.config(text=f"Result: {result:.2f} {to_unit}")
##    except ValueError:
##        result_label.config(text="Invalid input. Enter a number.")
##
### Create the main window
##window = tk.Tk()
##window.title("Length Converter")
##
### Create input entry
##entry_label = tk.Label(window, text="Enter length:")
##entry_label.pack()
##entry_value = tk.StringVar()
##entry = tk.Entry(window, textvariable=entry_value)
##entry.pack()
##
### Create "From" and "To" unit dropdowns
##from_var = tk.StringVar()
##to_var = tk.StringVar()
##from_unit_label = tk.Label(window, text="From:")
##from_unit_label.pack()
##from_unit_dropdown = tk.OptionMenu(window, from_var, "Meters", "Feet", "Inches")
##from_unit_dropdown.pack()
##to_unit_label = tk.Label(window, text="To:")
##to_unit_label.pack()
##to_unit_dropdown = tk.OptionMenu(window, to_var, "Meters", "Feet", "Inches")
##to_unit_dropdown.pack()
##
### Create conversion button
##convert_button = tk.Button(window, text="Convert", command=convert_length)
##convert_button.pack()
##
### Display the result
##result_label = tk.Label(window, text="")
##result_label.pack()
##
### Start the GUI main loop
##window.mainloop()

#_________________________________________________________________










