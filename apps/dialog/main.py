# -*- coding: utf-8 -*-

import sys
import tkinter as tk
from hil import Component
from apps.dialog.app import App

class Dialog(Component):
  def show():
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
    return {"Hello": "World"}
