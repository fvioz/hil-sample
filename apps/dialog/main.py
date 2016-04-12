# -*- coding: utf-8 -*-

import sys
import tkinter as tk
import apps.dialog.app
from hil import Component

class Dialog(Component):

  def show():
    # root = tk.Tcl()
    # app = App(master=root)
    # print(dir(app))
    # app.mainloop()
    sys.exit({"Hello": "World"})

