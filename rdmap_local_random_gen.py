from deta import Deta
import random as r
import time as t

deta = Deta('d0zr6g76_H4TfoXGfwwXQpYu2Z1T9QPTTTpyvF9xs') # configure your Deta project
db = deta.Base('data')  # access your DB
z = 1
x = 37
while z == 1:
    a = r.randint(-100,100.00)
    x = x + a
    y = {'temp':x}
    db.update(y,'vslive')
    t.sleep(0.01)
