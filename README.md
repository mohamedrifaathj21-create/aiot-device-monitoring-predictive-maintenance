# AIoT Device Monitoring & Predictive Maintenance System

A Python-based Industrial IoT (IIoT) monitoring platform that simulates a manufacturing machine, generates real-time sensor telemetry, publishes data through MQTT, stores telemetry in MongoDB Atlas, exposes REST APIs using FastAPI, and provides a real-time monitoring dashboard using Streamlit.

The project also includes anomaly detection, sensor trend analysis, and predictive maintenance capabilities.

---

## Project Overview

This project simulates a **Bottle Filling Machine** operating on an industrial production line.

The system continuously generates virtual machine telemetry such as:

* Temperature
* Vibration
* Pressure
* Energy consumption
* Humidity
* Machine status

The telemetry is converted into JSON and published through MQTT.

A separate MQTT-to-MongoDB service receives the telemetry and stores it in MongoDB Atlas.

FastAPI provides REST endpoints for accessing the stored data and running analytics.

A Streamlit dashboard consumes the FastAPI endpoints and displays the machine's current condition, alerts, trends, anomaly detection results, and predictive maintenance information.

---

## System Architecture

```text
Python Device Simulator
        |
        | JSON Telemetry
        v
MQTT Publisher
        |
        | MQTT
        v
HiveMQ MQTT Broker
broker.hivemq.com:1883
        |
        | Subscribe
        v
MQTT to MongoDB Service
        |
        v
MongoDB Atlas
aiot_database.telemetry
        |
        v
FastAPI REST API
Port 8000
        |
        v
Streamlit Dashboard
Port 8501
```

---

## Features

### Device Simulation

* Virtual industrial machine identity
* Configurable sampling interval
* Simulated sensor readings
* Machine operating status
* JSON telemetry generation

### MQTT Communication

* Paho MQTT client
* MQTT publisher
* MQTT subscriber
* HiveMQ public MQTT broker
* JSON telemetry messages

### Cloud Database

* MongoDB Atlas integration
* Automatic telemetry storage
* Timestamped machine data
* Device-based telemetry retrieval

### REST API

FastAPI provides endpoints for:

* Latest telemetry
* Historical telemetry
* Device information
* Anomaly detection
* Predictive maintenance
* Device-specific telemetry

### Monitoring Dashboard

Streamlit provides:

* Real-time machine overview
* Current sensor readings
* Machine status
* Critical alerts
* Sensor trends
* Sensor history charts
* Anomaly detection
* Predictive maintenance
* Machine health score
* Maintenance risk
* Maintenance recommendation

---

## Analytics

### Anomaly Detection

The system analyzes historical telemetry to identify unusual sensor behavior.

The dashboard reports:

* Number of telemetry data points
* Detected anomalies
* Sensor behavior status

### Trend Analysis

Sensor trends are analyzed to identify whether values are:

* Increasing
* Decreasing
* Stable

Current trend analysis includes:

* Temperature
* Vibration
* Pressure

### Predictive Maintenance

The project includes a maintenance analysis layer that calculates:

* Machine health score
* Machine health status
* Maintenance risk
* Maintenance recommendation
* Sensor trends

This provides a foundation for future machine-health and predictive-maintenance improvements.

---

## Technologies Used

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| Python         | Core development          |
| Paho MQTT      | MQTT communication        |
| HiveMQ         | MQTT broker               |
| MongoDB Atlas  | Telemetry database        |
| PyMongo        | MongoDB integration       |
| FastAPI        | REST API                  |
| Uvicorn        | API server                |
| Streamlit      | Monitoring dashboard      |
| Pandas         | Telemetry analysis        |
| Docker         | Containerization          |
| Docker Compose | Multi-service deployment  |
| python-dotenv  | Environment configuration |

---

## Project Structure

```text
aiot-device-simulator/
|
|-- device_simulator.py
|-- sensors.py
|-- telemetry.py
|-- config.py
|
|-- mqtt_publisher.py
|-- mqtt_subscriber.py
|-- mqtt_to_mongodb.py
|
|-- anomaly_detector.py
|-- trend_analyzer.py
|-- predictive_maintenance.py
|
|-- api.py
|-- dashboard.py
|
|-- mongo_test.py
|
|-- test_sensors.py
|-- test_anomaly.py
|-- test_predictive.py
|-- test_trend.py
|
|-- learning/
|   |-- lecture3_step1.py
|   |-- lecture3_step2.py
|
|-- requirements.txt
|-- Dockerfile
|-- docker-compose.yml
|-- .dockerignore
|-- .gitignore
|-- .env.example
|-- README.md
```

---

## Configuration

Create a `.env` file in the project root.

Example:

```env
MONGODB_URI=your_mongodb_connection_string
```

Do not commit the `.env` file to GitHub.

The repository includes `.env.example` as a configuration template.

---

## Security

Sensitive configuration is intentionally excluded from version control.

