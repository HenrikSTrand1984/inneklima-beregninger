import math

def absolute_humidity_balance(w_o, g, rho_air, Q_m3s):
    w_i = w_o + g / (rho_air * Q_m3s)
    return w_i

def dew_point_from_rh(T, RH):
    a = 17.62
    b = 243.12
    gamma = math.log(RH / 100) + (a * T) / (b + T)
    T_d = (b * gamma) / (a - gamma)
    return T_d

if __name__ == "__main__":
    T_d = dew_point_from_rh(22, 30)
    print(f"T_d ≈ {T_d:.1f} °C")
    w_i = absolute_humidity_balance(0.002, 0.0000222, 1.2, 0.06)
    print(f"w_i ≈ {w_i:.6f} kg/kg")
