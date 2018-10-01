#Author: Yasir Aslam Shah
#Project 1
#EID Ecen 5013
#Fall 2018

import sys
import Adafruit_DHT
import datetime
import calendar
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.uic import loadUi
from PySide.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
#declaring global variables
flag=[]
listA=[]
listB=[]
count1=[]
count2=[]
array_average1=[]
array_average2=[]
global average1
#function to call calender  
cal1=calendar.month(2018,10)
today=datetime.date.today()
date=format(today)
#to initailise graph
class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig=Figure(figsize=(width, height),dpi=dpi)
        self.axes =fig.add_subplot(111)
        self.axes.clear()
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
#to initialise graph to display the average of temperature
class MyDynamicMplCanvas(MyMplCanvas):
    def __init__(self,*args,**kwargs):
        MyMplCanvas.__init__(self,*args,**kwargs)
        timer=QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(10000)   #a timer of 10 sec is set to display the values on graph
    def update_figure(self):
        self.axes.clear()
        self.axes.plot([0,1,2,3],array_average1[-4:],'r')
        self.draw()
#to initailise graph2 to display the average of humidity values        
class MyDynamicMplCanvas1(MyMplCanvas):
    def __init__(self,*args,**kwargs):
        MyMplCanvas.__init__(self,*args,**kwargs)
        timer1=QtCore.QTimer(self)
        timer1.timeout.connect(self.update_figure)
        timer1.start(10000)#the timer of 10 sec is set to display the values on graph
    def update_figure(self):
        self.axes.clear()
        self.axes.plot([0,1,2,3],array_average2[-4:],'r')
        self.draw()
        
