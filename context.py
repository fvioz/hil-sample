# -*- coding: utf-8 -*-

from hil import Context

class AppContext(Context):
  def run(self):
    self.attention_level = "feedback"
    self.hands = "steering_wheel"
    self.user_state = "alert"
    self.user_capacity = "driver"
    self.eyes_orientation = "front"
