#oops
class area:
  def __init__(self, radius):
    self.radius = radius

  def fun(self):
    return 3.14 * self.radius * self.radius

odj = area(5)
print(odj.fun())
