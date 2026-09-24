from trend_analyzer import analyze_sensor_trends


def calculate_health_score(telemetry_history):
    """
    Calculate machine health score using:
    - Current sensor values
    - Sensor trends
    """

    if not telemetry_history:
        return 0

    latest = telemetry_history[-1]

    readings = latest.get(
        "readings",
        {}
    )

    temperature = readings.get(
        "temperature",
        0
    )

    vibration = readings.get(
        "vibration",
        0
    )

    pressure = readings.get(
        "pressure",
        0
    )

    score = 100

    # --------------------------------------------------
    # CURRENT TEMPERATURE
    # --------------------------------------------------

    if temperature >= 90:

        score -= 30

    elif temperature >= 85:

        score -= 15

    # --------------------------------------------------
    # CURRENT VIBRATION
    # --------------------------------------------------

    if vibration >= 5:

        score -= 35

    elif vibration >= 4:

        score -= 20

    # --------------------------------------------------
    # CURRENT PRESSURE
    # --------------------------------------------------

    if pressure < 4.8 or pressure > 7.2:

        score -= 25

    elif pressure < 5.0 or pressure > 7.0:

        score -= 10

    # --------------------------------------------------
    # TREND ANALYSIS
    # --------------------------------------------------

    trends = analyze_sensor_trends(
        telemetry_history
    )

    # Increasing temperature
    if trends["temperature"] == "INCREASING":

        score -= 5

    # Increasing vibration
    if trends["vibration"] == "INCREASING":

        score -= 10

    # Decreasing pressure
    if trends["pressure"] == "DECREASING":

        score -= 5

    # Keep score between 0 and 100
    score = max(
        0,
        min(100, score)
    )

    return score


def get_health_status(score):

    if score >= 80:

        return "GOOD"

    elif score >= 60:

        return "WARNING"

    else:

        return "CRITICAL"


def get_maintenance_risk(score):

    if score >= 80:

        return "LOW"

    elif score >= 60:

        return "MEDIUM"

    else:

        return "HIGH"


def generate_recommendation(
    telemetry_history
):

    if not telemetry_history:

        return (
            "No telemetry data available."
        )

    latest = telemetry_history[-1]

    readings = latest.get(
        "readings",
        {}
    )

    temperature = readings.get(
        "temperature",
        0
    )

    vibration = readings.get(
        "vibration",
        0
    )

    pressure = readings.get(
        "pressure",
        0
    )

    trends = analyze_sensor_trends(
        telemetry_history
    )

    recommendations = []

    # --------------------------------------------------
    # TEMPERATURE
    # --------------------------------------------------

    if temperature >= 90:

        recommendations.append(
            "Inspect cooling system and temperature source."
        )

    elif temperature >= 85:

        recommendations.append(
            "Monitor temperature closely."
        )

    if trends["temperature"] == "INCREASING":

        recommendations.append(
            "Temperature is increasing; monitor for overheating."
        )

    # --------------------------------------------------
    # VIBRATION
    # --------------------------------------------------

    if vibration >= 5:

        recommendations.append(
            "Inspect rotating components, bearings and mechanical alignment."
        )

    elif vibration >= 4:

        recommendations.append(
            "Monitor machine vibration for increasing mechanical stress."
        )

    if trends["vibration"] == "INCREASING":

        recommendations.append(
            "Vibration is increasing; possible mechanical wear may be developing."
        )

    # --------------------------------------------------
    # PRESSURE
    # --------------------------------------------------

    if pressure < 4.8:

        recommendations.append(
            "Inspect the pressure system for leaks or low pressure."
        )

    elif pressure > 7.2:

        recommendations.append(
            "Inspect pressure regulation and valves."
        )

    if trends["pressure"] == "DECREASING":

        recommendations.append(
            "Pressure is decreasing; monitor the pressure system."
        )

    # --------------------------------------------------
    # NORMAL CONDITION
    # --------------------------------------------------

    if not recommendations:

        return (
            "Machine operating normally. "
            "Continue routine monitoring."
        )

    return " ".join(
        recommendations
    )


def predict_maintenance(
    telemetry_history
):

    health_score = calculate_health_score(
        telemetry_history
    )

    health_status = get_health_status(
        health_score
    )

    maintenance_risk = get_maintenance_risk(
        health_score
    )

    recommendation = generate_recommendation(
        telemetry_history
    )

    trends = analyze_sensor_trends(
        telemetry_history
    )

    return {
        "health_score": health_score,
        "health_status": health_status,
        "maintenance_risk": maintenance_risk,
        "recommendation": recommendation,
        "sensor_trends": trends
    }