import numpy as np
import scipy.stats as stats

class SignalDetection:

    def __init__(self, hits, misses, falseAlarms, correctRejections):
        "Initializes the class using the self object and the signal detection variables."
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    def __str__(self):
        "Returns the class as a labeled list to enable printing and error detection."
        return f"hits: {self.hits}, misses: {self.misses}, false alarms: {self.falseAlarms}, correct rejections: {self.correctRejections}"

    def hit_rate(self):
        "Returns the hit rate based on the class object."
        self.hr = (self.hits / (self.hits + self.misses))
        return self.hr

    def false_alarm_rate(self):
        "Returns the false alarm rate based on the class object."
        self.far = (self.falseAlarms / (self.falseAlarms + self.correctRejections))
        return self.far
    
    def d_prime(self):
        "Returns the d-prime value given the hit rate and false alarm rate."
        hr = self.hit_rate()
        far = self.false_alarm_rate()
        z_h = stats.norm.ppf(hr)
        z_fa = stats.norm.ppf(far)
        self.dp = z_h - z_fa
        return self.dp

    def criterion(self):
        "Returns the criterion value given the hit rate and false alarm rate."
        hr = self.hit_rate()
        far = self.false_alarm_rate()
        z_h = stats.norm.ppf(hr)
        z_fa = stats.norm.ppf(far)
        self.c = -0.5 * (z_h + z_fa)
        return self.c
