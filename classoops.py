class parent:
  def function(self):
    print("i am good")

class child(parent):
  def __init__(self):
    print("i am bad") 
obj = parent()
pen = child()

pen.function()
