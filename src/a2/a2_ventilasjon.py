def calculate_ventilation_airflow(np, qp, A, qA):
    Q_tot_m3h = np * qp + A * qA
    Q_tot_ls = round(Q_tot_m3h / 3.6)
    return Q_tot_m3h, Q_tot_ls

if __name__ == "__main__":
    np = 20
    qp = 35
    A = 180
    qA = 3
    Q_tot_m3h, Q_tot_ls = calculate_ventilation_airflow(np, qp, A, qA)
    print(f"Q_tot = {Q_tot_m3h} m³/h (= {Q_tot_ls} l/s)")
    # Mini-regneark eksempel
    C_o = 400
    C_i_target = 1000
    G_CO2_per_person = 0.005
    G_CO2 = np * G_CO2_per_person
    from a2_co2_massebalanse import calculate_required_airflow  # Importer hvis i pakke
    Q_tot_co2_m3h = calculate_required_airflow(C_i_target, C_o, G_CO2)
    Q_tot_dim = max(Q_tot_m3h, Q_tot_co2_m3h)
    print(f"Dimensjonerende Q_tot: {Q_tot_dim} m³/h")
