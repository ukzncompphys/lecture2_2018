import numpy as np
from matplotlib import pyplot as plt
def gauss(x,sigma=1.0,x0=0.0,amp=1.0):
    y=amp*np.exp(-((x-x0)**2)/(2*sigma**2))
    return y

print __name__


if __name__=='__main__':

  x=np.arange(-5,5,0.01)
  #y=gauss(x)
  #y=gauss(x,1,0)
  y=gauss(x,amp=2.0,x0=-0.5)

  plt.plot(x,y)
  plt.show()





