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

def oscillator(x,t):
    # The initial x passed to the function will have the initial position in the first position
    # and the initial velocity in the second position
    c_1 = 6  #constant
    c_2 = 10 # constant
    k_1 = 25 # N/m
    k_2 = 30 # N/m
    k_3 = 22 # N/m
    m_1 = 9  # kg
    m_2 = 5  # kg
    m = m_1 + m_2 #kg

    # The output of the function will have the velocity in the first position and the acceleration in the second position
    solution = x[1],-(c_1/m*x[0]**3 + c_2/m*(x[0])**3 + k_1/m*x[0]+k_2/m*x[0] + k_3/m*x[0])
#x[0] = the velocity
#x[1] = acceleration
    return solution


#x = np.linspace(0.4,10,1500)
c_1 = 6  # constant
c_2 = 10  # constant
k_1 = 25  # N/m
k_2 = 30  # N/m
k_3 = 22  # N/m
m_1 = 9  # kg
m_2 = 5  # kg
m = m_1 + m_2  # kg


# the time from 0 to 10 s with 1500 points
t = np.linspace(0, 10, 1500)
# we start at a point x m and zero velocity.
initial = [2, 0]


# inital velocity is zero
#the output will 2 columns - 1. Velocity and 2. Acceleration as defined in the return of the function
output = odeint(oscillator, initial, t)

# odeint takes in three arg the function, the inital value and vector of time
T = 1/2*m_1*(output[:,0])**2 +1/2*m_2*output[:,0]**2
V = 1 / 2 * k_1 * initial[0] ** 2 + 1 / 4 *c_1 *initial[0] ** 4 + 1 / 2*k_2*initial[0]** 2 + 1 / 4 * c_2 * initial[0]** 4 + 1 / 2 * k_3 * initial[0] ** 2

E = T + V
#output[:,1] means items from beginnning through velocity -1
#plot acceleration and velocity
plt.plot(t, output[:, 1],linewidth = 1, label = 'acceleration')
plt.plot(t,output[:,0],'r--',linewidth = 2, label = 'velocity')
plt.ylabel('x(t)')
plt.xlabel('time(s)')
plt.legend()
plt.title('Motion for coupled oscillators')
plt.show()

#---Plot of the potential energy
plt.plot(t,V,'b-',linewidth = 1, label='Potential Energy', )

plt.plot(t,T,'r--',linewidth = 2, label = 'Kinetic energy')
plt.plot(t,E,'g',label='Total energy')
plt.xlabel('time')
plt.ylabel('Energy')
plt.legend()
plt.grid()
plt.show()



