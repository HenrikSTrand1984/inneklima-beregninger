def daylight_factor(E_i, E_o):
    df = (E_i / E_o) * 100
    return df

if __name__ == "__main__":
    df = daylight_factor(200, 10000)
    print(f"DF ≈ {df:.1f} %")
