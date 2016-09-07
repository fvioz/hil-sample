# -*- coding: utf-8 -*-

import time
from hil import Component

class React(Component):
  def run(self, id, participation, role):
    print(chr(7))
    return 'React'
