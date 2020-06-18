# Conversion Calculator # 
from tkinter import *
from tkinter import ttk
import os
#import index

class GUI():

    def __init__(self, master):

        self.master = master
        master.resizable(False, False)
        #master.configure(background="light blue")
        #master.geometry("300x300")
        master.title('Conversion Calculator')

        self.tabControl = ttk.Notebook(master)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab4, text='Calculator')
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Weight')
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='Length')
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='Tempurature')
        self.tab5 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab5, text='Volumn')
        self.tab6 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab6, text='Area')
        self.tabControl.pack(expand=1, fill="both")

        self.intial_wording11 = StringVar(self.tab1) 
        self.intial_wording11.set('Unit')
        self.intial_wording12 = StringVar(self.tab1)
        self.intial_wording12.set('Unit')
        self.entrybox1 = ttk.Entry(self.tab1, width=15)
        self.entrybox1.grid(column=0, row=1)
        self.entrybox1.focus_set()
        self.Iunit1 = StringVar()
        self.input_unit1 = ttk.Combobox(self.tab1, width=15, textvariable=self.Iunit1, state="readonly", values = ['Unit', 'Grams', 'Kilograms', 'Tons', 'Ounces', 'Pounds'])
        self.input_unit1.grid(column=1, row=1)
        self.input_unit1.current(0)
        self.convert_bttn1 = ttk.Button(self.tab1, text='Convert', width=15,command=self.weight)
        self.convert_bttn1.grid(column=0, row=3)
        #self.convert_bttncls1 = ttk.Button(self.tab1, text='Clear',width=15)
        #self.convert_bttncls1.grid(column=1, row=3)
        self.outputbox1 = ttk.Entry(self.tab1, width=15, state="readonly")
        self.outputbox1.grid(column=0, row=4)
        self.Ounit1 = StringVar()
        self.output_unit1 = ttk.Combobox(self.tab1, width=15, textvariable=self.Ounit1, state="readonly", values = ['Unit', 'Grams', 'Kilograms', 'Tons', 'Ounces', 'Pounds'])
        self.output_unit1.grid(column=1, row=4)
        self.output_unit1.current(0)

        self.intial_wording21 = StringVar(self.tab2)
        self.intial_wording21.set('Unit')
        self.intial_wording22 = StringVar(self.tab2)
        self.intial_wording22.set('Unit')
        self.entrybox2 = ttk.Entry(self.tab2, width=15)
        self.entrybox2.grid(column=0, row=1)
        self.entrybox2.focus_set()
        self.Iunit2 = StringVar()
        self.input_unit2 = ttk.Combobox(self.tab2, width=15, textvariable=self.Iunit2, state="readonly", values = ['Unit', 'Millimeters', 'Centimeters', 'Meters', 'Kilometers', 'Miles', 'Feet', 'Inches', 'Yards'])
        self.input_unit2.grid(column=1, row=1)
        self.input_unit2.current(0)
        self.convert_bttn2 = ttk.Button(self.tab2, text='Convert', width=15,command=self.length)
        self.convert_bttn2.grid(column=0, row=3)
        self.outputbox2 = ttk.Entry(self.tab2, width=15, state="readonly")
        self.outputbox2.grid(column=0, row=4)
        self.Ounit2 = StringVar()
        self.output_unit2 = ttk.Combobox(self.tab2, width=15, textvariable=self.Ounit2, state="readonly", values = ['Unit', 'Millimeters', 'Centimeters', 'Meters', 'Kilometers', 'Miles', 'Feet', 'Inches', 'Yards'])
        self.output_unit2.grid(column=1, row=4)
        self.output_unit2.current(0)

        self.intial_wording31 = StringVar(self.tab3) # self.tab 3 Formatting #
        self.intial_wording31.set('Unit')
        self.intial_wording32 = StringVar(self.tab3)
        self.intial_wording32.set('Unit')
        self.entrybox3 = ttk.Entry(self.tab3, width=15)
        self.entrybox3.grid(column=0, row=1)
        self.entrybox1.focus_set()
        self.Iunit3 = StringVar()
        self.input_unit3 = ttk.Combobox(self.tab3, width=15, textvariable=self.Iunit3, state="readonly", values = ['Unit', 'Celcius', 'Farenheit', 'Kelvin']) # self.intial_wording
        self.input_unit3.grid(column=1, row=1)
        self.input_unit3.current(0)
        self.convert_bttn3 = ttk.Button(self.tab3, text='Convert',width=15 ,command=self.tempurature)
        self.convert_bttn3.grid(column=0, row=3)
        self.outputbox3 = ttk.Entry(self.tab3, width=15, state="readonly")
        self.outputbox3.grid(column=0, row=4)
        self.Ounit3 = StringVar()
        self.output_unit3 = ttk.Combobox(self.tab3, width=15, textvariable=self.Ounit3, state="readonly", values = ['Unit', 'Celcius', 'Farenheit', 'Kelvin'])#self.intial_wording2, 
        self.output_unit3.grid(column=1, row=4)
        self.output_unit3.current(0)

        self.intial_wording51 = StringVar(self.tab5)
        self.intial_wording51.set('Unit')
        self.intial_wording52 = StringVar(self.tab5)
        self.intial_wording52.set('Unit')
        self.entrybox5 = ttk.Entry(self.tab5, width=15)
        self.entrybox5.grid(column=0, row=1)
        self.entrybox5.focus_set()
        self.Iunit5 = StringVar()
        self.input_unit5 = ttk.Combobox(self.tab5, width=15, textvariable=self.Iunit5, state="readonly", values = ['Unit', 'Liter', 'cubic millimeters', 'hectoliter', 'cubic meter', 'dectliter', 'centliter', 'milliliter'])
        self.input_unit5.grid(column=1, row=1)
        self.input_unit5.current(0)
        self.convert_bttn5 = ttk.Button(self.tab5, text='Convert', width=15,command=self.volumn)
        self.convert_bttn5.grid(column=0, row=3)
        self.outputbox5 = ttk.Entry(self.tab5, width=15, state="readonly")
        self.outputbox5.grid(column=0, row=4)
        self.Ounit5 = StringVar()
        self.output_unit5 = ttk.Combobox(self.tab5, width=15, textvariable=self.Ounit5, state="readonly", values = ['Unit', 'Liter', 'cubic millimeters', 'hectoliter', 'cubic meter', 'dectliter', 'centliter', 'milliliter'])
        self.output_unit5.grid(column=1, row=4)
        self.output_unit5.current(0)

        self.intial_wording61 = StringVar(self.tab6)
        self.intial_wording61.set('Unit')
        self.intial_wording62 = StringVar(self.tab6)
        self.intial_wording62.set('Unit')
        self.entrybox6 = ttk.Entry(self.tab6, width=15)
        self.entrybox6.grid(column=0, row=1)
        self.entrybox6.focus_set()
        self.Iunit6 = StringVar()
        self.input_unit6 = ttk.Combobox(self.tab6, width=15, textvariable=self.Iunit6, state="readonly", values = ['Unit','square meter','square decimeter','square cenimeter','square kilometer','are','hectare' ])
        self.input_unit6.grid(column=1, row=1)
        self.input_unit6.current(0)
        self.convert_bttn6 = ttk.Button(self.tab6, text='Convert', width=15,command=self.area)
        self.convert_bttn6.grid(column=0, row=3)
        self.outputbox6 = ttk.Entry(self.tab6, width=15, state="readonly")
        self.outputbox6.grid(column=0, row=4)
        self.Ounit6 = StringVar()
        self.output_unit6 = ttk.Combobox(self.tab6, width=15, textvariable=self.Ounit6, state="readonly", values = ['Unit','square meter','square decimeter','square cenimeter','square kilometer','are','hectare'])
        self.output_unit6.grid(column=1, row=4)
        self.output_unit6.current(0)

        #self.labe11=Label(self.tab4,text="Enter your equation")
        #self.Label1.grid(row=0, columnspan=8)
        #self.equa = ""
        #self.equation = StringVar()
        #self.calculation = Label(self.tab4, textvariable = self.equation)
        #self.equation.set("Enter your expression : ")
        #self.calculation.grid(row=2, columnspan=8)

        self.e = Entry(self.tab4) 
        self.e.grid(row=0,column=0,columnspan=6,pady=3) 
        self.e.focus_set() 
  

        self.Button0 = Button(self.tab4, text="0", command = lambda:self.btnPress(0), width=7, relief=SOLID)
        self.Button0.grid(row = 6, column = 2, padx=10, pady=10)
        self.Button1 = Button(self.tab4, text="1", command = lambda:self.btnPress(1), width=7, relief=SOLID)
        self.Button1.grid(row = 3, column = 1, padx=10, pady=10)
        self.Button2 = Button(self.tab4, text="2", command = lambda:self.btnPress(2), width=7, relief=SOLID)
        self.Button2.grid(row = 3, column = 2, padx=10, pady=10)
        self.Button3 = Button(self.tab4, text="3", command = lambda:self.btnPress(3), width=7, relief=SOLID)
        self.Button3.grid(row = 3, column = 3, padx=10, pady=10)
        self.Button4 = Button(self.tab4, text="4", command = lambda:self.btnPress(4), width=7, relief=SOLID)
        self.Button4.grid(row = 4, column = 1, padx=10, pady=10)
        self.Button5 = Button(self.tab4, text="5", command = lambda:self.btnPress(5), width=7, relief=SOLID)
        self.Button5.grid(row = 4, column = 2, padx=10, pady=10)
        self.Button6 = Button(self.tab4, text="6", command = lambda:self.btnPress(6), width=7, relief=SOLID)
        self.Button6.grid(row = 4, column = 3, padx=10, pady=10)
        self.Button7 = Button(self.tab4, text="7", command = lambda:self.btnPress(7), width=7, relief=SOLID)
        self.Button7.grid(row = 5, column = 1, padx=10, pady=10)
        self.Button8 = Button(self.tab4, text="8", command = lambda:self.btnPress(8), width=7, relief=SOLID)
        self.Button8.grid(row = 5, column = 2, padx=10, pady=10)
        self.Button9 = Button(self.tab4, text="9", command = lambda:self.btnPress(9), width=7, relief=SOLID)
        self.Button9.grid(row = 5, column = 3, padx=10, pady=10)
        self.Plus = Button(self.tab4, text="+", command = lambda:self.btnPress("+"), width=7, relief=SOLID)
        self.Plus.grid(row = 3, column = 4, padx=10, pady=10)
        self.Minus = Button(self.tab4, text="-", command = lambda:self.btnPress("-"), width=7, relief=SOLID)
        self.Minus.grid(row = 4, column = 4, padx=10, pady=10)
        self.Multiply = Button(self.tab4, text="*", command = lambda:self.btnPress("*"), width=7, relief=SOLID)
        self.Multiply.grid(row = 5, column = 4, padx=10, pady=10)
        self.Divide = Button(self.tab4, text="/", command = lambda:self.btnPress("/"), width=7, relief=SOLID)
        self.Divide.grid(row = 6, column = 4, padx=10, pady=10)
        self.Equal = Button(self.tab4, text="=", command = self.EqualPress, width=7, relief=SOLID)
        self.Equal.grid(row=6, column=3, padx=10, pady=10)
        self.Clear = Button(self.tab4, text="C", command = self.ClearPress, width=7, relief=SOLID)
        self.Clear.grid(row = 6, column = 1, padx=10, pady=10)


        self.master.bind('<Return>', self.keybind)

