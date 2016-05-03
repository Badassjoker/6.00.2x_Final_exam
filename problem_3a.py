import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    reproPro = 1.0 - CURRENTRABBITPOP / float(MAXRABBITPOP)
    pop = CURRENTRABBITPOP

    for i in range(pop):
        if random.random() < reproPro and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    eatPro = CURRENTRABBITPOP / float(MAXRABBITPOP)
    pop = CURRENTFOXPOP

    for i in range(pop):
        if random.random() < eatPro and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1

            if random.random() < 1.0/3.0:
                CURRENTFOXPOP += 1

        else:
            if random.random() < 0.9 and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbitPops, foxPops = [], []

    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitPops.append(CURRENTRABBITPOP)
        foxPops.append(CURRENTFOXPOP)

    return (rabbitPops, foxPops)

rab, fox = runSimulation(200)
xVals = pylab.array(range(200))
rabVals = pylab.array(rab)
foxVals = pylab.array(fox)
pylab.plot(rabVals, label = 'Rabbit population')
pylab.plot(foxVals, label = 'Fox population')
a, b, c = pylab.polyfit(xVals, rabVals, 2)
fitRabVals = a * (xVals**2) + b * xVals + c
d, e, f = pylab.polyfit(xVals, foxVals, 2)
fitfoxVals = d * (xVals**2) + e * xVals + f
pylab.plot(fitRabVals, '*', label = 'Fit rabbit population')
pylab.plot(fitfoxVals, 'o', label = 'Fit fox population')
pylab.title('Simulation of rabbits and foxes in a forest')
pylab.xlabel('Time step')
pylab.ylabel('Population')
pylab.legend()
pylab.show()