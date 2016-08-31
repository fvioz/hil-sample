# -*- coding: utf-8 -*-

import time
from hil import Component

class Bell(Component):
  def run(self, id):
    print(chr(7))
    return 'None'
