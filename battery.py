class Battery :
  def __init__(self, size=40) :
    self.size = size

  def get_range(self):
    if self.size == 40 :
      print('range is 100')
    elif self.size == 60 :
      print('range is 150 racks')
  
  def upgrade(self) :
    if self.size < 60 :
      self.size = 60
  



