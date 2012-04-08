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
    ser = serial.Serial()
    # constructor, parent widget is passed to constructor
    def __init__(self, master):
        # container for next 2 widgets
        frame = Frame(master)
        frame.grid()
        self.frame = frame
        # fg = foreground
        self.button = Button(frame, text="QUIT", fg="red", command=self.quit)
        self.button.grid(row=0)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.grid(row=0, column=1)
        
        

        self.textBox = Entry(master,text = "Hello")
        self.textBox.grid(row=1,sticky = W)

        
        self.ser.port = "COM9"
        self.ser.baudrate = int(9600)
        self.ser.timeout = 1

        try:
            self.ser.open()
        except serial.SerialException as e:
            logging.error("Could not open serial port %s: %s" % (self.ser.portstr, e))
            sys.exit(1)
        logging.info("Serving serial port: %s" % (self.ser.portstr,))
        
        #ser.close()

    def say_hi(self):
        self.ser.write(str.encode("Hello world\r\n",'ascii'))
    def quit(self):
        self.frame.quit()


root = Tk()
app = MainApp(root)
root.mainloop()