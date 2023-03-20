class Metropolis:
  def __init__(self, logTarget, initialState):
    """Initializes the class object using the self, a target function, and an initial state."""
    self.logTarget = logTarget
    self.currentState = initialState
    self.samples = []
    self.accepted = 0
    self.proposed = 0
  
  def __accept(self, proposal):
    """Checkes whether to accept or reject proposed value based on acceptance probability."""
    acceptanceProb = min(0, self.logTarget(proposal) - self.logTarget(self.currentState))
    if acceptanceProb > numpy.log(np.random.uniform()): 
      self.currentState = proposal
      self.accepted += 1 
      self.pr0posed += 1
      return True
    else: 
      self.proposed += 1
      return False

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
