from hil import Context

class AppContext(Context):
  def run(self):
    self.setValue('m_var1', '1')
    self.setValue('m_var2', '2')
    self.setValue('m_var3', '3')
