# -*- coding: utf-8 -*-

from hil import Core

from context import AppContext
from apps.bell.main import Bell
from apps.dialog.main import Dialog

class Main:
  def __init__(self):
    super(Main, self).__init__()
    self.components = [Bell, Dialog]
    self.context = AppContext

  def run(self):
    self.core = Core(self.components, self.context)
    self.core.start()

if __name__ == "__main__":
    main = Main()
    main.run()
