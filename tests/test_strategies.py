from crypto_intel.strategies.asset_class import score_signal

def test_stress_returns_zero():
    assert score_signal("major", "stress", {"strength": 0.8}) == 0.0

def test_major_caps():
    score = score_signal("major", "trend", {"strength": 0.9, "anomaly": 0.1, "vol_forecast": 0.3})
    assert 0 < score <= 0.08

def test_high_anomaly_zero():
    assert score_signal("large_alt", "trend", {"strength": 0.8, "anomaly": 0.8}) == 0.0

def test_high_vol_forecast_reduces():
    low = score_signal("major", "trend", {"strength": 0.8, "vol_tier": 0.4, "vol_forecast": 0.3})
    high = score_signal("major", "trend", {"strength": 0.8, "vol_tier": 0.4, "vol_forecast": 0.8})
    assert high < low
