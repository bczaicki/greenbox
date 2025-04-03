# Getting Started with GreenBox

This guide will help you set up your Raspberry Pi as a GreenBox plant monitoring and control system.

## Hardware Requirements

- Raspberry Pi (3B+ or newer recommended)
- DHT22 temperature and humidity sensor
- Soil moisture sensor
- Light sensor (LDR or digital light sensor)
- Relay module for controlling:
  - Water pump
  - Fan
  - Grow light
- Jumper wires
- Breadboard

## Wiring Diagram

```
Raspberry Pi GPIO Pinout:

Temperature/Humidity (DHT22) -> GPIO4
Soil Moisture Sensor -> GPIO17
Light Sensor -> GPIO18
Water Pump Relay -> GPIO23
Fan Relay -> GPIO24
Grow Light Relay -> GPIO25
```

## Software Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/greenbox.git
   cd greenbox
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create your configuration:
   ```bash
   cp config.yaml.example config.yaml
   # Edit config.yaml with your settings
   nano config.yaml
   ```

4. Run the application:
   ```bash
   python -m greenbox
   ```

## Running as a Service

To run GreenBox as a background service that starts automatically:

1. Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/greenbox.service
   ```

2. Add the following content (adjust paths as needed):
   ```
   [Unit]
   Description=GreenBox Plant Monitor
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 -m greenbox
   WorkingDirectory=/home/pi/greenbox
   StandardOutput=inherit
   StandardError=inherit
   Restart=always
   User=pi

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl enable greenbox
   sudo systemctl start greenbox
   ```

4. Check the status:
   ```bash
   sudo systemctl status greenbox
   ```

## Troubleshooting

### Sensor Issues

If you're having trouble with the DHT22 sensor:
- Ensure you have the correct GPIO pin in the config
- Check that the sensor is wired correctly (data, power, ground)
- Try adding a 10KΩ pull-up resistor between data and power

### Permission Issues

If you get permission errors when accessing GPIO:
- Run the application with sudo
- Or add your user to the gpio group:
  ```bash
  sudo usermod -a -G gpio $USER
  ```

## Extending GreenBox

GreenBox is designed to be extensible. To add new sensors or control capabilities:

1. Create a new sensor class in `src/sensors.py`
2. Add the appropriate control logic in `src/controller.py`
3. Update your configuration file with the new settings