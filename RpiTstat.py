#!/usr/bin/env python

import Tkinter as tk
import ttk
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


class App():

    def __init__(self,root):
        self.root = root
	
	self.GPIO_heat = 12
	self.GPIO_cool = 20
	self.GPIO_fan = 19
	
	self.setup_gpio()

        ttk.Button(self.root, text="Heat", command=self.onHeat).grid(row=10,column=10,padx=5,pady=5)
        ttk.Button(self.root, text="Cool", command=self.onCool).grid(row=10,column=20,padx=5,pady=5)
        ttk.Button(self.root, text="Fan", command=self.onFan).grid(row=10,column=30,padx=5,pady=5)
        ttk.Button(self.root, text="OFF", command=self.onOff).grid(row=20,column=20,padx=5,pady=5)
	
	#self.root.protocol("WM_DELETE_WINDOW", self.onExit)

    def onHeat(self):
	GPIO.output(self.GPIO_cool,0)
	GPIO.output(self.GPIO_fan,0)
	GPIO.output(self.GPIO_heat,1)
	
    def onCool(self):
	GPIO.output(self.GPIO_fan,0)
	GPIO.output(self.GPIO_heat,0)
	GPIO.output(self.GPIO_cool,1)
	
    def onFan(self):
	GPIO.output(self.GPIO_cool,0)
	GPIO.output(self.GPIO_heat,0)
	GPIO.output(self.GPIO_fan,1)
	
    def onOff(self):
	GPIO.output(self.GPIO_heat,0)
	GPIO.output(self.GPIO_cool,0)
	GPIO.output(self.GPIO_fan,0)
	
    def setup_gpio(self):
	GPIO.setup(self.GPIO_heat,GPIO.OUT)
	GPIO.setup(self.GPIO_cool,GPIO.OUT)
	GPIO.setup(self.GPIO_fan,GPIO.OUT)
	
    def onExit(self):
	self.onOff()
	
	
root = tk.Tk()
root.title("Thermostat")
app = App(root)
root.mainloop()


