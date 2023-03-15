class Metropolis:
  def __init__(self, logTarget, initialState):
    """Initializes the class object using the self, a target function, and an initial state."""
    self.logTarget = logTarget
    self.initialState = initialState

def acceptanceProb(initialState, proposedState):
    """Calculates acceptance probability given initial and proposed states."""
    self.acceptProb = min(1, (exp((proposedState/initialState))))
    return self.acceptProb
  
  def __accept(self, proposal):
    """Checkes whether to accept or reject proposed value based on acceptance probability."""
    if self == proposal: 
      yesno = True
    else:
      yesno = False
    return yesno

  def adapt(self):
    """Performs the adaptation phase of the Metropolis algorithm."""
    def adapt(self, blockLengths):
    """Performs the adaptation phase of the Metropolis algorithm."""
    
    proposedSD = 1
    targetAccept = 0.4 
    counterK = 0
    for block in blockLengths:
      while counterK <= blockLengths[0]: 
        rk = self.acceptanceProb(self.initialState, proposedSD)
        proposedSD = proposedSD * ((targetAccept/rk)**1.1)
        counterK += 1
    self.SD = proposedSD
    return self
  
  def sample(self, n):
    """Generates n samples from the target distribution using the Metropolis algorithm."""

    return self

  def summmary(self):
    """Returns a dictionary or structure containing the mean and a 95% credible interval of generated samples."""

    return summ
