import statistics


# --------------------------------------------------
# ANOMALY DETECTION
# --------------------------------------------------

def detect_anomalies(telemetry_history):
    """
    Detect unusual sensor readings using
    mean + standard deviation.

    telemetry_history:
        List of telemetry dictionaries.
    """

    if len(telemetry_history) < 5:
        return []

    anomalies = []

    # ----------------------------------------------
    # Extract sensor values
    # ----------------------------------------------

    temperatures = [
        item["readings"]["temperature"]
        for item in telemetry_history
        if "readings" in item
        and "temperature" in item["readings"]
    ]

    vibrations = [
        item["readings"]["vibration"]
        for item in telemetry_history
        if "readings" in item
        and "vibration" in item["readings"]
    ]

    pressures = [
        item["readings"]["pressure"]
        for item in telemetry_history
        if "readings" in item
        and "pressure" in item["readings"]
    ]

    # ----------------------------------------------
    # Temperature anomaly
    # ----------------------------------------------

    if len(temperatures) >= 5:

        mean_temperature = statistics.mean(
            temperatures
        )

        std_temperature = statistics.stdev(
            temperatures
        )

        latest_temperature = temperatures[-1]

        if std_temperature > 0:

            z_score = (
                latest_temperature - mean_temperature
            ) / std_temperature

            if abs(z_score) > 2:

                anomalies.append({
                    "sensor": "temperature",
                    "value": latest_temperature,
                    "mean": round(
                        mean_temperature,
                        2
                    ),
                    "z_score": round(
                        z_score,
                        2
                    ),
                    "message":
                        "Temperature is behaving unusually."
                })

    # ----------------------------------------------
    # Vibration anomaly
    # ----------------------------------------------

    if len(vibrations) >= 5:

        mean_vibration = statistics.mean(
            vibrations
        )

        std_vibration = statistics.stdev(
            vibrations
        )

        latest_vibration = vibrations[-1]

        if std_vibration > 0:

            z_score = (
                latest_vibration - mean_vibration
            ) / std_vibration

            if abs(z_score) > 2:

                anomalies.append({
                    "sensor": "vibration",
                    "value": latest_vibration,
                    "mean": round(
                        mean_vibration,
                        2
                    ),
                    "z_score": round(
                        z_score,
                        2
                    ),
                    "message":
                        "Vibration is behaving unusually."
                })

    # ----------------------------------------------
    # Pressure anomaly
    # ----------------------------------------------

    if len(pressures) >= 5:

        mean_pressure = statistics.mean(
            pressures
        )

        std_pressure = statistics.stdev(
            pressures
        )

        latest_pressure = pressures[-1]

        if std_pressure > 0:

            z_score = (
                latest_pressure - mean_pressure
            ) / std_pressure

            if abs(z_score) > 2:

                anomalies.append({
                    "sensor": "pressure",
                    "value": latest_pressure,
                    "mean": round(
                        mean_pressure,
                        2
                    ),
                    "z_score": round(
                        z_score,
                        2
                    ),
                    "message":
                        "Pressure is behaving unusually."
                })

    return anomalies