import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100  )
plt.plot(x,np.sin(x),label='sin')
plt.plot(x,np.cos(x),label='cos')
plt.legend()
plt.show()
         