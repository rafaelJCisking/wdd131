"""This module contains functions to help design a drinking water system."""

def water_column_height(tower_height, tank_height):
    """Calculate the height of a water column in a tower with an elevated tank."""
    # Formula: h = t + (3w / 4)
    return tower_height + (3 * tank_height / 4)


def pressure_gain_from_water_height(height):
    """Calculate the pressure gain from the height of a water column."""
    rho = 998.2       # Density of water in kg/m^3
    g = 9.80665       # Acceleration due to gravity in m/s^2
    # Formula: P = (rho * g * h) / 1000
    return (rho * g * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate the pressure loss from friction in a pipe."""
    rho = 998.2       # Density of water in kg/m^3
    # Formula: P = -(f * L * rho * v^2) / (2000 * d)
    return -(friction_factor * pipe_length * rho * fluid_velocity ** 2) / (2000 * pipe_diameter)


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate the pressure loss from fittings in a pipe."""
    rho = 998.2       # Density of water in kg/m^3
    # Formula: P = -(0.04 * rho * v^2 * n) / 2000
    return -(0.04 * rho * fluid_velocity ** 2 * quantity_fittings) / 2000


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate the Reynolds number for flow in a pipe."""
    rho = 998.2       # Density of water in kg/m^3
    mu = 0.0010016    # Dynamic viscosity of water in Pa*s
    # Formula: R = (rho * d * v) / mu
    return (rho * hydraulic_diameter * fluid_velocity) / mu


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate the pressure loss from a reduction in pipe diameter."""
    rho = 998.2       # Density of water in kg/m^3
    
    # Formula: k = (0.1 + 50 / R) * ((D/d)^4 - 1)
    # Note: The (0.1 + 50/R) must be grouped together!
    diameter_ratio = larger_diameter / smaller_diameter
    k = (0.1 + 50 / reynolds_number) * (diameter_ratio ** 4 - 1)
    
    # Formula: P = -(k * rho * v^2) / 2000
    return -(k * rho * fluid_velocity ** 2) / 2000