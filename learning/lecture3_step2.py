from dataclasses import dataclass
import random


@dataclass
class SensorModel:
    name: str
    value: float
    min_value: float
    max_value: float
    drift: float
    noise: float

    def read(self):
        self.value += random.uniform(-self.drift, self.drift)
        self.value = max(self.min_value, min(self.max_value, self.value))
        observed = self.value + random.uniform(-self.noise, self.noise)
        return round(observed, 2)


temperature_sensor = SensorModel(
    "temperature",
    72.0,
    65.0,
    95.0,
    0.35,
    0.20
)





vibration_sensor = SensorModel(
    "vibration",
    2.5,
    1.0,
    6.0,
    0.15,
    0.10
)

pressure_sensor = SensorModel(
    "pressure",
    6.0,
    4.5,
    7.5,
    0.10,
    0.05
)

energy_sensor = SensorModel(
    "energy",
    1.5,
    0.8,
    2.5,
    0.08,
    0.05
)

print("Temperature:", temperature_sensor.read())
print("Vibration:", vibration_sensor.read())
print("Pressure:", pressure_sensor.read())
print("Energy:", energy_sensor.read())