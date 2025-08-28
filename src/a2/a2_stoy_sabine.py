def reverberation_time(V, surfaces_alphas):
    A = sum(S * alpha for S, alpha in surfaces_alphas)
    T_60 = 0.16 * V / A if A > 0 else float('inf')
    return T_60

if __name__ == "__main__":
    T_60 = reverberation_time(500, [(200, 0.1), (100, 0.5), (50, 0.2)])
    print(f"T_60 ≈ {T_60:.2f} s")
