import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,plot,xlabel, ylabel, title, suptitle, show, grid,title,suptitle,legend
from numpy import log10,sqrt,cos,sin,tan, cosh, sinh, tanh, abs, exp
from scipy.constants import foot as meter_per_foot
import math
from GeorgeDouvosEquations import *
mile_ft = 5280
matplotlib.use('Qt5Agg')


# plot near and far distances for following settings as focus dist increases
f = 24
coc= 0.020 # mm
N = 8
us = np.arange(1,101,1)
nn = len(us)
NDs = np.zeros(nn)
FDs = np.zeros(nn)
for ii,u in enumerate(us):
   NDs[ii], FDs[ii] = limits(f,N,u,coc)

figure();plot(us,NDs,label='Near Dist');grid(True,'both',alpha = 0.2)
plt.minorticks_on()
xlabel('focus dist ft')
ylabel('ft')
legend()
title('f = %4.1f, N = %d, COC = %5.3fmm'%(f,N,coc))



print("sim finished")