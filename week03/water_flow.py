# water_flow.py

# 1. Constants for Earth's acceleration of gravity, water density, and water dynamic viscosity
WATER_DENSITY = 997.497  # kg/m^3
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2
WATER_DYNAMIC_VISCOSITY = 0.0010016  # kg/(m·s) or Pa·s


def water_column_height(tower_height, tank_height):
    """Compute and return the water column height."""
    h = tower_height + (3 * tank_height / 4)
    return h


def pressure_gain_from_water_height(height):
    """Compute and return the pressure gain from water height."""
    P = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return P


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Compute and return the pressure loss from a pipe."""
    P = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return P


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Compute and return the pressure loss from pipe fittings."""
    P = (-0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings) / 2000
    return P


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Compute and return the Reynolds number."""
    R = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return R


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Compute and return the pressure loss from a pipe reduction."""
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4) - 1
    P = (-k * WATER_DENSITY * fluid_velocity ** 2) / 2000
    return P


# 2. Additional functionality: Convert kilopascals to pounds per square inch
def kpa_to_psi(kpa):
    """Convert kilopascals to pounds per square inch."""
    return kpa * 0.145038


def main():
    # Get input from the user
    tower_height = float(input("Height of water tower (in meters): "))
    tank_height = float(input("Height of water tank walls (in meters): "))
    pipe_diameter = float(input("Diameter of water pipe (in meters): "))
    pipe_length = float(input("Length of water pipe (in meters): "))
    friction_factor = float(input("Friction factor of pipe: "))
    fluid_velocity = float(input("Fluid velocity (in meters/second): "))
    quantity_fittings = int(input("Quantity of fittings: "))
    larger_diameter = float(input("Larger pipe diameter (in meters): "))
    smaller_diameter = float(input("Smaller pipe diameter (in meters): "))

    # Call the six functions
    height = water_column_height(tower_height, tank_height)
    gain = pressure_gain_from_water_height(height)
    loss_pipe = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
    loss_fittings = pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
    re = reynolds_number(pipe_diameter, fluid_velocity)
    loss_reduction = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, re, smaller_diameter)

    # Print output for the user to see
    print(f"\n--- Water System Design Results ---")
    print(f"Water column height: {height:.2f} meters")
    print(f"Pressure gain: {gain:.2f} kPa ({kpa_to_psi(gain):.2f} psi)")
    print(f"Pressure loss from pipe: {loss_pipe:.2f} kPa")
    print(f"Pressure loss from fittings: {loss_fittings:.2f} kPa")
    print(f"Reynolds number: {re:.2f}")
    print(f"Pressure loss from pipe reduction: {loss_reduction:.2f} kPa")


if __name__ == "__main__":
    main()