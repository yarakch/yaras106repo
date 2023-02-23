import numpy
from scipy.special import ndtri

class SignalDetection:
  def __init__(self,hit,miss,fa,cr):
    # Define variables
    self.__hit = hit
    self.__miss = miss
    self.__fa = fa
    self.__cr = cr

  def __str__(self):
    "Returns the class as a labeled list to enable printing and error detection."
    return f"hits: {self.__hit}, misses: {self.__miss}, false alarms: {self.__fa}, correct rejections: {self.__cr}" 

    #self.hr = (hit / (hit + miss))
    #self.far = (fa / (fa + cr))
  def hitRate(self): # should this be private? ask Weds
    self.__hr = (self.__hit / (self.__hit + self.__miss))
    return self.__hr

  def falseAlarmRate(self): # should this be private? ask Weds
    self.__far = (self.__fa / (self.__fa + self.__cr))
    return self.__far

  def d_prime(self):
    # Calculates the d-Prime value
    self.__dprime = (ndtri(self.hitRate()) - ndtri(self.falseAlarmRate()))
    return self.__dprime #ask about ndtri vs norm.ppf
  
  def criterion(self):
    # Calculates the Criterion value
    self.__criterion = (-0.5 * (ndtri(self.hitRate()) + ndtri(self.falseAlarmRate())))
    return self.__criterion

  def __add__(self, other):
    return SignalDetection(self.__hit + other.__hit, self.__miss + other.__miss, self.__fa + other.__fa, self.__cr + other.__cr)

  def __mul__(self, scalar):
    return SignalDetection(self.__hit * scalar, self.__miss * scalar, self.__fa * scalar, self.__cr * scalar) 

def plot_roc(*objects): # * specifies unknown number of objects
    '''Drafted function for plot_roc(objects). Successfuly makes a graph but logic doesn't account for points where values are given out of order.
    Also not the most readable'''
    x_vals = [0] # initializing lists, beginnging with 0 to include point (0,0)
    y_vals = [0]
    for classObj in objects: # looping through arguments given to function to append all datapoints to appropriate lists
      classObj.hitRate()
      classObj.falseAlarmRate()
      newX = classObj.__hr
      x_vals.append(newX)
      newY = classObj.__far
      y_vals.append(newY)
    x_vals.append(1) # appending (1,1) to both lists per prompt
    y_vals.append(1)
    plt.plot(x_vals, y_vals) # generating plot points
    plt.xlabel('Hit Rate') # labeling axes
    plt.ylabel('False Alarm Rate')
    plt.title("Receiver Operating Curve") # plot title
    plt.show() # generating visual
    return
