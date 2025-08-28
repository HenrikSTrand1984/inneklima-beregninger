def air_age(V, Q_m3s):
    tau = V / Q_m3s
    return tau

if __name__ == "__main__":
    tau = air_age(200, 0.179)
    print(f"τ ≈ {tau:.0f} s (ca. {tau/3600:.1f} timer)")
