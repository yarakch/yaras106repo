import numpy
from scipy.special import ndtri

class SignalDetection:
  def __init__(self,hit,miss,fa,cr):
    # Define variables
    self.__hit = hit
    self.__miss = miss
    self.__fa = fa
    self.__cr = cr

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

