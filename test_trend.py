from trend_analyzer import analyze_sensor_trends


def test_sensor_trends():
    telemetry = [
        {
            "readings": {
                "temperature": 72,
                "vibration": 2.0,
                "pressure": 5.5
            }
        },
        {
            "readings": {
                "temperature": 74,
                "vibration": 2.2,
                "pressure": 5.4
            }
        },
        {
            "readings": {
                "temperature": 76,
                "vibration": 2.5,
                "pressure": 5.3
            }
        },
        {
            "readings": {
                "temperature": 79,
                "vibration": 2.9,
                "pressure": 5.2
            }
        },
        {
            "readings": {
                "temperature": 82,
                "vibration": 3.4,
                "pressure": 5.1
            }
        }
    ]

    result = analyze_sensor_trends(telemetry)

    # Verify all expected sensors are analyzed
    assert "temperature" in result
    assert "vibration" in result
    assert "pressure" in result

    # Verify the expected trends
    assert result["temperature"] == "INCREASING"
    assert result["vibration"] == "INCREASING"
    assert result["pressure"] == "STABLE"