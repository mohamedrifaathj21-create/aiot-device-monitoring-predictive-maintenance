from anomaly_detector import detect_anomalies


def test_anomaly_detection():
    # Normal telemetry
    telemetry = []

    for i in range(10):
        telemetry.append({
            "readings": {
                "temperature": 72 + (i * 0.1),
                "vibration": 2.0 + (i * 0.02),
                "pressure": 5.2 + (i * 0.02)
            }
        })

    # Add an unusual reading
    telemetry.append({
        "readings": {
            "temperature": 95.0,
            "vibration": 8.0,
            "pressure": 8.0
        }
    })

    anomalies = detect_anomalies(telemetry)

    # At least one anomaly should be detected
    assert len(anomalies) > 0