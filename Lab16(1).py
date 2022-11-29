import matplotlib.pyplot as plt
import numpy as np
import math
x= np.linspace(-1,6)
y=3*x+2**3
plt.plot(x,y,'g--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function')
plt.legend()
plt.show()
plt.savefig('/Users/llirik/Desktop/Univer/Lab16/restart.jpg', dpi=400)
