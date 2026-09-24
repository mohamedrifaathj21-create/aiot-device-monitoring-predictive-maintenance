from sensors import read_all_sensors


def test_read_all_sensors():
    readings = read_all_sensors()

    # Verify all expected sensors exist
    assert "temperature" in readings
    assert "vibration" in readings
    assert "pressure" in readings
    assert "energy" in readings
    assert "humidity" in readings

    # Verify sensor values are numeric
    assert isinstance(readings["temperature"], (int, float))
    assert isinstance(readings["vibration"], (int, float))
    assert isinstance(readings["pressure"], (int, float))
    assert isinstance(readings["energy"], (int, float))
    assert isinstance(readings["humidity"], (int, float))