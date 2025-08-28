import math

def co2_steady_state(C_o, G, Q):
    C_i = C_o + (G / Q) * 1e6
    return C_i

def co2_transient(C_o, C_initial, G, Q, V, t):
    G_m3s = G / 1000
    term1 = C_o
    term2 = (C_initial - C_o - (G_m3s / Q) * 1e6) * math.exp(-(Q / V) * t)
    term3 = (G_m3s / Q) * 1e6
    C_t = term1 + term2 + term3
    return C_t

def required_fresh_air(G, delta_C_max):
    Q_min = (G * 1e6) / delta_C_max
    return Q_min

if __name__ == "__main__":
    N = 25
    G_per = 0.005
    G_tot = N * G_per
    delta_C = 700
    Q_min = required_fresh_air(G_tot, delta_C)
    print(f"Q_min >= {Q_min:.1f} L/s ({Q_min/N:.1f} L/s per elev)")
    C_t = co2_transient(400, 400, 0.125, 0.179, 200, 3600)
    print(f"C(t=1h) ≈ {C_t:.0f} ppm")
