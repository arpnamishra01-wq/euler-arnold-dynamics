import numpy as np

def euler_arnold(t, xi, h):
    x1, x2, x3, x4, x5, x6 = xi
    h1, h2, h3, h4, h5, h6 = h

    dx1 = x2*x3*(h2 - h3) + x5*x6*(h5 - h6)
    dx2 = x3*x1*(h3 - h1) + x6*x4*(h6 - h4)
    dx3 = x1*x2*(h1 - h2) + x4*x5*(h4 - h5)

    dx4 = x3*x5*(-h3 - h5) + x2*x6*(h2 + h6)
    dx5 = x1*x6*(-h1 - h6) + x3*x4*(h3 + h4)
    dx6 = x2*x4*(-h2 - h4) + x1*x5*(h1 + h5)

    return [dx1, dx2, dx3, dx4, dx5, dx6]
