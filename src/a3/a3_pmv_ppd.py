import math

def approximate_pmv(M, Icl, T_a, T_r, v, RH):
    t_o = (T_a + T_r) / 2
    pmv_base = 0.303 * math.exp(-0.036 * M) + 0.028
    pmv = pmv_base * ((M - 58) + (Icl - 0.5)*10 + (t_o - 22)*0.2 + (v - 0.1)*2 + (RH - 50)*0.01)
    return pmv

def ppd_from_pmv(pmv):
    exp_term = math.exp( - (0.03353 * pmv**4 + 0.2179 * pmv**2))
    ppd = 100 - 95 * exp_term
    return ppd

if __name__ == "__main__":
    pmv = approximate_pmv(60, 0.5, 22, 22, 0.1, 50)
    ppd = ppd_from_pmv(pmv)
    print(f"PMV ≈ {pmv:.2f}, PPD ≈ {ppd:.1f} %")
