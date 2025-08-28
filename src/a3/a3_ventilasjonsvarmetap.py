def ventilation_heat_loss(Q_m3h, delta_T, eta_vg=0):
    phi = (1 - eta_vg) * 0.33 * Q_m3h * delta_T
    return phi

def ventilation_heat_loss_ls(Q_ls, delta_T, eta_vg=0):
    phi = (1 - eta_vg) * 1.2 * Q_ls * delta_T
    return phi

if __name__ == "__main__":
    phi_netto = ventilation_heat_loss(1800, 22, 0.80)
    print(f"Φ_netto ≈ {phi_netto:.0f} W")
