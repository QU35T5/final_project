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
    c_1 = 6
    c_2 = 10
    k_1 = 25 # N/m
    k_2 = 30 # N/m
    k_3 = 22 # N/m
    m_1 = 9  # kg
    m_2 = 5  # kg
    m = m_1 + m_2 #kg

    # The output of the function will have the velocity in the first position and the acceleration in the second position
    solution = x[1],-(c_1/m*x[0]**3 + c_2/m*(x[0])**3 + k_1/m*x[0]+k_2/m*x[0] + k_3/m*x[0])

    return solution

# the time from 0 to 30 s with 500 points
t = np.linspace(0, 10, 1500)

initial = [5, 0]

# inital velocity is zero
#the output will 2 columns - 1. Velocity and 2. Acceleration as defined in the return of the function
output = odeint(oscillator, initial, t)
#plot acceleration and velocity
plt.plot(t, output[:, 1],linewidth = 1, label = 'acceleration')
plt.plot(t,output[:,0],'r--',linewidth = 2, label = 'velocity')
plt.legend()
plt.ylabel('x(t)')
plt.xlabel('time(s)')
plt.title('Motion for coupled oscillators')
plt.show()


#We will say that the velocity v = x^dot then x^ddot is v^dot no

#define a function with the first argument being the variable you want to perform ODE on

#def func_pendulum (theta,t):

    #The initial theta passed to the function will have the initial position in the first position and the initial velocity in the second position
#   g  =9.8
#    l = 0.5
    #The output of the function will have the velocity in the first position and the acceleration in the second position
#    return[theta[1],-g/l*np.sin(theta[0])]


#The initial theta passed to the function will have the initial position in the first position and the initial velocity in the second position
#inital_theta = [np.pi/4,0]

#define a time vector
#time = np.linspace(0,5,1000)

#the output will 2 columns - 1. Velocity and 2. Acceleration as defined in the return of the function
#output = odeint(func_pendulum,inital_theta,time)

#plot acceleration and velocity
#plt.plot(time,output[:,1],'r',linewidth = 2, label = 'acceleration')
#plt.plot(time,output[:,0],'g:',linewidth = 2, label = 'velocity')
#plt.legend()
#plt.xlabel('time')
#plt.show()

#In case there are 2 or more generalised co-ordinates, for example (x,y) then, the initial values will be

#Init_values = [x,xdot,y,vdot]


#The output of your ODEINT function should be arranged as follows

#output = [xdot,xdotdot,ydot,ydotdot]

