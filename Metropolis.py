class Metropolis:
  def __init__(self, logTarget, initialState):
    """Initializes the class object using the self, a target function, and an initial state."""
    self.logTarget = logTarget
    self.currentState = initialState
    self.samples = []
    self.__accepted = 0
    self.__proposed = 0
  
  def __accept(self, proposal):
    """Checkes whether to accept or reject proposed value based on acceptance probability."""
    acceptanceProb = min(0, self.logTarget(proposal) - self.logTarget(self.currentState))
    if acceptanceProb > numpy.log(np.random.uniform()): 
      self.currentState = proposal
      self.__accepted += 1 
      self.__proposed += 1
      return True
    else: 
      self.__proposed += 1
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
        proposal = numpy.random.normal(loc=self.currentState, scale=proposedSD)
        self.__accept(proposal)
        K += 1
      acceptanceRate = self.__accepted / self.__proposed
      proposedSD = proposedSD * ((acceptanceRate / targetRate) **1.1)
      N += 1
    self.SD = proposedSD 
    return self 

  def sample(self, n):
    """Generates n samples from the target distribution using the Metropolis algorithm."""
    for sample in range(nSamples): 
      proposal = numpy.random.normal(self.currentState, self.SD)
      self.__accept(proposal)
      self.samples.append(self.currentState)
    return self

  def summmary(self):
    """Returns a dictionary or structure containing the mean and a 95% credible interval of generated samples."""
    mean = numpy.mean(self.samples)
    lower = numpy.percentile(self.samples, 2.5)
    upper = numpy.percentile(self.samples, 97.5)
    summ = {"mean": mean, "c025": lower, "c975": upper}
    return summ
