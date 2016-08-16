from hil import Core

from context import AppContext
from apps.bell.main import Bell
from apps.dialog.main import Dialog

class Main:
  def __init__(self):
    super(Main, self).__init__()
    self.apps = [Bell, Dialog]
    self.context = AppContext

  def run(self):
    self.core = Core(self.apps, self.context)
    self.core.start()

if __name__ == "__main__":
    main = Main()
    main.run()
