# test_water_flow.py

from pytest import approx
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi
)

def test_water_column_height():
    assert water_column_height(10, 20) == approx(25.0)
    assert water_column_height(0, 0) == approx(0.0)
    assert water_column_height(5.5, 8.0) == approx(11.5)

def test_pressure_gain_from_water_height():
    # P = (997.497 * 9.80665 * height) / 1000
    assert pressure_gain_from_water_height(10) == approx(97.821, abs=0.001)
    assert pressure_gain_from_water_height(0) == approx(0.0)
    assert pressure_gain_from_water_height(5.5) == approx(53.801, abs=0.001)

def test_pressure_loss_from_pipe():
    # P = (-f * L * rho * v^2) / (2000 * d)
    assert pressure_loss_from_pipe(0.1, 100, 0.02, 2) == approx(-39.89988, abs=0.001)
    assert pressure_loss_from_pipe(0.2, 50, 0.01, 1) == approx(-1.24687, abs=0.001)

def test_pressure_loss_from_fittings():
    # P = (-0.04 * rho * v^2 * n) / 2000
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)
    assert pressure_loss_from_fittings(2.0, 10) == approx(-0.79799, abs=0.001)

def test_reynolds_number():
    # R = (rho * d * v) / mu
    assert reynolds_number(0.1, 2) == approx(199180.71, abs=1.0)
    assert reynolds_number(0.05, 1.5) == approx(74692.76, abs=1.0)

def test_pressure_loss_from_pipe_reduction():
    # k = 0.1 + (50 / R) * (D / d)^4 - 1
    # P = (-k * rho * v^2) / 2000
    assert pressure_loss_from_pipe_reduction(0.2, 2, 100000, 0.1) == approx(1.7795, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.1, 3, 50000, 0.05) == approx(3.968, abs=0.001)

# 3. Test function that verifies the kPa to psi conversion function works correctly
def test_kpa_to_psi():
    assert kpa_to_psi(100) == approx(14.5038, abs=0.001)
    assert kpa_to_psi(0) == approx(0.0)