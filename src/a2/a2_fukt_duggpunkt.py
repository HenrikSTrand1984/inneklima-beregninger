import math

def saturation_vapor_pressure(T):
    a = 17.62
    b = 243.12
    p_sat = 6.112 * math.exp((a * T) / (b + T))
    return p_sat

def absolute_humidity(phi, T, p_total=1013):
    p_v = phi * saturation_vapor_pressure(T)
    x = 0.622 * (p_v / (p_total - p_v)) * 1000
    return x

def dew_point(T, phi):
    a = 17.62
    b = 243.12
    gamma = (a * T) / (b + T) + math.log(phi)
    T_dp = (b * gamma) / (a - gamma)
    return T_dp

if __name__ == "__main__":
    T = 24
    phi = 0.5
    T_dp = dew_point(T, phi)
    x = absolute_humidity(phi, T)
    print(f"T_dp ≈ {T_dp:.1f} °C, x ≈ {x:.1f} g/kg")
