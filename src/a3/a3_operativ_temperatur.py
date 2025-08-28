def operative_temperature_simple(T_a, T_r):
    t_o = (T_a + T_r) / 2
    return t_o

def operative_temperature_general(T_a, T_r, h_c, h_r):
    t_o = (h_c * T_a + h_r * T_r) / (h_c + h_r)
    return t_o

if __name__ == "__main__":
    t_o = operative_temperature_simple(22, 20)
    print(f"t_o ≈ {t_o:.1f} °C")
