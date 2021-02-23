import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 6.0, 250)

plt.hist(x, 6)
plt.show()
