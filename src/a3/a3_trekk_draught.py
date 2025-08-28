def draught_rate(T_a, v, Tu):
    if v < 0.05:
        return 0
    dr = (34 - T_a) * (v - 0.05)**0.62 * (0.37 * v * Tu + 3.14)
    return dr

if __name__ == "__main__":
    dr = draught_rate(22, 0.18, 0.20)
    print(f"DR ≈ {dr:.1f} %")
