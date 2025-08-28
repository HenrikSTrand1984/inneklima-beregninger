def calculate_indoor_co2(C_o, G_CO2, Q_tot):
    G_CO2_m3s = G_CO2 * 0.001
    C_i = C_o + (G_CO2_m3s * 1e6) / Q_tot
    return C_i

def calculate_required_airflow(C_i_target, C_o, G_CO2):
    delta_C = C_i_target - C_o
    G_CO2_m3s = G_CO2 * 0.001
    Q_tot_m3s = (G_CO2_m3s * 1e6) / delta_C
    Q_tot_m3h = Q_tot_m3s * 3600
    return Q_tot_m3h

if __name__ == "__main__":
    np = 20
    G_CO2_per_person = 0.005
    G_CO2 = np * G_CO2_per_person
    C_o = 400
    C_i_target = 1000
    Q_tot_m3h = calculate_required_airflow(C_i_target, C_o, G_CO2)
    print(f"Nødvendig Q_tot = {Q_tot_m3h:.0f} m³/h")
