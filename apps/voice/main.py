# -*- coding: utf-8 -*-

import time
from hil import Component

class Voice(Component):
  def run(self, id, participation, role):
    print(chr(7))
    return 'Voice'
