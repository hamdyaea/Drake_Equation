#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Calculate the Drake equation from explicit, adjustable assumptions."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class DrakeParameters:
    star_formation_rate: float = 1.0
    fraction_with_planets: float = 0.5
    habitable_planets_per_system: float = 1.0
    fraction_developing_life: float = 0.01
    fraction_developing_intelligence: float = 0.01
    fraction_communicating: float = 0.01
    detectable_years: float = 10.0

def estimate(p: DrakeParameters) -> float:
    values = vars(p)
    for name, value in values.items():
        if not math.isfinite(value) or value < 0:
            raise ValueError(f"{name} must be finite and nonnegative")
        if name.startswith("fraction_") and value > 1:
            raise ValueError(f"{name} must be <= 1")
    return math.prod(values.values())

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    defaults = DrakeParameters()
    for name, value in vars(defaults).items():
        parser.add_argument("--" + name.replace("_", "-"), type=float, default=value)
    args = parser.parse_args()
    try:
        result = estimate(DrakeParameters(**vars(args)))
    except ValueError as exc:
        parser.error(str(exc))
    print(f"Estimated detectable civilizations: {result:.10g}")

if __name__ == "__main__":
    main()
