from hil import Core

from apps.bell.main import Bell
from apps.dialog.main import Dialog

class Main:
  def __init__(self):
    super(Main, self).__init__()
    self.hil = Core()

  def run(self):
    self.hil.addComponent(Bell)
    self.hil.addComponent(Dialog)
    self.hil.start()

if __name__ == "__main__":
    main = Main()
    main.run()
