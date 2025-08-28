# Din spesifikke kode fra spørsmålet
from a3_co2_balanse import required_fresh_air
from a3_ventilasjonsvarmetap import ventilation_heat_loss
from a3_trekk_draught import draught_rate

if __name__ == "__main__":
    N = 20
    G_per = 0.005
    G_tot = N * G_per
    delta_C = 600
    Q_min = required_fresh_air(G_tot, delta_C)
    Q_m3h = 2000
    delta_T = 20
    eta_vg = 0.75
    phi_netto = ventilation_heat_loss(Q_m3h, delta_T, eta_vg)
    T_a = 22
    v = 0.18
    Tu = 0.20
    dr = draught_rate(T_a, v, Tu)
    print(f"9.1: Q_min >= {Q_min:.0f} L/s")
    print(f"9.2: Φ_netto ≈ {phi_netto:.0f} W")
    print(f"9.4: DR ≈ {dr:.1f} %")
