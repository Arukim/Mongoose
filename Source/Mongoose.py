from tkinter import *
import sys
import os
import threading
import time
import socket
import serial
import logging

class SerialManager:
    def __init__(self):
        ser = serial.Serial()




class MainApp:
    # constructor, parent widget is passed to constructor
    def __init__(self, master):
        # container for next 2 widgets
        frame = Frame(master)
        frame.grid()
        # fg = foreground
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.grid(row=0)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.grid(row=0, column=1)
        
        

        self.textBox = Entry(master,text = "Hello")
        self.textBox.grid(row=1,sticky = W)
    def say_hi(self):
        print("Hello world!")
root = Tk()
ser = serial.Serial()
ser.port = "COM9"
ser.baudrate = int(9600)
ser.timeout = 1

try:
    ser.open()
except serial.SerialException as e:
    logging.error("Could not open serial port %s: %s" % (ser.portstr, e))
    sys.exit(1)
logging.info("Serving serial port: %s" % (ser.portstr,))
output = "Hello world!"
ser.write(str.encode("Hello world",'ascii'))
ser.flush()
#ser.write(0(0x3x30)
#ser.write(0x30)
ser.close()
#app = MainApp(root)

#root.mainloop()