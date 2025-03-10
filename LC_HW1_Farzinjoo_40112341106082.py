import numpy as np
import matplotlib.pyplot as plt

M_alpha = -8.790
M_q = -2.075
M_deltaE = -11.87

dt = 0.01  
t_max = 5  
t = np.arange(0, t_max, dt)

deltaE_values = [-5, 0, 10]  

def solve_euler(deltaE):
    deltaE_rad = np.radians(deltaE)  
    theta = np.zeros_like(t)
    theta_dot = np.zeros_like(t)

    for i in range(1, len(t)):
        theta_ddot = M_alpha * theta[i-1] + M_q * theta_dot[i-1] + M_deltaE * deltaE_rad
        theta_dot[i] = theta_dot[i-1] + theta_ddot * dt
        theta[i] = theta[i-1] + theta_dot[i] * dt
    
    return theta

plt.figure(figsize=(8, 5))
for deltaE in deltaE_values:
    theta_response = solve_euler(deltaE)
    plt.plot(t, theta_response, label=f'δE = {deltaE} deg')

plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.title('Pitch Angle Response')
plt.legend()
plt.grid()
plt.show()
