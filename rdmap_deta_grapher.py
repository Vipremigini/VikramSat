import matplotlib.pyplot as plt
from deta import Deta
import time as t

deta = Deta('d0zr6g76_H4TfoXGfwwXQpYu2Z1T9QPTTTpyvF9xs')
db = deta.Base('data')

y = []
while True:
  a = db.get('vslive')
  a = a['temp']
  y.append(a)
  plt.plot(y)
  plt.draw()
  plt.pause(0.0001)
  plt.clf()
