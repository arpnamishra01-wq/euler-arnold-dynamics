from scipy.integrate import solve_ivp

def solve_system(func, xi0, h, t_span, t_eval):
    return solve_ivp(
        func,
        t_span,
        xi0,
        args=(h,),
        t_eval=t_eval,
        method="DOP853",
        rtol=1e-9,
        atol=1e-9
    )
