#Import required libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# -------------------------------------------------------------------------------
# Author: Marta B
# Do not copy, this is a project for University class
# Three oscillating springs with springs constants k_1,k_2 and k_1,2 are displaced from the origin x, describe the motion
# of oscillating springs. Considering the equation of motion for a 3-spring mass system
# x_doubedot = -(c_1/m*x**3 + c_2/m*x**3 + k_1/m*x+k_2/m*x + k_3/m*x
# -------------------------------------------------------------------------------

# The initial x passed to the function will have the initial position in the first position
# and the initial velocity in the second position
def T(v):
    m_1 = 9  # kg
    m_2 = 5  # kg

    return 1/2*m_1*v**2 +1/2*m_2*v**2

v = np.arange(0, 10, 0.5)
t = np.arange(0, 10, 1500)
# inital velocity is zero
# the output will 2 columns - 1. Velocity and 2. Acceleration as defined in the return of the function
plt.plot(t,v, label='Kinetic energy')
plt.legend()
plt.ylabel('Potential energy V(x)')
plt.xlabel('time (s)')
plt.title('Potential energy for three coupled oscillators')

plt.grid(b=True)
plt.show()
# We will say that the velocity v = x^dot then x^ddot is v^dot no