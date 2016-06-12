from hil import Core

from apps.bell.main import Bell
from apps.dialog.main import Dialog

class Main:
  def __init__(self):
    super(Main, self).__init__()
    self.hil = Core()
    self.apps = [Bell, Dialog]

  def run(self):
    for app in self.apps:
      self.hil.addComponent(app)
    self.hil.start()

if __name__ == "__main__":
    main = Main()
    main.run()
