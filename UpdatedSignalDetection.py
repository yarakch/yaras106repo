import numpy
from scipy.special import ndtri

class SignalDetection:
  def __init__(self,hit,miss,fa,cr):
    """Initializes the class object using the self, hit, miss, false alarm, and correct rejection variables."""
    self.__hit = hit
    self.__miss = miss
    self.__fa = fa
    self.__cr = cr

  def __str__(self):
    """Returns the class as a labeled list to enable printing and error detection."""
    return f"hits: {self.__hit}, misses: {self.__miss}, false alarms: {self.__fa}, correct rejections: {self.__cr}" 

  def hitRate(self): 
    """Calculates the hit rate given the hits and misses."""
    self.__hr = (self.__hit / (self.__hit + self.__miss))
    return self.__hr

  def falseAlarmRate(self):
    """Calculates the false alarm rate given the hits and misses."""
    self.__far = (self.__fa / (self.__fa + self.__cr))
    return self.__far

  def d_prime(self):
    """Calculates the d-Prime value given the hit rate and false alarm rate."""
    self.__dprime = (ndtri(self.hitRate()) - ndtri(self.falseAlarmRate()))
    return self.__dprime
  
  def criterion(self):
    """Calculates the Criterion value given the hit rate and false alarm rate."""
    self.__criterion = (-0.5 * (ndtri(self.hitRate()) + ndtri(self.falseAlarmRate())))
    return self.__criterion

  def __add__(self, other):
    """Overloads the addition operator to add two class objects to one another."""
    return SignalDetection(self.__hit + other.__hit, self.__miss + other.__miss, self.__fa + other.__fa, self.__cr + other.__cr)

  def __mul__(self, scalar):
    """Overloads the multiplication operator to multiply a class object by a scalar."""
    return SignalDetection(self.__hit * scalar, self.__miss * scalar, self.__fa * scalar, self.__cr * scalar) 

  def plot_roc(*objects): # * specifies unknown number of objects
    """Generates a receiver operating curve for several class objects given the hit rate and false alarm rate."""
    x_y = {0:0}
    for classObj in objects: # looping through arguments given to function to append all datapoints to appropriate lists
      classObj.hitRate()
      classObj.falseAlarmRate()
      newY = classObj.__hr
      newX = classObj.__far
      x_y[newX] = newY
    x_y[1] = 1
    dict_items = x_y.items()
    sorted_dict = sorted(dict_items)
    x_vals = []
    y_vals = []
    for x,y in sorted_dict: 
      x_vals.append(x)
      y_vals.append(y)
    plt.plot(x_vals, y_vals) # generating plot points
    plt.ylabel("Hit Rate") # labeling axes
    plt.xlabel("False Alarm Rate")
    plt.title("Receiver Operating Curve") # plot title
    plt.show() # generating visual
    return

def plot_sdt(self):
    """Generates a signal detection plot."""
    range = numpy.arange(-5, 5, 0.01)
    signal = norm.pdf(range, 0, 1)
    noise = norm.pdf(range, (self.d_prime()), 1)

    peakX = [0, self.d_prime()]
    peakY = [(max(signal)), max(noise)] 

    plt.plot(range, signal, label="Signal", color='g')
    plt.plot(range, noise, label="Noise", color='r')
    plt.axvline(x=(self.criterion()), label="Criterion", color='c')
    plt.plot(peakX,peakY,label='Distance\nBtwn Peaks', color='b')
    plt.title("Signal Detection Theory (SDT) Plot")
    plt.legend(loc='upper right')
    plt.show()
    return
