import numpy as np
import matplotlib.pyplot as plt
data = np.array(np.loadtxt('screen.log'))[2000:3000]
a= np.shape(data)[0]
plt.plot(range(a),data)
plt.show()
