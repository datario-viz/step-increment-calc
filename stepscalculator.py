# This code uses the conventional method of calcuting increments slope of a linear function

def calc():
  print("Type the values in order: Final, Initial, Steps: ")
  xf = input()
  print("Now input Initial: ")
  xi = input()
  print("Finally input Steps: ")
  steps = input()
  def increments():
    print((int(xf) - int(xi)) / int(steps))
  print(increments())
  calc()

calc()
