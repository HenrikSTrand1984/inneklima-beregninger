import math

def operative_temperature(T_air, T_rad):
    return (T_air + T_rad) / 2

def approximate_pmv(M, Icl, T_air, T_rad, v_air, RH):
    T_op = operative_temperature(T_air, T_rad)
    pmv = 0.303 * math.exp(-0.036 * M) + 0.028
    pmv *= (M - 58) + (Icl - 0.5)*10 + (T_op - 22)*0.2 + (v_air - 0.1)*2 + (RH - 50)*0.01
    ppd = 100 - 95 * math.exp(- (0.03353 * pmv**4 + 0.2179 * pmv**2))
    return pmv, ppd

if __name__ == "__main__":
    pmv, ppd = approximate_pmv(60, 0.5, 22, 22, 0.1, 50)
    print(f"PMV ≈ {pmv:.2f}, PPD ≈ {ppd:.1f}%")
