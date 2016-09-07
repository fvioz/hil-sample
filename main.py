# -*- coding: utf-8 -*-

from hil import Core

from context import AppContext
from apps.vibration.main import Vibration
from apps.voice.main import Voice
from apps.react.main import React
from apps.sound.main import Sound
from apps.dialog.main import Dialog

class Main:
  def __init__(self):
    super(Main, self).__init__()
    self.components = [Vibration, Voice, React, Sound, Dialog]
    self.context = AppContext

  def run(self):
    self.core = Core(self.components, self.context)
    self.core.start()

if __name__ == "__main__":
    main = Main()
    main.run()