class Logic(GUI):

    def keybind (self, event):
        self.convert_bttn1.invoke()
        self.convert_bttn2.invoke()
        self.convert_bttn3.invoke()
        self.convert_bttn5.invoke()
        self.convert_bttn6.invoke()
        self.Equal.invoke()
        self.Claer.invoke()


    def weight(self):
        Weight_Conversion_Values = {'Grams': 1,
                                    'Kilograms': 1000,
                                    'Tons': 1000000, 
                                    'Ounces': 28.3495,
                                    'Pounds': 453.592}
        self.outputbox1.delete(0, END)
        if self.Iunit1.get() != '':
            if self.Ounit1.get() != '':
                try:
                    self.outputbox1.config(state='NORMAL')
                    self.outputbox1.delete(0, 'end') 
                    self.outputbox1.config(state='readonly')
                    text = float(self.entrybox1.get())
                    newtext = text*(Weight_Conversion_Values[self.Iunit1.get()])*(int(1)/(Weight_Conversion_Values[self.Ounit1.get()]))
                    self.outputbox1.config(state='NORMAL')
                    self.outputbox1.insert(0, newtext)
                    self.outputbox1.config(state='readonly')
                except ValueError:
                    error_message = 'non-int error'
                    self.outputbox1.config(state='NORMAL')
                    self.outputbox1.insert(0, error_message)
                    self.outputbox1.config(state='readonly')

    def length(self):
        Length_Conversion_Values = {'Meters': 1,
                                    'Kilometers': 1000,
                                    'Centimeters': 0.01,
                                    'Millimeters': 0.001,
                                    'Miles': 1609.344498,
                                    'Feet': 0.304799999,
                                    'Inches': 0.02539998,
                                    'Yards': 0.9144027578}
        self.outputbox2.delete(0, END)
        if self.Iunit2.get() != '':
            if self.Ounit2.get() != '':
                try:
                    self.outputbox2.config(state='NORMAL')
                    self.outputbox2.delete(0, 'end') 
                    self.outputbox2.config(state='readonly')
                    text = float(self.entrybox2.get())
                    newtext = text*(Length_Conversion_Values[self.Iunit2.get()])*(int(1)/(Length_Conversion_Values[self.Ounit2.get()]))
                    self.outputbox2.config(state='NORMAL')
                    self.outputbox2.insert(0, newtext)
                    self.outputbox2.config(state='readonly')
                except ValueError:
                    error_message = 'non-int error'
                    self.outputbox2.config(state='NORMAL')
                    self.outputbox2.insert(0, error_message)
                    self.outputbox2.config(state='readonly')

    def volumn(self):

        volumn_Conversion_Values = {'Liter': 1,
                                    'cubic millimeters': 0.000001,
                                    'hectoliter': 100,
                                    'cubic meter': 1000,
                                    'dectliter': 0.1,
                                    'centliter': 0.01,
                                    'milliliter': 0.001}
        
        self.outputbox5.delete(0, END)
        if self.Iunit5.get() != '':
            if self.Ounit5.get() != '':
                try:
                    self.outputbox5.config(state='NORMAL')
                    self.outputbox5.delete(0, 'end') 
                    self.outputbox5.config(state='readonly')
                    text = float(self.entrybox5.get())
                    newtext = text*(volumn_Conversion_Values[self.Iunit5.get()])*(int(1)/(volumn_Conversion_Values[self.Ounit5.get()]))
                    self.outputbox5.config(state='NORMAL')
                    self.outputbox5.insert(0, newtext)
                    self.outputbox5.config(state='readonly')
                except ValueError:
                    error_message = 'non-int error'
                    self.outputbox5.config(state='NORMAL')
                    self.outputbox5.insert(0, error_message)
                    self.outputbox5.config(state='readonly')

    def area(self):

        area_Conversion_Values = {'square meter': 1,
                                  'square decimeter': 0.01,
                                  'square cenimeter': 0.0001,
                                  'square kilometer': 1000000,
                                  'are': 100,
                                  'hectare': 10000}
        
        self.outputbox6.delete(0, END)
        if self.Iunit6.get() != '':
            if self.Ounit6.get() != '':
                try:
                    self.outputbox6.config(state='NORMAL')
                    self.outputbox6.delete(0, 'end') 
                    self.outputbox6.config(state='readonly')
                    text = float(self.entrybox6.get())
                    newtext = text*(area_Conversion_Values[self.Iunit6.get()])*(int(1)/(area_Conversion_Values[self.Ounit6.get()]))
                    self.outputbox6.config(state='NORMAL')
                    self.outputbox6.insert(0, newtext)
                    self.outputbox6.config(state='readonly')
                except ValueError:
                    error_message = 'non-int error'
                    self.outputbox6.config(state='NORMAL')
                    self.outputbox6.insert(0, error_message)
                    self.outputbox6.config(state='readonly')

    
    def tempurature(self):
        self.outputbox3.delete(0, END)
        if self.Iunit3.get() == 'Celcius':
            self.outputbox3.config(state='NORMAL')
            self.outputbox3.delete(0, 'end') 
            self.outputbox3.config(state='readonly')
            try:
                if self.Ounit3.get() == 'Kelvin':
                    if float(self.entrybox3.get()) >= -273.15:
                        text = float(self.entrybox3.get())
                        newtext = text + 273.15
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, newtext)
                        self.outputbox3.config(state='readonly')
                    else:
                        error_message = 'X ≥ -273.15'
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, error_message)
                        self.outputbox3.config(state='readonly')
                if self.Ounit3.get() == 'Farenheit':
                    if float(self.entrybox3.get()) >= -273.15:
                        text = float(self.entrybox3.get())
                        newtext = text*9/5 + 32
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, newtext)
                        self.outputbox3.config(state='readonly')
                    else:
                        error_message = 'X ≥ -273.15'
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, error_message)
                        self.outputbox3.config(state='readonly')
            except ValueError:
                    error_message = 'non-int error'
                    self.outputbox3.config(state='NORMAL')
                    self.outputbox3.insert(0, error_message)
                    self.outputbox3.config(state='readonly')
        if self.Iunit3.get() == 'Farenheit':
            self.outputbox3.config(state='NORMAL')
            self.outputbox3.delete(0, 'end') 
            self.outputbox3.config(state='readonly')
            try:
                if self.Ounit3.get() == 'Kelvin':
                    if float(self.entrybox3.get()) >= -459.67:
                        text = float(self.entrybox3.get())
                        newtext = (text+459.67)*5/9
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, newtext)
                        self.outputbox3.config(state='readonly')
                    else:
                        error_message = 'X ≥ -459.67'
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, error_message)
                        self.outputbox3.config(state='readonly')
                if self.Ounit3.get() == 'Celcius':
                    if float(self.entrybox3.get()) >= -459.67:
                        text = float(self.entrybox3.get())
                        newtext = (text-32)*5/9
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, newtext)
                        self.outputbox3.config(state='readonly')
                    else:
                        error_message = 'X ≥ -459.67'
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, error_message)
                        self.outputbox3.config(state='readonly')
            except ValueError:
                    error_message = 'non-int error'
                    self.outputbox3.config(state='NORMAL')
                    self.outputbox3.insert(0, error_message)
                    self.outputbox3.config(state='readonly')
        if self.Iunit3.get() == 'Kelvin':
            self.outputbox3.config(state='NORMAL')
            self.outputbox3.delete(0, 'end') 
            self.outputbox3.config(state='readonly')
            try:
                if self.Ounit3.get() == 'Celcius':
                    if float(self.entrybox3.get()) >= 0:
                        text = float(self.entrybox3.get())
                        newtext = text - 273.15
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, newtext)
                        self.outputbox3.config(state='readonly')
                    else:
                        error_message = 'X ≥ 0'
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, error_message)
                        self.outputbox3.config(state='readonly')
                if self.Ounit3.get() == 'Farenheit':
                    if float(self.entrybox3.get()) >= 0:
                        text = float(self.entrybox3.get())
                        newtext = text*9/5 - 459.67
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, newtext)
                        self.outputbox3.config(state='readonly')
                    else:
                        error_message = 'X ≥ 0'
                        self.outputbox3.config(state='NORMAL')
                        self.outputbox3.insert(0, error_message)
                        self.outputbox3.config(state='readonly')
            except ValueError:
                    error_message = 'non-int error'
                    self.outputbox3.config(state='NORMAL')
                    self.outputbox3.insert(0, error_message)
                    self.outputbox3.config(state='readonly')

    def getandreplace(self): 
  
        """replace x with * and ÷ with /"""
        self.expression = self.e.get() 
        self.newtext=self.expression.replace('/','/') 
        self.newtext=self.newtext.replace('x','*') 
  
    def btnPress(self,num):
        self.e.insert(END,num)
  
    def EqualPress(self):
        self.getandreplace() 
        try: 
            self.value= eval(self.newtext)  
        except (SyntaxError or NameError): 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.e.delete(0,END) 
            self.e.insert(0,self.value) 

        
     
    def ClearPress(self):
        self.e.delete(0,END)


def main():
    root = Tk()
    test = Logic(root)
    #root.title("Conversion")
    width=640
    height=480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.configure(background='light blue')
    #root.geometry("%dx%d+%d+%d" % (400, 350, x, y))
    #root.resizable(0, 0)
    root.resizable(False,False)
    root.mainloop()
main()