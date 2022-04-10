import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,plot,xlabel, ylabel, title, suptitle, show, grid,title,suptitle,legend,subplot
from numpy import log10,sqrt,cos,sin,tan, cosh, sinh, tanh, abs, exp
from scipy.constants import foot as meter_per_foot
import math
from GeorgeDouvosEquations import *
mile_ft = 5280
matplotlib.use('Qt5Agg')


# plot near and far distances for following settings as focus dist increases
f = 200
coc= 0.020 # mm
N = 8
us = np.arange(100,4000,10)
nn = len(us)
NDs = np.zeros(nn)
FDs = np.zeros(nn)
for ii,u in enumerate(us):
   NDs[ii], FDs[ii] = limits(f,N,u,coc)

figure
subplot(2,1,1);plot(us,NDs,label='Near Dist');grid(True,'both',alpha = 0.2)
plt.minorticks_on()
xlabel('focus dist ft')
ylabel('ft')
legend()
title('f = %4.1f, N = %d, COC = %5.3fmm'%(f,N,coc))

subplot(2,1,2);plot(us,FDs,label='Far Dist');grid(True,'both',alpha = 0.2)
plt.minorticks_on()
xlabel('focus dist ft')
ylabel('ft')
legend()


f = 200
coc= 0.020 # mm
N = 8
us = np.arange(100,4000,10)
nn = len(us)
NDs = np.zeros(nn)
FDs = np.zeros(nn)
for ii,u in enumerate(us):
   NDs[ii], FDs[ii] = limits(f,N,u,coc)

figure
subplot(2,1,1);plot(us,NDs,label='Near Dist');grid(True,'both',alpha = 0.2)
plt.minorticks_on()
xlabel('focus dist ft')
ylabel('ft')
legend()
title('f = %4.1f, N = %d, COC = %5.3fmm'%(f,N,coc))

subplot(2,1,2);plot(us,FDs,label='Far Dist');grid(True,'both',alpha = 0.2)
plt.minorticks_on()
xlabel('focus dist ft')
ylabel('ft')
legend()


print("sim finished")