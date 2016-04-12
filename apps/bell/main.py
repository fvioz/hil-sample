# -*- coding: utf-8 -*-

import sys
from hil import Component

class Bell(Component):

  def play():
    print(chr(7))
    sys.exit("{}")
