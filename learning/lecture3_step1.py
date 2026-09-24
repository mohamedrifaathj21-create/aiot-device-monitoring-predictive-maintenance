import random

temperature = 72.0

for _ in range(10):
    temperature += random.uniform(-0.35, 0.35)
    noise = random.uniform(-0.20, 0.20)
    observed = temperature + noise
    print(f"Underlying: {temperature:.2f} °C | Observed: {observed:.2f} °C")