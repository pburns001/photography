import numpy as np
import matplotlib.pyplot as py
from matplotlib.pyplot import plot,xlabel, ylabel, title, suptitle, show
from numpy import log10,sqrt,cos,sin,tan, cosh, sinh, tanh, abs, exp
from scipy.constants import foot as meter_per_foot
import math
mile_ft = 5280

# George D  OptimumCSP
def opt(un_ft,uf_ft,f_mm):
    """
    compute optimal F# and using optimal F# compute coc, optimal focus dist
    un_ft  near distance in ft
    uf_ft  far distance in ft
    f   focal length in mm
    """
    # get un and uf in units of mm
    un = un_ft*meter_per_foot*1000
    uf = uf_ft*meter_per_foot*1000
    vn = un*f/(un-f)        # vn in mm
    vf = uf*f/(uf-f)        # vf in mm
    dv = vn-vf
    Nopt = sqrt(375*dv)     # opt f#
    Ct = sqrt((dv/(2*Nopt))**2 + (Nopt/750)**2) # coc in mm
    uopt = 2*un*uf/(un+uf)/1000      # optimal focusing distance in meters
    return Ct,Nopt,uopt/meter_per_foot

def non_opt(un_ft,uf_ft,f_mm,N):
    """
    compute optimal F#, Using provided F# compute coc, optimal focus dist,
    un_ft  near distance in ft
    uf_ft  far distance in ft
    f   focal length in mm
    """
    # get un and uf in units of mm
    un = un_ft*meter_per_foot*1000
    uf = uf_ft*meter_per_foot*1000
    vn = un*f/(un-f)        # vn in mm
    vf = uf*f/(uf-f)        # vf in mm
    dv = vn-vf
    Nopt = sqrt(375*dv)     # opt f#
    Ct = sqrt((dv/(2*N))**2 + (N/750)**2) # coc in mm
    uopt = 2*un*uf/(un+uf)/1000      # optimal focusing distance in meters
    return Ct,Nopt,uopt/meter_per_foot


#c,nopt,uopt_ft = coc(100*meter_per_foot,1000*meter_per_foot,100,10)

# Given focus dist, f#, f, and coc, compute near and far limits of dof
#uopt = 2*un*uf/(un+uf)
# essentially GD Trud DOF
def limits(f,N,u_ft,coc):
    """
    :param f:       focal length mm
    :param N:       f #
    :param u:       focal dist ft
    :param coc:     mm
    :return:
    """
    u = u_ft*meter_per_foot*1000        # focus dist in mm
    v = u*f/(u-f)
    dv = 1/375*N*sqrt(562500*coc**2 - N**2)     # focus spread
    # compute vn and vf from v and dv
    vf = v-dv/2
    vn = vf + dv
    un = f*vn/(vn-f)
    uf = f*vf/(vf-f)
    if uf<0:
        uf = math.inf
    return un/1000/meter_per_foot,uf/1000/meter_per_foot



if __name__ == "__main__":
    un = 189
    uf = 1911
    f = 200
    N = 8
    c, Nopt, uopt_ft = opt(un, uf, f)
    print(
        f"near dist = {un:7.1f}ft, far dist = {uf:7.1f}ft, f = {f:4.1f}mm\nCOC = {c:6.3f}mm, Opt F# = {Nopt:3.1f}, Optimal focus distance = {uopt_ft:6.1f}ft")
    print("\n\n")

    f = 24
    N = 8
    u_ft = 100
    coc = 0.020
    un,uf = limits(f,N,u_ft,coc)
    un_ft = np.floor(un)
    un_in = np.round((un%1)*12)
    uf_ft = np.floor(uf)
    uf_in = np.round((uf%1)*12)
    print(f"Focus dist = {u_ft:7.1f}ft, N = {N}, f = {f:4.1f}mm, COC = {coc}mm")
    if uf_ft == math.inf:
        print(f"Near dist = {un_ft}'{un_in}\", Far dist = {uf_ft}'")
    else:
        print(f"Near dist = {un_ft}'{un_in}\", Far dist = {uf_ft}'{uf_in}\"")


