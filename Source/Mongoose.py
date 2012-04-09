from tkinter import *
from serial.tools.list_ports import comports
import sys
import os
import threading
import time
import socket
import serial
import logging
import serial

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

        self.openCom = Button(frame, text="Connect", command=self.openCom)
        self.openCom.grid(row=0, column=1)
        
        

        self.textBox = Entry(master,text = "Hello")
        self.textBox.grid(row=1,sticky = W)

        self.comList = Listbox(master)
        self.comList.grid(row = 0, column=2)
        self.comList.insert(END, "COM9")

        portList = comports()
        for com,desc,hwid in portList:
            print("Found COM port:",com, "\n")
            self.comList.insert(0, com)  
        
    def openCom(self):
        if(self.openCom.cget("text") == "Connect"):
            curSelect = self.comList.curselection()
            try:
                item = self.comList.get(curSelect)
            except ValueErroe: pass
        
            self.ser.port = item
            self.ser.baudrate = int(9600)
            self.ser.timeout = 1

            try:
                self.ser.open()
            except serial.SerialException as e:
                logging.error("Could not open serial port %s: %s" % (self.ser.portstr, e))
                sys.exit(1)
            logging.info("Serving serial port: %s" % (self.ser.portstr,))                        
            self.ser.write(str.encode("Connected to " + self.ser.port + "\r\n",'ascii'))
            self.openCom.config(text = "Disconnect")
        else:
            self.ser.close()
            self.openCom.config(text = "Connect")
    def quit(self):
        self.frame.quit()


root = Tk()
app = MainApp(root)
root.mainloop()