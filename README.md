Here’s a comprehensive **GreenBox Technical Overview** document for a new user, based on the internal technical materials I found:  

---

# 📦 GreenBox Technical Overview

## Introduction

GreenBox is the **central hub** of the GreenThumb AI system, designed to empower small-scale farmers and gardeners with precision agriculture tools. It connects seamlessly with **GreenLink** sensor nodes (based on Raspberry Pi Pico), gathering real-time soil and environmental data to drive smart farming decisions.

Built on **Raspberry Pi 4** hardware, GreenBox is **solar-ready**, **open-source**, and optimized for easy integration, automation, and future scaling.

---

## Hardware Architecture

### GreenBox Core
- **Device**: Raspberry Pi 4  
- **Power Options**: Standard AC or solar-based setup  
- **Connectivity**: Wi-Fi (primary), potential support for LoRa in future versions  
- **Expansion**: USB, GPIO headers available for hardware modifications

### GreenLink Sensor Nodes
- **Device**: Raspberry Pi Pico with sensors attached
- **Sensors Included**:
  - Capacitive Soil Moisture Sensor
  - DHT22 Temperature and Humidity Sensor
  - ADS1115 ADC Module (for analog soil moisture readings)

---

## System Setup Overview

### Phase 1: Hardware Setup
- Connect DHT22 to Pi Zero W GPIO pins.
- Wire the ADS1115 ADC and attach soil moisture sensors.
- Ensure all power supplies and SD cards are properly installed.

### Phase 2: Software Installation
- Flash Raspberry Pi OS onto both Pi devices.
- Enable I2C communication using `raspi-config`.
- Install libraries:
  - `Adafruit_DHT` for DHT22 sensor
  - `adafruit-circuitpython-ads1x15` for ADS1115 module
- Write Python scripts to collect temperature, humidity, and soil moisture data.

### Phase 3: Communication Setup
Choose a communication method:
- **HTTP**: Use Flask to set up a basic web server on GreenBox.
- **MQTT**: Use Mosquitto broker for lightweight messaging.

Update the Pi Zero W (GreenLink) scripts to POST or PUBLISH sensor data to GreenBox, and configure GreenBox to receive and log/display data accordingly.

### Phase 4: Testing and Refinement
- Verify successful sensor reading transmission.
- Add error handling to sensor scripts.
- Optionally expand system to multiple GreenLinks or integrate cloud connections later.

---

## Key Features

| Feature | Description |
|:---|:---|
| **Central Hub** | GreenBox acts as the system "brain," receiving and processing all sensor data. |
| **Solar-Ready** | Compatible with solar power setups, ideal for off-grid farming. |
| **Open Source** | Fully open hardware and software for extensibility and community-driven innovation. |
| **Real-Time Data** | Immediate visibility into environmental conditions via dashboards. |
| **Edge Processing** | Processes sensor readings locally to reduce dependency on constant internet connectivity. |

---

## Future Extensions

- **Cloud Integration**: Enable remote monitoring and predictive analytics.
- **Advanced Sensor Additions**: Expand with more soil nutrient, pH, or light sensors.
- **LoRaWAN**: Add longer-range wireless communication.
- **Machine Learning**: On-device predictions for irrigation or fertilization.

---

## Quick Start Checklist

1. Flash Raspberry Pi OS to GreenBox and GreenLink SD cards.
2. Wire sensors to GreenLink as per diagrams.
3. Enable I2C and install necessary Python libraries.
4. Set up communication protocol (HTTP or MQTT).
5. Test basic data transmission.
6. Expand as needed with additional GreenLinks!

---

# 🚀 Welcome to GreenBox

By following this guide, you'll be well on your way to using **smart farming technology** to improve yields, save resources, and foster more sustainable farming practices.  
