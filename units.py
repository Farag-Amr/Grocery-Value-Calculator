"""Convert grocery weights.

Supported units are grams, kilograms, ounces, and pounds.
Ounces here are avoirdupois weight. Fluid ounces are volume and do not belong here.
Every conversion goes through grams, including when both units are the same.
"""

# Grams per avoirdupois unit. One pound is 16 of these ounces.
# Keys are the spellings accepted after strip() and lower().
GRAMS_PER_UNIT = {
    "kg": 1000,
    "kilogram": 1000,
    "kilograms": 1000,
    "g": 1,
    "gram": 1,
    "grams": 1,
    "lb": 453.59237,
    "pound": 453.59237,
    "pounds": 453.59237,
    "oz": 28.349523125,
    "ounce": 28.349523125,
    "ounces": 28.349523125,
}

def convert(quantity, from_unit, to_unit):
    """Return quantity converted from from_unit to to_unit.

    quantity may be a number or a numeric string, and it must be greater than zero.
    Unit text matches with surrounding spaces and capital letters removed.
    Raises TypeError when a unit is not a string.
    Raises ValueError when the quantity is not usable or a unit is not supported.
    """

    amount = float(quantity)
    if amount <= 0:
        raise ValueError("quantity must be greater than zero")
    elif not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("from_unit and to_unit must be strings")

    source = from_unit.strip().lower()
    target = to_unit.strip().lower()
    if source not in GRAMS_PER_UNIT:
        raise ValueError(f"unsupported unit: {from_unit}")
    if target not in GRAMS_PER_UNIT:
        raise ValueError(f"unsupported unit: {to_unit}")

    grams = amount * GRAMS_PER_UNIT[source]
    return grams / GRAMS_PER_UNIT[target]
