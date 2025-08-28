import math

def total_noise_level(levels_db):
    sum_intensity = sum(10**(L / 10) for L in levels_db)
    L_tot = 10 * math.log10(sum_intensity)
    return L_tot

if __name__ == "__main__":
    L_tot = total_noise_level([50, 53])
    print(f"L_tot ≈ {L_tot:.1f} dB(A)")
