# GreenBox

A Raspberry Pi-based IoT device for monitoring and controlling plant growing environments.

## Features
- Temperature and humidity monitoring
- Automated watering system control
- Light schedule management
- Remote monitoring and control via web interface

## Installation
```
pip install -r requirements.txt
```

## Usage
```python
from greenbox import GreenBoxController

# Initialize controller
controller = GreenBoxController()

# Start monitoring
controller.start()
```

## Development
```
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```