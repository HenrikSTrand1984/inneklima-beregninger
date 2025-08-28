from src.a2.a2_ventilasjon import calculate_ventilation_airflow

def test_calculate_ventilation_airflow():
    np, qp, A, qA = 20, 35, 180, 3
    Q_tot_m3h, Q_tot_ls = calculate_ventilation_airflow(np, qp, A, qA)
    assert Q_tot_m3h == 1240
    assert Q_tot_ls == 344
