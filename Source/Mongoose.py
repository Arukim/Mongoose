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

if sys.version_info >= (3, 0):
    def character(b):
        return b.decode('latin1')
else:
    def character(b):
        return b

class MainApp:
    ser = serial.Serial()
    # constructor, parent widget is passed to constructor
    def __init__(self, master):
        master.wm_title("Mongoose")
        # container for next 2 widgets
        frame = Frame(master)
        frame.grid()
        self.frame = frame
        # fg = foreground
        self.button = Button(frame, text="QUIT", fg="red", command=self.quit)
        self.button.grid(row=0)

        self.openCom = Button(frame, text="Connect", command=self.openCom)
        self.openCom.grid(row=0, column=1)
        
        self.output = Text(frame)
        self.output.grid(row = 2)
        
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
            except ValueError: pass
        
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
            self._start_reader()
            self.openCom.config(text = "Disconnect")
        else:
            self.ser.close()
            self.openCom.config(text = "Connect")
    def quit(self):
        self.frame.quit()

    def _start_reader(self):
        self._reader_alive = True
        # start serial->console thread
        self.receiver_thread = threading.Thread(target=self.reader)
        self.receiver_thread.setDaemon(True)
        self.receiver_thread.start()

    def _stop_reader(self):
        self._reader_alive = False
        self.receiver_thread.join()

    def reader(self):
        try:
            while self._reader_alive:
                data = character(self.ser.read(1))
                self.output.insert(INSERT,data)
        except serial.SerialException as e:
            self.alive = False
            # would be nice if the console reader could be interruptted at this
            # point...
            raise



root = Tk()
app = MainApp(root)
root.mainloop()