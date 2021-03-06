# -*- coding: utf-8 -*-

import tkinter as tk

class App(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.master = master
    self.pack()
    self.createWidgets()

  def createWidgets(self):
    self.hi_there = tk.Button(self)
    self.hi_there["text"] = "Hello World\n(click me)"
    self.hi_there["command"] = self.say_hi
    self.hi_there.pack(side="top")

    self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    self.QUIT.pack(side="bottom")

  def say_hi(self):
    print("hi there, everyone!")
