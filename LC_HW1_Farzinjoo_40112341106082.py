import numpy as np
import matplotlib.pyplot as plt

# پارامترهای مسئله
h = 0.01
t = np.arange(0, 5, h)
N = len(t)

# ضرایب داده‌شده
M_alpha = -8.790
M_q = -2.075
M_deltaE = -11.87

# متغیرهای حالت
theta = np.zeros(N)
thetadot = np.zeros(N)

# ورودی سکان
deltaE = np.zeros(N)
deltaE[N//2:] = 10

# روش اویلر
for k in range(N-1):
 thetadot [k+1] = thetadot [k] + h * (M_alpha * theta[k] + M_q * thetadot[k] + M_deltaE * deltaE[k])
theta[k+1] = theta[k] + h * thetadot[k]

# رسم نمودار
plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
plt.plot(t, theta, 'b', linewidth=1.5)
plt.xlabel('زمان (ثانیه)')
plt.ylabel('زاویه پیچ θ (درجه)')
plt.title('پاسخ زاویه پیچ به ورودی سکان')
plt.grid()

plt.subplot(2,1,2)
plt.plot(t, deltaE, 'r', linewidth=1.5)
plt.xlabel('زمان (ثانیه)')
plt.ylabel('ورودی δ_E (درجه)')
plt.title('ورودی سکان')
plt.grid()

plt.tight_layout()
plt.show()
