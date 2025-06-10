
import numpy as np
import matplotlib.pyplot as plt


def bias_squared(x):
    return x-(x**0.5)+np.log(x)

def variance(x):
    return (x**2)
Bayes_Error = 0.1304
x =np.linspace(0,1,400)
print(x)
y_bias = bias_squared(x)
y_variance= variance(x)

plt.figure(figsize=(10,6))
plt.plot(x,y_bias)
plt.plot(x,y_variance)
plt.title("Bais-variance ")
plt.tight_layout()
plt.show()
