# -*- coding: utf-8 -*-

from hil import Context

class AppContext(Context):
  def run(self):
    self.attention_level = 'hight'
    self.m_var1 = '1'
    self.m_var2 = '2'
    self.m_var3 = 3