class project(QDialog):
    def __init__(self):
        super(project,self).__init__()
        loadUi ('projectl.ui',self)
        self.setWindowTitle('ProjectOne')
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)
        self.average_hum()
        self.average_temp()
        self.main_widget = QWidget(self)
        self.main_widget1 = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        self.main_widget.setGeometry(QtCore.QRect(50,450,200,150))
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(dc)
        t = QVBoxLayout(self.main_widget1)
        self.main_widget1.setGeometry(QtCore.QRect(250,450,200,150))
        sc = MyDynamicMplCanvas1(self.main_widget1, width=5, height=4, dpi=100)
        t.addWidget(sc)
    @pyqtSlot()
    #date1=format(today)
    #self.label_Time.setText(str(date))
    #function to derive the average of humidity and display the average after every two seconds.
    #the values are automatically displayed on the graphic userinterface
    #the average values is stored in a global varaible and is also dislayed on graph
    def average_hum(self):   
        try:
            self.label_Time.setText(str(date))
            self.label_2.setText(cal1)
            #print(cal1)
            global average1
            #global array_average1[]
            humidity,temperature = Adafruit_DHT.read_retry(22,4)
            if humidity == None:#if the sensor is not connected the console prints an error message
                self.label_Hum1.setText("Not Connected")
            else:    
                #print('Humidity ={0:0.1f}%'.format(humidity))
                hum=humidity
                listA.append(hum)                
            sum1=sum(listA)
            #print(sum1)
            #print('Timestamp : {:%H:%M:%S}'.format(datetime.datetime.now()))
            #print('Date :{:%Y-%m-%d}'.format(datetime.datetime.now()))
            length1=len(listA)
            average1=(sum1/length1)
            array_average1.append(average1)
            #print('Hum_average is')
            #print(array_average1)
            self.label_AveA1.setText(str(average1))
            a=1
            count1.append(a)
            counter1=sum(count1)
            #print('count is ')
            #print( counter1)
            if counter1 == 10:
                listA.clear()
                #print('yaha')
                count1.clear()
        finally:
            QtCore.QTimer.singleShot(2000,self.average_hum)#the average function for humidity is called after every 2 sec 
    #function to calculate the average temperture values automatically after every 2.5 seconds
    #the avergae function is used also to feed the graph to display the values every 10 seconds
    def average_temp(self):
        try:
            global average2
            humidity,temperature = Adafruit_DHT.read_retry(22,4)
            #print('yasir')
            if temperature == None:#if the sensor is not connected, an error message is displayed on UI
                self.label_temp1.setText("Not Connected")
            else:
                #print('Temperature ={0:0.f}*'.format(temperature))
                temp=temperature
                listB.append(temp)
            sum2=sum(listB)
            #print(sum2)
            length2=len(listB)
            average2=(sum2/length2)
            array_average2.append(average2)
            #print('Temp_average')
            #print(average2)
            self.label_AveB1.setText(str(average2))
            b=1
            count2.append(b)
            counter2=sum(count2)
            #print(counter2)
            #after ten entries the array is cleared
            if counter2 == 10:
                listB.clear()
                #print('waha')
                count2.clear()
        finally:
            #this function is called to display average temperature every 2.5 seconds
            QtCore.QTimer.singleShot(2500,self.average_temp)
    #function defined at clicking pushbutton1(Refresh) to display current temperature
    #in celsuis, farenheut and kelvin.The curent temp is displayed with a timestamp
    def on_pushButton1_clicked(self):
        timer_temp=(datetime.datetime.now().strftime('%H:%M:%S'))
        self.label_Time2.setText(str(timer_temp))
        humidity,temperature = Adafruit_DHT.read_retry(22,4)
        farenhiet=((temperature *9)/5 + 32) #for temperature conversion to farenhiet
        kelvin = temperature+273 #for temperature conversion to kelvin
        if temperature == None:#if sensor is not connected, an error message is displayed
            self.label_temp1.setText("Not Connected")
        else:
            if flag == 2:#to display values in farenheit
                self.label_Temp1.setText(str(farenhiet))
                print("farenhiet")
            elif flag ==3:#to display values in kelvin
                self.label_Temp1.setText(str(kelvin))
                print('kelvin')
            elif flag ==1:    #to display temperature in celsius
                self.label_Temp1.setText(str(temperature))
                print('temperature')
            print('Temp ={0:0.1f}*'.format(temperature))
            self.label_Temp1.setText(str(temperature))
            temp=temperature
            listB.append(temp)
    #function defined at pushbutton clicked(Refresh) to display the current humidity.The humidity 
    #is displayed with current timestamp
    def on_pushButton2_clicked(self):
        #displaying time stamp
        timer_hum =(datetime.datetime.now().strftime('%H:%M:%S'))
        self.label_Time1.setText(str(timer_hum))
        humidity,temperature = Adafruit_DHT.read_retry(22,4)
        if humidity == None:
            #if the humidty sensor is not connected an error is displayed as not connected
            self.label_Hum1.setText("Not Connected")
        else:    
            self.label_Hum1.setText(str(humidity))
            #print('Humidity ={0:0.1f}%'.format(humidity))
            hum=humidity
            listA.append(hum)
            comp1=self.lineEdit.text())
            if comp1 == None:
                self.label_AlertA.setText('Set Threshold')
            else:    
                if comp1 >humidity:
                    self.label_AlertA.setText('Alert!')
                else:
                    self.label_Alert.setText('Normal!')
    #pushbutton 3 is used to display the current temperature in farenheit        
    def on_pushButton3_clicked(self):
        humidity,temperature = Adafruit_DHT.read_retry(22,4)
        if temperature == None:
            self.label_temp1.setText("Not Connected")
        else:
            farenhiet=((temperature *9)/5 + 32)
            self.label_Temp1.setText(str(farenhiet))
    #pushbutton 4 is used to display the current temperature in kelvin     
    def on_pushButton4_clicked(self):
        humidity,temperature = Adafruit_DHT.read_retry(22,4)
        if temperature == None:
            self.label_temp1.setText("Not Connected")
        else:
            kelvin=temperature+273 
            self.label_Temp1.setText(str(kelvin))
    #pushbutton 5 is clicked to display temperature in celsius     
    def on_pushButton5_clicked(self):
        humidity,temperature = Adafruit_DHT.read_retry(22,4)
        if temperature == None:
            self.label_temp1.setText("Not Connected")
        else:
            self.label_Temp1.setText(str(temperature)) 


app=QApplication(sys.argv)
widget=project()
widget.show()
sys.exit(app.exec_())



