Author:Yasir Aslam Shah
Project 1
EID
Fall 2018

This project is written in Python 3 for interfacing Humidity and Temperature sensor DHT22 with a graphical User Interface that displays data on the GUI.The GUI is constructed using PyQt5 and is designed using QT designer.The GUI contains various pushbuttons and to refresh the system and display current temperature and humidity.The average temperature and humidity is also displayed in the GUI that refreshed automatically after every 2 seconds.The average data for both the Humdity and Temperature values are stored and displayed in a graph.Two different graphs display the average values for humidity and Temperature seperately.

Basic Requirements:
1.Current Temperature/Humidity on pressing 'Refresh' Button
2.The error message 'NOT CONNECTED' displayed when the sensor is not connected
  
Extra Credits:
1.The average values for both humidity and temperature is displayed on GUI and is updated every two seconds
2.The temperature units are interchangable using Pushbuttons for Celsius,Farenhiet and Kelvin
3.The average temperature and humidty values are displayed over two seperate graphs and refreshed every 10 seconds
4.Calender and current date is displayed on the graphical console
5.Alert system to tell user if the humidity and temperature exceeds the input theshold value

The GUI file and the python code is saved in the same file and can be run using command line as :Python3 pro.py
The GUI can be closed and exited using close button at the top right of top bar

Refrence links:
1.https://www.youtube.com/watch?v=7SrD4l2o [for QT]
2.https://gist.github.com/pklaus/3e16982d952969eb8a9a [for Graph Plotting]
3.https://circuitpython.readthedocs.io/projects/dht/en/latest/ [sensor DHT22]
4.https://github.com/adafruit/circuitpython [Sensor DHT22]

