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
      self.proposed += 1
      return True
    else: 
      self.proposed += 1
      return False

  def adapt(self):
    """Performs the adaptation phase of the Metropolis algorithm."""
    proposedSD = 1
    targetRate = 0.4
    acceptanceRate = 0
    N = 0
    K = 0
    while N < len(blockLengths):
      while K < blockLengths[N]:
        proposal = np.random.normal(loc=self.currentState, scale=proposedSD)
        self.__accept(proposal)
        K += 1
      acceptanceRate = self.__accepted / self.__proposed
      proposedSD = proposedSD * ((acceptanceRate / targetRate) **1.1)
      N += 1
    self.SD = proposedSD  

  def sample(self, n):
    """Generates n samples from the target distribution using the Metropolis algorithm."""
    for sample in range(nSamples): 
      proposal = np.random.normal(self.currentState, self.SD)
      self.__accept(proposal)
      self.samples.append(self.currentState)
    return self

  def summmary(self):
    """Returns a dictionary or structure containing the mean and a 95% credible interval of generated samples."""

    return summ
