def calculate_heat_load(U, A_trans, delta_T, Q_vent, T_i, T_o, Q_sol, Q_internal):
    Q_trans = U * A_trans * delta_T
    rho_cp = 0.34
    Q_vent_W = rho_cp * Q_vent * (T_i - T_o)
    Q_rom = Q_trans + Q_vent_W + Q_sol + Q_internal
    return Q_rom

if __name__ == "__main__":
    Q_rom = calculate_heat_load(0.2, 50, 20, 1240, 22, 0, 500, 1000)
    print(f"Varmelast Q_rom ≈ {Q_rom:.0f} W")