The `.gitignore` file excludes:

```text
.env
.env.*
.venv/
__pycache__/
*.pyc
```

Never publish your real MongoDB connection string, username, password, API keys, or other credentials.

---

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd aiot-device-simulator
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Configure MongoDB

Create `.env`:

```env
MONGODB_URI=your_mongodb_connection_string
```

Make sure the MongoDB Atlas cluster allows your development machine to connect.

---

# Running the Project

The system consists of multiple services.

## 1. Start the MQTT to MongoDB service

Open PowerShell:

```powershell
python mqtt_to_mongodb.py
```

Expected output:

```text
Connecting to MongoDB Atlas...
MongoDB Atlas connected successfully!
Connecting to MQTT broker...
Connected to MQTT broker!
Subscribed to: aiot/MCH-007/telemetry
```

---

## 2. Start the MQTT publisher

Open another PowerShell window:

```powershell
.\.venv\Scripts\Activate.ps1
python mqtt_publisher.py
```

The publisher generates telemetry every 5 seconds.

Example:

```text
Telemetry published successfully!
Topic: aiot/MCH-007/telemetry
Message: {...}
```

---

## 3. Start FastAPI

Open another PowerShell window:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn api:app --reload
```

API:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 4. Start the Streamlit dashboard

Open another PowerShell window:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run dashboard.py
```

Dashboard:

```text
http://localhost:8501
```

---

## API Endpoints

| Endpoint                 | Description                     |
| ------------------------ | ------------------------------- |
| `/`                      | API status                      |
| `/telemetry`             | Latest telemetry records        |
| `/telemetry/latest`      | Latest telemetry                |
| `/devices`               | List available devices          |
| `/devices/{device_id}`   | Telemetry for a specific device |
| `/telemetry/anomalies`   | Anomaly detection results       |
| `/telemetry/maintenance` | Predictive maintenance analysis |

FastAPI interactive documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Docker Deployment

The project includes Docker support.

Build and start all services:

```powershell
docker compose up --build
```

Services:

```text
FastAPI       -> http://localhost:8000
Streamlit     -> http://localhost:8501
MQTT Broker   -> HiveMQ public broker
MongoDB       -> MongoDB Atlas
```

Stop services:

```powershell
docker compose down
```

---

# Dashboard

The Streamlit dashboard provides a centralized view of the machine.

### System Overview

Displays:

* Device ID
* Machine status
* Critical alerts
* Last telemetry update

### Live Sensor Monitoring

Displays:

* Temperature
* Vibration
* Pressure
* Energy
* Humidity

### Machine Health

Displays the calculated machine-health condition.

### Active Alerts

Sensor thresholds are used to identify critical conditions.

### Anomaly Detection

Displays:

* Number of analyzed data points
* Number of detected anomalies
* Anomaly information

### Predictive Maintenance

Displays:

* Health score
* Health status
* Maintenance risk
* Recommendation
* Sensor trends

### Sensor History

Interactive charts visualize historical sensor values.

---

# Data Flow

```text
Sensor Simulation
       |
       v
Telemetry Generation
       |
       v
JSON Serialization
       |
       v
MQTT Publisher
       |
       v
HiveMQ Broker
       |
       v
MQTT Subscriber
       |
       v
MongoDB Atlas
       |
       v
FastAPI
       |
       v
Streamlit Dashboard
       |
       v
Monitoring and Analytics
```

---

# Testing

The project includes separate test files for major components:

```text
test_sensors.py
test_anomaly.py
test_predictive.py
test_trend.py
```

These tests can be used while developing and extending the analytics modules.

---

# Future Improvements

Potential future enhancements include:

* Machine-learning-based anomaly detection
* More advanced predictive-maintenance models
* Multiple simulated industrial machines
* User authentication
* Role-based dashboard access
* MQTT authentication and TLS
* Alert notifications
* Email, WhatsApp, or Teams notifications
* Historical reporting
* Grafana integration
* CI/CD pipeline
* Cloud deployment
* Kubernetes deployment
* Edge-device integration
* Real ESP32 or STM32 sensor integration

---

# Project Objectives

This project demonstrates practical experience with:

* Python programming
* Object-oriented sensor simulation
* Embedded and IoT concepts
* MQTT communication
* JSON telemetry
* MongoDB
* REST APIs
* FastAPI
* Streamlit
* Data analysis
* Anomaly detection
* Predictive maintenance concepts
* Docker
* Environment configuration
* Multi-service application architecture

---

# Portfolio Project

**Project:** AIoT Device Monitoring & Predictive Maintenance System

**Domain:** Industrial IoT / AIoT / Predictive Maintenance

**Core Technologies:**

```text
Python
MQTT
MongoDB Atlas
FastAPI
Streamlit
Docker
Pandas
```

The project demonstrates an end-to-end AIoT pipeline from simulated industrial sensor data through communication, cloud storage, APIs, analytics, and real-time visualization.
