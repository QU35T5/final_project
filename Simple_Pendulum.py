#Considering the equation of motion for a simple pendulum
#theta_doubledot = - (g/l)* sin(theta)

#Import required libraties
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def funct(x,t):
    c_1 = 3
    c_2 = 4
    k_1 = 25
    k_2 = 30
    k_3 = 22
    m_1 = 9
    m_2 = 5
    m = m_1 + m_2
    return(x[1],-(c_1/m*x[0]**3 + c_2/m*(x[0])**3 + k_1/m*x[0]+k_2/m*x[0] + k_3/m*x[0]))


times = np.linspace(0, 30, 500)

inits = [10, 0]

# inital velocity is zero
output = odeint(funct, inits, times)

plt.plot(times, output[:, 1])
plt.ylabel('x(t)')
plt.xlabel('t')
plt.title('Motion for coupled oscillators')
plt.show()
#We will say that the velocity v = x^dot then x^ddot is v^dot no
def func(x,t):
    k = 10
    m = 10
    return(x[1], -k/m*x[0])
time = np.linspace(0, 10, 500)
init = [10,0]
# inital velocity is zero
output = odeint(func, init, time)
plt.plot(time, output[:, 1], 'r')
plt.show()


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

